# Agent 输出消耗优化方案 Top 10（2026）

基于 20+ 篇最新研究和工程实践，按效果影响力排序。

**Research date:** 2026-05-03

---

## 1. 动态模型路由（Model Routing）
**节省：40-60%**

将请求按复杂度分层路由到不同模型：简单任务用 Haiku/Flash（~$0.15/M），复杂任务用 Opus/GPT-4o。RouteLLM（ICLR 2025）矩阵分解路由器仅用 14% 的 GPT-4 调用量就达到 95% 的性能。

**工具：** LiteLLM Router、RouteLLM、OpenRouter

---

## 2. Prompt 缓存（Prefix Caching）
**节省：40-90%**

将静态内容（system prompt、tool 定义）放在 prompt 前缀，利用 KV cache 复用。Anthropic 缓存命中仅收 10% 基础价，OpenAI 自动缓存 50% 折扣。2000 token 的 system prompt 跑 50 轮，从 102K token 降至 ~12K token。

**关键：** 结构化 prompt（静态在前，动态在后），cache hit rate 目标 >80%

---

## 3. 语义缓存（Semantic Caching）
**节省：20-50%**

用 embedding 向量匹配语义相似的查询，直接返回缓存结果，完全跳过 LLM 调用。GPTCache、Zep 等工具可吸收 30-50% 的重复查询。嵌入成本 ~$0.02/M tokens 远低于 LLM 调用费。

---

## 4. 输出约束与结构化输出（Output Constraints）
**节省：30-80%（输出端）**

- 设置精确的 `max_tokens`（分类任务只需 10 token，不是 4096）
- 使用 JSON mode / function calling 替代自由文本，避免冗余解释
- Chain-of-Draft 提示：用 ~5 词/步代替完整推理链，用 7.6% 的 token 达到同等准确率
- JSON 比 YAML/TSV 多用约 2x token，内部管道可切换格式

---

## 5. Prompt 压缩（Prompt Compression）
**节省：30-50%（输入端）**

- LLMLingua（微软）：压缩冗余 token，3-4x 压缩比，保留 90%+ 语义
- 精简 system prompt：去除冗余指令（"always be helpful, polite, professional" → "be professional"）
- RAG 优化：先检索 20 chunks → reranker 筛选 top 5 → 发送给主模型
- 预摘要注入：500 token 原文 → 100 token 摘要

---

## 6. 上下文窗口管理（Context Window Management）
**节省：50-80%（token 累积）**

Agent 循环中，每次调用都会重发完整历史，token 成本呈二次方增长。

**方案：**
- **滑动窗口**：只保留最近 N 轮（5-8 轮）
- **定期摘要压缩**：每 K 步用廉价模型压缩历史为摘要（如 Haiku）
- **状态重置**：阶段间丢弃推理痕迹，只保留关键结果
- **子 agent 隔离**：独立子任务不共享上下文，减少 53.7% token 消耗

---

## 7. 批处理 API（Batch API）
**节省：50%**

OpenAI / Anthropic Batch API 对非实时工作负载半价处理。与 prefix caching 叠加可达 95% 折扣（Anthropic）。适用于：夜间分析、批量分类、embedding 生成、文档处理。

---

## 8. 确定性任务替换为代码（Deterministic Step Replacement）
**节省：消除整个 LLM 调用**

> "最被忽视的优化：一些 agent 步骤根本不需要 LLM"

审计 agent 轨迹，找出输出格式 >95% 一致的步骤（日期提取、JSON 校验、SQL 生成），替换为确定性代码。每个替换同时消除 token、延迟和失败模式。

---

## 9. 思考输出抑制与预算控制（Thinking Budget Control）
**节省：60-70%（推理 token）**

- Claude 4.6 的 `thinking.display: "omitted"`：模型内部推理但不输出推理痕迹，不计费
- `budget_tokens` 参数：为每轮设置推理 token 上限，简单路由轮设 800，复杂推理轮设 5000
- 大多数 agent 轮次是例行调度，不需要深度推理

---

