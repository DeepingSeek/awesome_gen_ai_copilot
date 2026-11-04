<a name="readme-top"></a>

<div align="center">

<!-- Banner: add assets/banner.png to the repository, then uncomment the next line to display it
<img src="assets/banner.png" alt="Awesome Gen AI Copilot banner" width="100%">
-->

<h1>Awesome Gen AI Copilot</h1>

<p><strong>A curated list of GenAI and Copilot projects for solo developers, super individuals, and small teams.</strong><br>Covers Agents, Skills, Workflows, MCP, Coding Agents, RAG, Azure AI, Foundry, and GitHub Copilot.</p>

<p>
	<a href="https://awesome.re"><img src="https://awesome.re/badge.svg" alt="Awesome"></a>
	<a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-2ea44f?labelColor=555" alt="MIT License"></a>
</p>

<p><sub>Agents · Skills · Workflows · MCP · Coding agents · RAG · Azure AI · Foundry</sub></p>

</div>

<p align="center"><a href="README.md">中文</a> · <b>English</b></p>

This list is compiled from multiple Awesome projects and official resources, then regrouped by real-world use case. It favors entry points that are suitable for public release, easy to browse, and useful for further research. The full candidate catalog is maintained separately as local research material.

## Start Here

Not sure how Agents, Skills, Workflows, and MCP differ? Read the [classification guide](#classification) first, then choose an entry point by goal.

| I want to... | Start here |
|---|---|
| Have AI complete a task independently | [01. Agents and AI applications](#01-agents-and-ai-applications) |
| Reuse ready-made Skills packages | [02. Agent skills and plugins](#02-agent-skills-and-plugins) |
| Chain AI steps into an automated workflow | [03. Workflows and automation](#03-workflows-and-automation) |
| Connect agents to data, browsers, and tools | [04. MCP, protocols and tool connections](#04-mcp-protocols-and-tool-connections) |
| Use AI to write code and review PRs | [05. Coding agents and assistants](#05-coding-agents-and-assistants) |
| Build my own agent application | [06. Agent frameworks, runtimes and sandboxes](#06-agent-frameworks-runtimes-and-sandboxes) |
| Build knowledge-base Q&A or long-term memory | [07. Knowledge, RAG, data ingestion and research](#07-knowledge-rag-data-ingestion-and-research) |
| Run evaluations, observability, or safety checks | [08. Evaluation, observability and safety](#08-evaluation-observability-and-safety) |
| Set up a one-person company or a virtual team | [09. OPC and virtual teams](#09-opc-and-virtual-teams) |
| Learn the fundamentals of LLMs systematically | [10. Learning, workshops and cookbooks](#10-learning-workshops-and-cookbooks) |
| Build within the Azure or GitHub Copilot ecosystem | [11. Azure AI, Foundry and Copilot](#11-azure-ai-foundry-and-copilot) |
| Find official Azure / Foundry samples | [11. Azure AI, Foundry and Copilot](#11-azure-ai-foundry-and-copilot) |

## Explore by Category

<table align="center" width="100%">
  <tr>
    <td align="center" width="33%" valign="top">
      <big><big>🤖</big></big><br>
      <a href="#01-agents-and-ai-applications"><b>01. Agents and AI applications</b></a><br>
      <sub>Agents and applications that take a goal and execute it independently</sub>
    </td>
    <td align="center" width="33%" valign="top">
      <big><big>🧩</big></big><br>
      <a href="#02-agent-skills-and-plugins"><b>02. Agent skills and plugins</b></a><br>
      <sub>Reusable capability packages that agents can call</sub>
    </td>
    <td align="center" width="33%" valign="top">
      <big><big>🔁</big></big><br>
      <a href="#03-workflows-and-automation"><b>03. Workflows and automation</b></a><br>
      <sub>Processes made of triggers, steps, and approvals</sub>
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
      <sub>Navigational collections for discovering resources</sub>
    </td>
  </tr>
</table>

## Classification

The same project may have several capabilities. Classify it by its primary usage and positioning. These are editorial guidelines, not official definitions from the projects.

| Concept | Core definition |
|---|---|
| Agent | Software that can take a goal, plan, and execute tasks on its own. |
| Skill | A reusable capability package that an agent calls. It encapsulates task steps, tool boundaries, inputs and outputs, and domain knowledge. |
| Workflow | A process that chains triggers, steps, tools, state, and human approvals to complete a task. |
| Framework | An SDK or runtime for building agents, managing state, and orchestrating tool calls. |

MCP is covered separately. It is a protocol and ecosystem that lets agents access data, tools, and external systems in a structured way, so it is not compared at the same level as the four concepts above.

## Curated Picks

The following projects are editor's picks, selected by hand based on license, maintenance status, and category representativeness. They **do not represent an objective ranking** and are not sorted by stars. Curated picks also appear in their categories. Each top-level category recommends at most one item.

- [nanobot](https://github.com/HKUDS/nanobot) - A lightweight personal AI agent that runs locally, good for trying things out on your own machine. <sub>Updated 2026-11-03 · ★ 49.8k · MIT</sub>
- [Anthropic Skills](https://github.com/anthropics/skills) - The official reference collection for Claude Skills, useful for understanding how Skills are structured and written. <sub>Updated 2026-10-28 · ★ 186.9k</sub>
- [Langflow](https://github.com/langflow-ai/langflow) - Visually orchestrates LLM, agent, and RAG applications, good for quick prototypes. <sub>Updated 2026-11-03 · ★ 156.3k · MIT</sub>
- [Model Context Protocol](https://github.com/modelcontextprotocol/modelcontextprotocol) - The entry point to the MCP specification and ecosystem, good for learning the basic concepts of tool connections. <sub>Updated 2026-11-03 · ★ 9.6k · NOASSERTION</sub>
- [Codex](https://github.com/openai/codex) - An open-source terminal coding agent with sandboxed execution, suitable for trying out in a local repository. <sub>Updated 2026-11-03 · ★ 132.9k · Apache-2.0</sub>
- [LangGraph](https://github.com/langchain-ai/langgraph) - A graph orchestration framework for stateful, resumable agent workflows, for developers who need precise control over flow. <sub>Updated 2026-11-03 · ★ 44.4k · MIT</sub>
- [LlamaIndex](https://github.com/run-llama/llama_index) - A framework for data connection, indexing, and retrieval, good for building RAG applications. <sub>Updated 2026-10-26 · ★ 52.8k · MIT</sub>
- [AI Agents for Beginners](https://github.com/microsoft/ai-agents-for-beginners) - A 12-lesson introductory course on AI agents from Microsoft, good for a systematic start. <sub>Updated 2026-11-02 · ★ 78.8k · MIT</sub>
- [GitHub Copilot SDK](https://github.com/github/copilot-sdk) - Integrates GitHub Copilot capabilities into your own applications and automation workflows. <sub>Updated 2026-11-03 · ★ 10.7k · MIT</sub>

## Recent Updates

<!-- BEGIN:recent-updates -->
1. [Significant-Gravitas/AutoGPT](https://github.com/Significant-Gravitas/AutoGPT) <sub>2026-11-03 · commit<br>Repository has new pushes</sub>
2. [openclaw/openclaw](https://github.com/openclaw/openclaw) <sub>2026-11-03 · commit<br>fix(telegram): refresh typing after delivered messages (191709)；fix(google): ke…</sub>
3. [langgenius/dify](https://github.com/langgenius/dify) <sub>2026-11-03 · commit<br>feat(dify-ui): add PasswordField and use it for every password input (45249)；ci…</sub>
4. [BerriAI/litellm](https://github.com/BerriAI/litellm) <sub>2026-11-03 · commit<br>feat(realtime)!: support latest OpenAI audio models (35600)；fix(anthropic): sen…</sub>
5. [n8n-io/n8n](https://github.com/n8n-io/n8n) <sub>2026-11-03 · commit<br>chore: Flaky test: insights.controller.test.ts (2 master or merge-queue commits…</sub>
6. [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) <sub>2026-11-03 · commit<br>fix(desktop): an inline update report belongs to the failure it was opened for；…</sub>
7. [Codium-ai/pr-agent](https://github.com/Codium-ai/pr-agent) <sub>2026-11-03 · commit<br>fix: deprecate no-op self-review marker keys (4598)；fix(azure): resolve agent i…</sub>
8. [garrytan/gstack](https://github.com/garrytan/gstack) <sub>2026-11-03 · commit<br>v1.94.8.0 fix(approvals): no identifying approval text in public-repo PR bodies…</sub>
9. [QwenLM/qwen-code](https://github.com/QwenLM/qwen-code) <sub>2026-11-03 · commit<br>fix(core): require explicit trust for project frontmatter and LSP (16182)；fix(w…</sub>
10. [mastra-ai/mastra](https://github.com/mastra-ai/mastra) <sub>2026-11-03 · commit<br>feat(playground-ui): Knowledge explorer tree and graph that load lazily at scal…</sub>
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

Agent products that take a goal, plan, and execute tasks independently, plus collections that help you discover application forms.

### Agents


- [AutoGPT](https://github.com/Significant-Gravitas/AutoGPT) - An open-source project exploring autonomous task decomposition, tool use, and agent execution. <sub>Updated 2026-11-03 · ★ 187.9k · NOASSERTION</sub>
- [OpenClaw](https://github.com/openclaw/openclaw) - A self-hosted personal assistant runtime with channels, Skills, memory, and tool orchestration. <sub>Updated 2026-11-03 · ★ 393.8k · MIT</sub>
- [Hermes Agent](https://github.com/NousResearch/hermes-agent) - A personal agent with memory, tools, browser control, and long-running tasks. <sub>Updated 2026-11-03 · ★ 260.0k · MIT</sub>
- [LibreChat](https://github.com/LibreChat-AI/LibreChat) - A chat application supporting multiple models, agents, MCP, and self-hosted deployment. <sub>Updated 2026-11-03 · ★ 46.7k · MIT</sub>
- [nanobot](https://github.com/HKUDS/nanobot) - A lightweight personal AI agent that runs locally. <sub>Updated 2026-11-03 · ★ 49.8k · MIT</sub>
- [QwenPaw](https://github.com/agentscope-ai/QwenPaw) - A self-hostable personal AI assistant project. <sub>Updated 2026-11-03 · ★ 37.3k · Apache-2.0</sub>
- [Khoj](https://github.com/khoj-ai/khoj) - An AI agent that combines a personal knowledge base, research, and automation. <sub>Updated 2026-08-02 · ★ 38.0k · AGPL-3.0</sub>
- [AnythingLLM](https://github.com/Mintplex-Labs/anything-llm) - A local-first app for documents, RAG, agents, and workspaces. <sub>Updated 2026-11-03 · ★ 67.9k · MIT</sub>
- [Agent Zero](https://github.com/agent0ai/agent-zero) - An extensible personal AI agent with tools, sub-agents, and local execution. <sub>Updated 2026-11-01 · ★ 19.7k · NOASSERTION</sub>
- [Open Interpreter](https://github.com/openinterpreter/openinterpreter) - An agent that executes code, calls tools, and completes computer tasks from natural-language instructions. <sub>Updated 2026-11-01 · ★ 68.8k · Apache-2.0</sub>
### Browser agents and web automation

- [Browser Use](https://github.com/browser-use/browser-use) - Lets agents complete web operations and tasks through a browser. <sub>Updated 2026-11-02 · ★ 119.9k · MIT</sub>
- [Skyvern](https://github.com/Skyvern-AI/skyvern) - A browser automation platform based on vision and LLMs. <sub>Updated 2026-11-03 · ★ 23.3k · AGPL-3.0</sub>
- [agent-browser](https://github.com/vercel-labs/agent-browser) - An agent automation tool with CLI and browser control. <sub>Updated 2026-11-03 · ★ 45.3k · Apache-2.0</sub>
- [UI-TARS desktop](https://github.com/bytedance/UI-TARS-desktop) - A multimodal agent application for desktop interaction. <sub>Updated 2026-10-09 · ★ 39.5k · Apache-2.0</sub>
### Agent project collections

- [Awesome LLM Apps](https://github.com/Shubhamsaboo/awesome-llm-apps) - A collection of runnable AI agents, Agent Skills, RAG, and LLM applications. <sub>Updated 2026-10-22 · ★ 143.8k · Apache-2.0</sub>
- [Awesome AI Agents](https://github.com/e2b-dev/awesome-ai-agents) - A discovery entry point for AI agent projects, frameworks, and applications. <sub>Updated 2026-08-21 · ★ 30.8k · NOASSERTION</sub>

<p align="right"><a href="#readme-top">Back to top ↑</a></p>

## 02. Agent skills and plugins

Task steps, tool boundaries, inputs and outputs, and domain knowledge packaged as capability packages that an agent can call. They are not agents that plan and execute goals on their own.

### Skills catalogs

- [Anthropic Skills](https://github.com/anthropics/skills) - The official reference collection of Claude Skills, including skills for documents, spreadsheets, and presentations. <sub>Updated 2026-10-28 · ★ 186.9k</sub>
- [Awesome Claude Skills](https://github.com/ComposioHQ/awesome-claude-skills) - A curated directory of Claude Skills and related resources. <sub>Updated 2026-09-18 · ★ 78.6k</sub>
- [Awesome Agent Skills](https://github.com/VoltAgent/awesome-agent-skills) - A discovery and reference entry point for Skills across agent clients. <sub>Updated 2026-11-02 · ★ 36.8k · MIT</sub>
- [Awesome Skills](https://github.com/vivy-yi/awesome-skills) - An aggregated list of cross-domain Agent Skills. <sub>Updated 2026-06-07 · ★ <1k · MIT</sub>
- [Awesome OpenClaw Skills](https://github.com/VoltAgent/awesome-openclaw-skills) - A curated directory of OpenClaw Skills. <sub>Updated 2026-10-30 · ★ 53.5k · MIT</sub>
- [Claude Code Official Plugins](https://github.com/anthropics/claude-plugins-official) - The official Claude Code plugin directory, with reusable agent capabilities. <sub>Updated 2026-11-03 · ★ 45.9k · Apache-2.0</sub>

### Skills packages and domain capabilities

- [Superpowers](https://github.com/obra/superpowers) - A skills framework and engineering workflow for software development agents. <sub>Updated 2026-11-03 · ★ 311.4k · MIT</sub>
- [Agent Skills](https://github.com/addyosmani/agent-skills) - Engineering skills and command workflows for coding agents. <sub>Updated 2026-11-01 · ★ 112.9k · MIT</sub>
- [Vercel Agent Skills](https://github.com/vercel-labs/agent-skills) - A collection of Agent Skills for the Vercel ecosystem. <sub>Updated 2026-10-28 · ★ 33.4k</sub>
- [NVIDIA Skills](https://github.com/NVIDIA/skills) - Skills for scenarios such as Physical AI, CUDA, simulation, and RAG. <sub>Updated 2026-11-02 · ★ 3.8k · Apache-2.0</sub>
- [.NET Agent Skills](https://github.com/dotnet/skills) - Skills for .NET, AI, RAG, agent, and MCP development. <sub>Updated 2026-11-03 · ★ 5.8k · MIT</sub>
- [Trail of Bits Skills](https://github.com/trailofbits/skills) - Skills for security research, vulnerability discovery, auditing, and verification. <sub>Updated 2026-11-02 · ★ 8.0k · CC-BY-SA-4.0</sub>
- [Context Engineering Skills](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) - A collection of skills for context engineering and agent task design. <sub>Updated 2026-10-12 · ★ 18.3k · MIT</sub>
- [Agent Skills for Marketing](https://github.com/aaron-he-zhu/aaron-marketing-skills) - Marketing skills covering SEO, GEO, advertising, email, and growth operations. <sub>Updated 2026-11-03 · ★ 3.1k · Apache-2.0</sub>
- [Matt Pocock Skills](https://github.com/mattpocock/skills) - A collection of Skills for Claude Code, along with engineering practices. <sub>Updated 2026-11-01 · ★ 310.6k · MIT</sub>
- [Andrej Karpathy Skills](https://github.com/multica-ai/andrej-karpathy-skills) - A practice collection that turns engineering methods into Coding Agent Skills. <sub>Updated 2026-04-20 · ★ 228.7k</sub>
- [UI UX Pro Max Skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) - A skill package for agent UI design, frontend implementation, and UX review. <sub>Updated 2026-11-02 · ★ 144.5k · MIT</sub>
- [Taste Skill](https://github.com/Leonxlnx/taste-skill) - A Skill that constrains agent design judgment and output quality. <sub>Updated 2026-11-03 · ★ 109.0k · MIT</sub>
- [Last 30 Days Skill](https://github.com/mvanhorn/last30days-skill) - An agent Skill for cross-site search, research, and summarization. <sub>Updated 2026-11-01 · ★ 66.4k · MIT</sub>
- [Marketing Skills](https://github.com/coreyhaines31/marketingskills) - A collection of Skills covering marketing, SEO, growth, and conversion workflows. <sub>Updated 2026-10-31 · ★ 58.2k · MIT</sub>
- [Obsidian Skills](https://github.com/kepano/obsidian-skills) - Agent Skills for Obsidian knowledge management and automation. <sub>Updated 2026-09-15 · ★ 50.7k · MIT</sub>
- [Scientific Agent Skills](https://github.com/K-Dense-AI/scientific-agent-skills) - Agent Skills for scientific search, analysis, and writing. <sub>Updated 2026-11-02 · ★ 55.9k · MIT</sub>
- [Diagram Design](https://github.com/cathrynlavery/diagram-design) - An agent Skill for generating architecture and flow diagrams. <sub>Updated 2026-11-03 · ★ 64.5k · MIT</sub>
- [Wshobson Agents](https://github.com/wshobson/agents) - A collection of plugins, Skills, and workflows across multiple coding agent harnesses. <sub>Updated 2026-11-02 · ★ 42.1k · MIT</sub>

<p align="right"><a href="#readme-top">Back to top ↑</a></p>

## 03. Workflows and automation

Projects that chain triggers, steps, tools, state, and human approvals. The focus is how to organize one complete execution, not a single capability.

### Workflow automation

- [n8n](https://github.com/n8n-io/n8n) - A visual workflow automation platform with AI agent nodes and connectors to external systems. <sub>Updated 2026-11-03 · ★ 209.4k · NOASSERTION</sub>
- [Dify](https://github.com/langgenius/dify) - A development platform for visually building agents, LLM apps, and workflows. <sub>Updated 2026-11-03 · ★ 160.3k · NOASSERTION</sub>
- [Langflow](https://github.com/langflow-ai/langflow) - A workflow platform for visually orchestrating LLM, agent, and RAG applications. <sub>Updated 2026-11-03 · ★ 156.3k · MIT</sub>

### Agent workflow suites

- [DeerFlow](https://github.com/bytedance/deer-flow) - An agent workflow project for research, writing, and knowledge processing. <sub>Updated 2026-11-03 · ★ 84.9k · MIT</sub>
- [gstack](https://github.com/garrytan/gstack) - A collection of Claude Code roles and workflows for software development. <sub>Updated 2026-11-03 · ★ 138.7k · MIT</sub>
- [Everything Claude Code](https://github.com/affaan-m/ECC) - A collection of agents, hooks, and development workflows for Claude Code. <sub>Updated 2026-11-02 · ★ 295.9k · MIT</sub>
- [Ruflo](https://github.com/ruvnet/ruflo) - A runtime for agent orchestration, memory management, and autonomous workflows. <sub>Updated 2026-11-03 · ★ 80.7k · MIT</sub>
- [BMAD Method](https://github.com/bmad-code-org/BMAD-METHOD) - A method of roles, phases, and delivery workflows for AI-assisted software development. <sub>Updated 2026-11-03 · ★ 54.9k · NOASSERTION</sub>
- [Oh My ClaudeCode](https://github.com/Yeachan-Heo/oh-my-claudecode) - A multi-agent collaboration and task orchestration extension for Claude Code. <sub>Updated 2026-11-03 · ★ 40.5k · MIT</sub>

<p align="right"><a href="#readme-top">Back to top ↑</a></p>

## 04. MCP, protocols and tool connections

Lets agents access data, tools, browsers, and external systems in a structured way.

### Protocols and interaction standards

- [Model Context Protocol](https://github.com/modelcontextprotocol/modelcontextprotocol) - The MCP protocol, specification, and ecosystem entry point. <sub>Updated 2026-11-03 · ★ 9.6k · NOASSERTION</sub>
- [Agent Client Protocol](https://github.com/agentclientprotocol/agent-client-protocol) - A protocol for connecting code editors and agent runtimes. <sub>Updated 2026-11-03 · ★ 4.6k · Apache-2.0</sub>
- [AG-UI](https://github.com/ag-ui-protocol/ag-ui) - Streams agent state, events, and human-in-the-loop interactions to front-end applications. <sub>Updated 2026-11-03 · ★ 17.0k · MIT</sub>

### Servers, clients and connectors

- [MCP Servers](https://github.com/modelcontextprotocol/servers) - Official MCP server reference implementations and examples. <sub>Updated 2026-10-29 · ★ 91.8k · NOASSERTION</sub>
- [GitHub MCP Server](https://github.com/github/github-mcp-server) - Lets agents use GitHub data and operations through MCP. <sub>Updated 2026-11-02 · ★ 34.2k · MIT</sub>
- [Playwright MCP](https://github.com/microsoft/playwright-mcp) - A browser operation MCP server based on Playwright. <sub>Updated 2026-11-01 · ★ 39.1k · Apache-2.0</sub>
- [AWS MCP](https://github.com/awslabs/mcp) - A collection of MCP servers for AWS services, knowledge, and tools. <sub>Updated 2026-11-03 · ★ 9.9k · Apache-2.0</sub>
- [Context7](https://github.com/upstash/context7) - Gives agents up-to-date library and framework documentation through MCP. <sub>Updated 2026-11-03 · ★ 64.1k · MIT</sub>
- [MCP Registry](https://github.com/modelcontextprotocol/registry) - The official MCP server registry, an authoritative entry point for discovering MCP servers.
- [Agent-Reach](https://github.com/Panniantong/Agent-Reach) - A toolkit that gives agents access to internet information. <sub>Updated 2026-11-01 · ★ 108.2k · MIT</sub>

### Collections and courses

- [Awesome MCP Servers](https://github.com/punkpeye/awesome-mcp-servers) - A discovery directory of MCP servers. <sub>Updated 2026-11-02 · ★ 97.2k · MIT</sub>
- [MCP for Beginners](https://github.com/microsoft/mcp-for-beginners) - A cross-language introductory course on the Model Context Protocol. <sub>Updated 2026-11-02 · ★ 17.6k · MIT</sub>

<p align="right"><a href="#readme-top">Back to top ↑</a></p>

## 05. Coding agents and assistants

Executable agents for requirement clarification, code writing, testing, review, and software delivery. General-purpose workflow suites are listed under Workflows.

### Coding agent products

- [Claude Code](https://github.com/anthropics/claude-code) - A terminal coding agent for code repositories, with tool calling and development workflows. <sub>Updated 2026-11-03 · ★ 154.3k</sub>
- [Codex](https://github.com/openai/codex) - An open-source terminal coding agent with sandboxed execution. <sub>Updated 2026-11-03 · ★ 132.9k · Apache-2.0</sub>
- [OpenCode](https://github.com/anomalyco/opencode) - An open-source, model-agnostic terminal coding agent. <sub>Updated 2026-11-03 · ★ 224.2k · MIT</sub>
- [Gemini CLI](https://github.com/google-gemini/gemini-cli) - Google's open-source terminal agent for Gemini, with terminal and MCP workflows. <sub>Updated 2026-11-03 · ★ 108.7k · Apache-2.0</sub>
- [OpenHands](https://github.com/OpenHands/OpenHands) - A software development agent platform with terminal, browser, and sandboxed execution. <sub>Updated 2026-11-03 · ★ 92.5k · MIT</sub>
- [Cline](https://github.com/cline/cline) - A model-agnostic agent that runs tool calls and coding tasks in VS Code. <sub>Updated 2026-11-03 · ★ 71.2k · Apache-2.0</sub>
- [Aider](https://github.com/Aider-AI/aider) - A terminal pair-programming tool for Git repositories. <sub>Updated 2026-05-22 · ★ 49.9k · Apache-2.0</sub>
- [SWE-agent](https://github.com/SWE-agent/SWE-agent) - A software engineering agent for real GitHub issues. <sub>Updated 2026-11-02 · ★ 20.7k · MIT</sub>
- [Continue](https://github.com/continuedev/continue) - An open-source coding assistant and agent platform that connects to different models. <sub>Updated 2026-11-03 · ★ 36.4k · Apache-2.0</sub>
- [Qwen Code](https://github.com/QwenLM/qwen-code) - An open-source agent for terminal-based code development and task execution. <sub>Updated 2026-11-03 · ★ 28.9k · Apache-2.0</sub>
- [Pi](https://github.com/earendil-works/pi) - A coding agent and extensible runtime for terminal task execution. <sub>Updated 2026-11-03 · ★ 119.7k · MIT</sub>
- [Goose](https://github.com/aaif-goose/goose) - An extensible code and task execution agent with tool and model integration. <sub>Updated 2026-11-03 · ★ 56.2k · Apache-2.0</sub>
- [CC Switch](https://github.com/farion1231/cc-switch) - A desktop tool for managing coding agent configuration and model switching. <sub>Updated 2026-11-03 · ★ 151.4k · MIT</sub>
- [Claude Code Router](https://github.com/musistudio/claude-code-router) - Provides model routing and tool orchestration for Claude Code. <sub>Updated 2026-10-10 · ★ 38.0k · MIT</sub>
- [Tabby](https://github.com/TabbyML/tabby) - A self-hostable code completion and coding assistant platform. <sub>Updated 2026-06-30 · ★ 33.9k · NOASSERTION</sub>
- [GPT Pilot](https://github.com/Pythagora-io/gpt-pilot) - A development tool that uses agents to help generate and iterate on software projects. <sub>Updated 2026-06-18 · ★ 33.6k · NOASSERTION</sub>

### Review and repository automation

- [PR-Agent](https://github.com/The-PR-Agent/pr-agent) - Automatically analyzes pull requests and generates reviews, descriptions, and improvement suggestions. <sub>Updated 2026-11-03 · ★ 14.2k · MIT</sub>
- [AGENTS.md](https://github.com/agentsmd/agents.md) - A general format for declaring agent constraints, commands, and workflows in a code repository. <sub>Updated 2026-09-10 · ★ 25.3k · MIT</sub>

<p align="right"><a href="#readme-top">Back to top ↑</a></p>

## 06. Agent frameworks, runtimes and sandboxes

SDKs, frameworks, and infrastructure for building agents, managing state, orchestrating multiple agents, and running tool-calling workflows.

### Agent frameworks and SDKs

- [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) - A Python agent SDK with tools, handoffs, guardrails, and tracing. <sub>Updated 2026-11-03 · ★ 30.5k · MIT</sub>
- [Pydantic AI](https://github.com/pydantic/pydantic-ai) - A Python framework for type-safe, structured-output, and testable agents. <sub>Updated 2026-11-03 · ★ 21.0k · MIT</sub>
- [LangGraph](https://github.com/langchain-ai/langgraph) - A graph orchestration framework for stateful, branching, and resumable agent workflows. <sub>Updated 2026-11-03 · ★ 44.4k · MIT</sub>
- [LangChain](https://github.com/langchain-ai/langchain) - A development framework for composing models, tools, retrieval, and agents. <sub>Updated 2026-11-03 · ★ 148.9k · MIT</sub>
- [CrewAI](https://github.com/crewAIInc/crewAI) - Organizes multi-agent collaboration through roles and tasks. <sub>Updated 2026-11-03 · ★ 60.4k · MIT</sub>
- [AutoGen](https://github.com/microsoft/autogen) - Microsoft's multi-agent conversation and orchestration framework. <sub>Updated 2026-10-28 · ★ 61.7k · CC-BY-4.0</sub>
- [Google ADK](https://github.com/google/adk-python) - Google's development framework for code-first agents, evaluation, and deployment. <sub>Updated 2026-11-03 · ★ 22.1k · Apache-2.0</sub>
- [smolagents](https://github.com/huggingface/smolagents) - A lightweight, code-based agent framework from Hugging Face. <sub>Updated 2026-10-29 · ★ 30.2k · Apache-2.0</sub>
- [Agno](https://github.com/agno-agi/agno) - A lightweight agent framework with support for models, tools, knowledge, and memory. <sub>Updated 2026-11-03 · ★ 43.0k · Apache-2.0</sub>
- [Mastra](https://github.com/mastra-ai/mastra) - A framework for TypeScript agents, workflows, memory, and observability. <sub>Updated 2026-11-03 · ★ 29.3k · NOASSERTION</sub>
- [DSPy](https://github.com/stanfordnlp/dspy) - Optimizes prompts and language model calls programmatically. <sub>Updated 2026-11-02 · ★ 38.9k · MIT</sub>
- [Stagehand](https://github.com/browserbase/stagehand) - A framework for building browser agents that combine natural language with Playwright. <sub>Updated 2026-11-03 · ★ 25.9k · MIT</sub>
- [mcp-use](https://github.com/mcp-use/mcp-use) - A development library for building agents and client apps with MCP. <sub>Updated 2026-11-02 · ★ 10.8k · MIT</sub>


### Multi-agent platforms

- [CAMEL](https://github.com/camel-ai/camel) - A framework for multi-agent collaboration, simulation, and research. <sub>Updated 2026-11-02 · ★ 18.0k · Apache-2.0</sub>
- [MiroFish](https://github.com/666ghj/MiroFish) - An open-source platform for swarm intelligence, prediction, and multi-agent simulation. <sub>Updated 2026-10-16 · ★ 83.6k · AGPL-3.0</sub>

### Agent infrastructure, UI and observability

- [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) - An agent harness that supports plugin extensions and tool calls. <sub>Updated 2026-10-30 · ★ 270.2k · MIT</sub>
- [E2B](https://github.com/e2b-dev/e2b) - Isolated cloud environments where agents can generate code and run tasks. <sub>Updated 2026-11-02 · ★ 14.7k · Apache-2.0</sub>
- [CopilotKit](https://github.com/CopilotKit/CopilotKit) - Agent-native applications, generative UI, shared state, and human approval flows. <sub>Updated 2026-11-03 · ★ 38.5k · MIT</sub>
- [Headroom](https://github.com/headroomlabs-ai/headroom) - Compresses context and tool output to reduce the overhead of long agent contexts. <sub>Updated 2026-11-03 · ★ 78.7k · Apache-2.0</sub>
- [LiteLLM](https://github.com/BerriAI/litellm) - A gateway for unified multi-model calls, routing, fallback, and cost governance. <sub>Updated 2026-11-03 · ★ 62.6k · NOASSERTION</sub>

<p align="right"><a href="#readme-top">Back to top ↑</a></p>

## 07. Knowledge, RAG, data ingestion and research

Projects for knowledge retrieval, memory, and research. Personal business and virtual team projects are in the OPC category.

### RAG and data layer

- [LlamaIndex](https://github.com/run-llama/llama_index) - A framework for data connection, indexing, retrieval, and agent applications. <sub>Updated 2026-10-26 · ★ 52.8k · MIT</sub>
- [Haystack](https://github.com/deepset-ai/haystack) - A modular framework for search, RAG, and agent pipelines. <sub>Updated 2026-11-03 · ★ 26.9k · Apache-2.0</sub>
- [Chroma](https://github.com/chroma-core/chroma) - An open-source vector database for AI applications. <sub>Updated 2026-10-30 · ★ 29.6k · Apache-2.0</sub>
- [Qdrant](https://github.com/qdrant/qdrant) - A vector database that supports filtering and similarity search. <sub>Updated 2026-11-02 · ★ 35.4k · Apache-2.0</sub>
- [pgvector](https://github.com/pgvector/pgvector) - Vector similarity search inside PostgreSQL. <sub>Updated 2026-10-31 · ★ 23.6k · NOASSERTION</sub>
- [GraphRAG](https://github.com/microsoft/graphrag) - A system that combines graph structure and community summaries with retrieval-augmented generation. <sub>Updated 2026-11-02 · ★ 36.5k · MIT</sub>
- [Azure Search OpenAI Demo](https://github.com/Azure-Samples/azure-search-openai-demo) - A representative enterprise RAG sample combining Azure AI Search and Azure OpenAI, actively maintained.
- [Firecrawl](https://github.com/firecrawl/firecrawl) - A data platform that converts web pages into structured content for LLMs and agents. <sub>Updated 2026-11-03 · ★ 198.1k · AGPL-3.0</sub>
- [Crawl4AI](https://github.com/unclecode/crawl4ai) - An open-source web scraping and crawling framework for LLMs and agents. <sub>Updated 2026-11-02 · ★ 86.8k · Apache-2.0</sub>

### Agent memory

- [Mem0](https://github.com/mem0ai/mem0) - Cross-session memory, time-aware retrieval, and agent context management. <sub>Updated 2026-10-30 · ★ 68.3k · Apache-2.0</sub>
- [Letta](https://github.com/letta-ai/letta) - A platform for stateful agents with editable long-term memory. <sub>Updated 2026-10-18 · ★ 25.3k · Apache-2.0</sub>
- [Cognee](https://github.com/topoteretes/cognee) - An agent data layer that combines knowledge graphs, memory, and retrieval. <sub>Updated 2026-11-03 · ★ 33.0k · Apache-2.0</sub>
- [OpenViking](https://github.com/volcengine/OpenViking) - A context database for agent memory, knowledge, and Skills. <sub>Updated 2026-11-03 · ★ 41.4k · AGPL-3.0</sub>
- [Hindsight](https://github.com/vectorize-io/hindsight) - An agent memory system for long-term memory and personalized retrieval. <sub>Updated 2026-11-02 · ★ 58.2k · MIT</sub>

### Research and knowledge workflows

- [Claude Code Memory](https://github.com/thedotmack/claude-mem) - Saves and retrieves cross-session working context for coding agents. <sub>Updated 2026-11-03 · ★ 111.1k · Apache-2.0</sub>
- [AutoResearch](https://github.com/karpathy/autoresearch) - A workflow in which agents modify experiment code automatically and iterate on research runs. <sub>Updated 2026-03-26 · ★ 99.1k</sub>
- [Understand Anything](https://github.com/Egonex-AI/Understand-Anything) - An agent tool for codebase understanding, visualization, and knowledge-graph construction. <sub>Updated 2026-10-26 · ★ 90.1k · MIT</sub>
- [CodeGraph](https://github.com/colbymchenry/codegraph) - Models a codebase as a knowledge graph to help coding agents understand and navigate code. <sub>Updated 2026-11-01 · ★ 76.3k · MIT</sub>

### RAG collections

- [Awesome RAG](https://github.com/brandonhimpfen/awesome-rag) - A discovery entry point for RAG frameworks, vector databases, and retrieval tools. <sub>Updated 2026-09-06 · ★ <1k</sub>


<p align="right"><a href="#readme-top">Back to top ↑</a></p>

## 08. Evaluation, observability and safety

Projects for evaluation, observability, red teaming, and safety checks. They help validate quality and risk before launch.

### Evaluation and red teaming

- [Promptfoo](https://github.com/promptfoo/promptfoo) - An evaluation tool covering tests, red teaming, and CI/CD for prompts, agents, and RAG.
- [DeepEval](https://github.com/confident-ai/deepeval) - An active evaluation framework for LLMs and agents that can be paired with Langfuse and Phoenix to form an evaluation chain.
- [PyRIT](https://github.com/microsoft/PyRIT) - Microsoft's open-source framework for identifying generative AI risks and red teaming.
- [garak](https://github.com/NVIDIA/garak) - NVIDIA's LLM vulnerability scanner, with probes for prompt injection, data leakage, and hallucination.
- [AI Agent Evals](https://github.com/microsoft/ai-agent-evals) - Runs agent evaluations as a GitHub Action, showing how evaluation can enter CI.

### Observability and tracing

- [Langfuse](https://github.com/langfuse/langfuse) - A platform for tracing, evaluation, prompt management, and datasets for LLMs and agents. <sub>Updated 2026-11-03 · ★ 36.9k · NOASSERTION</sub>
- [Arize Phoenix](https://github.com/Arize-ai/phoenix) - An observability and evaluation tool for AI applications and agents. <sub>Updated 2026-11-03 · ★ 12.1k · NOASSERTION</sub>

<p align="right"><a href="#readme-top">Back to top ↑</a></p>

## 09. OPC and virtual teams

Projects designed for one-person companies, AI virtual employees, role division, and multi-agent organizations.

### Virtual teams and role systems

- [OPB-Skills](https://github.com/chendongqi/OPB-Skills) - Virtual team Skills covering product, R&D, design, marketing, and operations. <sub>Updated 2026-02-11 · ★ <1k</sub>
- [AGI-Super-Team](https://github.com/aAAaqwq/AGI-Super-Team) - A multi-role, cross-client AI virtual team solution. <sub>Updated 2026-11-03 · ★ <1k · MIT</sub>
- [Agency Agents](https://github.com/msitarzewski/agency-agents) - A library of specialist roles, each defined with responsibilities, communication style, and deliverables. <sub>Updated 2026-10-25 · ★ 166.2k · MIT</sub>
- [Kompany](https://github.com/Fei2-Labs/Kompany) - C-suite roles, task classification, and direction for multi-agent collaboration. <sub>Updated 2026-10-24 · ★ <1k · AGPL-3.0</sub>
- [solo-founder-os](https://github.com/alex-jb/solo-founder-os) - Roles, shared materials, and an agent communication scheme for independent founders. <sub>Updated 2026-07-08 · ★ <1k · MIT</sub>
- [MetaGPT](https://github.com/FoundationAgents/MetaGPT) - A multi-agent framework that simulates a software company through role division. <sub>Updated 2026-01-21 · ★ 71.1k · MIT</sub>
- [ChatDev](https://github.com/OpenBMB/ChatDev) - Collaborative software development simulated by agents with different roles. <sub>Updated 2026-10-30 · ★ 34.6k · Apache-2.0</sub>

### Solo business operating systems

- [opc-skill](https://github.com/jiangye1314/opc-skill) - Positioning, validation, customer acquisition, delivery, and review workflows for one-person companies in China. <sub>Updated 2026-05-05 · ★ <1k · NOASSERTION</sub>
- [opc](https://github.com/seedquan/opc) - A reference for product development roles, workflows, and quality gates. <sub>Updated 2026-04-10 · ★ <1k · MIT</sub>
- [opc_agent](https://github.com/CroTuyuzhe/opc_agent) - A Boss Agent and extensible Skill plugin scheme. <sub>Updated 2026-04-24 · ★ <1k · Apache-2.0</sub>
- [opc-x](https://github.com/opc-x/opc-x) - A composition concept of departments, atomic skills, and a one-person company execution protocol. <sub>Updated 2026-10-23 · ★ <1k</sub>

### OPC collections

- [Awesome Solo AI](https://github.com/yerdaulet-damir/awesome-solo-ai) - AI tools and business pipelines for independent developers and solopreneurs. <sub>Updated 2026-10-26 · ★ <1k · NOASSERTION</sub>

<p align="right"><a href="#readme-top">Back to top ↑</a></p>

## 10. Learning, workshops and cookbooks

Materials and tutorials for building a general understanding, learning paths, and technical background.

### Courses and tutorials

- [AI Agents for Beginners](https://github.com/microsoft/ai-agents-for-beginners) - A 12-lesson introductory course on AI agents from Microsoft. <sub>Updated 2026-11-02 · ★ 78.8k · MIT</sub>
- [Datawhale Self-LLM](https://github.com/datawhalechina/self-llm) - Chinese materials on deploying, using, and practicing large language models. <sub>Updated 2026-10-29 · ★ 32.7k · Apache-2.0</sub>
- [LLM Course](https://github.com/mlabonne/llm-course) - A course for learning LLMs through a roadmap and Colab notebooks. <sub>Updated 2026-02-05 · ★ 84.9k · Apache-2.0</sub>
- [Hugging Face Diffusion Models Course](https://github.com/huggingface/diffusion-models-class) - Hugging Face's online course materials on diffusion models. <sub>Updated 2026-10-14 · ★ 4.4k · Apache-2.0</sub>
- [Hands-on LLM App Development (llm-universe)](https://github.com/datawhalechina/llm-universe) - A beginner-friendly tutorial on developing LLM applications. <sub>Updated 2026-08-27 · ★ 14.3k</sub>
- [Happy-LLM](https://github.com/datawhalechina/happy-llm) - A Chinese tutorial that covers large language models from principles to training pipelines. <sub>Updated 2026-08-08 · ★ 34.7k · NOASSERTION</sub>
- [OpenAI Cookbook](https://github.com/openai/openai-cookbook) - Examples and practical guides for using the OpenAI API. <sub>Updated 2026-11-03 · ★ 76.9k · MIT</sub>
- [Learn Claude Code](https://github.com/shareAI-lab/learn-claude-code) - A tutorial project that explains coding agent architecture and tool calling through step-by-step implementation. <sub>Updated 2026-10-27 · ★ 79.8k · MIT</sub>
- [Generative AI for Beginners](https://github.com/microsoft/generative-ai-for-beginners) - Microsoft's official, systematic introductory course on generative AI.
- [OpenAI Workshop](https://github.com/microsoft/OpenAIWorkshop) - A still-maintained OpenAI and Azure AI workshop that serves as an advanced path after introductory courses.

### Reference collections

- [Awesome Generative AI](https://github.com/steven2358/awesome-generative-ai) - A collection of generative AI projects, tools, and learning resources. <sub>Updated 2026-10-30 · ★ 12.8k · CC0-1.0</sub>
- [Awesome Generative AI Guide](https://github.com/aishwaryanr/awesome-generative-ai-guide) - A generative AI guide organized by use, build, understanding, and learning paths. <sub>Updated 2026-11-02 · ★ 30.1k · MIT</sub>
- [Awesome Artificial Intelligence](https://github.com/owainlewis/awesome-artificial-intelligence) - An entry point to AI courses, books, lectures, papers, and tools. <sub>Updated 2026-08-15 · ★ 16.8k · MIT</sub>
- [Awesome LLM Papers](https://github.com/guyulongcs/Awesome-LLM-papers) - An index of LLM papers and topic-focused readings. <sub>Updated 2026-09-19 · ★ <1k</sub>
- [Awesome ChatGPT Prompts](https://github.com/f/prompts.chat) - Prompt examples and basic references. <sub>Updated 2026-11-03 · ★ 175.7k · NOASSERTION</sub>
- [Awesome ChatGPT Prompts Zh](https://github.com/PlexPt/awesome-chatgpt-prompts-zh) - A collection of Chinese prompt examples. <sub>Updated 2026-04-28 · ★ 64.3k · MIT</sub>

<p align="right"><a href="#readme-top">Back to top ↑</a></p>

## 11. Azure AI, Foundry and Copilot

Skills, MCP, Agent Framework, samples, and development tools across the Microsoft cloud and GitHub Copilot ecosystem.

### Official discovery portals

- [Azure-Samples](https://github.com/Azure-Samples) - Azure's official samples organization page, for discovering more service samples.

### Skills and MCP extensions

- [Azure Skills](https://github.com/microsoft/azure-skills) - A comprehensive entry point for Azure Skills, Azure MCP, and Foundry MCP. <sub>Updated 2026-11-02 · ★ 1.6k · MIT</sub>
- [Microsoft Skills](https://github.com/microsoft/skills) - A modular collection of Agent Skills for Microsoft Foundry and Azure development. <sub>Updated 2026-11-02 · ★ 3.2k · MIT</sub>
- [GitHub Awesome Copilot](https://github.com/github/awesome-copilot) - GitHub's official resource hub for Copilot agents, instructions, skills, hooks, and plugins. <sub>Updated 2026-11-03 · ★ 40.7k · MIT</sub>
- [Skills and MCPs](https://github.com/msftse-org/skills-and-mcps) - MAF Python SDK, Foundry Agents, and MCP practice examples. <sub>Updated 2026-03-11 · ★ <1k</sub>

### Agent SDKs and frameworks

- [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) - The development entry point and examples for Microsoft Agent Framework. <sub>Updated 2026-11-03 · ★ 14.5k · MIT</sub>
- [Semantic Kernel](https://github.com/microsoft/semantic-kernel) - Microsoft's SDK for models, plugins, and agent orchestration. <sub>Updated 2026-11-02 · ★ 28.7k · MIT</sub>
- [GitHub Copilot SDK](https://github.com/github/copilot-sdk) - An SDK for integrating GitHub Copilot capabilities into applications and automation workflows. <sub>Updated 2026-11-03 · ★ 10.7k · MIT</sub>

### Foundry and Azure samples

- [Azure AI Foundry Agents Samples](https://github.com/Azure-Samples/ai-foundry-agents-samples) - The official sample collection for Foundry Agents. <sub>Updated 2026-02-03 · ★ <1k · MIT</sub>
- [Python OpenAI Demos](https://github.com/Azure-Samples/python-openai-demos) - Python examples for OpenAI, RAG, vector search, and hybrid search. <sub>Updated 2026-10-29 · ★ <1k · MIT</sub>
- [Agent Playground](https://github.com/Azure-Samples/agent-playground) - A playground for planning, orchestration, memory, error recovery, and agent communication. <sub>Updated 2026-04-21 · ★ <1k · MIT</sub>
- [Agent Framework Samples](https://github.com/kinfey/Agent-Framework-Samples) - Samples for Microsoft Agent Framework, GitHub Models, and Foundry Agent Service. <sub>Updated 2026-06-20 · ★ <1k · MIT</sub>
- [Azure AI Samples](https://github.com/Azure-Samples/azureai-samples) - The official community samples entry point for Azure AI, suited to a service overview.
- [Foundry Samples](https://github.com/microsoft-foundry/foundry-samples) - Microsoft Foundry's main samples repository, covering multi-language and infrastructure samples.

<p align="right"><a href="#readme-top">Back to top ↑</a></p>

## 12. Awesome collections

Navigational repositories for discovering AI applications, agents, Skills, MCP, Copilot, LLM learning materials, and personal business tools. These projects are indexes or resource catalogs, not runnable frameworks or applications.

### Awesome lists

- [Awesome LLM Apps](https://github.com/Shubhamsaboo/awesome-llm-apps) - Runnable AI agents, Agent Skills, RAG, and LLM applications. <sub>Updated 2026-10-22 · ★ 143.8k · Apache-2.0</sub>
- [Awesome AI Agents](https://github.com/e2b-dev/awesome-ai-agents) - A discovery entry point for AI agent projects, frameworks, and applications. <sub>Updated 2026-08-21 · ★ 30.8k · NOASSERTION</sub>
- [Awesome Claude Skills](https://github.com/ComposioHQ/awesome-claude-skills) - A curated directory of Claude Skills and related resources. <sub>Updated 2026-09-18 · ★ 78.6k</sub>
- [Awesome Agent Skills](https://github.com/VoltAgent/awesome-agent-skills) - A discovery and reference entry point for Skills across agent clients. <sub>Updated 2026-11-02 · ★ 36.8k · MIT</sub>
- [Awesome Skills](https://github.com/vivy-yi/awesome-skills) - An aggregated list of cross-domain Agent Skills. <sub>Updated 2026-06-07 · ★ <1k · MIT</sub>
- [Awesome MCP Servers](https://github.com/punkpeye/awesome-mcp-servers) - A discovery directory of MCP servers. <sub>Updated 2026-11-02 · ★ 97.2k · MIT</sub>
- [Awesome RAG](https://github.com/brandonhimpfen/awesome-rag) - A discovery entry point for RAG frameworks, vector databases, and retrieval tools. <sub>Updated 2026-09-06 · ★ <1k</sub>
- [Awesome Solo AI](https://github.com/yerdaulet-damir/awesome-solo-ai) - AI tools and business pipelines for independent developers and solopreneurs. <sub>Updated 2026-10-26 · ★ <1k · NOASSERTION</sub>
- [Awesome Generative AI](https://github.com/steven2358/awesome-generative-ai) - A collection of generative AI projects, tools, and learning resources. <sub>Updated 2026-10-30 · ★ 12.8k · CC0-1.0</sub>
- [Awesome Generative AI Guide](https://github.com/aishwaryanr/awesome-generative-ai-guide) - A generative AI guide organized by use, build, understanding, and learning paths. <sub>Updated 2026-11-02 · ★ 30.1k · MIT</sub>
- [Awesome Artificial Intelligence](https://github.com/owainlewis/awesome-artificial-intelligence) - AI courses, books, lectures, papers, and tools. <sub>Updated 2026-08-15 · ★ 16.8k · MIT</sub>
- [Awesome LLM Papers](https://github.com/guyulongcs/Awesome-LLM-papers) - An index of LLM papers and topic-focused readings. <sub>Updated 2026-09-19 · ★ <1k</sub>
- [Awesome ChatGPT Prompts](https://github.com/f/prompts.chat) - Prompt examples and basic references. <sub>Updated 2026-11-03 · ★ 175.7k · NOASSERTION</sub>
- [Awesome ChatGPT Prompts Zh](https://github.com/PlexPt/awesome-chatgpt-prompts-zh) - A collection of Chinese prompt examples. <sub>Updated 2026-04-28 · ★ 64.3k · MIT</sub>
- [GitHub Awesome Copilot](https://github.com/github/awesome-copilot) - GitHub's official resource hub for Copilot agents, instructions, skills, hooks, and plugins. <sub>Updated 2026-11-03 · ★ 40.7k · MIT</sub>

### Course collections

Learning collections marked `Course`, including courses, lesson-by-lesson tutorials, learning paths, and hands-on practice for beginners. They can also appear in other categories by topic.

- [AI Agents for Beginners](https://github.com/microsoft/ai-agents-for-beginners) - A 12-lesson introductory course on AI agents from Microsoft. <sub>Updated 2026-11-02 · ★ 78.8k · MIT</sub>
- [MCP for Beginners](https://github.com/microsoft/mcp-for-beginners) - A cross-language introductory course on the Model Context Protocol. <sub>Updated 2026-11-02 · ★ 17.6k · MIT</sub>
- [LLM Course](https://github.com/mlabonne/llm-course) - A course for learning LLMs through a roadmap and Colab notebooks. <sub>Updated 2026-02-05 · ★ 84.9k · Apache-2.0</sub>
- [Hugging Face Diffusion Models Course](https://github.com/huggingface/diffusion-models-class) - Hugging Face's online course materials on diffusion models. <sub>Updated 2026-10-14 · ★ 4.4k · Apache-2.0</sub>
- [Datawhale Self-LLM](https://github.com/datawhalechina/self-llm) - Chinese course materials on deploying, using, and practicing large language models. <sub>Updated 2026-10-29 · ★ 32.7k · Apache-2.0</sub>
- [Hands-on LLM App Development (llm-universe)](https://github.com/datawhalechina/llm-universe) - A beginner-friendly tutorial on developing LLM applications. <sub>Updated 2026-08-27 · ★ 14.3k</sub>
- [Happy-LLM](https://github.com/datawhalechina/happy-llm) - A Chinese tutorial that covers large language models from principles to training pipelines. <sub>Updated 2026-08-08 · ★ 34.7k · NOASSERTION</sub>

<p align="right"><a href="#readme-top">Back to top ↑</a></p>

## Watchlist

Projects with unique value but limited maintenance activity or maturity. They are not promoted to the top and are listed for reference only.

- [Awesome LLM](https://github.com/Hannibal046/Awesome-LLM) - An overview of LLM academic, engineering, deployment, and course resources. <sub>Updated 2025-07-31 · ★ 27.5k · CC0-1.0</sub>
- [AgentVerse](https://github.com/OpenBMB/AgentVerse) - A platform for multi-agent simulation, research, and collaborative experiments. <sub>Updated 2024-09-09 · ★ 5.2k · Apache-2.0</sub>
- [STORM](https://github.com/stanford-oval/storm) - A system that generates cited knowledge articles through multi-round research. <sub>Updated 2025-09-30 · ★ 31.8k · MIT</sub>

<p align="right"><a href="#readme-top">Back to top ↑</a></p>

## Legacy / Archived

Archived or superseded projects that still have historical reference value. They are not counted in the main recommendations.

- [Anthropic Courses](https://github.com/anthropics/courses) - Anthropic's official educational courses and practice materials. <sub>Updated 2026-08-28 · ★ 23.0k · NOASSERTION · Archived</sub>
- [Flowise](https://github.com/FlowiseAI/Flowise) - Build LLM, agent, and RAG workflows visually. <sub>Updated 2026-08-13 · ★ 55.5k · NOASSERTION · Archived</sub>
- [Daytona](https://github.com/daytonaio/daytona) - Isolated execution environments for AI-generated code and agent tasks. <sub>Updated 2026-07-24 · ★ 71.4k · Archived</sub>
- [Kimi CLI](https://github.com/MoonshotAI/kimi-cli) - A coding agent that supports planning, code understanding, and terminal operations. <sub>Updated 2026-09-22 · ★ 11.4k · Apache-2.0 · Archived</sub>

<p align="right"><a href="#readme-top">Back to top ↑</a></p>

## Inclusion Criteria

**Priority inclusion**

- Directly related to the definition of its category, mainly for the GenAI, Agent, Skills, MCP, Coding Agent, RAG, or Copilot ecosystems.
- Publicly accessible, with documentation, examples, or an installation method that can be tried.
- Shows signs of recent maintenance. Archived or long-unmaintained projects may be kept, but they are labeled.
- Provides direct value to individual developers, solo founders, or small teams.

**Usually not included**

- Marketing-only pages, waitlists, or projects without real code or documentation.
- General-purpose software unrelated to the topic, or one-off experimental repositories.
- Projects that contain malicious code, infringe copyright, or are clearly misleading.
- Forks, mirrors, or same-named repositories that duplicate an already included project.

**Additional conventions**

- The same project appears only once within the same category. Category 12 is a navigational collection and may repeat topic categories.
- A project may fit several categories. Its primary usage decides where it goes.
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
- Do not add stars or update badges manually. The automated task maintains them.

## Maintenance

- The [track-upstream](.github/workflows/track-upstream.yml) workflow runs daily at 01:00 UTC. It refreshes each entry's update date, stars, and license, and updates Recent Updates.
- Do not edit the content between `<!-- BEGIN:recent-updates -->` and `<!-- END:recent-updates -->` by hand.
- The `<sub>` metadata at the end of each entry is generated by the script. Manual edits will be overwritten.
- When the script detects a broken link or an archived project, it flags it automatically. Confirm manually before acting.
- This English version (`README.en.md`) is maintained by hand and mirrors `README.md`, which remains the source of truth. The tracking workflow updates only `README.md`.

## License and attribution

This repository is licensed under the MIT License. See [LICENSE](LICENSE) for the full text. Project names, links, and brief factual descriptions are used for resource discovery and research reference. External projects' code, documentation, images, and licenses belong to their original owners. Read the license and terms of the corresponding repository before use or redistribution.
