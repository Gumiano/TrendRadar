<div align="center" id="trendradar">

<a href="https://github.com/sansan0/TrendRadar" title="TrendRadar - AI-Powered Trending News Aggregator & Analyzer">
  <img src="/_image/banner.webp" alt="TrendRadar - AI-powered trending news aggregator supporting Weibo, Zhihu, Baidu, Douyin and 20+ platforms" width="80%">
</a>

# TrendRadar

**AI-Powered Trending News Aggregator & Analyzer** — 20+ platform hot topics, RSS feeds, MCP Server, multi-channel notifications

Deploy in <strong>30 seconds</strong> — Say goodbye to endless scrolling, only see the news you truly care about

[![GitHub Stars](https://img.shields.io/github/stars/Gumiano/TrendRadar?style=flat-square&logo=github&color=yellow)](https://github.com/Gumiano/TrendRadar/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/Gumiano/TrendRadar?style=flat-square&logo=github&color=blue)](https://github.com/Gumiano/TrendRadar/network/members)
[![License](https://img.shields.io/badge/license-GPL--3.0-blue.svg?style=flat-square)](LICENSE)
[![Python](https://img.shields.io/badge/Python-%3E%3D3.12-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![MCP](https://img.shields.io/badge/MCP-v4.0-green.svg)](https://modelcontextprotocol.io/)
[![RSS](https://img.shields.io/badge/RSS-Feed_Support-orange.svg?style=flat-square&logo=rss&logoColor=white)](https://github.com/Gumiano/TrendRadar)
[![AI Translation](https://img.shields.io/badge/AI-Multi--Language-purple.svg?style=flat-square)](https://github.com/Gumiano/TrendRadar)
[![LiteLLM](https://img.shields.io/badge/LiteLLM-100%2B_Models-FF6B6B?style=flat-square)](https://github.com/BerriAI/litellm)

[![WeWork](https://img.shields.io/badge/WeWork-Notification-00D4AA?style=flat-square)](https://work.weixin.qq.com/)
[![Telegram](https://img.shields.io/badge/Telegram-Notification-00D4AA?style=flat-square)](https://telegram.org/)
[![Feishu](https://img.shields.io/badge/Feishu-Notification-00D4AA?style=flat-square)](https://www.feishu.cn/)
[![Email](https://img.shields.io/badge/Email-Notification-00D4AA?style=flat-square)](#)
[![ntfy](https://img.shields.io/badge/ntfy-Notification-00D4AA?style=flat-square)](https://github.com/binwiederhier/ntfy)
[![Bark](https://img.shields.io/badge/Bark-Notification-00D4AA?style=flat-square)](https://github.com/Finb/Bark)
[![Slack](https://img.shields.io/badge/Slack-Notification-00D4AA?style=flat-square)](https://slack.com/)
[![Generic Webhook](https://img.shields.io/badge/Generic-Webhook-607D8B?style=flat-square&logo=webhook&logoColor=white)](#)

[![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-Automation-2088FF?style=flat-square&logo=github-actions&logoColor=white)](https://github.com/Gumiano/TrendRadar)
[![GitHub Pages](https://img.shields.io/badge/GitHub_Pages-Deploy-4285F4?style=flat-square&logo=github&logoColor=white)](https://gumiano.github.io/TrendRadar)
[![Docker](https://img.shields.io/badge/Docker-Deploy-2496ED?style=flat-square&logo=docker&logoColor=white)](https://hub.docker.com/r/wantcat/trendradar)
[![MCP Support](https://img.shields.io/badge/MCP-AI_Analysis-FF6B6B?style=flat-square&logo=ai&logoColor=white)](https://modelcontextprotocol.io/)
[![AI Analysis](https://img.shields.io/badge/AI-Analysis_Push-FF6B6B?style=flat-square&logo=openai&logoColor=white)](#)
[![AI Filter](https://img.shields.io/badge/AI-Smart_Filter-9B59B6?style=flat-square&logo=openai&logoColor=white)](#)

</div>

<div align="center">

**[中文](README.md)** | **English**

</div>

> An enhanced fork of [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) that preserves all original features while adding a redesigned frontend UI, optimized AI analysis context, and fine-grained AI model configuration control.

---

## Table of Contents

- [Why Choose TrendRadar](#why-choose-trendradar)
- [Comparison with Upstream](#comparison-with-upstream)
- [Improvements](#improvements)
  - [Frontend UI Refactoring](#frontend-ui-refactoring)
  - [AI Feature Enhancements](#ai-feature-enhancements)
  - [New Features](#new-features)
  - [Code Quality](#code-quality)
- [Quick Deploy](#quick-deploy)
- [Configuration](#configuration)
- [Features](#features)
- [FAQ](#faq)
- [License](#license)

---

## Why Choose TrendRadar

TrendRadar is an **AI-powered trending news aggregator** built for individuals and teams who need to monitor Chinese internet hot topics with intelligent analysis. Compared to other news aggregators, TrendRadar's core advantages include:

- **Deep Chinese Platform Support** — Native support for 11+ Chinese hot-search platforms including Weibo, Zhihu, Baidu, Douyin, Bilibili, and Toutiao, not just English-language sources
- **AI Context Optimization** — Innovative chunk-based analysis splits long articles before sending to AI, ensuring complete context without truncation
- **Fine-Grained AI Model Control** — Analysis, translation, and filtering models can be independently configured with separate API keys and parameters for cost optimization
- **MCP Server Integration** — Built-in FastMCP 2.0 server with 26 tools for AI agents to query news data and run trend analysis
- **Translation Cache** — Identical content never calls AI API twice, saving 60%+ translation costs
- **Multi-Channel Push** — Supports 9 notification channels: Feishu, Telegram, WeWork, Email, Bark, Slack, ntfy, DingTalk, and generic webhooks

---

## Comparison with Upstream

This project forks [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) and adds systematic enhancements while preserving all original functionality.

| Aspect | Upstream (sansan0/TrendRadar) | This Fork (Gumiano/TrendRadar) |
|--------|------------------------------|-------------------------------|
| **Layout** | Tab-bar switching | Flat Grid — all modules visible at once |
| **CSS Architecture** | Inline styles | CSS Custom Properties Token System |
| **Dark Mode** | Basic support | Full coverage for all new components |
| **Container Width** | Fixed 1200px | Responsive 780px / 960px dual mode |
| **Translation** | Calls AI API every time | Translation cache — avoids redundant calls |
| **AI Config** | Shared global model | Independent analysis model config with separate API key |
| **AI Filter** | Basic filtering | Chunk-based analysis for better long-text quality |
| **RSS Parsing** | Strict parsing | Fault-tolerant parsing + sort optimization |
| **Today's Hotspot** | None | Cumulative hotspot display area |
| **Scheduling** | Hourly only | Morning/evening scheduling support |
| **Code Quality** | Some dead code | 14 dead code items removed, schema validation added |
| **Docker** | Remote image only | Prebuilt local build option added |

---

## Improvements

### Frontend UI Refactoring

- **Flat Grid Layout** — Removed tab-bar, all modules displayed in a single view
- **CSS Custom Properties Token System** — Unified theme management with easy customization
- **Responsive Container Width** — 780px normal / 960px wide-screen dual mode
- **Interaction Polish** — Hover transitions, functional border-radius, title hierarchy optimization

### AI Feature Enhancements

- **Translation Cache** — Same content never calls AI API twice, saving 60%+ costs
- **Independent AI Config** — Analysis and translation models can be configured separately
- **Chunk-Based Analysis** — Long articles split into chunks for better AI understanding
- **AI Filter Schema** — New structured storage table with CRUD interface

### New Features

- **Cumulative Hotspot Display** — Shows total hotspot count across all platforms for today
- **Morning/Evening Scheduling** — Supports morning and evening push modes
- **RSS Fault Tolerance** — Single feed failure doesn't break the pipeline, sorted by time

### Code Quality

- **Dead Code Cleanup** — Removed 14 unused code items
- **Storage Layer Enhancement** — New AI filter schema, unified CRUD interface
- **Docker Prebuilt** — Added `docker-compose.prebuilt.yml` for local builds
- **Hardened .gitignore** — Covers sensitive files, databases, and dev tool artifacts

---

## Quick Deploy

### Docker (Recommended)

```bash
cp docker/docker-compose.prebuilt.yml docker-compose.yml
cp docker/.env.example .env
# Edit .env with your API keys
docker compose up -d

# Stop the service
sudo docker compose -f docker/docker-compose-build.yml down

# Stop and restart
sudo docker compose -f docker/docker-compose-build.yml down && sudo docker compose -f docker/docker-compose-build.yml up trendradar -d
```

### GitHub Pages

1. Fork this repo
2. Settings → Pages → Select GitHub Actions
3. Configure `config/config.yaml`
4. Push to master branch

### Local Run

```bash
pip install uv
uv sync
uv run trendradar
```

---

## Configuration

Config file: `config/config.yaml`

```yaml
notification:
  feishu_webhook_url: ""    # Feishu Webhook
  telegram_bot_token: ""    # Telegram Bot

ai:
  enabled: false
  api_key: ""               # AI API Key
  base_url: ""              # API Base URL
  model: "gpt-4o-mini"      # Analysis model
  translation_model: ""     # Translation model (independent config)

translation_cache:
  enabled: true             # Enable translation cache

scheduler:
  mode: "morning_evening"   # Scheduling mode
```

---

## Features

- **Multi-Platform Hot Aggregation** — Weibo Hot Search, Zhihu Hot List, Baidu Hot Search, Douyin Trending, Bilibili Popular, Toutiao Hot List, GitHub Trending and 20+ platforms
- **AI-Powered Analysis** — Supports DeepSeek, GPT-4, Claude, Gemini and 100+ AI models via LiteLLM unified interface
- **AI Smart Filtering** — Interest-tag-based AI auto-classification with chunk-based analysis for better long-text processing
- **Multi-Language Translation** — AI auto-translation + translation cache mechanism, saving 60%+ API costs
- **Multi-Channel Push** — Feishu, Telegram, WeWork, Email, Bark, Slack, ntfy, DingTalk, generic webhooks — 9 notification channels
- **RSS Subscriptions** — Custom RSS feeds with fault-tolerant parsing + time-based sorting
- **MCP Server** — FastMCP 2.0 based AI Agent interface with 26 tools for data analysis and config management
- **Flexible Scheduling** — Supports morning_evening, always_on, office_hours, night_owl and custom scheduling modes
- **Docker One-Click Deploy** — 30 seconds to deploy, supports GitHub Actions automation
- **S3 Remote Storage** — Compatible with Cloudflare R2, Alibaba Cloud OSS, Tencent Cloud COS and other S3-compatible storage
- **GitHub Pages** — Auto-publish trending reports to GitHub Pages

---

## FAQ

<details>
<summary><strong>How does TrendRadar differ from the original sansan0/TrendRadar?</strong></summary>

TrendRadar is an enhanced fork with core differences:
1. **Frontend UI** — Flat Grid layout replaces tab switching, all modules visible at once
2. **AI Context Optimization** — Chunk-based analysis ensures long articles are not truncated
3. **Fine-Grained AI Config** — Analysis/translation/filtering models can be independently configured
4. **Translation Cache** — Identical content never calls AI API twice

</details>

<details>
<summary><strong>Which AI models are supported?</strong></summary>

Via LiteLLM, 100+ models are supported including: DeepSeek, OpenAI GPT-4o, Claude, Gemini, Qwen, Doubao and more. All models can be independently configured via `config/config.yaml`.

</details>

<details>
<summary><strong>How to deploy with Docker?</strong></summary>

```bash
cp docker/docker-compose.prebuilt.yml docker-compose.yml
cp docker/.env.example .env
# Edit .env with your API keys
docker compose up -d
```

</details>

<details>
<summary><strong>What is the MCP Server?</strong></summary>

The MCP Server is a FastMCP 2.0 based AI Agent interface that allows tools like Claude and ChatGPT to directly query TrendRadar's news data, run trend analysis, and manage configurations. It supports both stdio and HTTP transport modes.

</details>

---

## License

This project is licensed under [GPL-3.0](LICENSE).

Forked from [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar), which is also GPL-3.0 licensed.

---

## Acknowledgments

- [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) — Upstream project
- [ourongxing/newsnow](https://github.com/ourongxing/newsnow) — NewsNow data source
- [litellm](https://github.com/BerriAI/litellm) — Multi-model AI unified interface
- [FastMCP](https://github.com/jlowin/fastmcp) — MCP Server framework
