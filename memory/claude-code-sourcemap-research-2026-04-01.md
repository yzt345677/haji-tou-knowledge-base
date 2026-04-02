# Claude Code Sourcemap 研究报告 🔍

_研究时间：2026-04-01 10:35_
_来源：https://github.com/ChinaSiro/claude-code-sourcemap_

---

## 📋 项目概览

| 项目 | 信息 |
|------|------|
| **仓库** | [ChinaSiro/claude-code-sourcemap](https://github.com/ChinaSiro/claude-code-sourcemap) |
| **创建时间** | 2026-03-31 08:15:54 UTC |
| **最后更新** | 2026-04-01 02:30:57 UTC |
| **Stars** | 5,399 ⭐ |
| **语言** | TypeScript |
| **大小** | 73.8 MB |
| **还原版本** | @anthropic-ai/claude-code v2.1.88 |
| **还原文件数** | 4,756 个（含 1,884 个 .ts/.tsx 源文件） |
| **还原方式** | 提取 cli.js.map 中的 sourcesContent 字段 |

**性质：** 非官方整理版，基于公开 npm 发布包与 source map 分析还原，仅供研究使用

**来源：** 一切基于 Linux.do 论坛用户"飘然与我同"的情报提供

---

## 🏗️ 项目架构

```
restored-src/src/
├── main.tsx                    # CLI 入口
├── tools/                      # 工具实现（30+ 个）
├── commands/                   # 命令实现（40+ 个）
├── services/                   # API、MCP、分析等服务
├── utils/                      # 工具函数（git、model、auth、env 等）
├── context/                    # React Context
├── coordinator/                # 多 Agent 协调模式
├── assistant/                  # 助手模式（KAIROS）
├── buddy/                      # AI 伴侣 UI
├── remote/                     # 远程会话
├── plugins/                    # 插件系统
├── skills/                     # 技能系统
├── voice/                      # 语音交互
└── vim/                        # Vim 模式
```

---

## 🛠️ 工具系统（30+ 个）

### 文件操作类
- `FileReadTool` — 读取文件
- `FileWriteTool` — 写入文件
- `FileEditTool` — 编辑文件
- `GlobTool` — 文件匹配
- `GrepTool` — 内容搜索
- `LSPTool` — 语言服务器协议

### Shell 执行类
- `BashTool` — Bash 命令执行
- `PowerShellTool` — PowerShell 命令执行
- `REPLTool` — REPL 交互

### 任务管理类
- `TaskCreateTool` — 创建任务
- `TaskGetTool` — 获取任务
- `TaskListTool` — 列出任务
- `TaskOutputTool` — 获取任务输出
- `TaskStopTool` — 停止任务
- `TaskUpdateTool` — 更新任务

### MCP 集成类
- `MCPTool` — MCP 工具调用
- `ListMcpResourcesTool` — 列出 MCP 资源
- `ReadMcpResourceTool` — 读取 MCP 资源
- `McpAuthTool` — MCP 认证

### 团队协作类
- `TeamCreateTool` — 创建团队
- `TeamDeleteTool` — 删除团队
- `AgentTool` — Agent 调用

### 其他工具
- `WebSearchTool` — 网络搜索
- `WebFetchTool` — 网页抓取
- `SkillTool` — 技能调用
- `ConfigTool` — 配置管理
- `TodoWriteTool` — TODO 列表
- `AskUserQuestionTool` — 询问用户
- `SendMessageTool` — 发送消息
- `RemoteTriggerTool` — 远程触发
- `ScheduleCronTool` — 定时任务
- `SleepTool` — 延迟执行
- `EnterPlanModeTool` / `ExitPlanModeTool` — 计划模式
- `EnterWorktreeTool` / `ExitWorktreeTool` — 工作树
- `BriefTool` — 简报
- `NotebookEditTool` — 笔记本编辑
- `ToolSearchTool` — 工具搜索
- `SyntheticOutputTool` — 合成输出

---

## 🎯 技能系统（Skills）

```
skills/
├── bundled/              # 内置技能
├── bundledSkills.ts      # 内置技能列表
├── loadSkillsDir.ts      # 技能目录加载
└── mcpSkillBuilders.ts   # MCP 技能构建器
```

**对比 OpenClaw Skills：**
- OpenClaw：从 ClawHub 安装独立 .skill 文件夹
- Claude Code：内置技能 + MCP 技能构建器

**启发：**
- 可以考虑内置一些核心技能（如 file-read、file-write、bash 等）
- MCP 技能构建器可以动态创建工具包装器

---

## 🤖 协调器模式（Coordinator）

```
coordinator/
└── coordinatorMode.ts    # 多 Agent 协调模式
```

**功能推测：**
- 多 Agent 任务分配
- Agent 间通信协调
- 任务分解与结果汇总

**对比 OpenClaw：**
- OpenClaw 有 `sessions_spawn` 和 `subagents` 用于子 Agent 管理
- 可以研究 Claude Code 的协调器实现，优化 OpenClaw 的子 Agent 协作

---

## 📦 命令系统（40+ 个）

```
commands/
├── commit.ts             # Git commit
├── review.ts             # Code review
├── config.ts             # 配置管理
└── ...                   # 40+ 个命令
```

**对比 OpenClaw：**
- OpenClaw 使用工具（tools）而非命令（commands）
- 命令系统更适合 CLI 交互，工具系统更适合 API 调用

---

## 🔧 核心服务

```
services/
├── api.ts                # Anthropic API 调用
├── mcp.ts                # MCP 服务
├── analytics.ts          # 分析服务
└── ...
```

---

## 💡 对 OpenClaw 的启发

### 1. 工具系统扩展
**现状：** OpenClaw 有 14 个核心工具（read、write、edit、exec、browser 等）

**可借鉴：**
- 任务管理系统（TaskCreate/TaskList/TaskOutput）
- MCP 深度集成（ListMcpResources/ReadMcpResource）
- 团队协作工具（TeamCreate/AgentTool）
- 定时任务（ScheduleCronTool）
- 远程触发（RemoteTriggerTool）

### 2. 技能系统优化
**现状：** OpenClaw Skills 从 ClawHub 安装

**可借鉴：**
- 内置核心技能（减少安装步骤）
- MCP 技能构建器（动态创建工具包装器）
- 技能目录热加载

### 3. 协调器模式
**现状：** OpenClaw 有 `sessions_spawn` 和 `subagents`

**可借鉴：**
- 多 Agent 任务自动分解
- Agent 间通信协议
- 结果汇总与冲突解决

### 4. UI/UX 改进
**现状：** OpenClaw 主要通过消息交互

**可借鉴：**
- `buddy/` — AI 伴侣 UI（更友好的交互界面）
- `ink/` — Terminal UI（React Ink 渲染）
- `vim/` — Vim 模式（编辑器集成）
- `voice/` — 语音交互

### 5. 成本追踪
**发现文件：** `cost-tracker.ts`、`costHook.ts`

**功能：**
- 实时 Token 使用统计
- 成本预估与警告
- 模型使用分析

**对比 OpenClaw：**
- OpenClaw 有 `session_status` 和 `model-usage` skill
- 可以研究 Claude Code 的实时追踪实现

---

## 🔐 安全注意事项

**仓库声明：**
- 本仓库为非官方整理版，仅供研究使用
- 不代表官方原始内部开发仓库结构
- 源码版权归 Anthropic 所有
- 请勿用于商业用途

**研究建议：**
- 学习架构设计，不直接复制代码
- 理解工具实现思路，自行实现
- 注意版权问题，避免侵权

---

## 📚 后续研究方向

### 优先级 P0（核心架构）
1. **工具系统设计** — 研究 Tool.ts 基类实现
2. **技能系统架构** — 研究 skills/ 目录结构
3. **协调器模式** — 研究 coordinatorMode.ts

### 优先级 P1（实用功能）
4. **任务管理系统** — 研究 Task.ts 实现
5. **MCP 集成** — 研究 MCPTool、McpAuthTool
6. **成本追踪** — 研究 cost-tracker.ts、costHook.ts

### 优先级 P2（UI/UX）
7. **Terminal UI** — 研究 ink/ 目录（React Ink）
8. **AI 伴侣 UI** — 研究 buddy/ 目录
9. **Vim 模式** — 研究 vim/ 目录

### 优先级 P3（高级功能）
10. **语音交互** — 研究 voice/ 目录
11. **远程会话** — 研究 remote/ 目录
12. **插件系统** — 研究 plugins/ 目录

---

## 🔗 相关链接

- **GitHub 仓库：** https://github.com/ChinaSiro/claude-code-sourcemap
- **npm 包：** https://www.npmjs.com/package/@anthropic-ai/claude-code
- **来源论坛：** https://linux.do/u/huo0
- **Anthropic 官网：** https://www.anthropic.com

---

_研究者：哈基偷 🐱_
_研究时间：2026-04-01 10:35_
