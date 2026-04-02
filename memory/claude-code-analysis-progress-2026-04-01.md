# Claude Code 源码分析进度 📝

_分析时间：2026-04-01 11:00_

---

## ✅ 已完成（第一阶段）

### 1. Tool.ts 核心架构分析（29KB）

**关键设计模式：**

#### Tool 类型定义
```typescript
export type Tool<Input, Output, P> = {
  name: string
  call(args, context, canUseTool, parentMessage, onProgress): Promise<ToolResult<Output>>
  description(input, options): Promise<string>
  inputSchema: Input
  outputSchema?: z.ZodType<unknown>
  
  // 安全控制
  isConcurrencySafe(input): boolean
  isReadOnly(input): boolean
  isDestructive?(input): boolean
  checkPermissions(input, context): Promise<PermissionResult>
  validateInput?(input, context): Promise<ValidationResult>
  
  // UI 渲染
  renderToolUseMessage(input, options): React.ReactNode
  renderToolResultMessage(content, progressMessages, options): React.ReactNode
  renderToolUseProgressMessage?(progressMessages, options): React.ReactNode
  
  // 高级功能
  interruptBehavior?(): 'cancel' | 'block'
  isSearchOrReadCommand?(input): {isSearch, isRead, isList}
  toAutoClassifierInput(input): unknown  // 安全分类器
}
```

#### buildTool 工厂函数
```typescript
const TOOL_DEFAULTS = {
  isEnabled: () => true,
  isConcurrencySafe: () => false,  // 默认不安全（fail-closed）
  isReadOnly: () => false,          // 默认写操作
  isDestructive: () => false,
  checkPermissions: (input) => ({behavior: 'allow', updatedInput: input}),
  toAutoClassifierInput: () => '',
  userFacingName: () => def.name,
}

export function buildTool<D>(def: D): BuiltTool<D> {
  return {...TOOL_DEFAULTS, ...def}
}
```

**设计亮点：**
1. **安全优先** — 默认 fail-closed（不安全/写操作/非破坏性）
2. **类型安全** — Zod schema 验证输入输出
3. **可扩展** — 30+ 工具共享基类，各自实现特定逻辑
4. **UI 分离** — render 系列方法支持 Terminal UI（React Ink）

---

### 2. main.tsx 入口流程分析（50KB+）

**启动流程：**
```
1. 模块加载前优化
   - profileCheckpoint('main_tsx_entry')
   - startMdmRawRead()  // MDM 配置并行读取
   - startKeychainPrefetch()  // Keychain 凭据预取

2. 命令行解析
   - 处理 cc:// 深链 URL
   - 处理 claude ssh/host
   - 处理 claude assistant
   - 处理 --print/-p 非交互模式

3. 初始化
   - eagerLoadSettings()  // 加载设置
   - init()  // 核心初始化
   - runMigrations()  // 数据迁移（版本 11）

4. 延迟预取
   - startDeferredPrefetches()
   - initUser(), getUserContext()
   - countFilesRoundedRg()  // 文件计数
   - settingsChangeDetector.initialize()
```

**性能优化：**
- 并行预取（MDM/Keychain/Git）
- 懒加载（feature() 条件导入）
- 缓存预热（文件计数/模型能力）
- 启动分析器（profileCheckpoint/Report）

---

### 3. 技能系统分析（skills/bundled/index.ts）

**内置技能列表：**
```typescript
function initBundledSkills(): void {
  registerUpdateConfigSkill()      // 配置更新
  registerKeybindingsSkill()       // 快捷键
  registerVerifySkill()            // 代码验证
  registerDebugSkill()             // 调试
  registerLoremIpsumSkill()        // 占位文本
  registerSkillifySkill()          // 技能生成
  registerRememberSkill()          // 记忆
  registerSimplifySkill()          // 简化
  registerBatchSkill()             // 批量处理
  registerStuckSkill()             // 卡住求助
  
  // 特性门控技能
  if (feature('KAIROS')) registerDreamSkill()
  if (feature('REVIEW_ARTIFACT')) registerHunterSkill()
  if (feature('AGENT_TRIGGERS')) registerLoopSkill()
  if (feature('BUILDING_CLAUDE_APPS')) registerClaudeApiSkill()
}
```

**设计特点：**
- 特性门控（feature()）— 按需加载
- 注册制 — 统一接口
- 可扩展 — 新增技能只需添加 register 调用

---

### 4. 协调器模式分析（coordinatorMode.ts，19KB）

