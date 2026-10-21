<div align="center">

<h1>Awesome Gen AI Copilot</h1>

<p><strong>面向个人开发者、超级个体和小型团队的 GenAI / Copilot 项目精选。</strong><br>覆盖 Agent、Skills、Workflow、MCP、Coding Agent、RAG、Azure AI、Foundry 与 GitHub Copilot。</p>

<p>
	<a href="https://awesome.re"><img src="https://awesome.re/badge.svg" alt="Awesome"></a>
	<a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-2ea44f?labelColor=555" alt="MIT License"></a>
</p>

<p><sub>Agents · Skills · Workflows · MCP · Coding agents · RAG · Azure AI · Foundry</sub></p>

</div>

这个列表从多个 Awesome 项目和官方资源中整理而来，并按实际使用场景重新归类。优先收录适合公开发布、方便直接浏览和便于进一步研究的精选入口；完整候选目录作为本地研究资料单独维护。

> **分类边界**：Agent 是可独立接收目标并执行任务的软件；Skill 是被 Agent 调用的可复用能力包；Workflow 是由触发器、步骤、工具和审批组成的流程；Framework 是用于构建它们的 SDK 或运行时。

## 近期更新

<!-- BEGIN:recent-updates -->
1. [volcengine/OpenViking](https://github.com/volcengine/OpenViking) <sub>2026-10-21 · commit<br>fix(codex-plugin): preserve canonical PreCompact session identity (5660)；fix(ga…</sub>
2. [openclaw/openclaw](https://github.com/openclaw/openclaw) <sub>2026-10-21 · commit<br>feat(ui): preview hex colors in chat messages (179039)；Add shared enterprise-ma…</sub>
3. [QwenLM/qwen-code](https://github.com/QwenLM/qwen-code) <sub>2026-10-21 · commit<br>test(managed-agent): reuse the run on a same-key retry (FG11d) (14981)；fix(cli)…</sub>
4. [langgenius/dify](https://github.com/langgenius/dify) <sub>2026-10-21 · commit<br>test(web): exercise workflow controls and access points through real owners (44…</sub>
5. [Significant-Gravitas/AutoGPT](https://github.com/Significant-Gravitas/AutoGPT) <sub>2026-10-21 · commit<br>仓库有新推送</sub>
6. [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) <sub>2026-10-21 · commit<br>fix(refs): refuse ambiguous stale-ref recovery (2145)；fix(cdp): keep the attach…</sub>
7. [mastra-ai/mastra](https://github.com/mastra-ai/mastra) <sub>2026-10-21 · commit<br>test(core): add cross-engine regression coverage for agent-loop fixes (27929)；f…</sub>
8. [pydantic/pydantic-ai](https://github.com/pydantic/pydantic-ai) <sub>2026-10-21 · commit<br>Disable gh-aw's daily AI-credits guardrail with max-daily-ai-credits: -1 on the…</sub>
9. [HKUDS/nanobot](https://github.com/HKUDS/nanobot) <sub>2026-10-21 · commit<br>fix(webui): stabilize earlier-history loading and reclaim space (6349)；fix(gate…</sub>
10. [BerriAI/litellm](https://github.com/BerriAI/litellm) <sub>2026-10-21 · commit<br>fix(router): normalize native Responses latency per output token (47727)；fix(ti…</sub>
<!-- END:recent-updates -->

## Contents

<details>
<summary>展开完整目录</summary>

- [Agents and AI applications](#01-agents-and-ai-applications)
	- [Agents](#agents)
	- [Browser agents and web automation](#browser-agents-and-web-automation)
	- [Agent project collections](#agent-project-collections)
- [Agent skills](#02-agent-skills)
	- [Skills catalogs](#skills-catalogs)
	- [Skills packages and domain capabilities](#skills-packages-and-domain-capabilities)
- [Workflows and automation](#03-workflows-and-automation)
	- [Workflow automation](#workflow-automation)
	- [Agent workflow suites](#agent-workflow-suites)
- [MCP and tool connections](#04-mcp-and-tool-connections)
	- [Protocols and interaction standards](#protocols-and-interaction-standards)
	- [Servers, clients and connectors](#servers-clients-and-connectors)
	- [Collections and courses](#collections-and-courses)
- [Coding agents](#05-coding-agents)
	- [Coding agent products](#coding-agent-products)
	- [Review and repository automation](#review-and-repository-automation)
- [Agent frameworks and runtimes](#06-agent-frameworks-and-runtimes)
	- [Agent frameworks and SDKs](#agent-frameworks-and-sdks)
	- [Multi-agent platforms](#multi-agent-platforms)
	- [Web access and data tools](#web-access-and-data-tools)
	- [Code understanding tools](#code-understanding-tools)
	- [Agent infrastructure, UI and observability](#agent-infrastructure-ui-and-observability)
- [Knowledge, RAG and research](#07-knowledge-rag-and-research)
	- [RAG and data layer](#rag-and-data-layer)
	- [Agent memory](#agent-memory)
	- [Research and knowledge workflows](#research-and-knowledge-workflows)
	- [RAG collections](#rag-collections)
- [OPC and virtual teams](#08-opc-and-virtual-teams)
	- [Virtual teams and role systems](#virtual-teams-and-role-systems)
	- [Solo business operating systems](#solo-business-operating-systems)
	- [OPC collections](#opc-collections)
- [LLM background](#09-llm-background)
	- [Courses and tutorials](#courses-and-tutorials)
	- [Reference collections](#reference-collections)
- [Azure AI, Foundry and Copilot](#10-azure-ai-foundry-and-copilot)
	- [Skills and MCP extensions](#skills-and-mcp-extensions)
	- [Agent SDKs and frameworks](#agent-sdks-and-frameworks)
	- [Foundry and Azure samples](#foundry-and-azure-samples)
- [Awesome collections](#11-awesome-collections)
	- [Awesome lists](#awesome-lists)
	- [Course collections](#course-collections)
- [License and attribution](#license-and-attribution)

</details>

## 01. Agents and AI applications

可独立接收目标、规划并执行任务的 Agent 产品，以及便于发现应用形态的项目合集。

### Agents


- [AutoGPT](https://github.com/Significant-Gravitas/AutoGPT) - 探索自主任务分解、工具使用和 Agent 运行的开源项目。 <sub>更新 2026-10-21 · ★ 187687 · NOASSERTION</sub>
- [OpenClaw](https://github.com/openclaw/openclaw) - 自托管个人助理、频道、Skills、记忆和工具编排运行时。 <sub>更新 2026-10-21 · ★ 392707 · MIT</sub>
- [Hermes Agent](https://github.com/NousResearch/hermes-agent) - 支持记忆、工具、浏览器和长期任务的个人 Agent。 <sub>更新 2026-10-21 · ★ 255656 · MIT</sub>
- [LibreChat](https://github.com/danny-avila/LibreChat) - 支持多模型、Agent、MCP 和自托管部署的对话应用。 <sub>更新 2026-10-20 · ★ 46098 · MIT</sub>
- [nanobot](https://github.com/HKUDS/nanobot) - 轻量、可本地运行的个人 AI Agent。 <sub>更新 2026-10-21 · ★ 49227 · MIT</sub>
- [QwenPaw](https://github.com/agentscope-ai/QwenPaw) - 可自托管的个人 AI 助手项目。 <sub>更新 2026-10-21 · ★ 35883 · Apache-2.0</sub>
- [Khoj](https://github.com/khoj-ai/khoj) - 结合个人知识库、研究和自动化能力的 AI Agent。 <sub>更新 2026-08-02 · ★ 37765 · AGPL-3.0</sub>
- [AnythingLLM](https://github.com/Mintplex-Labs/anything-llm) - 本地优先的文档、RAG、Agent 和工作区应用。 <sub>更新 2026-10-21 · ★ 67374 · MIT</sub>
- [Agent Zero](https://github.com/agent0ai/agent-zero) - 支持工具、子 Agent 和本地运行的可扩展个人 AI Agent。 <sub>更新 2026-10-14 · ★ 19526 · NOASSERTION</sub>
### Browser agents and web automation

- [Browser Use](https://github.com/browser-use/browser-use) - 让 Agent 通过浏览器完成网页操作和任务执行。 <sub>更新 2026-10-20 · ★ 118696 · MIT</sub>
- [Skyvern](https://github.com/Skyvern-AI/skyvern) - 基于视觉和 LLM 的浏览器自动化平台。 <sub>更新 2026-10-21 · ★ 23239 · AGPL-3.0</sub>
- [agent-browser](https://github.com/vercel-labs/agent-browser) - 提供 CLI 和浏览器控制能力的 Agent 自动化工具。 <sub>更新 2026-10-21 · ★ 44354 · Apache-2.0</sub>
- [Stagehand](https://github.com/browserbase/stagehand) - 结合自然语言和 Playwright 构建浏览器 Agent 的框架。 <sub>更新 2026-10-21 · ★ 25755 · MIT</sub>
- [UI-TARS desktop](https://github.com/bytedance/UI-TARS-desktop) - 面向桌面交互的多模态 Agent 应用。 <sub>更新 2026-10-09 · ★ 39356 · Apache-2.0</sub>
### Agent project collections

- [Awesome LLM Apps](https://github.com/Shubhamsaboo/awesome-llm-apps) - 可运行的 AI Agent、Agent Skills、RAG 和 LLM 应用集合。 <sub>更新 2026-10-18 · ★ 142456 · Apache-2.0</sub>
- [Awesome LLM Projects](https://github.com/InfiniteAICreations/awesome-llm-projects) - 面向不同模型和应用场景的 LLM 项目集合。 <sub>更新 2025-02-11 · ★ 80 · CC0-1.0</sub>
- [Awesome AI Agents](https://github.com/e2b-dev/awesome-ai-agents) - AI Agent 项目、框架和应用发现入口。 <sub>更新 2026-08-21 · ★ 30549 · NOASSERTION</sub>
- [Awesome AI Tools](https://github.com/awesome-ai-tools/curated-ai-agents) - Agent 框架、平台和自主 Agent 资源精选。 <sub>更新 2026-03-26 · ★ 2 · MIT</sub>

## 02. Agent skills

将任务步骤、工具边界、输入输出和领域知识封装为可被 Agent 调用的能力包；它们不是独立负责目标规划和执行的 Agent。

### Skills catalogs

- [Anthropic Skills](https://github.com/anthropics/skills) - Claude Skills 的官方参考集合，包含文档、表格、演示文稿等技能。 <sub>更新 2026-10-09 · ★ 182547</sub>
- [Awesome Claude Skills](https://github.com/ComposioHQ/awesome-claude-skills) - Claude Skills 和相关资源的精选目录。 <sub>更新 2026-09-18 · ★ 77550</sub>
- [Awesome Agent Skills](https://github.com/VoltAgent/awesome-agent-skills) - 跨 Agent 客户端的 Skills 发现与参考入口。 <sub>更新 2026-10-20 · ★ 36095 · MIT</sub>
- [Awesome Skills](https://github.com/vivy-yi/awesome-skills) - 跨领域 Agent Skills 聚合列表。 <sub>更新 2026-06-07 · ★ 3 · MIT</sub>
- [Awesome OpenClaw Skills](https://github.com/VoltAgent/awesome-openclaw-skills) - OpenClaw Skills 的精选目录。 <sub>更新 2026-10-19 · ★ 53249 · MIT</sub>
- [Claude Code Official Plugins](https://github.com/anthropics/claude-plugins-official) - Claude Code 官方插件目录，包含可复用的 Agent 能力。 <sub>更新 2026-10-21 · ★ 43455 · Apache-2.0</sub>

### Skills packages and domain capabilities

- [Superpowers](https://github.com/obra/superpowers) - 面向软件开发 Agent 的技能框架和工程工作流。 <sub>更新 2026-10-21 · ★ 302690 · MIT</sub>
- [Agent Skills](https://github.com/addyosmani/agent-skills) - 面向编码 Agent 的工程技能和命令工作流。 <sub>更新 2026-10-13 · ★ 109058 · MIT</sub>
- [Vercel Agent Skills](https://github.com/vercel-labs/agent-skills) - Vercel 生态相关的 Agent Skills 集合。 <sub>更新 2026-10-14 · ★ 32733</sub>
- [NVIDIA Skills](https://github.com/NVIDIA/skills) - 面向 Physical AI、CUDA、仿真和 RAG 等场景的技能集合。 <sub>更新 2026-10-21 · ★ 3672 · Apache-2.0</sub>
- [.NET Agent Skills](https://github.com/dotnet/skills) - .NET、AI、RAG、Agent 和 MCP 开发技能。 <sub>更新 2026-10-21 · ★ 5690 · MIT</sub>
- [Trail of Bits Skills](https://github.com/trailofbits/skills) - 安全研究、漏洞发现、审计和验证技能。 <sub>更新 2026-10-20 · ★ 7667 · CC-BY-SA-4.0</sub>
- [Context Engineering Skills](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) - 面向上下文工程和 Agent 任务设计的技能集合。 <sub>更新 2026-10-12 · ★ 18182 · MIT</sub>
- [Agent Skills for Marketing](https://github.com/aaron-he-zhu/aaron-marketing-skills) - 覆盖 SEO、GEO、广告、邮件和增长运营的营销技能。 <sub>更新 2026-10-21 · ★ 2995 · Apache-2.0</sub>
- [Matt Pocock Skills](https://github.com/mattpocock/skills) - 面向 Claude Code 的 Skills 集合与工程实践。 <sub>更新 2026-10-19 · ★ 298918 · MIT</sub>
- [Andrej Karpathy Skills](https://github.com/multica-ai/andrej-karpathy-skills) - 将工程方法整理为 Coding Agent Skills 的实践集合。 <sub>更新 2026-04-20 · ★ 221593</sub>
- [UI UX Pro Max Skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) - 面向 Agent 界面设计、前端实现和 UX 评审的技能包。 <sub>更新 2026-10-15 · ★ 138104 · MIT</sub>
- [Taste Skill](https://github.com/Leonxlnx/taste-skill) - 用于约束 Agent 设计判断和输出质量的 Skill。 <sub>更新 2026-10-20 · ★ 100001 · MIT</sub>
- [Last 30 Days Skill](https://github.com/mvanhorn/last30days-skill) - 跨网站检索、研究和总结的 Agent Skill。 <sub>更新 2026-10-20 · ★ 64905 · MIT</sub>
- [Marketing Skills](https://github.com/coreyhaines31/marketingskills) - 覆盖营销、SEO、增长和转化流程的 Skills 集合。 <sub>更新 2026-10-19 · ★ 55717 · MIT</sub>
- [Obsidian Skills](https://github.com/kepano/obsidian-skills) - 面向 Obsidian 知识管理与自动化的 Agent Skills。 <sub>更新 2026-09-15 · ★ 49835 · MIT</sub>
- [Scientific Agent Skills](https://github.com/K-Dense-AI/scientific-agent-skills) - 面向科研检索、分析和写作的 Agent Skills。 <sub>更新 2026-10-19 · ★ 53341 · MIT</sub>
- [Diagram Design](https://github.com/cathrynlavery/diagram-design) - 用于生成架构图和流程图的 Agent Skill。 <sub>更新 2026-10-20 · ★ 59136 · MIT</sub>
- [Wshobson Agents](https://github.com/wshobson/agents) - 跨多个 Coding Agent harness 的插件、Skills 和工作流集合。 <sub>更新 2026-10-19 · ★ 41335 · MIT</sub>

## 03. Workflows and automation

由触发器、步骤、工具、状态和人工审批串联任务的流程与自动化项目，重点是如何组织一次完整执行，而不是提供单个能力。

### Workflow automation

- [n8n](https://github.com/n8n-io/n8n) - 可视化工作流自动化平台，支持 AI Agent 节点和外部系统连接。 <sub>更新 2026-10-21 · ★ 208170 · NOASSERTION</sub>
- [Flowise](https://github.com/FlowiseAI/Flowise) - 用可视化方式构建 LLM、Agent 和 RAG 工作流。 <sub>更新 2026-08-13 · ★ 55512 · NOASSERTION · 已归档</sub>
- [Dify](https://github.com/langgenius/dify) - 可视化构建 Agent、LLM 应用和工作流的开发平台。 <sub>更新 2026-10-21 · ★ 159090 · NOASSERTION</sub>
- [Langflow](https://github.com/langflow-ai/langflow) - 可视化编排 LLM、Agent 和 RAG 应用的工作流平台。 <sub>更新 2026-10-21 · ★ 155879 · MIT</sub>

### Agent workflow suites

- [DeerFlow](https://github.com/bytedance/deer-flow) - 面向研究、写作和知识处理的 Agent 工作流项目。 <sub>更新 2026-10-21 · ★ 84224 · MIT</sub>
- [gstack](https://github.com/garrytan/gstack) - 面向软件开发流程的 Claude Code 角色与工作流集合。 <sub>更新 2026-10-21 · ★ 137099 · MIT</sub>
- [Everything Claude Code](https://github.com/affaan-m/everything-claude-code) - Claude Code 的 Agent、Hooks 和开发工作流集合。 <sub>更新 2026-10-20 · ★ 285034 · MIT</sub>
- [Ruflo](https://github.com/ruvnet/ruflo) - 面向 Agent 编排、记忆管理和自治工作流的运行时。 <sub>更新 2026-10-21 · ★ 77958 · MIT</sub>
- [BMAD Method](https://github.com/bmad-code-org/BMAD-METHOD) - 面向 AI 辅助软件开发的角色、阶段和交付工作流方法。 <sub>更新 2026-10-20 · ★ 54390 · NOASSERTION</sub>
- [Oh My ClaudeCode](https://github.com/Yeachan-Heo/oh-my-claudecode) - Claude Code 的多 Agent 协作和任务编排扩展。 <sub>更新 2026-10-21 · ★ 40125 · MIT</sub>

## 04. MCP and tool connections

让 Agent 以结构化方式访问数据、工具、浏览器和外部系统。

### Protocols and interaction standards

- [Model Context Protocol](https://github.com/modelcontextprotocol/modelcontextprotocol) - MCP 协议、规范和生态入口。 <sub>更新 2026-10-20 · ★ 9492 · NOASSERTION</sub>
- [Agent Client Protocol](https://github.com/agentclientprotocol/agent-client-protocol) - 连接代码编辑器和 Agent 运行时的协议。 <sub>更新 2026-10-21 · ★ 4473 · Apache-2.0</sub>
- [AG-UI](https://github.com/ag-ui-protocol/ag-ui) - 将 Agent 状态、事件和人机交互流式传输到前端应用。 <sub>更新 2026-10-20 · ★ 16731 · MIT</sub>

### Servers, clients and connectors

- [MCP Servers](https://github.com/modelcontextprotocol/servers) - 官方 MCP Server 参考实现和示例。 <sub>更新 2026-10-19 · ★ 91434 · NOASSERTION</sub>
- [GitHub MCP Server](https://github.com/github/github-mcp-server) - 让 Agent 通过 MCP 使用 GitHub 数据和操作。 <sub>更新 2026-10-19 · ★ 33807 · MIT</sub>
- [Playwright MCP](https://github.com/microsoft/playwright-mcp) - 基于 Playwright 的浏览器操作 MCP Server。 <sub>更新 2026-10-19 · ★ 38447 · Apache-2.0</sub>
- [AWS MCP](https://github.com/awslabs/mcp) - AWS 服务、知识和工具的 MCP 集合。 <sub>更新 2026-10-21 · ★ 9800 · Apache-2.0</sub>
- [mcp-use](https://github.com/pietrozullo/mcp-use) - 使用 MCP 构建 Agent 和客户端应用的开发库。 <sub>更新 2026-10-21 · ★ 10791 · MIT</sub>
- [Context7](https://github.com/upstash/context7) - 通过 MCP 为 Agent 提供最新的库和框架文档上下文。 <sub>更新 2026-10-20 · ★ 63393 · MIT</sub>

### Collections and courses

- [Awesome MCP Servers](https://github.com/punkpeye/awesome-mcp-servers) - MCP Server 发现目录。 <sub>更新 2026-10-18 · ★ 96677 · MIT</sub>
- [Awesome MCP Servers by AppCypher](https://github.com/appcypher/awesome-mcp-servers) - 按文件、数据库、浏览器和服务类型整理的 MCP 资源。 <sub>更新 2026-05-06 · ★ 5797 · 已归档</sub>
- [Awesome MCP Servers by Machine Dawn](https://github.com/machinedawn/awesome-mcp-servers) - 大规模 MCP Server 候选目录。 <sub>更新 2026-03-03 · ★ 0 · MIT</sub>
- [MCP for Beginners](https://github.com/microsoft/mcp-for-beginners) - 面向 Model Context Protocol 的跨语言入门课程。 <sub>更新 2026-10-21 · ★ 17485 · MIT</sub>

## 05. Coding agents

面向需求澄清、代码编写、测试、审查和软件交付的可执行 Agent；通用工作流套件单独放在 Workflow 分类。

### Coding agent products

- [Claude Code](https://github.com/anthropics/claude-code) - 面向代码仓库的终端 Coding Agent，支持工具调用和开发工作流。 <sub>更新 2026-10-21 · ★ 152679</sub>
- [Codex](https://github.com/openai/codex) - 支持沙箱执行的开源终端 Coding Agent。 <sub>更新 2026-10-21 · ★ 130209 · Apache-2.0</sub>
- [OpenCode](https://github.com/anomalyco/opencode) - 开源、模型无关的终端 Coding Agent。 <sub>更新 2026-10-21 · ★ 219155 · MIT</sub>
- [Gemini CLI](https://github.com/google-gemini/gemini-cli) - Google Gemini 的开源终端 Agent，支持终端和 MCP 工作流。 <sub>更新 2026-10-21 · ★ 107478 · Apache-2.0</sub>
- [OpenHands](https://github.com/OpenHands/OpenHands) - 支持终端、浏览器和沙箱执行的软件开发 Agent 平台。 <sub>更新 2026-10-21 · ★ 91428 · MIT</sub>
- [Cline](https://github.com/cline/cline) - 可在 VS Code 中执行工具调用和代码任务的模型无关 Agent。 <sub>更新 2026-10-21 · ★ 70717 · Apache-2.0</sub>
- [Aider](https://github.com/Aider-AI/aider) - 面向 Git 仓库的终端结对编程工具。 <sub>更新 2026-05-22 · ★ 49674 · Apache-2.0</sub>
- [SWE-agent](https://github.com/SWE-agent/SWE-agent) - 针对真实 GitHub Issue 的软件工程 Agent。 <sub>更新 2026-10-19 · ★ 20605 · MIT</sub>
- [Continue](https://github.com/continuedev/continue) - 可连接不同模型的开源代码助手和 Agent 平台。 <sub>更新 2026-10-20 · ★ 36276 · Apache-2.0</sub>
- [Qwen Code](https://github.com/QwenLM/qwen-code) - 面向终端代码开发和任务执行的开源 Agent。 <sub>更新 2026-10-21 · ★ 28615 · Apache-2.0</sub>
- [Kimi CLI](https://github.com/MoonshotAI/kimi-cli) - 支持规划、代码理解和终端操作的 Coding Agent。 <sub>更新 2026-09-22 · ★ 11416 · Apache-2.0 · 已归档</sub>
- [Pi](https://github.com/earendil-works/pi) - 面向终端任务执行的 Coding Agent 和可扩展运行时。 <sub>更新 2026-10-21 · ★ 116781 · MIT</sub>
- [Open Interpreter](https://github.com/openinterpreter/openinterpreter) - 通过自然语言执行代码、调用工具和完成计算机任务的 Agent。 <sub>更新 2026-10-11 · ★ 68626 · Apache-2.0</sub>
- [Goose](https://github.com/aaif-goose/goose) - 可扩展的代码和任务执行 Agent，支持工具与模型集成。 <sub>更新 2026-10-21 · ★ 55470 · Apache-2.0</sub>
- [CC Switch](https://github.com/farion1231/cc-switch) - 管理 Coding Agent 配置与模型切换的桌面工具。 <sub>更新 2026-10-21 · ★ 146930 · MIT</sub>
- [Claude Code Router](https://github.com/musistudio/claude-code-router) - 为 Claude Code 提供模型路由和工具编排能力。 <sub>更新 2026-10-10 · ★ 37772 · MIT</sub>
- [Tabby](https://github.com/TabbyML/tabby) - 可自托管的代码补全和 Coding Assistant 平台。 <sub>更新 2026-06-30 · ★ 33920 · NOASSERTION</sub>
- [GPT Pilot](https://github.com/Pythagora-io/gpt-pilot) - 通过 Agent 协助生成和迭代软件项目的开发工具。 <sub>更新 2026-06-18 · ★ 33650 · NOASSERTION</sub>

### Review and repository automation

- [PR-Agent](https://github.com/Codium-ai/pr-agent) - 自动分析 Pull Request 并生成审查、说明和改进建议。 <sub>更新 2026-10-20 · ★ 13513 · MIT</sub>
- [AGENTS.md](https://github.com/agentsmd/agents.md) - 在代码仓库中声明 Agent 约束、命令和工作流的通用格式。 <sub>更新 2026-09-10 · ★ 25023 · MIT</sub>

## 06. Agent frameworks and runtimes

用于构建 Agent、管理状态、编排多 Agent 和运行工具调用工作流的 SDK、框架与基础设施。

### Agent frameworks and SDKs

- [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) - 支持工具、handoffs、guardrails 和 tracing 的 Python Agent SDK。 <sub>更新 2026-10-20 · ★ 30189 · MIT</sub>
- [Pydantic AI](https://github.com/pydantic/pydantic-ai) - 面向类型安全、结构化输出和可测试 Agent 的 Python 框架。 <sub>更新 2026-10-21 · ★ 20758 · MIT</sub>
- [LangGraph](https://github.com/langchain-ai/langgraph) - 面向有状态、可分支和可恢复 Agent 工作流的图编排框架。 <sub>更新 2026-10-21 · ★ 43609 · MIT</sub>
- [LangChain](https://github.com/langchain-ai/langchain) - 提供模型、工具、检索和 Agent 组合能力的开发框架。 <sub>更新 2026-10-20 · ★ 148175 · MIT</sub>
- [CrewAI](https://github.com/crewAIInc/crewAI) - 通过角色和任务组织多 Agent 协作。 <sub>更新 2026-10-20 · ★ 59932 · MIT</sub>
- [AutoGen](https://github.com/microsoft/autogen) - Microsoft 的多 Agent 对话和编排框架。 <sub>更新 2026-10-16 · ★ 61502 · CC-BY-4.0</sub>
- [Google ADK](https://github.com/google/adk-python) - 面向代码优先 Agent、评估和部署的 Google 开发框架。 <sub>更新 2026-10-21 · ★ 21932 · Apache-2.0</sub>
- [smolagents](https://github.com/huggingface/smolagents) - Hugging Face 的轻量代码型 Agent 框架。 <sub>更新 2026-10-06 · ★ 29954 · Apache-2.0</sub>
- [Agno](https://github.com/agno-agi/agno) - 支持模型、工具、知识和记忆的轻量 Agent 框架。 <sub>更新 2026-10-20 · ★ 42847 · Apache-2.0</sub>
- [Mastra](https://github.com/mastra-ai/mastra) - 面向 TypeScript Agent、工作流、记忆和可观测性的框架。 <sub>更新 2026-10-21 · ★ 28969 · NOASSERTION</sub>
- [DSPy](https://github.com/stanfordnlp/dspy) - 以程序化方式优化提示词和语言模型调用。 <sub>更新 2026-10-20 · ★ 38711 · MIT</sub>


### Multi-agent platforms

- [CAMEL](https://github.com/camel-ai/camel) - 面向多 Agent 协作、模拟和研究的框架。 <sub>更新 2026-10-19 · ★ 17941 · Apache-2.0</sub>
- [MetaGPT](https://github.com/geekan/MetaGPT) - 使用角色分工模拟软件公司的多 Agent 框架。 <sub>更新 2026-01-21 · ★ 70942 · MIT</sub>
- [AgentVerse](https://github.com/OpenBMB/AgentVerse) - 用于多 Agent 模拟、研究和协作实验的平台。 <sub>更新 2024-09-09 · ★ 5158 · Apache-2.0</sub>
- [ChatDev](https://github.com/OpenBMB/ChatDev) - 通过不同角色 Agent 模拟软件公司的协作式开发。 <sub>更新 2026-10-16 · ★ 34561 · Apache-2.0</sub>
- [MiroFish](https://github.com/666ghj/MiroFish) - 用于群体智能、预测和多 Agent 模拟的开源平台。 <sub>更新 2026-10-16 · ★ 80915 · AGPL-3.0</sub>

### Web access and data tools

- [Firecrawl](https://github.com/firecrawl/firecrawl) - 将网页转换为适合 LLM 和 Agent 使用的结构化内容的数据平台。 <sub>更新 2026-10-21 · ★ 193549 · AGPL-3.0</sub>
- [Crawl4AI](https://github.com/unclecode/crawl4ai) - 面向 LLM 和 Agent 的开源网页抓取与爬取框架。 <sub>更新 2026-10-20 · ★ 85949 · Apache-2.0</sub>
- [Agent-Reach](https://github.com/Panniantong/Agent-Reach) - 为 Agent 提供互联网信息访问能力的工具集。 <sub>更新 2026-10-20 · ★ 100377 · MIT</sub>

### Code understanding tools

- [Understand Anything](https://github.com/Egonex-AI/Understand-Anything) - 用于代码库理解、可视化和知识图谱构建的 Agent 工具。 <sub>更新 2026-10-12 · ★ 87296 · MIT</sub>
- [CodeGraph](https://github.com/colbymchenry/codegraph) - 将代码库建模为知识图谱，帮助 Coding Agent 理解和导航代码。 <sub>更新 2026-10-21 · ★ 74552 · MIT</sub>

### Agent infrastructure, UI and observability

- [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) - 支持插件化扩展和工具调用的 Agent harness。 <sub>更新 2026-10-17 · ★ 256161 · MIT</sub>
- [E2B](https://github.com/e2b-dev/e2b) - 为 Agent 生成代码和执行任务提供隔离的云端环境。 <sub>更新 2026-10-20 · ★ 14480 · Apache-2.0</sub>
- [Langfuse](https://github.com/langfuse/langfuse) - 面向 LLM 和 Agent 的 tracing、评估、提示词和数据集平台。 <sub>更新 2026-10-21 · ★ 36114 · NOASSERTION</sub>
- [Arize Phoenix](https://github.com/Arize-ai/phoenix) - AI 应用和 Agent 的可观测性与评估工具。 <sub>更新 2026-10-21 · ★ 11931 · NOASSERTION</sub>
- [CopilotKit](https://github.com/CopilotKit/CopilotKit) - Agent-native 应用、生成式 UI、共享状态和人工审批流程。 <sub>更新 2026-10-21 · ★ 38146 · MIT</sub>
- [Daytona](https://github.com/daytonaio/daytona) - 为 AI 生成代码和 Agent 任务提供隔离执行环境。 <sub>更新 2026-07-24 · ★ 71515 · 已归档</sub>
- [Headroom](https://github.com/headroomlabs-ai/headroom) - 压缩上下文和工具输出，降低 Agent 长上下文开销。 <sub>更新 2026-10-21 · ★ 76861 · Apache-2.0</sub>
- [LiteLLM](https://github.com/BerriAI/litellm) - 统一多模型调用、路由、回退和成本治理的网关。 <sub>更新 2026-10-21 · ★ 61692 · NOASSERTION</sub>

## 07. Knowledge, RAG and research

知识检索、记忆和研究相关的项目；个人业务与虚拟团队项目见 OPC 分类。

### RAG and data layer

- [LlamaIndex](https://github.com/run-llama/llama_index) - 数据连接、索引、检索和 Agent 应用框架。 <sub>更新 2026-10-21 · ★ 52590 · MIT</sub>
- [Haystack](https://github.com/deepset-ai/haystack) - 用于搜索、RAG 和 Agent Pipeline 的模块化框架。 <sub>更新 2026-10-21 · ★ 26796 · Apache-2.0</sub>
- [Chroma](https://github.com/chroma-core/chroma) - 面向 AI 应用的开源向量数据库。 <sub>更新 2026-10-20 · ★ 29541 · Apache-2.0</sub>
- [Qdrant](https://github.com/qdrant/qdrant) - 支持过滤和相似度检索的向量数据库。 <sub>更新 2026-10-21 · ★ 35165 · Apache-2.0</sub>
- [pgvector](https://github.com/pgvector/pgvector) - 在 PostgreSQL 中实现向量相似度搜索。 <sub>更新 2026-10-18 · ★ 23424 · NOASSERTION</sub>
- [GraphRAG](https://github.com/microsoft/graphrag) - 将图结构和社区摘要结合到检索增强生成中的系统。 <sub>更新 2026-10-20 · ★ 36397 · MIT</sub>

### Agent memory

- [Mem0](https://github.com/mem0ai/mem0) - 跨会话记忆、时间检索和 Agent 上下文管理。 <sub>更新 2026-10-21 · ★ 67551 · Apache-2.0</sub>
- [Letta](https://github.com/letta-ai/letta) - 支持有状态 Agent 和可编辑长期记忆的平台。 <sub>更新 2026-10-18 · ★ 25211 · Apache-2.0</sub>
- [Cognee](https://github.com/topoteretes/cognee) - 将知识图谱、记忆和检索组合起来的 Agent 数据层。 <sub>更新 2026-10-21 · ★ 32603 · Apache-2.0</sub>
- [OpenViking](https://github.com/volcengine/OpenViking) - 面向 Agent 记忆、知识和 Skills 的上下文数据库。 <sub>更新 2026-10-21 · ★ 40472 · AGPL-3.0</sub>
- [Hindsight](https://github.com/vectorize-io/hindsight) - 面向长期记忆和个性化检索的 Agent 记忆系统。 <sub>更新 2026-10-20 · ★ 52097 · MIT</sub>

### Research and knowledge workflows

- [STORM](https://github.com/stanford-oval/storm) - 通过多轮研究生成带引用知识文章的系统。 <sub>更新 2025-09-30 · ★ 31669 · MIT</sub>
- [Claude Code Memory](https://github.com/thedotmack/claude-mem) - 为 Coding Agent 保存和检索跨会话工作上下文。 <sub>更新 2026-10-21 · ★ 102006 · Apache-2.0</sub>
- [AutoResearch](https://github.com/karpathy/autoresearch) - 让 Agent 自动修改实验代码并迭代运行研究实验的工作流。 <sub>更新 2026-03-26 · ★ 98261</sub>

### RAG collections

- [Awesome RAG](https://github.com/brandonhimpfen/awesome-rag) - RAG 框架、向量数据库和检索工具发现入口。 <sub>更新 2026-09-06 · ★ 4</sub>


## 08. OPC and virtual teams

面向一人公司、AI 虚拟员工、角色分工和多 Agent 组织设计的项目。

### Virtual teams and role systems

- [OPB-Skills](https://github.com/chendongqi/OPB-Skills) - 覆盖产品、研发、设计、营销和运营的虚拟团队 Skills。 <sub>更新 2026-02-11 · ★ 129</sub>
- [AGI-Super-Team](https://github.com/aAAaqwq/AGI-Super-Team) - 多角色、跨客户端的 AI 虚拟团队方案。 <sub>更新 2026-10-20 · ★ 109 · MIT</sub>
- [Agency Agents](https://github.com/msitarzewski/agency-agents) - 带职责、沟通风格和交付物定义的专业角色库。 <sub>更新 2026-10-19 · ★ 162536 · MIT</sub>
- [Kompany](https://github.com/Fei2-Labs/Kompany) - C-suite 角色、任务分类和多 Agent 协作方向。 <sub>更新 2026-10-17 · ★ 6 · AGPL-3.0</sub>
- [solo-founder-os](https://github.com/alex-jb/solo-founder-os) - 面向独立创始人的角色、共享资料和 Agent 通信方案。 <sub>更新 2026-07-08 · ★ 12 · MIT</sub>

### Solo business operating systems

- [opc-skill](https://github.com/jiangye1314/opc-skill) - 面向中文一人公司的定位、验证、获客、交付和复盘流程。 <sub>更新 2026-05-05 · ★ 34 · NOASSERTION</sub>
- [opc](https://github.com/seedquan/opc) - 产品开发角色、流程和质量门参考。 <sub>更新 2026-04-10 · ★ 0 · MIT</sub>
- [opc_agent](https://github.com/CroTuyuzhe/opc_agent) - Boss Agent 与可扩展 Skill 插件方案。 <sub>更新 2026-04-24 · ★ 4 · Apache-2.0</sub>
- [opc-x](https://github.com/opc-x/opc-x) - 部门、原子技能和一人公司执行协议的组合设想。 <sub>更新 2026-09-22 · ★ 0</sub>

### OPC collections

- [Awesome Solo AI](https://github.com/yerdaulet-damir/awesome-solo-ai) - 面向独立开发者和 Solopreneur 的 AI 工具与业务链路。 <sub>更新 2026-10-20 · ★ 41 · NOASSERTION</sub>
- [Awesome Solopreneur AI](https://github.com/jakeolschewski/awesome-solopreneur-ai) - 一人公司获客、交付和运营工具集合。 <sub>更新 2026-04-14 · ★ 1 · NOASSERTION</sub>

## 09. LLM background

用于建立全局认知、学习路径和技术背景的资料与教程。

### Courses and tutorials

- [Anthropic Courses](https://github.com/anthropics/courses) - Anthropic 官方教育课程与练习资料。 <sub>更新 2026-08-28 · ★ 22905 · NOASSERTION · 已归档</sub>
- [AI Agents for Beginners](https://github.com/microsoft/ai-agents-for-beginners) - Microsoft 提供的 12 课 AI Agent 入门课程。 <sub>更新 2026-10-20 · ★ 77571 · MIT</sub>
- [Datawhale Self-LLM](https://github.com/datawhalechina/self-llm) - 中文大模型部署、使用和实践资料。 <sub>更新 2026-09-12 · ★ 32543 · Apache-2.0</sub>
- [LLM Course](https://github.com/mlabonne/llm-course) - 通过路线图和 Colab 笔记本学习大语言模型的课程资源。 <sub>更新 2026-02-05 · ★ 84524 · Apache-2.0</sub>
- [Hugging Face Diffusion Models Course](https://github.com/huggingface/diffusion-models-class) - Hugging Face 的扩散模型在线课程资料。 <sub>更新 2026-10-14 · ★ 4380 · Apache-2.0</sub>
- [动手学大模型应用开发](https://github.com/datawhalechina/llm-universe) - 面向初学者的大模型应用开发教程。 <sub>更新 2026-08-27 · ★ 14175</sub>
- [Happy-LLM](https://github.com/datawhalechina/happy-llm) - 从原理到训练流程学习大语言模型的中文教程。 <sub>更新 2026-08-08 · ★ 34480 · NOASSERTION</sub>
- [OpenAI Cookbook](https://github.com/openai/openai-cookbook) - 使用 OpenAI API 的示例与实践指南。 <sub>更新 2026-10-21 · ★ 76726 · MIT</sub>
- [Learn Claude Code](https://github.com/shareAI-lab/learn-claude-code) - 通过逐步实现理解 Coding Agent 架构和工具调用的教程项目。 <sub>更新 2026-09-28 · ★ 78919 · MIT</sub>

### Reference collections

- [Awesome LLM](https://github.com/Hannibal046/Awesome-LLM) - LLM 学术、工程、部署和课程资源总览。 <sub>更新 2025-07-31 · ★ 27444 · CC0-1.0</sub>
- [MLNLP-World Awesome LLM](https://github.com/MLNLP-World/Awesome-LLM) - 中文 LLM 资源、模型和实践入口。 <sub>更新 2024-03-28 · ★ 253</sub>
- [Awesome Generative AI](https://github.com/steven2358/awesome-generative-ai) - 生成式 AI 项目、工具和学习资源集合。 <sub>更新 2026-10-15 · ★ 12744 · CC0-1.0</sub>
- [Awesome Generative AI Guide](https://github.com/aishwaryanr/awesome-generative-ai-guide) - 按使用、构建、理解和学习路径组织的生成式 AI 指南。 <sub>更新 2026-10-15 · ★ 29894 · MIT</sub>
- [Awesome Artificial Intelligence](https://github.com/owainlewis/awesome-artificial-intelligence) - AI 课程、书籍、讲座、论文和工具入口。 <sub>更新 2026-08-15 · ★ 16704 · MIT</sub>
- [Awesome LLM Papers](https://github.com/guyulongcs/Awesome-LLM-papers) - LLM 论文与主题精读索引。 <sub>更新 2026-09-19 · ★ 38</sub>
- [Awesome ChatGPT Prompts](https://github.com/f/awesome-chatgpt-prompts) - 提示词案例和基础参考。 <sub>更新 2026-10-21 · ★ 173746 · NOASSERTION</sub>
- [Awesome ChatGPT Prompts Zh](https://github.com/PlexPt/awesome-chatgpt-prompts-zh) - 中文提示词案例集合。 <sub>更新 2026-04-28 · ★ 63816 · MIT</sub>

## 10. Azure AI, Foundry and Copilot

微软云和 GitHub Copilot 生态的 Skills、MCP、Agent Framework、示例与开发工具。

### Skills and MCP extensions

- [Azure Skills](https://github.com/microsoft/azure-skills) - Azure Skills、Azure MCP 和 Foundry MCP 的综合入口。 <sub>更新 2026-10-20 · ★ 1583 · MIT</sub>
- [Microsoft Skills](https://github.com/microsoft/skills) - Microsoft Foundry 与 Azure 开发的模块化 Agent Skills 集合。 <sub>更新 2026-10-20 · ★ 3137 · MIT</sub>
- [GitHub Awesome Copilot](https://github.com/github/awesome-copilot) - GitHub 官方 Copilot Agents、Instructions、Skills、Hooks 和 Plugins 资源库。 <sub>更新 2026-10-21 · ★ 40247 · MIT</sub>
- [Skills and MCPs](https://github.com/msftse/skills-and-mcps) - MAF Python SDK、Foundry Agents 和 MCP 实践示例。 <sub>更新 2026-03-11 · ★ 0</sub>

### Agent SDKs and frameworks

- [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) - Microsoft Agent Framework 的开发入口和示例。 <sub>更新 2026-10-21 · ★ 14239 · MIT</sub>
- [Semantic Kernel](https://github.com/microsoft/semantic-kernel) - Microsoft 的模型、插件和 Agent 编排 SDK。 <sub>更新 2026-10-21 · ★ 28682 · MIT</sub>
- [GitHub Copilot SDK](https://github.com/github/copilot-sdk) - 将 GitHub Copilot 能力集成到应用和自动化流程的 SDK。 <sub>更新 2026-10-21 · ★ 10564 · MIT</sub>

### Foundry and Azure samples

- [Azure AI Foundry Agents Samples](https://github.com/Azure-Samples/ai-foundry-agents-samples) - Foundry Agents 官方示例集合。 <sub>更新 2026-02-03 · ★ 33 · MIT</sub>
- [Python OpenAI Demos](https://github.com/Azure-Samples/python-openai-demos) - Python OpenAI、RAG、向量检索和混合检索示例。 <sub>更新 2026-10-15 · ★ 383 · MIT</sub>
- [Agent Playground](https://github.com/Azure-Samples/agent-playground) - 规划、编排、记忆、错误恢复和 Agent 通信 Playground。 <sub>更新 2026-04-21 · ★ 3 · MIT</sub>
- [Agent Framework Samples](https://github.com/kinfey/Agent-Framework-Samples) - Microsoft Agent Framework、GitHub Models 和 Foundry Agent Service 示例。 <sub>更新 2026-06-20 · ★ 1 · MIT</sub>

## 11. Awesome collections

用于发现 AI 应用、Agent、Skills、MCP、Copilot、LLM 学习资料和个人业务工具的导航型仓库。这些项目本身是索引或资源目录，不等同于可直接运行的框架或应用。

### Awesome lists

- [Awesome LLM Apps](https://github.com/Shubhamsaboo/awesome-llm-apps) - 可运行的 AI Agent、Agent Skills、RAG 和 LLM 应用集合。 <sub>更新 2026-10-18 · ★ 142456 · Apache-2.0</sub>
- [Awesome LLM Projects](https://github.com/InfiniteAICreations/awesome-llm-projects) - 面向不同模型和应用场景的 LLM 项目集合。 <sub>更新 2025-02-11 · ★ 80 · CC0-1.0</sub>
- [Awesome AI Agents](https://github.com/e2b-dev/awesome-ai-agents) - AI Agent 项目、框架和应用发现入口。 <sub>更新 2026-08-21 · ★ 30549 · NOASSERTION</sub>
- [Awesome AI Tools](https://github.com/awesome-ai-tools/curated-ai-agents) - Agent 框架、平台和自主 Agent 资源精选。 <sub>更新 2026-03-26 · ★ 2 · MIT</sub>
- [Awesome Claude Skills](https://github.com/ComposioHQ/awesome-claude-skills) - Claude Skills 和相关资源的精选目录。 <sub>更新 2026-09-18 · ★ 77550</sub>
- [Awesome Agent Skills](https://github.com/VoltAgent/awesome-agent-skills) - 跨 Agent 客户端的 Skills 发现与参考入口。 <sub>更新 2026-10-20 · ★ 36095 · MIT</sub>
- [Awesome Skills](https://github.com/vivy-yi/awesome-skills) - 跨领域 Agent Skills 聚合列表。 <sub>更新 2026-06-07 · ★ 3 · MIT</sub>
- [Awesome MCP Servers](https://github.com/punkpeye/awesome-mcp-servers) - MCP Server 发现目录。 <sub>更新 2026-10-18 · ★ 96677 · MIT</sub>
- [Awesome MCP Servers by AppCypher](https://github.com/appcypher/awesome-mcp-servers) - 按文件、数据库、浏览器和服务类型整理的 MCP 资源。 <sub>更新 2026-05-06 · ★ 5797 · 已归档</sub>
- [Awesome MCP Servers by Machine Dawn](https://github.com/machinedawn/awesome-mcp-servers) - 大规模 MCP Server 候选目录。 <sub>更新 2026-03-03 · ★ 0 · MIT</sub>
- [Awesome RAG](https://github.com/brandonhimpfen/awesome-rag) - RAG 框架、向量数据库和检索工具发现入口。 <sub>更新 2026-09-06 · ★ 4</sub>
- [Awesome Solo AI](https://github.com/yerdaulet-damir/awesome-solo-ai) - 面向独立开发者和 Solopreneur 的 AI 工具与业务链路。 <sub>更新 2026-10-20 · ★ 41 · NOASSERTION</sub>
- [Awesome Solopreneur AI](https://github.com/jakeolschewski/awesome-solopreneur-ai) - 一人公司获客、交付和运营工具集合。 <sub>更新 2026-04-14 · ★ 1 · NOASSERTION</sub>
- [Awesome LLM](https://github.com/Hannibal046/Awesome-LLM) - LLM 学术、工程、部署和课程资源总览。 <sub>更新 2025-07-31 · ★ 27444 · CC0-1.0</sub>
- [MLNLP-World Awesome LLM](https://github.com/MLNLP-World/Awesome-LLM) - 中文 LLM 资源、模型和实践入口。 <sub>更新 2024-03-28 · ★ 253</sub>
- [Awesome Generative AI](https://github.com/steven2358/awesome-generative-ai) - 生成式 AI 项目、工具和学习资源集合。 <sub>更新 2026-10-15 · ★ 12744 · CC0-1.0</sub>
- [Awesome Generative AI Guide](https://github.com/aishwaryanr/awesome-generative-ai-guide) - 按使用、构建、理解和学习路径组织的生成式 AI 指南。 <sub>更新 2026-10-15 · ★ 29894 · MIT</sub>
- [Awesome Artificial Intelligence](https://github.com/owainlewis/awesome-artificial-intelligence) - AI 课程、书籍、讲座、论文和工具入口。 <sub>更新 2026-08-15 · ★ 16704 · MIT</sub>
- [Awesome LLM Papers](https://github.com/guyulongcs/Awesome-LLM-papers) - LLM 论文与主题精读索引。 <sub>更新 2026-09-19 · ★ 38</sub>
- [Awesome ChatGPT Prompts](https://github.com/f/awesome-chatgpt-prompts) - 提示词案例和基础参考。 <sub>更新 2026-10-21 · ★ 173746 · NOASSERTION</sub>
- [Awesome ChatGPT Prompts Zh](https://github.com/PlexPt/awesome-chatgpt-prompts-zh) - 中文提示词案例集合。 <sub>更新 2026-04-28 · ★ 63816 · MIT</sub>
- [GitHub Awesome Copilot](https://github.com/github/awesome-copilot) - GitHub 官方 Copilot Agents、Instructions、Skills、Hooks 和 Plugins 资源库。 <sub>更新 2026-10-21 · ★ 40247 · MIT</sub>

### Course collections

带有 `Course` 标识的学习资料合集，包含课程、分课时教程、学习路线和适合入门的系统实践；它们也可以按主题在其他分类中重复出现。

- [Anthropic Courses](https://github.com/anthropics/courses) - Anthropic 官方教育课程与练习资料。 <sub>更新 2026-08-28 · ★ 22905 · NOASSERTION · 已归档</sub>
- [AI Agents for Beginners](https://github.com/microsoft/ai-agents-for-beginners) - Microsoft 提供的 12 课 AI Agent 入门课程。 <sub>更新 2026-10-20 · ★ 77571 · MIT</sub>
- [MCP for Beginners](https://github.com/microsoft/mcp-for-beginners) - 面向 Model Context Protocol 的跨语言入门课程。 <sub>更新 2026-10-21 · ★ 17485 · MIT</sub>
- [LLM Course](https://github.com/mlabonne/llm-course) - 通过路线图和 Colab 笔记本学习大语言模型的课程资源。 <sub>更新 2026-02-05 · ★ 84524 · Apache-2.0</sub>
- [Hugging Face Diffusion Models Course](https://github.com/huggingface/diffusion-models-class) - Hugging Face 的扩散模型在线课程资料。 <sub>更新 2026-10-14 · ★ 4380 · Apache-2.0</sub>
- [Datawhale Self-LLM](https://github.com/datawhalechina/self-llm) - 中文大模型部署、使用和实践课程资料。 <sub>更新 2026-09-12 · ★ 32543 · Apache-2.0</sub>
- [动手学大模型应用开发](https://github.com/datawhalechina/llm-universe) - 面向初学者的大模型应用开发教程。 <sub>更新 2026-08-27 · ★ 14175</sub>
- [Happy-LLM](https://github.com/datawhalechina/happy-llm) - 从原理到训练流程学习大语言模型的中文教程。 <sub>更新 2026-08-08 · ★ 34480 · NOASSERTION</sub>

## License and attribution

本仓库采用 MIT License，完整许可文本见 [LICENSE](LICENSE)。项目名称、链接和简短事实性说明用于资源发现与研究参考；外部项目的代码、文档、图片和许可证归原项目所有，使用或再发布前请阅读对应仓库的许可证和条款。
