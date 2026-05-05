# coding=utf-8
"""
Tests for AI Analyzer token limit handling

Reproduces the bug where chunking logic only checks analyzed_count,
not actual token count, causing prompts to exceed model context window.
"""

import pytest
from unittest.mock import MagicMock, patch
from datetime import datetime
from typing import Dict, List, Any

from trendradar.ai.analyzer import AIAnalyzer, AIAnalysisResult


class MockAIClient:
    """Mock AI client to capture prompts"""

    def __init__(self):
        self.call_count = 0
        self.last_prompt = ""
        self.last_messages = []
        self.api_key = "test-key-12345"
        self.api_base = ""

    def validate_config(self):
        return True, ""

    def chat(self, messages: List[Dict], **kwargs) -> str:
        self.call_count += 1
        self.last_messages = messages
        # Extract user message content
        for msg in messages:
            if msg.get("role") == "user":
                self.last_prompt = msg.get("content", "")
        return '{"core_trends": "test", "sentiment_controversy": "test", "signals": "test", "rss_insights": "test", "outlook_strategy": "test"}'


def create_large_standalone_data(item_count: int = 100) -> Dict[str, Any]:
    """Create large standalone data to simulate token overflow"""
    platforms = []
    for i in range(item_count):
        platforms.append({
            "id": f"platform_{i}",
            "name": f"Platform {i}",
            "items": [
                {
                    "title": f"This is a test news title number {i} with some additional context",
                    "ranks": [1, 2, 3],
                    "first_time": "09:00",
                    "last_time": "18:00",
                    "count": 5,
                    "rank_timeline": [
                        {"time": "09:00", "rank": 1},
                        {"time": "12:00", "rank": 2},
                        {"time": "15:00", "rank": 3},
                    ]
                }
            ]
        })
    return {"platforms": platforms, "rss_feeds": []}


def create_small_stats(count: int = 5) -> List[Dict]:
    """Create small stats list (below chunk_size threshold)"""
    stats = []
    for i in range(count):
        stats.append({
            "word": f"keyword_{i}",
            "titles": [
                {
                    "title": f"News title {i}",
                    "source_name": f"Source {i}",
                    "ranks": [1],
                    "first_time": "09:00",
                    "last_time": "18:00",
                    "count": 1,
                }
            ]
        })
    return stats