## 10. 轨迹缩减（Trajectory Reduction）
**节省：输入 token 40-60%，总成本 21-36%**

AgentDiet（arXiv 2509.23586）：在 agent 执行中自动移除无用、冗余、过时信息。用廉价 LLM 做反思模块，每 2 步压缩一步，移除 69-77% 的处理内容，保持 agent 性能不变。

---

## 组合效果

```
模型路由         (-40-60%)
  + Prompt 压缩   (-30-50%)
  + 语义缓存       (-30-50%)
  + 结构化输出     (-30-80% 输出端)
  + 批处理 API     (-50%)
  ─────────────────────────
  组合节省          70-90%
```

**建议实施顺序：** 缓存（零代码改动）→ 模型路由（最高影响）→ 输出约束 → Prompt 压缩 → 轨迹管理 → 批处理

---

## Sources

1. [Reducing AI Agent Inference Costs](https://harnessengineering.academy/blog/reducing-ai-agent-inference-costs-caching-strategies-model-routing-and-token-optimization-techniques/) — 2026-04-18
2. [How to Reduce LLM Costs by 50-70%](https://www.frenxt.com/research/how-to-reduce-llm-costs) — 2026-04-08
3. [Cost Optimization Strategies for LLM-Based Agents](https://getathenic.com/blog/llm-cost-optimization-ai-agents) — 2024-10-30
4. [Agent Cost Optimization: How to Track and Reduce](https://swarmsignal.net/agent-cost-optimization-how-to-track-and-reduce-llm-spend/) — 2026-04-17
5. [Agentic AI Cost Optimization: Cut LLM Costs by 60-80%](https://mdsanwarhossain.me/blog-agentic-ai-cost-optimization.html) — 2026-04-06
6. [LLM Token Optimization Strategies: The Complete Guide for 2026](https://www.tokenoptimize.dev/guides/llm-token-optimization-strategies)
7. [Prompt Caching for AI Agents: Architecture Patterns](https://zylos.ai/research/2026-02-24-prompt-caching-ai-agents-architecture) — 2026-02-24
8. [Inference Acceleration for AI Agent Loops](https://zylos.ai/research/2026-04-03-inference-acceleration-ai-agent-loops) — 2026-04-03
9. [Prompt Caching Economics 2026](https://agentmarketcap.ai/blog/2026/04/09/prompt-caching-economics-production-agent-workloads-2026) — 2026-04-09
10. [Token Optimization: Reduce Agent Costs by 70%](https://theaiuniversity.com/docs/cost-optimization/token-optimization)
11. [AI Agent Cost Optimization: Token Economics](https://zylos.ai/research/2026-02-19-ai-agent-cost-optimization-token-economics) — 2026-02-19
12. [AI Agent Loop Token Costs: How to Constrain Context](https://www.augmentcode.com/guides/ai-agent-loop-token-cost-context-constraints) — 2026-04-06
13. [8 Production Patterns for Token-Efficient Agentic AI](https://medium.com/@sohamghosh_23912/8-production-patterns-for-token-efficient-agentic-ai-3764030a81c3) — 2026-02-28
14. [AgentDiet: Reducing Cost of LLM Agents with Trajectory Reduction](https://arxiv.org/html/2509.23586v2) — arXiv
15. [CROP: Cost-Regularized Optimization of Prompts](https://arxiv.org/pdf/2604.14214) — arXiv
16. [SkillReducer: Optimizing LLM Agent Skills for Token Efficiency](https://arxiv.org/abs/2603.29919v1) — arXiv
17. [Prompt Caching Guide 2026](https://tokenmix.ai/blog/prompt-caching-guide) — 2026-04-07
18. [How to Build an LLM Router](https://blog.appxlab.io/2026/04/05/llm-router-api-cost-reduction/) — 2026-04-05
19. [LLM cost optimization 2025 playbook](https://spacetimeagents.com/blog/llm-cost-optimization-2025-playbook) — 2026-02-26
20. [ATLAS-RTC: Token-Level Runtime Control](https://arxiv.org/html/2603.27905v2) — arXiv
