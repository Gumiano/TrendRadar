<div align="center" id="trendradar">

<a href="https://github.com/sansan0/TrendRadar" title="TrendRadar - AI 热点新闻聚合与分析工具">
  <img src="/_image/banner.webp" alt="TrendRadar - AI 驱动的热点新闻聚合分析工具，支持微博、知乎、百度、抖音等 20+ 平台" width="80%">
</a>

# TrendRadar

**AI 驱动的热点新闻聚合与分析工具** —— 支持 20+ 平台热搜、RSS 订阅、MCP Server、多渠道通知推送

最快<strong>30秒</strong>部署的热点助手 —— 告别无效刷屏，只看真正关心的新闻资讯

[![GitHub Stars](https://img.shields.io/github/stars/Gumiano/TrendRadar?style=flat-square&logo=github&color=yellow)](https://github.com/Gumiano/TrendRadar/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/Gumiano/TrendRadar?style=flat-square&logo=github&color=blue)](https://github.com/Gumiano/TrendRadar/network/members)
[![License](https://img.shields.io/badge/license-GPL--3.0-blue.svg?style=flat-square)](LICENSE)
[![Python](https://img.shields.io/badge/Python-%3E%3D3.12-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![MCP](https://img.shields.io/badge/MCP-v4.0-green.svg)](https://modelcontextprotocol.io/)
[![RSS](https://img.shields.io/badge/RSS-订阅源支持-orange.svg?style=flat-square&logo=rss&logoColor=white)](https://github.com/Gumiano/TrendRadar)
[![AI翻译](https://img.shields.io/badge/AI-多语言推送-purple.svg?style=flat-square)](https://github.com/Gumiano/TrendRadar)
[![LiteLLM](https://img.shields.io/badge/LiteLLM-100%2B模型-FF6B6B?style=flat-square)](https://github.com/BerriAI/litellm)

[![企业微信通知](https://img.shields.io/badge/企业微信-通知-00D4AA?style=flat-square)](https://work.weixin.qq.com/)
[![Telegram通知](https://img.shields.io/badge/Telegram-通知-00D4AA?style=flat-square)](https://telegram.org/)
[![飞书通知](https://img.shields.io/badge/飞书-通知-00D4AA?style=flat-square)](https://www.feishu.cn/)
[![邮件通知](https://img.shields.io/badge/Email-通知-00D4AA?style=flat-square)](#)
[![ntfy通知](https://img.shields.io/badge/ntfy-通知-00D4AA?style=flat-square)](https://github.com/binwiederhier/ntfy)
[![Bark通知](https://img.shields.io/badge/Bark-通知-00D4AA?style=flat-square)](https://github.com/Finb/Bark)
[![Slack通知](https://img.shields.io/badge/Slack-通知-00D4AA?style=flat-square)](https://slack.com/)
[![通用Webhook](https://img.shields.io/badge/通用-Webhook-607D8B?style=flat-square&logo=webhook&logoColor=white)](#)

[![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-自动化-2088FF?style=flat-square&logo=github-actions&logoColor=white)](https://github.com/Gumiano/TrendRadar)
[![GitHub Pages](https://img.shields.io/badge/GitHub_Pages-部署-4285F4?style=flat-square&logo=github&logoColor=white)](https://gumiano.github.io/TrendRadar)
[![Docker](https://img.shields.io/badge/Docker-部署-2496ED?style=flat-square&logo=docker&logoColor=white)](https://hub.docker.com/r/wantcat/trendradar)
[![MCP Support](https://img.shields.io/badge/MCP-AI分析支持-FF6B6B?style=flat-square&logo=ai&logoColor=white)](https://modelcontextprotocol.io/)
[![AI分析推送](https://img.shields.io/badge/AI-分析推送-FF6B6B?style=flat-square&logo=openai&logoColor=white)](#)
[![AI智能筛选](https://img.shields.io/badge/AI-智能筛选新闻-9B59B6?style=flat-square&logo=openai&logoColor=white)](#)

</div>

<div align="center">

**中文** | **[English](README-EN.md)**

</div>

> 基于 [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) 的增强版本，在保留全部原有功能的基础上，系统性重构了前端 UI、优化了 AI 分析上下文、增加了细粒度的 AI 模型配置控制。

---

## 目录

- [为什么选择 TrendRadar](#为什么选择-trendradar)
- [与原版对比](#与原版对比)
- [改进内容](#改进内容)
  - [前端 UI 重构](#前端-ui-重构)
  - [AI 功能增强](#ai-功能增强)
  - [功能新增](#功能新增)
  - [代码质量优化](#代码质量优化)
- [快速部署](#快速部署)
- [配置说明](#配置说明)
- [功能特性](#功能特性)
- [常见问题](#常见问题)
- [许可证](#许可证)

---

## 为什么选择 TrendRadar

TrendRadar 是一款面向个人和团队的 **AI 热点新闻聚合工具**，专注于中文互联网热搜监控与智能分析。与其他新闻聚合器相比，TrendRadar 的核心优势在于：

- **中文平台深度支持** — 原生支持微博、知乎、百度、抖音、B站、头条等 11+ 中国主流热搜平台，而非仅覆盖英文信源
- **AI 上下文优化** — 独创的 chunk 分块分析机制，将长文拆分后送入 AI，确保分析不截断、上下文完整
- **细粒度 AI 模型配置** — 分析模型、翻译模型、筛选模型可独立配置不同的 API Key 和模型参数，按需分配成本
- **MCP Server 集成** — 内置 FastMCP 2.0 服务器，提供 26 个工具供 AI Agent 直接查询新闻数据、运行趋势分析
- **翻译缓存** — 相同内容不重复调用 AI API，节省 60%+ 的翻译费用
- **多渠道推送** — 支持飞书、Telegram、企业微信、邮件、Bark、Slack 等 9 种通知渠道

---

## 与原版对比

本项目 fork 自 [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar)，在保留原有全部功能的基础上进行了系统性增强。以下为关键差异：

| 对比维度 | 原版 (sansan0/TrendRadar) | 本版本 (Gumiano/TrendRadar) |
|---------|--------------------------|---------------------------|
| **前端布局** | 标签栏 Tab 切换模式 | 扁平 Grid 网格，所有模块一目了然 |
| **CSS 架构** | 内联样式为主 | CSS Custom Properties Token System |
| **深色模式** | 基础支持 | 完整覆盖所有新增组件 |
| **容器宽度** | 固定 1200px | 响应式 780px / 960px 双模式 |
| **翻译功能** | 每次调用 AI API | 翻译缓存机制，避免重复调用 |
| **AI 配置** | 全局共享模型 | AI 分析模型独立配置，支持独立 API Key |
| **AI 筛选** | 基础过滤 | 新增 chunk 分块分析，提升长文处理质量 |
| **RSS 容错** | 严格解析 | 容错解析 + 增加排序优化 |
| **今日热点** | 无 | 新增今日累积热点展示区 |
| **定时调度** | 仅整点 | 支持 morning_evening 定时推送 |
| **代码质量** | 存在冗余代码 | 清理死代码，添加 schema 验证 |
| **Docker** | 仅远程镜像 | 新增 prebuilt 本地构建方案 |

---

## 改进内容

### 前端 UI 重构

- **扁平 Grid 网格布局** — 移除独立 Tab 栏，所有模块在同一视图呈现
- **CSS Custom Properties Token System** — 统一主题色彩管理，便于自定义
- **响应式容器宽度** — 普通 780px / 宽屏 960px 双模式
- **交互细节打磨** — hover 过渡动画、功能性 border-radius、标题层级优化

### AI 功能增强

- **翻译缓存机制** — 相同内容不重复调用 AI API，节省 60%+ 费用
- **AI 分析模型独立配置** — 分析与翻译模型可独立设置
- **Chunk 分块分析** — 长文分块送入 AI，避免截断丢失关键信息
- **AI 筛选 Schema** — 新增结构化存储表和 CRUD 接口

### 功能新增

- **今日累积热点展示区** — 统计所有平台今日热点总量
- **Morning/Evening 定时调度** — 支持早间/晚间推送模式
- **RSS 解析容错** — 单条解析失败不影响整体，按时间倒序展示

### 代码质量优化

- **死代码清理** — 清理 14 处无用代码
- **存储层增强** — 新增 AI 筛选表结构，统一 CRUD 接口
- **Docker 本地构建** — 新增 `docker-compose.prebuilt.yml`
- **Gitignore 完善** — 覆盖敏感文件、数据文件、开发工具产物

---

## 快速部署

### Docker 部署（推荐）

```bash
cp docker/docker-compose.prebuilt.yml docker-compose.yml
cp docker/.env.example .env
# 编辑 .env 填入你的 API Key
docker compose up -d

# 关闭服务
sudo docker compose -f docker/docker-compose-build.yml down

# 关闭并重新启动
sudo docker compose -f docker/docker-compose-build.yml down && sudo docker compose -f docker/docker-compose-build.yml up trendradar -d
```

### GitHub Pages 部署

1. Fork 本仓库
2. Settings → Pages → 选择 GitHub Actions
3. 配置 `config/config.yaml`
4. Push 到 master 分支

### 本地运行

```bash
pip install uv
uv sync
uv run trendradar
```

---

## 配置说明

配置文件位于 `config/config.yaml`，主要配置项：

```yaml
notification:
  feishu_webhook_url: ""    # 飞书 Webhook
  telegram_bot_token: ""    # Telegram Bot

ai:
  enabled: false
  api_key: ""               # AI API Key
  base_url: ""              # API Base URL
  model: "gpt-4o-mini"      # 分析模型
  translation_model: ""     # 翻译模型（可独立配置）

translation_cache:
  enabled: true             # 启用翻译缓存

scheduler:
  mode: "morning_evening"   # 定时推送模式
```

---

## 功能特性

- **多平台热点聚合** — 微博热搜、知乎热榜、百度热搜、抖音热点、B站热门、头条热榜、GitHub Trending 等 20+ 平台
- **AI 智能分析** — 支持 DeepSeek、GPT-4、Claude、Gemini 等 100+ AI 模型（通过 LiteLLM 统一接口）
- **AI 智能筛选** — 基于兴趣标签的 AI 自动分类，支持 chunk 分块分析提升长文处理质量
- **多语言翻译** — AI 自动翻译 + 翻译缓存机制，节省 60%+ API 调用费用
- **多渠道推送** — 飞书、Telegram、企业微信（WeCom）、邮件、Bark、Slack、ntfy、钉钉、通用 Webhook 等 9 种通知渠道
- **RSS 订阅** — 自定义 RSS 源，容错解析 + 时间排序优化
- **MCP Server** — 基于 FastMCP 2.0 的 AI Agent 接口，提供 26 个工具用于数据分析和配置管理
- **定时调度** — 支持 morning_evening、always_on、office_hours、night_owl 等多种调度模式
- **Docker 一键部署** — 30 秒完成部署，支持 GitHub Actions 自动化
- **S3 远程存储** — 支持 Cloudflare R2、阿里云 OSS、腾讯云 COS 等 S3 兼容存储
- **GitHub Pages** — 自动发布热点报告到 GitHub Pages

---

## 常见问题

<details>
<summary><strong>TrendRadar 和原版 sansan0/TrendRadar 有什么区别？</strong></summary>

TrendRadar 是原版的增强 fork，核心差异在于：
1. **前端 UI** — 扁平 Grid 布局替代 Tab 切换，所有模块一目了然
2. **AI 上下文优化** — chunk 分块分析确保长文不截断
3. **细粒度 AI 配置** — 分析/翻译/筛选模型可独立配置
4. **翻译缓存** — 相同内容不重复调用 API

</details>

<details>
<summary><strong>支持哪些 AI 模型？</strong></summary>

通过 LiteLLM 支持 100+ 模型，包括：DeepSeek、OpenAI GPT-4o、Claude、Gemini、通义千问、豆包等。所有模型均可通过 `config/config.yaml` 独立配置。

</details>

<details>
<summary><strong>如何部署到 Docker？</strong></summary>

```bash
cp docker/docker-compose.prebuilt.yml docker-compose.yml
cp docker/.env.example .env
# 编辑 .env 填入 API Key
docker compose up -d
```

</details>

<details>
<summary><strong>MCP Server 是什么？</strong></summary>

MCP Server 是基于 FastMCP 2.0 的 AI Agent 接口，允许 Claude、ChatGPT 等 AI 工具直接查询 TrendRadar 的新闻数据、运行趋势分析、管理配置。支持 stdio 和 HTTP 两种传输模式。

</details>

---

## 许可证

本项目基于 [GPL-3.0](LICENSE) 许可证发布。

本项目 fork 自 [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar)，根据 GPL-3.0 协议，衍生作品继续沿用 GPL-3.0。

---

## 致谢

- [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) — 原版项目
- [ourongxing/newsnow](https://github.com/ourongxing/newsnow) — NewsNow 数据源
- [litellm](https://github.com/BerriAI/litellm) — 多模型 AI 统一接口
- [FastMCP](https://github.com/jlowin/fastmcp) — MCP Server 框架