class TestTokenLimitHandling:
    """Test cases for token limit handling"""

    def test_small_stats_large_standalone_should_chunk(self):
        """
        BUG REPRODUCTION: When stats count is small but standalone data is large,
        the prompt can exceed model context window without triggering chunking.
        """
        # Arrange
        small_stats = create_small_stats(count=5)  # Below chunk_size (15)
        large_standalone = create_large_standalone_data(item_count=100)

        ai_config = {
            "MODEL": "test-model",
            "API_KEY": "test-key-12345",
            "API_BASE": "",
            "TIMEOUT": 30,
            "MAX_TOKENS": 5000,
        }

        analysis_config = {
            "MAX_NEWS_FOR_ANALYSIS": 80,
            "CHUNK_SIZE": 15,
            "INCLUDE_RSS": False,
            "INCLUDE_RANK_TIMELINE": True,
            "INCLUDE_STANDALONE": True,
            "LANGUAGE": "Chinese",
            "PROMPT_FILE": "ai_analysis_prompt.txt",
        }

        mock_client = MockAIClient()

        with patch('trendradar.ai.analyzer.AIClient', return_value=mock_client):
            analyzer = AIAnalyzer(
                ai_config=ai_config,
                analysis_config=analysis_config,
                get_time_func=lambda: datetime(2024, 1, 1, 12, 0, 0),
                debug=False,
            )

            # Act
            result = analyzer.analyze(
                stats=small_stats,
                rss_stats=None,
                report_mode="incremental",
                report_type="增量更新",
                standalone_data=large_standalone,
            )

            # Assert - current behavior: no chunking happens
            # analyzed_count=5 < chunk_size=15, so chunking is NOT triggered
            # But the prompt is likely too large for the model
            print(f"Analyzed news: {result.analyzed_news}")
            print(f"Prompt length (chars): {len(mock_client.last_prompt)}")

            # This test demonstrates the bug - the prompt is sent without chunking
            # even though it may exceed the model's context window
            assert result.success, f"Analysis should succeed but got error: {result.error}"

            # The key assertion: verify that chunking was NOT triggered
            # (this is the bug - it SHOULD have been triggered for large prompts)
            # We can check by seeing if only one API call was made
            assert mock_client.call_count == 1, (
                f"Expected 1 API call (no chunking), got {mock_client.call_count}. "
                f"This means chunking was triggered when it shouldn't have been for small stats."
            )

    def test_large_standalone_generates_long_prompt(self):
        """
        Verify that large standalone data generates a prompt that could exceed
        model context limits.
        """
        # Arrange
        small_stats = create_small_stats(count=5)
        large_standalone = create_large_standalone_data(item_count=100)

        ai_config = {
            "MODEL": "test-model",
            "API_KEY": "test-key-12345",
            "API_BASE": "",
            "TIMEOUT": 30,
            "MAX_TOKENS": 5000,
        }

        analysis_config = {
            "MAX_NEWS_FOR_ANALYSIS": 80,
            "CHUNK_SIZE": 15,
            "INCLUDE_RSS": False,
            "INCLUDE_RANK_TIMELINE": True,
            "INCLUDE_STANDALONE": True,
            "LANGUAGE": "Chinese",
            "PROMPT_FILE": "ai_analysis_prompt.txt",
        }

        mock_client = MockAIClient()

        with patch('trendradar.ai.analyzer.AIClient', return_value=mock_client):
            analyzer = AIAnalyzer(
                ai_config=ai_config,
                analysis_config=analysis_config,
                get_time_func=lambda: datetime(2024, 1, 1, 12, 0, 0),
                debug=False,
            )

            # Act
            result = analyzer.analyze(
                stats=small_stats,
                rss_stats=None,
                report_mode="incremental",
                report_type="增量更新",
                standalone_data=large_standalone,
            )

            # Assert - the prompt is long
            # With 100 standalone items, each ~100 chars, plus system prompt,
            # the total should be significant
            assert len(mock_client.last_prompt) > 10000, (
                f"Expected long prompt with large standalone data, "
                f"got {len(mock_client.last_prompt)} chars"
            )

            # Rough token estimate: ~4 chars per token for Chinese/mixed content
            # A 50K context model can handle ~200K chars
            # This test verifies the prompt could be problematic
            estimated_tokens = len(mock_client.last_prompt) // 4
            print(f"Estimated tokens: {estimated_tokens}")

            # The prompt should be large enough to potentially cause issues
            # with a 50K context model
            assert estimated_tokens > 10000, (
                f"Expected prompt to be large enough to cause token issues, "
                f"estimated {estimated_tokens} tokens"
            )

    def test_chunking_triggered_by_analyzed_count(self):
        """
        Verify that chunking IS triggered when analyzed_count exceeds chunk_size,
        even with small standalone data.
        """
        # Arrange
        large_stats = create_small_stats(count=20)  # Above chunk_size (15)
        small_standalone = create_large_standalone_data(item_count=5)

        ai_config = {
            "MODEL": "test-model",
            "API_KEY": "test-key-12345",
            "API_BASE": "",
            "TIMEOUT": 30,
            "MAX_TOKENS": 5000,
        }

        analysis_config = {
            "MAX_NEWS_FOR_ANALYSIS": 80,
            "CHUNK_SIZE": 15,
            "INCLUDE_RSS": False,
            "INCLUDE_RANK_TIMELINE": True,
            "INCLUDE_STANDALONE": True,
            "LANGUAGE": "Chinese",
            "PROMPT_FILE": "ai_analysis_prompt.txt",
        }

        mock_client = MockAIClient()

        with patch('trendradar.ai.analyzer.AIClient', return_value=mock_client):
            analyzer = AIAnalyzer(
                ai_config=ai_config,
                analysis_config=analysis_config,
                get_time_func=lambda: datetime(2024, 1, 1, 12, 0, 0),
                debug=False,
            )

            # Act
            result = analyzer.analyze(
                stats=large_stats,
                rss_stats=None,
                report_mode="incremental",
                report_type="增量更新",
                standalone_data=small_standalone,
            )

            # Assert - chunking should be triggered
            # analyzed_count=20 > chunk_size=15, so chunking should happen
            # This means multiple API calls: N chunks + 1 synthesis
            assert mock_client.call_count > 1, (
                f"Expected multiple API calls for chunking, got {mock_client.call_count}. "
                f"This means chunking was NOT triggered when it should have been."
            )

            # The result should still be successful
            assert result.success, f"Analysis should succeed but got error: {result.error}"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
