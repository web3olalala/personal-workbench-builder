# Personal Workbench Builder

一个面向非技术用户的跨平台 Agent Skill：先理解用户真实的生活或工作流程，再规划功能、判断可行性、制作 3 套可点击 UI、完成开发与数据持久化，并在需要时接入多端同步、PWA 和正式部署。

本项目遵循开放的 [Agent Skills 规范](https://agentskills.io/specification)，核心 `SKILL.md` 不依赖某一家模型或 Agent 的专属字段。可在 Codex、Claude Code、Cursor、Gemini CLI、GitHub Copilot、WorkBuddy、千问办公（QwenWork）等支持 Agent Skills 的工具中使用；其他能够读取本地文件并执行脚本的 Agent，也可以手动加载 `SKILL.md`。

它不是固定 Dashboard 模板，也不会在用户只说一句“我想做个工作台”时立即开始写代码。

## 为什么叫这个名字

`personal-workbench-builder` 直接表达了 Skill 的用途：为不同职业、习惯和工作流的人搭建个人工作台。它比带个人昵称的名称更容易被其他人理解、搜索和复用，同时保留了原始构想的核心。

## 能做什么

- 用每轮 2～3 个普通问题了解用户，而不是让小白自己写产品需求。
- 从真实流程、痛点、高频任务和长期记录需求中推导功能。
- 在开发前标出哪些功能可直接实现、依赖第三方服务、需要授权，或暂时无法稳定实现。
- 在功能确认后制作 3 套结构和交互都明显不同的可点击 Dashboard。
- 根据用户选择开发正式版本，支持桌面与手机。
- 按实际需要选择本地持久化或带账号隔离的云端同步。
- 在长期使用场景中完成正式部署、PWA 和系统化 QA。
- 通过 `.personal-workbench/` 保存项目状态，支持以后增量增加功能或重做界面。

## 安装

打开你正在使用的 Agent，把下面这句话发给它：

```text
请帮我安装这个项目作为 Skill：
https://github.com/web3olalala/personal-workbench-builder
```

安装完成后，告诉 Agent：

```text
使用 personal-workbench-builder，帮我创建个人工作台。
```

就这么简单。你不需要自己下载文件、输入命令或判断安装目录，交给 Agent 处理即可。Codex、Claude Code、Cursor、Gemini CLI、GitHub Copilot、WorkBuddy 和千问办公等支持 Skill 的 Agent 都可以使用。

启动后，Skill 会先通过聊天了解你的需求，不会立即开始写代码。

## 工作方式

```text
了解用户与现状
  → 梳理真实工作流
  → 功能与可行性方案
  → 用户确认功能
  → 3 套可点击 UI
  → 用户确认方向
  → 正式开发
  → 持久化 / 同步 / 自动化
  → 部署与 PWA
  → QA
  → 长期增量迭代
```

功能方案和最终 UI 是两个明确的确认点。进入正式开发后，普通技术选择、代码实现、Bug 修复和测试由 Agent 自主完成；只有账号授权、API Key、数据权限、外部服务创建和必须由本人决定的事项会暂停等待用户。

## 项目状态

Skill 会在目标项目中维护：

```text
.personal-workbench/
├── requirements.md
├── workflow.md
├── feature-map.md
├── design-choice.md
├── decisions.md
└── project-state.json
```

这些文件记录需求、已确认功能、设计选择、数据模式、外部依赖、部署状态和当前阶段。再次调用时优先读取它们，避免重复提问和从零重建。

初始化状态：

```bash
python3 scripts/init_workbench_state.py --project-root /path/to/project
```

检查状态：

```bash
python3 scripts/validate_workbench_state.py --project-root /path/to/project
```

## 可选 Starter

`assets/react-vite-pwa-starter/` 是一个很小的 React + TypeScript + Vite + PWA 起点，仅供全新项目使用，要求 Node.js 20.19 或更高版本。复制脚本会拒绝覆盖非空目录：

```bash
python3 scripts/copy_starter.py /path/to/empty-project
```

Starter 是起点，不是固定视觉模板。实际功能、导航、信息架构和视觉方向必须来自访谈与用户确认。

## 仓库结构

```text
personal-workbench-builder/
├── SKILL.md
├── README.md
├── LICENSE
├── agents/
│   └── openai.yaml       # Codex 可选界面元数据，其他 Agent 可忽略
├── references/
│   ├── interview.md
│   ├── workflow-and-planning.md
│   ├── feasibility.md
│   ├── design-prototypes.md
│   ├── implementation.md
│   ├── storage.md
│   ├── sync-and-security.md
│   ├── automation.md
│   ├── pwa-and-deployment.md
│   ├── qa.md
│   ├── state-schema.md
│   └── scenario-tests.md
├── scripts/
│   ├── init_workbench_state.py
│   ├── validate_workbench_state.py
│   ├── copy_starter.py
│   ├── validate_scenarios.py
│   └── validate_skill.py
└── assets/
    ├── state-template/
    └── react-vite-pwa-starter/
```

## 本仓库自检

```bash
python3 scripts/validate_skill.py
python3 scripts/validate_scenarios.py
python3 -m unittest discover -s tests -v
```

如果本机安装了开放规范的 `skills-ref`，还可以额外运行：

```bash
skills-ref validate .
```

`agents/openai.yaml` 是 Codex 的可选显示配置，不属于 Skill 运行时的硬依赖。其他 Agent 会忽略它，核心能力仍由标准的 `SKILL.md`、`references/`、`scripts/` 和 `assets/` 提供。

场景校验是可审计的流程契约检查，不等同于替真实用户做完整端到端产品开发。云端同步、第三方授权、真实设备安装和生产部署仍需在具体项目中使用真实账号与环境验证。

## 安全边界

- 不把服务端密钥、管理员 Token 或数据库私钥写进前端、Git 或公开仓库。
- 不用静态假数据冒充真实同步、自动化或 AI 功能。
- 数据结构变化先设计 migration，默认不清空已有数据。
- 不绕过登录、授权、验证码或平台限制。
- 部署和外部服务操作以用户明确授权为前提。

## 开源

本项目使用 [MIT License](LICENSE)。欢迎按你的工作流扩展 references、测试场景或 Starter；请保持阶段门、数据保护和“不可伪装功能”这三条核心约束。