**核心概念：**
```typescript
// 协调器模式检测
export function isCoordinatorMode(): boolean {
  if (feature('COORDINATOR_MODE')) {
    return isEnvTruthy(process.env.CLAUDE_CODE_COORDINATOR_MODE)
  }
  return false
}

// 协调器系统提示
export function getCoordinatorSystemPrompt(): string {
  return `You are Claude Code, an AI assistant that orchestrates tasks across multiple workers.

## Your Role
- Direct workers to research, implement and verify
- Synthesize results and communicate with user
- Answer questions directly when possible

## Tools
- AgentTool — Spawn a new worker
- SendMessageTool — Continue an existing worker
- TaskStopTool — Stop a running worker

## Workflow
1. Research — Workers (parallel)
2. Synthesis — You (coordinator)
3. Implementation — Workers
4. Verification — Workers
```

**多 Agent 协作流程：**
```
用户请求
  ↓
协调器分析任务
  ↓
并行启动多个 Worker（AgentTool）
  ↓
Worker 独立执行（Research/Implement/Verify）
  ↓
Worker 完成 → <task-notification> 消息
  ↓
协调器综合结果 → 回复用户
  ↓
继续 Worker（SendMessageTool）或启动新 Worker
```

**Worker 提示设计原则：**
1. **自包含** — Worker 看不到协调器对话，必须包含所有上下文
2. **具体化** — 文件路径、行号、错误消息
3. **目的明确** — "这个研究用于 PR 描述"vs"用于实现规划"
4. **Continue vs Spawn** — 根据上下文重叠度决定

---

## 📊 对 OpenClaw 的启发

### 1. 工具系统扩展

**现状对比：**
| 功能 | OpenClaw | Claude Code | 差距 |
|------|----------|-------------|------|
| 工具基类 | 无（独立实现） | Tool.ts | 缺少统一接口 |
| 安全控制 | 工具级策略 | isConcurrencySafe/isReadOnly/isDestructive | 细粒度控制 |
| UI 渲染 | 无 | renderToolUseMessage 等 | Terminal UI |
| 进度追踪 | 无 | renderToolUseProgressMessage | 实时进度 |

**建议实现：**
```typescript
// OpenClaw Tool 基类（建议）
abstract class BaseTool {
  abstract name: string
  abstract call(args, context): Promise<ToolResult>
  
  // 安全控制（默认 fail-closed）
  isConcurrencySafe(): boolean { return false }
  isReadOnly(): boolean { return false }
  isDestructive(): boolean { return false }
  
  // UI 渲染（可选）
  renderProgress?(progress): React.ReactNode
  renderResult?(result): React.ReactNode
}
```

### 2. 技能系统优化

**现状对比：**
| 功能 | OpenClaw | Claude Code |
|------|----------|-------------|
| 安装方式 | ClawHub 下载 | 内置 + MCP |
| 加载机制 | 启动时扫描 | 注册制 + 特性门控 |
| 技能类型 | 独立 .skill 文件夹 | 函数注册 |

**建议实现：**
```typescript
// OpenClaw 技能注册（建议）
function initBundledSkills(): void {
  registerTokenOptimizerSkill()  // Token 优化
  registerPromptGuardSkill()     // 安全防御
  registerHealthcheckSkill()     // 健康检查
  registerWeatherSkill()         // 天气查询
  
  // 特性门控
  if (feature('TTS')) registerTtsSkill()
  if (feature('BROWSER')) registerBrowserSkill()
}
```

### 3. 协调器模式借鉴

**OpenClaw 已有：**
- `sessions_spawn` — 子 Agent 创建
- `subagents` — 子 Agent 管理
- `sessions_send` — 跨会话消息

**可改进：**
1. **任务分解** — 自动将大任务拆分为子任务
2. **上下文管理** — Worker 间共享上下文（scratchpad）
3. **结果综合** — 自动汇总多个 Worker 结果
4. **进度追踪** — 实时显示 Worker 状态

---

## 📝 下一步分析计划

### 第二阶段（进行中）
- [ ] 工具系统深度分析 — FileEditTool/BashTool/MCPTool 实现
- [ ] 命令系统分析 — commands.ts、40+ 命令实现
- [ ] 服务层分析 — API/MCP/Analytics

### 第三阶段
- [ ] 成本追踪系统 — cost-tracker.ts/costHook.ts
- [ ] 状态管理 — context/、state/
- [ ] UI 系统 — ink/（React Ink）

### 第四阶段
- [ ] 整理分析笔记
- [ ] 创建 claude-code-analysis.html
- [ ] 推送到 GitHub

---

_分析者：哈基偷 🐱_
_分析时间：2026-04-01 11:00_
