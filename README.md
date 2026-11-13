<a name="readme-top"></a>

<div align="center">

<!-- Banner: add assets/banner.png to the repository, then uncomment the next line to display it
<img src="assets/banner.png" alt="Awesome Gen AI Copilot banner" width="100%">
-->

<h1>Awesome Gen AI Copilot</h1>

<p><strong>A curated list of GenAI and Copilot projects for solo developers, indie builders, and small teams.</strong><br>Covers agents, skills, workflows, MCP, coding agents, RAG, Azure AI, Foundry, and GitHub Copilot.</p>

<p>
	<a href="https://awesome.re"><img src="https://awesome.re/badge.svg" alt="Awesome"></a>
	<a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-2ea44f?labelColor=555" alt="MIT License"></a>
</p>

<p><sub>Agents · Skills · Workflows · MCP · Coding agents · RAG · Azure AI · Foundry</sub></p>

</div>

<p align="center"><b>English</b> · <a href="README.zh-CN.md">简体中文</a></p>

This list draws on several Awesome projects and official resources, regrouped by real-world use case. It favors entry points that are easy to browse and useful for further research. The full candidate catalog is maintained separately as local research material.

## Start Here

Not sure how agents, skills, workflows, and MCP differ? Read the [classification guide](#classification) first, then pick an entry point based on your goal.

| I want to... | Start here |
|---|---|
| Have AI complete a task on its own | [01. Agents and AI applications](#01-agents-and-ai-applications) |
| Reuse ready-made skill packages | [02. Agent skills and plugins](#02-agent-skills-and-plugins) |
| Chain AI steps into an automated workflow | [03. Workflows and automation](#03-workflows-and-automation) |
| Connect agents to data, browsers, and tools | [04. MCP, protocols and tool connections](#04-mcp-protocols-and-tool-connections) |
| Use AI to write code and review PRs | [05. Coding agents and assistants](#05-coding-agents-and-assistants) |
| Build my own agent app | [06. Agent frameworks, runtimes and sandboxes](#06-agent-frameworks-runtimes-and-sandboxes) |
| Build knowledge-base Q&A or long-term memory | [07. Knowledge, RAG, data ingestion and research](#07-knowledge-rag-data-ingestion-and-research) |
| Run evaluations, observability, or safety checks | [08. Evaluation, observability and safety](#08-evaluation-observability-and-safety) |
| Set up a one-person company or a virtual team | [09. OPC and virtual teams](#09-opc-and-virtual-teams) |
| Learn LLM fundamentals systematically | [10. Learning, workshops and cookbooks](#10-learning-workshops-and-cookbooks) |
| Build within the Azure or GitHub Copilot ecosystem | [11. Azure AI, Foundry and Copilot](#11-azure-ai-foundry-and-copilot) |
| Find official Azure and Foundry samples | [11. Azure AI, Foundry and Copilot](#11-azure-ai-foundry-and-copilot) |

## Explore by Category

<table align="center" width="100%">
  <tr>
    <td align="center" width="33%" valign="top">
      <big><big>🤖</big></big><br>
      <a href="#01-agents-and-ai-applications"><b>01. Agents and AI applications</b></a><br>
      <sub>Agents and apps that take a goal and carry it out on their own</sub>
    </td>
    <td align="center" width="33%" valign="top">
      <big><big>🧩</big></big><br>
      <a href="#02-agent-skills-and-plugins"><b>02. Agent skills and plugins</b></a><br>
      <sub>Reusable capability packages that agents can call</sub>
    </td>
    <td align="center" width="33%" valign="top">
      <big><big>🔁</big></big><br>
      <a href="#03-workflows-and-automation"><b>03. Workflows and automation</b></a><br>
      <sub>Processes built from triggers, steps, and approvals</sub>
    </td>
  </tr>
  <tr>
    <td align="center" width="33%" valign="top">
      <big><big>🔌</big></big><br>
      <a href="#04-mcp-protocols-and-tool-connections"><b>04. MCP, protocols and tool connections</b></a><br>
      <sub>Structured access to data, tools, and external systems</sub>
    </td>
    <td align="center" width="33%" valign="top">
      <big><big>💻</big></big><br>
      <a href="#05-coding-agents-and-assistants"><b>05. Coding agents and assistants</b></a><br>
      <sub>Agents that write, test, and review code</sub>
    </td>
    <td align="center" width="33%" valign="top">
      <big><big>🏗️</big></big><br>
      <a href="#06-agent-frameworks-runtimes-and-sandboxes"><b>06. Agent frameworks, runtimes and sandboxes</b></a><br>
      <sub>SDKs, frameworks, and runtimes for building agents</sub>
    </td>
  </tr>
  <tr>
    <td align="center" width="33%" valign="top">
      <big><big>📚</big></big><br>
      <a href="#07-knowledge-rag-data-ingestion-and-research"><b>07. Knowledge, RAG, data ingestion and research</b></a><br>
      <sub>Knowledge retrieval, memory, and research workflows</sub>
    </td>
    <td align="center" width="33%" valign="top">
      <big><big>🧪</big></big><br>
      <a href="#08-evaluation-observability-and-safety"><b>08. Evaluation, observability and safety</b></a><br>
      <sub>Evaluation, observability, and safety checks</sub>
    </td>
    <td align="center" width="33%" valign="top">
      <big><big>👥</big></big><br>
      <a href="#09-opc-and-virtual-teams"><b>09. OPC and virtual teams</b></a><br>
      <sub>One-person companies, role division, and virtual teams</sub>
    </td>
  </tr>
  <tr>
    <td align="center" width="33%" valign="top">
      <big><big>🎓</big></big><br>
      <a href="#10-learning-workshops-and-cookbooks"><b>10. Learning, workshops and cookbooks</b></a><br>
      <sub>Courses, tutorials, and foundational references</sub>
    </td>
    <td align="center" width="33%" valign="top">
      <big><big>☁️</big></big><br>
      <a href="#11-azure-ai-foundry-and-copilot"><b>11. Azure AI, Foundry and Copilot</b></a><br>
      <sub>The Microsoft cloud and GitHub Copilot ecosystem</sub>
    </td>
    <td align="center" width="33%" valign="top">
      <big><big>⭐</big></big><br>
      <a href="#12-awesome-collections"><b>12. Awesome collections</b></a><br>
      <sub>Curated indexes for discovering resources</sub>
    </td>
  </tr>
</table>

## Classification

A single project can offer several capabilities. Classify it by its primary use and positioning. These are editorial guidelines, not official definitions from the projects.

| Concept | Core definition |
|---|---|
| Agent | Software that can take a goal, plan, and execute tasks on its own. |
| Skill | A reusable capability package that an agent can call. It bundles task steps, tool boundaries, inputs and outputs, and domain knowledge. |
| Workflow | A process that links triggers, steps, tools, state, and human approvals to complete a task. |
| Framework | An SDK or runtime for building agents, managing state, and orchestrating tool calls. |

MCP is covered separately. It is a protocol and ecosystem that gives agents structured access to data, tools, and external systems, so it is not ranked alongside the four concepts above.

## ⭐ Star Growth Top 15 (Last 7 Days)

Ranked by net GitHub star gain over the last 7 days, based on daily automated snapshots of tracked projects.

<!-- BEGIN:recent-updates -->
_2026-11-06 → 2026-11-13_

1. [mattpocock/skills](https://github.com/mattpocock/skills) <sub>+7.5k ★ · ★ 323.3k</sub>
2. [anthropics/skills](https://github.com/anthropics/skills) <sub>+6.0k ★ · ★ 193.8k</sub>
3. [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) <sub>+5.8k ★ · ★ 280.1k</sub>
4. [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) <sub>+4.3k ★ · ★ 50.4k</sub>
5. [affaan-m/ECC](https://github.com/affaan-m/ECC) <sub>+4.1k ★ · ★ 302.1k</sub>
6. [obra/superpowers](https://github.com/obra/superpowers) <sub>+3.7k ★ · ★ 316.9k</sub>
7. [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) <sub>+3.6k ★ · ★ 114.5k</sub>
8. [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) <sub>+3.3k ★ · ★ 116.9k</sub>
9. [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) <sub>+3.0k ★ · ★ 148.8k</sub>
10. [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) <sub>+3.0k ★ · ★ 116.7k</sub>
11. [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) <sub>+2.6k ★ · ★ 232.6k</sub>
12. [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) <sub>+2.3k ★ · ★ 201.4k</sub>
13. [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) <sub>+2.1k ★ · ★ 263.0k</sub>
14. [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) <sub>+2.0k ★ · ★ 111.4k</sub>
15. [farion1231/cc-switch](https://github.com/farion1231/cc-switch) <sub>+1.8k ★ · ★ 154.1k</sub>
<!-- END:recent-updates -->

## Contents

1. [01. Agents and AI applications](#01-agents-and-ai-applications)
2. [02. Agent skills and plugins](#02-agent-skills-and-plugins)
3. [03. Workflows and automation](#03-workflows-and-automation)
4. [04. MCP, protocols and tool connections](#04-mcp-protocols-and-tool-connections)
5. [05. Coding agents and assistants](#05-coding-agents-and-assistants)
6. [06. Agent frameworks, runtimes and sandboxes](#06-agent-frameworks-runtimes-and-sandboxes)
7. [07. Knowledge, RAG, data ingestion and research](#07-knowledge-rag-data-ingestion-and-research)
8. [08. Evaluation, observability and safety](#08-evaluation-observability-and-safety)
9. [09. OPC and virtual teams](#09-opc-and-virtual-teams)
10. [10. Learning, workshops and cookbooks](#10-learning-workshops-and-cookbooks)
11. [11. Azure AI, Foundry and Copilot](#11-azure-ai-foundry-and-copilot)
12. [12. Awesome collections](#12-awesome-collections)
13. [Watchlist](#watchlist)
14. [Legacy / Archived](#legacy--archived)
15. [License and attribution](#license-and-attribution)

## 01. Agents and AI applications

Agent products that take a goal, plan, and carry out tasks on their own, plus collections for discovering agent applications.

### Agents

- [AutoGPT](https://github.com/Significant-Gravitas/AutoGPT) - An open-source project exploring autonomous task decomposition, tool use, and agent execution. <sub>Updated 2026-11-13 · ★ 188.0k · NOASSERTION</sub>
- [OpenClaw](https://github.com/openclaw/openclaw) - A self-hosted personal assistant runtime with channels, Skills, memory, and tool orchestration. <sub>Updated 2026-11-13 · ★ 394.4k · MIT</sub>
- [Hermes Agent](https://github.com/NousResearch/hermes-agent) - A personal agent with memory, tools, browser control, and long-running tasks. <sub>Updated 2026-11-13 · ★ 263.0k · MIT</sub>
- [LibreChat](https://github.com/LibreChat-AI/LibreChat) - A chat app that supports multiple models, agents, and MCP, with self-hosted deployment. <sub>Updated 2026-11-13 · ★ 47.1k · MIT</sub>
- [nanobot](https://github.com/HKUDS/nanobot) - A lightweight personal AI agent that runs locally. <sub>Updated 2026-11-13 · ★ 50.1k · MIT</sub>
- [QwenPaw](https://github.com/agentscope-ai/QwenPaw) - A self-hostable personal AI assistant. <sub>Updated 2026-11-13 · ★ 37.7k · Apache-2.0</sub>
- [Khoj](https://github.com/khoj-ai/khoj) - An AI agent that combines a personal knowledge base, research, and automation. <sub>Updated 2026-08-02 · ★ 38.1k · AGPL-3.0</sub>
- [AnythingLLM](https://github.com/Mintplex-Labs/anything-llm) - A local-first app for documents, RAG, agents, and workspaces. <sub>Updated 2026-11-13 · ★ 68.2k · MIT</sub>
- [Agent Zero](https://github.com/agent0ai/agent-zero) - An extensible personal AI agent with tools, sub-agents, and local execution. <sub>Updated 2026-11-12 · ★ 19.8k · NOASSERTION</sub>
- [Open Interpreter](https://github.com/openinterpreter/openinterpreter) - An agent that runs code, calls tools, and completes computer tasks from natural-language instructions. <sub>Updated 2026-11-13 · ★ 68.9k · Apache-2.0</sub>
- [openfilm](https://github.com/openfilm/openfilm) - An open-source AI video agent that turns coding agents into video creators, with an editor for refining the output.

### Browser agents and web automation

- [Browser Use](https://github.com/browser-use/browser-use) - Lets agents complete web tasks through a browser. <sub>Updated 2026-11-13 · ★ 120.9k · MIT</sub>
- [Skyvern](https://github.com/Skyvern-AI/skyvern) - A browser automation platform built on vision models and LLMs. <sub>Updated 2026-11-13 · ★ 23.4k · AGPL-3.0</sub>
- [agent-browser](https://github.com/vercel-labs/agent-browser) - An agent automation tool with a CLI and browser control. <sub>Updated 2026-11-13 · ★ 50.4k · Apache-2.0</sub>
- [UI-TARS desktop](https://github.com/bytedance/UI-TARS-desktop) - A multimodal agent app for desktop interaction. <sub>Updated 2026-10-09 · ★ 39.6k · Apache-2.0 · Archived</sub>

### Agent project collections

- [Awesome LLM Apps](https://github.com/Shubhamsaboo/awesome-llm-apps) - A collection of runnable AI agents, agent skills, RAG projects, and LLM applications. <sub>Updated 2026-11-11 · ★ 144.5k · Apache-2.0</sub>
- [Awesome AI Agents](https://github.com/e2b-dev/awesome-ai-agents) - A starting point for discovering AI agent projects, frameworks, and apps. <sub>Updated 2026-08-21 · ★ 30.9k · NOASSERTION</sub>

<p align="right"><a href="#readme-top">Back to top ↑</a></p>

## 02. Agent skills and plugins

Packaged capabilities that an agent can call. Each bundles task steps, tool boundaries, inputs and outputs, and domain knowledge. They do not plan and pursue goals on their own.

### Skills catalogs

- [Anthropic Skills](https://github.com/anthropics/skills) - The official reference collection of Claude Skills, including skills for documents, spreadsheets, and presentations. <sub>Updated 2026-11-06 · ★ 193.8k</sub>
- [Awesome Claude Skills](https://github.com/ComposioHQ/awesome-claude-skills) - A curated directory of Claude Skills and related resources. <sub>Updated 2026-09-18 · ★ 79.4k</sub>
- [Awesome Agent Skills](https://github.com/VoltAgent/awesome-agent-skills) - A starting point for discovering skills across agent clients. <sub>Updated 2026-11-05 · ★ 37.1k · MIT</sub>
- [Awesome Skills](https://github.com/vivy-yi/awesome-skills) - An aggregated list of cross-domain agent skills. <sub>Updated 2026-06-07 · ★ <1k · MIT</sub>
- [Awesome OpenClaw Skills](https://github.com/VoltAgent/awesome-openclaw-skills) - A curated directory of OpenClaw Skills. <sub>Updated 2026-10-30 · ★ 53.7k · MIT</sub>
- [Claude Code Official Plugins](https://github.com/anthropics/claude-plugins-official) - The official Claude Code plugin directory, with reusable agent capabilities. <sub>Updated 2026-11-13 · ★ 47.1k · Apache-2.0</sub>

### Skills packages and domain capabilities

- [Superpowers](https://github.com/obra/superpowers) - A skills framework and engineering workflow for software development agents. <sub>Updated 2026-11-03 · ★ 316.9k · MIT</sub>
- [Agent Skills](https://github.com/addyosmani/agent-skills) - Engineering skills and command workflows for coding agents. <sub>Updated 2026-11-01 · ★ 116.9k · MIT</sub>
- [Vercel Agent Skills](https://github.com/vercel-labs/agent-skills) - A collection of agent skills for the Vercel ecosystem. <sub>Updated 2026-11-12 · ★ 34.0k</sub>
- [NVIDIA Skills](https://github.com/NVIDIA/skills) - Skills for scenarios such as physical AI, CUDA, simulation, and RAG. <sub>Updated 2026-11-12 · ★ 4.0k · Apache-2.0</sub>
- [.NET Agent Skills](https://github.com/dotnet/skills) - Skills for .NET, AI, RAG, agent, and MCP development. <sub>Updated 2026-11-12 · ★ 6.1k · MIT</sub>
- [Trail of Bits Skills](https://github.com/trailofbits/skills) - Skills for security research, vulnerability discovery, auditing, and verification. <sub>Updated 2026-11-12 · ★ 8.2k · CC-BY-SA-4.0</sub>
- [Context Engineering Skills](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) - A collection of skills for context engineering and agent task design. <sub>Updated 2026-10-12 · ★ 18.3k · MIT</sub>
- [Agent Skills for Marketing](https://github.com/aaron-he-zhu/aaron-marketing-skills) - Marketing skills covering SEO, GEO, advertising, email, and growth operations. <sub>Updated 2026-11-13 · ★ 3.1k · Apache-2.0</sub>
- [Matt Pocock Skills](https://github.com/mattpocock/skills) - A collection of Claude Code skills, along with engineering practices. <sub>Updated 2026-11-12 · ★ 323.3k · MIT</sub>
- [Andrej Karpathy Skills](https://github.com/multica-ai/andrej-karpathy-skills) - A practice collection that turns engineering methods into coding agent skills. <sub>Updated 2026-04-20 · ★ 232.6k</sub>
- [UI UX Pro Max Skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) - A skill package for agent-driven UI design, frontend implementation, and UX review. <sub>Updated 2026-11-10 · ★ 148.8k · MIT</sub>
- [Taste Skill](https://github.com/Leonxlnx/taste-skill) - A skill that constrains agent design judgment and output quality. <sub>Updated 2026-11-08 · ★ 114.5k · MIT</sub>
- [Last 30 Days Skill](https://github.com/mvanhorn/last30days-skill) - An agent skill for cross-site search, research, and summarization. <sub>Updated 2026-11-13 · ★ 67.5k · MIT</sub>
- [Marketing Skills](https://github.com/coreyhaines31/marketingskills) - A collection of skills covering marketing, SEO, growth, and conversion workflows. <sub>Updated 2026-11-11 · ★ 60.0k · MIT</sub>
- [Obsidian Skills](https://github.com/kepano/obsidian-skills) - Agent skills for Obsidian knowledge management and automation. <sub>Updated 2026-11-11 · ★ 52.1k · MIT</sub>
- [Scientific Agent Skills](https://github.com/K-Dense-AI/scientific-agent-skills) - Agent skills for scientific search, analysis, and writing. <sub>Updated 2026-11-09 · ★ 57.0k · MIT</sub>
- [Diagram Design](https://github.com/cathrynlavery/diagram-design) - An agent skill for generating architecture and flow diagrams. <sub>Updated 2026-11-12 · ★ 66.8k · MIT</sub>
- [Wshobson Agents](https://github.com/wshobson/agents) - A collection of plugins, skills, and workflows across multiple coding agent harnesses. <sub>Updated 2026-11-09 · ★ 42.5k · MIT</sub>
- [ai-skills](https://github.com/sanjay3290/ai-skills) - 24 cross-platform agent skills for Claude Code, Cursor, Codex, and Gemini CLI, covering databases, messaging, research, TTS, DevOps, and Google Workspace.
- [Archify](https://github.com/tt-a1i/archify) - Turns ideas, plans, or codebases into interactive diagrams. An agent skill for Claude Code, Codex, and more.
- [baoyu-skills](https://github.com/JimLiu/baoyu-skills) - 20+ agent skills by Baoyu for content work, including cover images, article illustrations, and WeChat publishing.
- [md2wechat-skill](https://github.com/geekjourneyx/md2wechat-skill) - A CLI and skill for WeChat Official Account publishing, with Markdown formatting, AI illustrations, previews, and draft creation.
- [guizang-social-card-skill](https://github.com/op7418/guizang-social-card-skill) - A skill for Claude Code and Codex that generates Xiaohongshu carousels and WeChat cover images, with 28 layouts and 10 themes.

<p align="right"><a href="#readme-top">Back to top ↑</a></p>

## 03. Workflows and automation

Projects that chain triggers, steps, tools, state, and human approvals. They focus on organizing a complete execution, not on a single capability.

### Workflow automation

- [n8n](https://github.com/n8n-io/n8n) - A visual workflow automation platform with AI agent nodes and connectors to external systems. <sub>Updated 2026-11-13 · ★ 210.4k · NOASSERTION</sub>
- [Dify](https://github.com/langgenius/dify) - A development platform for visually building agents, LLM apps, and workflows. <sub>Updated 2026-11-13 · ★ 161.1k · NOASSERTION</sub>
- [Langflow](https://github.com/langflow-ai/langflow) - A workflow platform for visually orchestrating LLM, agent, and RAG applications. <sub>Updated 2026-11-13 · ★ 156.6k · MIT</sub>

### Agent workflow suites

- [DeerFlow](https://github.com/bytedance/deer-flow) - An agent workflow project for research, writing, and knowledge processing. <sub>Updated 2026-11-13 · ★ 85.3k · MIT</sub>
- [gstack](https://github.com/garrytan/gstack) - A collection of Claude Code roles and workflows for software development. <sub>Updated 2026-11-13 · ★ 141.4k · MIT</sub>
- [Everything Claude Code](https://github.com/affaan-m/ECC) - A collection of agents, hooks, and development workflows for Claude Code. <sub>Updated 2026-11-09 · ★ 302.1k · MIT</sub>
- [Ruflo](https://github.com/ruvnet/ruflo) - A runtime for agent orchestration, memory management, and autonomous workflows. <sub>Updated 2026-11-13 · ★ 81.6k · MIT</sub>
- [BMAD Method](https://github.com/bmad-code-org/BMAD-METHOD) - A method of roles, phases, and delivery workflows for AI-assisted software development. <sub>Updated 2026-11-12 · ★ 55.3k · NOASSERTION</sub>
- [Oh My ClaudeCode](https://github.com/Yeachan-Heo/oh-my-claudecode) - A multi-agent collaboration and task orchestration extension for Claude Code. <sub>Updated 2026-11-13 · ★ 40.8k · MIT</sub>
- [ccblog](https://github.com/Mor-Li/ccblog) - A multi-agent automation pipeline for generating WeChat Official Account articles.

<p align="right"><a href="#readme-top">Back to top ↑</a></p>

## 04. MCP, protocols and tool connections

Lets agents access data, tools, browsers, and external systems in a structured way.

### Protocols and interaction standards

- [Model Context Protocol](https://github.com/modelcontextprotocol/modelcontextprotocol) - The entry point to the MCP specification and ecosystem. <sub>Updated 2026-11-12 · ★ 9.7k · NOASSERTION</sub>
- [Agent Client Protocol](https://github.com/agentclientprotocol/agent-client-protocol) - A protocol for connecting code editors and agent runtimes. <sub>Updated 2026-11-12 · ★ 4.6k · Apache-2.0</sub>
- [AG-UI](https://github.com/ag-ui-protocol/ag-ui) - Streams agent state, events, and human-in-the-loop interactions to front-end applications. <sub>Updated 2026-11-12 · ★ 17.2k · MIT</sub>

### Servers, clients and connectors

- [MCP Servers](https://github.com/modelcontextprotocol/servers) - Official MCP server reference implementations and examples. <sub>Updated 2026-11-12 · ★ 92.0k · NOASSERTION</sub>
- [GitHub MCP Server](https://github.com/github/github-mcp-server) - Lets agents use GitHub data and operations through MCP. <sub>Updated 2026-11-13 · ★ 34.4k · MIT</sub>
- [Playwright MCP](https://github.com/microsoft/playwright-mcp) - A browser-control MCP server built on Playwright. <sub>Updated 2026-11-13 · ★ 39.6k · Apache-2.0</sub>
- [AWS MCP](https://github.com/awslabs/mcp) - A collection of MCP servers for AWS services, knowledge, and tools. <sub>Updated 2026-11-12 · ★ 9.9k · Apache-2.0</sub>
- [Context7](https://github.com/upstash/context7) - Gives agents up-to-date library and framework documentation through MCP. <sub>Updated 2026-11-13 · ★ 64.7k · MIT</sub>
- [MCP Registry](https://github.com/modelcontextprotocol/registry) - The official MCP server registry, an authoritative place to discover MCP servers. <sub>Updated 2026-11-13 · ★ 7.5k · NOASSERTION</sub>
- [Agent-Reach](https://github.com/Panniantong/Agent-Reach) - A toolkit that gives agents access to internet information. <sub>Updated 2026-11-08 · ★ 111.4k · MIT</sub>
- [Concat](https://github.com/jub0t/Concat) - A local-first, open-source, cross-platform video editor (beta) that you can script through a JSON-RPC API and MCP.

### Collections and courses

- [Awesome MCP Servers](https://github.com/punkpeye/awesome-mcp-servers) - A discovery directory of MCP servers. <sub>Updated 2026-11-06 · ★ 97.7k · MIT</sub>
- [MCP for Beginners](https://github.com/microsoft/mcp-for-beginners) - A cross-language introductory course on the Model Context Protocol. <sub>Updated 2026-11-13 · ★ 17.6k · MIT</sub>

<p align="right"><a href="#readme-top">Back to top ↑</a></p>

## 05. Coding agents and assistants

Executable agents for requirement clarification, code writing, testing, review, and software delivery. General-purpose workflow suites are listed under Workflows.

### Coding agent products

- [Claude Code](https://github.com/anthropics/claude-code) - A terminal coding agent for code repositories, with tool calling and development workflows. <sub>Updated 2026-11-13 · ★ 155.5k</sub>
- [Codex](https://github.com/openai/codex) - An open-source terminal coding agent with sandboxed execution. <sub>Updated 2026-11-13 · ★ 135.1k · Apache-2.0</sub>
- [OpenCode](https://github.com/anomalyco/opencode) - An open-source, model-agnostic terminal coding agent. <sub>Updated 2026-11-13 · ★ 226.5k · MIT</sub>
- [Gemini CLI](https://github.com/google-gemini/gemini-cli) - Google's open-source terminal agent for Gemini, with terminal and MCP workflows. <sub>Updated 2026-11-13 · ★ 108.8k · Apache-2.0</sub>
- [OpenHands](https://github.com/OpenHands/OpenHands) - A software development agent platform with terminal, browser, and sandboxed execution. <sub>Updated 2026-11-13 · ★ 93.4k · MIT</sub>
- [Cline](https://github.com/cline/cline) - A model-agnostic agent that runs tool calls and coding tasks in VS Code. <sub>Updated 2026-11-13 · ★ 71.6k · Apache-2.0</sub>
- [Aider](https://github.com/Aider-AI/aider) - A terminal pair-programming tool for Git repositories. <sub>Updated 2026-05-22 · ★ 50.1k · Apache-2.0</sub>
- [SWE-agent](https://github.com/SWE-agent/SWE-agent) - A software engineering agent for resolving real GitHub issues. <sub>Updated 2026-11-09 · ★ 20.8k · MIT</sub>
- [Continue](https://github.com/continuedev/continue) - An open-source coding assistant and agent platform that works with different models. <sub>Updated 2026-11-05 · ★ 36.5k · Apache-2.0</sub>
- [Qwen Code](https://github.com/QwenLM/qwen-code) - An open-source agent for terminal-based code development and task execution. <sub>Updated 2026-11-13 · ★ 30.0k · Apache-2.0</sub>
- [Pi](https://github.com/earendil-works/pi) - A coding agent and extensible runtime for terminal task execution. <sub>Updated 2026-11-13 · ★ 121.7k · MIT</sub>
- [Goose](https://github.com/aaif-goose/goose) - An extensible code and task execution agent with tool and model integration. <sub>Updated 2026-11-13 · ★ 56.5k · Apache-2.0</sub>
- [CC Switch](https://github.com/farion1231/cc-switch) - A desktop tool for managing coding agent configurations and switching models. <sub>Updated 2026-11-13 · ★ 154.1k · MIT</sub>
- [Claude Code Router](https://github.com/musistudio/claude-code-router) - Provides model routing and tool orchestration for Claude Code. <sub>Updated 2026-10-10 · ★ 38.1k · MIT</sub>
- [Tabby](https://github.com/TabbyML/tabby) - A self-hostable code completion and coding assistant platform. <sub>Updated 2026-06-30 · ★ 33.9k · NOASSERTION</sub>
- [GPT Pilot](https://github.com/Pythagora-io/gpt-pilot) - A development tool that uses agents to help generate and iterate on software projects. <sub>Updated 2026-06-18 · ★ 33.6k · NOASSERTION</sub>

### Review and repository automation

- [PR-Agent](https://github.com/The-PR-Agent/pr-agent) - Automatically analyzes pull requests and generates reviews, descriptions, and improvement suggestions. <sub>Updated 2026-11-12 · ★ 16.0k · MIT</sub>
- [AGENTS.md](https://github.com/agentsmd/agents.md) - A common format for declaring agent constraints, commands, and workflows in a code repository. <sub>Updated 2026-09-10 · ★ 25.5k · MIT</sub>

<p align="right"><a href="#readme-top">Back to top ↑</a></p>

## 06. Agent frameworks, runtimes and sandboxes

SDKs, frameworks, and infrastructure for building agents, managing state, orchestrating multiple agents, and running tool-calling workflows.

### Agent frameworks and SDKs

- [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) - A Python agent SDK with tools, handoffs, guardrails, and tracing. <sub>Updated 2026-11-13 · ★ 30.6k · MIT</sub>
- [Pydantic AI](https://github.com/pydantic/pydantic-ai) - A Python framework for type-safe, structured-output, and testable agents. <sub>Updated 2026-11-13 · ★ 21.2k · MIT</sub>
- [LangGraph](https://github.com/langchain-ai/langgraph) - A graph orchestration framework for stateful, branching, and resumable agent workflows. <sub>Updated 2026-11-13 · ★ 44.9k · MIT</sub>
- [LangChain](https://github.com/langchain-ai/langchain) - A development framework for composing models, tools, retrieval, and agents. <sub>Updated 2026-11-12 · ★ 149.4k · MIT</sub>
- [CrewAI](https://github.com/crewAIInc/crewAI) - Organizes multi-agent collaboration through roles and tasks. <sub>Updated 2026-11-13 · ★ 60.8k · MIT</sub>
- [AutoGen](https://github.com/microsoft/autogen) - Microsoft's framework for multi-agent conversations and orchestration. <sub>Updated 2026-11-12 · ★ 61.8k · CC-BY-4.0</sub>
- [Google ADK](https://github.com/google/adk-python) - Google's development framework for code-first agents, evaluation, and deployment. <sub>Updated 2026-11-13 · ★ 22.2k · Apache-2.0</sub>
- [smolagents](https://github.com/huggingface/smolagents) - A lightweight, code-based agent framework from Hugging Face. <sub>Updated 2026-11-10 · ★ 30.3k · Apache-2.0</sub>
- [Agno](https://github.com/agno-agi/agno) - A lightweight agent framework with support for models, tools, knowledge, and memory. <sub>Updated 2026-11-13 · ★ 43.2k · Apache-2.0</sub>
- [Mastra](https://github.com/mastra-ai/mastra) - A framework for TypeScript agents, workflows, memory, and observability. <sub>Updated 2026-11-13 · ★ 29.5k · NOASSERTION</sub>
- [DSPy](https://github.com/stanfordnlp/dspy) - Optimizes prompts and language model calls programmatically. <sub>Updated 2026-11-12 · ★ 39.0k · MIT</sub>
- [Stagehand](https://github.com/browserbase/stagehand) - A framework for building browser agents that combine natural language with Playwright. <sub>Updated 2026-11-13 · ★ 26.0k · MIT</sub>
- [mcp-use](https://github.com/mcp-use/mcp-use) - A development library for building agents and client apps with MCP. <sub>Updated 2026-11-12 · ★ 10.9k · MIT</sub>

### Multi-agent platforms

- [CAMEL](https://github.com/camel-ai/camel) - A framework for multi-agent collaboration, simulation, and research. <sub>Updated 2026-11-09 · ★ 18.0k · Apache-2.0</sub>
- [MiroFish](https://github.com/666ghj/MiroFish) - An open-source platform for swarm intelligence, prediction, and multi-agent simulation. <sub>Updated 2026-10-16 · ★ 85.4k · AGPL-3.0</sub>

### Agent infrastructure, UI and observability

- [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) - An agent harness that supports plugin extensions and tool calls. <sub>Updated 2026-11-11 · ★ 280.1k · MIT</sub>
- [E2B](https://github.com/e2b-dev/e2b) - Isolated cloud environments where agents can generate code and run tasks. <sub>Updated 2026-11-13 · ★ 14.8k · Apache-2.0</sub>
- [CopilotKit](https://github.com/CopilotKit/CopilotKit) - Tools for agent-native apps, including generative UI, shared state, and human-approval flows. <sub>Updated 2026-11-13 · ★ 38.7k · MIT</sub>
- [Headroom](https://github.com/headroomlabs-ai/headroom) - Compresses context and tool output to reduce the overhead of long agent contexts. <sub>Updated 2026-11-13 · ★ 79.5k · Apache-2.0</sub>
- [LiteLLM](https://github.com/BerriAI/litellm) - A gateway for unified multi-model calls, with routing, fallbacks, and cost governance. <sub>Updated 2026-11-13 · ★ 63.2k · NOASSERTION</sub>

<p align="right"><a href="#readme-top">Back to top ↑</a></p>

## 07. Knowledge, RAG, data ingestion and research

Projects for knowledge retrieval, memory, and research. Personal business and virtual team projects belong in category 09 (OPC and virtual teams).

### RAG and data layer

- [LlamaIndex](https://github.com/run-llama/llama_index) - A framework for data connection, indexing, retrieval, and agent applications. <sub>Updated 2026-11-11 · ★ 52.9k · MIT</sub>
- [Haystack](https://github.com/deepset-ai/haystack) - A modular framework for search, RAG, and agent pipelines. <sub>Updated 2026-11-13 · ★ 27.0k · Apache-2.0</sub>
- [Chroma](https://github.com/chroma-core/chroma) - An open-source vector database for AI applications. <sub>Updated 2026-11-07 · ★ 29.7k · Apache-2.0</sub>
- [Qdrant](https://github.com/qdrant/qdrant) - A vector database with filtering and similarity search. <sub>Updated 2026-11-13 · ★ 35.5k · Apache-2.0</sub>
- [pgvector](https://github.com/pgvector/pgvector) - Vector similarity search inside PostgreSQL. <sub>Updated 2026-11-13 · ★ 23.7k · NOASSERTION</sub>
- [GraphRAG](https://github.com/microsoft/graphrag) - Combines graph structure and community summaries with retrieval-augmented generation. <sub>Updated 2026-11-09 · ★ 36.6k · MIT</sub>
- [Azure Search OpenAI Demo](https://github.com/Azure-Samples/azure-search-openai-demo) - A representative enterprise RAG sample that combines Azure AI Search and Azure OpenAI, and is actively maintained. <sub>Updated 2026-11-13 · ★ 7.8k · MIT</sub>
- [Firecrawl](https://github.com/firecrawl/firecrawl) - A data platform that converts web pages into structured content for LLMs and agents. <sub>Updated 2026-11-13 · ★ 201.4k · AGPL-3.0</sub>
- [Crawl4AI](https://github.com/unclecode/crawl4ai) - An open-source web scraping and crawling framework for LLMs and agents. <sub>Updated 2026-11-12 · ★ 87.3k · Apache-2.0</sub>
- [MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) - A crawler for content and comments on Xiaohongshu, Douyin, Kuaishou, Bilibili, Weibo, Baidu Tieba, and Zhihu.

### Agent memory

- [Mem0](https://github.com/mem0ai/mem0) - Cross-session memory, time-aware retrieval, and agent context management. <sub>Updated 2026-11-06 · ★ 68.9k · Apache-2.0</sub>
- [Letta](https://github.com/letta-ai/letta) - A platform for stateful agents with editable long-term memory. <sub>Updated 2026-10-18 · ★ 25.4k · Apache-2.0</sub>
- [Cognee](https://github.com/topoteretes/cognee) - An agent data layer that combines knowledge graphs, memory, and retrieval. <sub>Updated 2026-11-13 · ★ 33.3k · Apache-2.0</sub>
- [OpenViking](https://github.com/volcengine/OpenViking) - A context database for agent memory, knowledge, and skills. <sub>Updated 2026-11-13 · ★ 42.1k · AGPL-3.0</sub>
- [Hindsight](https://github.com/vectorize-io/hindsight) - An agent memory system for long-term memory and personalized retrieval. <sub>Updated 2026-11-13 · ★ 60.8k · MIT</sub>

### Research and knowledge workflows

- [Claude Code Memory](https://github.com/thedotmack/claude-mem) - Saves and retrieves cross-session working context for coding agents. <sub>Updated 2026-11-13 · ★ 116.7k · Apache-2.0</sub>
- [AutoResearch](https://github.com/karpathy/autoresearch) - A workflow in which agents automatically modify experiment code and iterate on research runs. <sub>Updated 2026-03-26 · ★ 100.0k</sub>
- [Understand Anything](https://github.com/Egonex-AI/Understand-Anything) - An agent tool for codebase understanding, visualization, and knowledge-graph construction. <sub>Updated 2026-11-13 · ★ 92.5k · MIT</sub>
- [CodeGraph](https://github.com/colbymchenry/codegraph) - Models a codebase as a knowledge graph to help coding agents understand and navigate code. <sub>Updated 2026-11-01 · ★ 77.5k · MIT</sub>
- [GPT Researcher](https://github.com/assafelovic/gpt-researcher) - An autonomous deep-research agent that works with many LLM providers and can research any topic.

### RAG collections

- [Awesome RAG](https://github.com/brandonhimpfen/awesome-rag) - A starting point for RAG frameworks, vector databases, and retrieval tools. <sub>Updated 2026-09-06 · ★ <1k</sub>

<p align="right"><a href="#readme-top">Back to top ↑</a></p>

## 08. Evaluation, observability and safety

Projects for evaluation, observability, red teaming, and safety checks. They help validate quality and risk before launch.

### Evaluation and red teaming

- [Promptfoo](https://github.com/promptfoo/promptfoo) - An evaluation tool covering tests, red teaming, and CI/CD for prompts, agents, and RAG. <sub>Updated 2026-11-13 · ★ 27.1k · MIT</sub>
- [DeepEval](https://github.com/confident-ai/deepeval) - An evaluation framework for LLMs and agents. It can be paired with Langfuse and Phoenix to build an evaluation pipeline. <sub>Updated 2026-11-12 · ★ 19.5k · Apache-2.0</sub>
- [PyRIT](https://github.com/microsoft/PyRIT) - Microsoft's open-source framework for identifying generative AI risks through red teaming. <sub>Updated 2026-11-13 · ★ 4.8k · MIT</sub>
- [garak](https://github.com/NVIDIA/garak) - NVIDIA's LLM vulnerability scanner, with probes for prompt injection, data leakage, and hallucination. <sub>Updated 2026-11-06 · ★ 10.0k · Apache-2.0</sub>
- [AI Agent Evals](https://github.com/microsoft/ai-agent-evals) - Runs agent evaluations as a GitHub Action, showing how evaluation can run in CI. <sub>Updated 2026-05-20 · ★ <1k · MIT</sub>

### Observability and tracing

- [Langfuse](https://github.com/langfuse/langfuse) - A platform for tracing, evaluation, prompt management, and datasets for LLMs and agents. <sub>Updated 2026-11-13 · ★ 37.4k · NOASSERTION</sub>
- [Arize Phoenix](https://github.com/Arize-ai/phoenix) - An observability and evaluation tool for AI applications and agents. <sub>Updated 2026-11-13 · ★ 12.3k · NOASSERTION</sub>

<p align="right"><a href="#readme-top">Back to top ↑</a></p>

## 09. OPC and virtual teams

Projects designed for one-person companies, AI virtual employees, role division, and multi-agent organizations.

### Virtual teams and role systems

- [OPB-Skills](https://github.com/chendongqi/OPB-Skills) - Virtual team skills covering product, R&D, design, marketing, and operations. <sub>Updated 2026-02-11 · ★ <1k</sub>
- [AGI-Super-Team](https://github.com/aAAaqwq/AGI-Super-Team) - A multi-role, cross-client AI virtual team solution. <sub>Updated 2026-11-05 · ★ <1k · MIT</sub>
- [Agency Agents](https://github.com/msitarzewski/agency-agents) - A library of specialist roles, each defined by its responsibilities, communication style, and deliverables. <sub>Updated 2026-11-09 · ★ 168.0k · MIT</sub>
- [Kompany](https://github.com/Fei2-Labs/Kompany) - C-suite roles, task classification, and direction for multi-agent collaboration. <sub>Updated 2026-11-04 · ★ <1k · AGPL-3.0</sub>
- [solo-founder-os](https://github.com/alex-jb/solo-founder-os) - Roles, shared materials, and an agent communication scheme for independent founders. <sub>Updated 2026-07-08 · ★ <1k · MIT</sub>
- [MetaGPT](https://github.com/FoundationAgents/MetaGPT) - A multi-agent framework that simulates a software company through role division. <sub>Updated 2026-01-21 · ★ 71.3k · MIT</sub>
- [ChatDev](https://github.com/OpenBMB/ChatDev) - Collaborative software development simulated by agents with different roles. <sub>Updated 2026-11-06 · ★ 34.7k · Apache-2.0</sub>

### Solo business operating systems

- [opc-skill](https://github.com/jiangye1314/opc-skill) - Positioning, validation, customer acquisition, delivery, and review workflows for one-person companies in China. <sub>Updated 2026-05-05 · ★ <1k · NOASSERTION</sub>
- [opc](https://github.com/seedquan/opc) - A reference for product development roles, workflows, and quality gates. <sub>Updated 2026-04-10 · ★ <1k · MIT</sub>
- [opc_agent](https://github.com/CroTuyuzhe/opc_agent) - A boss agent and an extensible skill plugin scheme. <sub>Updated 2026-04-24 · ★ <1k · Apache-2.0</sub>
- [opc-x](https://github.com/opc-x/opc-x) - A composition concept covering departments, atomic skills, and an execution protocol for one-person companies. <sub>Updated 2026-10-23 · ★ <1k</sub>

### OPC collections

- [Awesome Solo AI](https://github.com/yerdaulet-damir/awesome-solo-ai) - AI tools and business pipelines for independent developers and solopreneurs. <sub>Updated 2026-11-06 · ★ <1k · NOASSERTION</sub>

<p align="right"><a href="#readme-top">Back to top ↑</a></p>

## 10. Learning, workshops and cookbooks

Materials and tutorials for building a general understanding, learning paths, and technical background.

### Courses and tutorials

- [AI Agents for Beginners](https://github.com/microsoft/ai-agents-for-beginners) - A 12-lesson introductory course on AI agents from Microsoft. <sub>Updated 2026-11-07 · ★ 79.5k · MIT</sub>
- [Datawhale Self-LLM](https://github.com/datawhalechina/self-llm) - Chinese-language materials on deploying, using, and practicing large language models. <sub>Updated 2026-10-29 · ★ 32.8k · Apache-2.0</sub>
- [LLM Course](https://github.com/mlabonne/llm-course) - A course that teaches LLMs through a roadmap and Colab notebooks. <sub>Updated 2026-02-05 · ★ 85.1k · Apache-2.0</sub>
- [Hugging Face Diffusion Models Course](https://github.com/huggingface/diffusion-models-class) - Hugging Face's online course materials on diffusion models. <sub>Updated 2026-11-10 · ★ 4.4k · Apache-2.0</sub>
- [Hands-on LLM App Development (llm-universe)](https://github.com/datawhalechina/llm-universe) - A beginner-friendly tutorial on building LLM applications. <sub>Updated 2026-08-27 · ★ 14.3k</sub>
- [Happy-LLM](https://github.com/datawhalechina/happy-llm) - A Chinese-language tutorial covering large language models, from principles to training pipelines. <sub>Updated 2026-08-08 · ★ 34.9k · NOASSERTION</sub>
- [OpenAI Cookbook](https://github.com/openai/openai-cookbook) - Examples and practical guides for using the OpenAI API. <sub>Updated 2026-11-12 · ★ 77.1k · MIT</sub>
- [Learn Claude Code](https://github.com/shareAI-lab/learn-claude-code) - A tutorial project that explains coding agent architecture and tool calling through step-by-step implementation. <sub>Updated 2026-10-27 · ★ 80.4k · MIT</sub>
- [Generative AI for Beginners](https://github.com/microsoft/generative-ai-for-beginners) - Microsoft's official, systematic introductory course on generative AI. <sub>Updated 2026-11-12 · ★ 123.4k · MIT</sub>
- [OpenAI Workshop](https://github.com/microsoft/OpenAIWorkshop) - A still-maintained OpenAI and Azure AI workshop that works well as a follow-up to introductory courses. <sub>Updated 2026-11-06 · ★ <1k · MIT</sub>

### Reference collections

- [Awesome Generative AI](https://github.com/steven2358/awesome-generative-ai) - A collection of generative AI projects, tools, and learning resources. <sub>Updated 2026-10-30 · ★ 12.8k · CC0-1.0</sub>
- [Awesome Generative AI Guide](https://github.com/aishwaryanr/awesome-generative-ai-guide) - A generative AI guide organized by use, build, understanding, and learning path. <sub>Updated 2026-11-02 · ★ 30.3k · MIT</sub>
- [Awesome Artificial Intelligence](https://github.com/owainlewis/awesome-artificial-intelligence) - An entry point to AI courses, books, lectures, papers, and tools. <sub>Updated 2026-08-15 · ★ 16.8k · MIT</sub>
- [Awesome LLM Papers](https://github.com/guyulongcs/Awesome-LLM-papers) - An index of LLM papers and topic-focused readings. <sub>Updated 2026-09-19 · ★ <1k</sub>
- [Awesome ChatGPT Prompts](https://github.com/f/prompts.chat) - Prompt examples and basic references. <sub>Updated 2026-11-13 · ★ 177.0k · NOASSERTION</sub>
- [Awesome ChatGPT Prompts Zh](https://github.com/PlexPt/awesome-chatgpt-prompts-zh) - A collection of Chinese prompt examples. <sub>Missing</sub>

<p align="right"><a href="#readme-top">Back to top ↑</a></p>

## 11. Azure AI, Foundry and Copilot

Skills, MCP, Agent Framework, samples, and development tools across the Microsoft cloud and GitHub Copilot ecosystem.

### Official discovery portals

- [Azure-Samples](https://github.com/Azure-Samples) - Azure's official samples organization page, for discovering more service samples.

### Skills and MCP extensions

- [Azure Skills](https://github.com/microsoft/azure-skills) - A comprehensive entry point for Azure Skills, Azure MCP, and Foundry MCP. <sub>Updated 2026-11-12 · ★ 1.6k · MIT</sub>
- [Microsoft Skills](https://github.com/microsoft/skills) - A modular collection of agent skills for Microsoft Foundry and Azure development. <sub>Updated 2026-11-12 · ★ 3.2k · MIT</sub>
- [GitHub Awesome Copilot](https://github.com/github/awesome-copilot) - GitHub's official resource hub for Copilot agents, instructions, skills, hooks, and plugins. <sub>Updated 2026-11-13 · ★ 41.1k · MIT</sub>
- [Skills and MCPs](https://github.com/msftse-org/skills-and-mcps) - MAF Python SDK, Foundry Agents, and MCP practice examples. <sub>Updated 2026-03-11 · ★ <1k</sub>

### Agent SDKs and frameworks

- [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) - The development entry point and examples for Microsoft Agent Framework. <sub>Updated 2026-11-13 · ★ 14.7k · MIT</sub>
- [Semantic Kernel](https://github.com/microsoft/semantic-kernel) - Microsoft's SDK for models, plugins, and agent orchestration. <sub>Updated 2026-11-12 · ★ 28.8k · MIT</sub>
- [GitHub Copilot SDK](https://github.com/github/copilot-sdk) - An SDK for integrating GitHub Copilot capabilities into applications and automation workflows. <sub>Updated 2026-11-13 · ★ 10.7k · MIT</sub>

### Foundry and Azure samples

- [Azure AI Foundry Agents Samples](https://github.com/Azure-Samples/ai-foundry-agents-samples) - The official sample collection for Foundry Agents. <sub>Updated 2026-02-03 · ★ <1k · MIT</sub>
- [Python OpenAI Demos](https://github.com/Azure-Samples/python-openai-demos) - Python examples for OpenAI, RAG, vector search, and hybrid search. <sub>Updated 2026-11-12 · ★ <1k · MIT</sub>
- [Agent Playground](https://github.com/Azure-Samples/agent-playground) - A playground for planning, orchestration, memory, error recovery, and agent communication. <sub>Updated 2026-04-21 · ★ <1k · MIT</sub>
- [Agent Framework Samples](https://github.com/kinfey/Agent-Framework-Samples) - Samples for Microsoft Agent Framework, GitHub Models, and Foundry Agent Service. <sub>Updated 2026-06-20 · ★ <1k · MIT</sub>
- [Azure AI Samples](https://github.com/Azure-Samples/azureai-samples) - The official community samples entry point for Azure AI, good for a service overview. <sub>Updated 2026-10-06 · ★ <1k · MIT</sub>
- [Foundry Samples](https://github.com/microsoft-foundry/foundry-samples) - Microsoft Foundry's main samples repository, covering multi-language and infrastructure samples. <sub>Updated 2026-11-13 · ★ <1k · MIT</sub>

<p align="right"><a href="#readme-top">Back to top ↑</a></p>

## 12. Awesome collections

Navigational repositories for discovering AI applications, agents, skills, MCP, Copilot, LLM learning materials, and personal business tools. These projects are indexes or resource catalogs, not runnable frameworks or applications.

### Awesome lists

- [Awesome LLM Apps](https://github.com/Shubhamsaboo/awesome-llm-apps) - Runnable AI agents, agent skills, RAG projects, and LLM applications. <sub>Updated 2026-11-11 · ★ 144.5k · Apache-2.0</sub>
- [Awesome AI Agents](https://github.com/e2b-dev/awesome-ai-agents) - A starting point for discovering AI agent projects, frameworks, and apps. <sub>Updated 2026-08-21 · ★ 30.9k · NOASSERTION</sub>
- [Awesome Claude Skills](https://github.com/ComposioHQ/awesome-claude-skills) - A curated directory of Claude Skills and related resources. <sub>Updated 2026-09-18 · ★ 79.4k</sub>
- [Awesome Agent Skills](https://github.com/VoltAgent/awesome-agent-skills) - A starting point for discovering skills across agent clients. <sub>Updated 2026-11-05 · ★ 37.1k · MIT</sub>
- [Awesome Skills](https://github.com/vivy-yi/awesome-skills) - An aggregated list of cross-domain agent skills. <sub>Updated 2026-06-07 · ★ <1k · MIT</sub>
- [Awesome MCP Servers](https://github.com/punkpeye/awesome-mcp-servers) - A discovery directory of MCP servers. <sub>Updated 2026-11-06 · ★ 97.7k · MIT</sub>
- [Awesome RAG](https://github.com/brandonhimpfen/awesome-rag) - A starting point for RAG frameworks, vector databases, and retrieval tools. <sub>Updated 2026-09-06 · ★ <1k</sub>
- [Awesome Solo AI](https://github.com/yerdaulet-damir/awesome-solo-ai) - AI tools and business pipelines for independent developers and solopreneurs. <sub>Updated 2026-11-06 · ★ <1k · NOASSERTION</sub>
- [Awesome Generative AI](https://github.com/steven2358/awesome-generative-ai) - A collection of generative AI projects, tools, and learning resources. <sub>Updated 2026-10-30 · ★ 12.8k · CC0-1.0</sub>
- [Awesome Generative AI Guide](https://github.com/aishwaryanr/awesome-generative-ai-guide) - A generative AI guide organized by use, build, understanding, and learning path. <sub>Updated 2026-11-02 · ★ 30.3k · MIT</sub>
- [Awesome Artificial Intelligence](https://github.com/owainlewis/awesome-artificial-intelligence) - AI courses, books, lectures, papers, and tools. <sub>Updated 2026-08-15 · ★ 16.8k · MIT</sub>
- [Awesome LLM Papers](https://github.com/guyulongcs/Awesome-LLM-papers) - An index of LLM papers and topic-focused readings. <sub>Updated 2026-09-19 · ★ <1k</sub>
- [Awesome ChatGPT Prompts](https://github.com/f/prompts.chat) - Prompt examples and basic references. <sub>Updated 2026-11-13 · ★ 177.0k · NOASSERTION</sub>
- [Awesome ChatGPT Prompts Zh](https://github.com/PlexPt/awesome-chatgpt-prompts-zh) - A collection of Chinese prompt examples. <sub>Missing</sub>
- [GitHub Awesome Copilot](https://github.com/github/awesome-copilot) - GitHub's official resource hub for Copilot agents, instructions, skills, hooks, and plugins. <sub>Updated 2026-11-13 · ★ 41.1k · MIT</sub>

### Course collections

Learning resources labeled `Course`, including full courses, lesson-by-lesson tutorials, learning paths, and hands-on practice for beginners. Some also appear in other categories by topic.

- [AI Agents for Beginners](https://github.com/microsoft/ai-agents-for-beginners) - A 12-lesson introductory course on AI agents from Microsoft. <sub>Updated 2026-11-07 · ★ 79.5k · MIT</sub>
- [MCP for Beginners](https://github.com/microsoft/mcp-for-beginners) - A cross-language introductory course on the Model Context Protocol. <sub>Updated 2026-11-13 · ★ 17.6k · MIT</sub>
- [LLM Course](https://github.com/mlabonne/llm-course) - A course that teaches LLMs through a roadmap and Colab notebooks. <sub>Updated 2026-02-05 · ★ 85.1k · Apache-2.0</sub>
- [Hugging Face Diffusion Models Course](https://github.com/huggingface/diffusion-models-class) - Hugging Face's online course materials on diffusion models. <sub>Updated 2026-11-10 · ★ 4.4k · Apache-2.0</sub>
- [Datawhale Self-LLM](https://github.com/datawhalechina/self-llm) - Chinese-language course materials on deploying, using, and practicing large language models. <sub>Updated 2026-10-29 · ★ 32.8k · Apache-2.0</sub>
- [Hands-on LLM App Development (llm-universe)](https://github.com/datawhalechina/llm-universe) - A beginner-friendly tutorial on building LLM applications. <sub>Updated 2026-08-27 · ★ 14.3k</sub>
- [Happy-LLM](https://github.com/datawhalechina/happy-llm) - A Chinese-language tutorial covering large language models, from principles to training pipelines. <sub>Updated 2026-08-08 · ★ 34.9k · NOASSERTION</sub>

<p align="right"><a href="#readme-top">Back to top ↑</a></p>

## Watchlist

Projects with unique value but limited recent maintenance or maturity. They are not promoted to the top and are listed for reference only.

- [Awesome LLM](https://github.com/Hannibal046/Awesome-LLM) - An overview of LLM academic, engineering, deployment, and course resources. <sub>Updated 2025-07-31 · ★ 27.5k · CC0-1.0</sub>
- [AgentVerse](https://github.com/OpenBMB/AgentVerse) - A platform for multi-agent simulation, research, and collaborative experiments. <sub>Updated 2024-09-09 · ★ 5.2k · Apache-2.0</sub>
- [STORM](https://github.com/stanford-oval/storm) - A system that generates cited knowledge articles through multi-round research. <sub>Updated 2025-09-30 · ★ 31.9k · MIT</sub>

<p align="right"><a href="#readme-top">Back to top ↑</a></p>

## Legacy / Archived

Archived or superseded projects that still have historical value. They are not counted in the main recommendations.

- [Anthropic Courses](https://github.com/anthropics/courses) - Anthropic's official educational courses and practice materials. <sub>Updated 2026-08-28 · ★ 23.0k · NOASSERTION · Archived</sub>
- [Flowise](https://github.com/FlowiseAI/Flowise) - Build LLM, agent, and RAG workflows visually. <sub>Updated 2026-08-13 · ★ 55.6k · NOASSERTION · Archived</sub>
- [Daytona](https://github.com/daytonaio/daytona) - Isolated execution environments for AI-generated code and agent tasks. <sub>Updated 2026-07-24 · ★ 71.3k · Archived</sub>
- [Kimi CLI](https://github.com/MoonshotAI/kimi-cli) - A coding agent that supports planning, code understanding, and terminal operations. <sub>Updated 2026-09-22 · ★ 11.4k · Apache-2.0 · Archived</sub>

<p align="right"><a href="#readme-top">Back to top ↑</a></p>

## Inclusion Criteria

**Priority inclusion**

- Directly related to its category, mainly within the GenAI, agent, skills, MCP, coding agent, RAG, or Copilot ecosystems.
- Publicly accessible, with documentation, examples, or an installation method you can try.
- Shows signs of recent maintenance. Archived or long-unmaintained projects may be kept, but they are labeled.
- Provides direct value to individual developers, solo founders, or small teams.

**Usually not included**

- Marketing-only pages, waitlists, or projects without real code or documentation.
- General-purpose software unrelated to the topic, or one-off experimental repositories.
- Projects that contain malicious code, infringe copyright, or are clearly misleading.
- Forks, mirrors, or same-named repositories that duplicate an already included project.

**Additional conventions**

- A project appears only once within a category. Category 12 is a navigational collection and may repeat topics from other categories.
- A project may fit several categories. Its primary use decides where it goes.
- A URL is updated only when a project is renamed or moved and the original link is broken or wrong.

## Contributing

Recommendations are welcome through Issues or Pull Requests. Please include, where possible:

1. The official project name and repository link;
2. The suggested category (01–12);
3. A one-line description covering the project's positioning, core capabilities, and main use cases;
4. Reasons for inclusion, such as documentation quality, maintenance status, or relevance to this list.

Entries follow this format:

```markdown
- [Project Name](<repository-url>) - One-line description.
```

- Use ` - ` between the project name and the description, and end the description with a period.
- Do not add star counts or update badges manually. The automated workflow maintains them.

## Maintenance

- The [track-upstream](.github/workflows/track-upstream.yml) workflow runs daily at 01:00 UTC. It refreshes each entry's update date, stars, and license, records a daily star snapshot, and updates the 7-day Star Growth Top 15 board.
- Do not edit the content between `<!-- BEGIN:recent-updates -->` and `<!-- END:recent-updates -->` by hand.
- The `<sub>` metadata at the end of each entry is generated by the script. Manual edits will be overwritten.
- The script flags broken links and archived projects automatically. Confirm them manually before taking action.
- `README.md` (English) is the source of truth, and `README.zh-CN.md` is its Chinese translation. The workflow refreshes both files, but descriptions are edited by hand in each one.

## License and attribution

This repository is licensed under the MIT License. See [LICENSE](LICENSE) for the full text. Project names, links, and brief factual descriptions are included for resource discovery and research. Each external project's code, documentation, images, and license belong to its original owners. Check the license and terms of the corresponding repository before using or redistributing it.
