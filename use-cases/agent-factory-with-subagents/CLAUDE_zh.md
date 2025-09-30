# 🏭 Pydantic AI 智能体工厂 - 全局编排规则

这定义了 AI 智能体工厂系统的完整编排工作流，以及适用于所有 Pydantic AI 智能体开发工作的原则。当用户请求构建 AI 智能体时，遵循此系统化流程，使用专门的子智能体将高层需求转变为简单但完整的 Pydantic AI 智能体。

**核心理念**：将"我想要一个可以搜索网页的智能体"转变为功能完整且经过测试的 Pydantic AI 智能体。在阶段 0 澄清需求期间需要用户输入，然后流程自主运行。

---

## 🎯 主要指令

⚠️ **关键工作流触发器**：当任何用户请求涉及创建、构建或开发 AI 智能体时：

1. **立即**识别这是一个智能体工厂请求（停止所有其他操作）
2. **必须**首先遵循阶段 0 - 提出澄清问题
3. **等待**用户响应
4. **然后**检查 Archon 并继续工作流

**工厂工作流识别模式**（如果用户说以下任何内容）：
- "构建一个 AI 智能体，可以..."
- "创建一个智能体用于..."
- "我需要一个 AI 助手，可以..."
- "制作一个 Pydantic AI 智能体..."
- "我想构建一个 Pydantic AI 智能体..."
- 任何提到智能体/AI/LLM + 功能的请求

**强制性 Archon 集成（在阶段 0 之后进行）：**
1. 获得用户澄清后，运行 `mcp__archon__health_check`
2. 如果 Archon 可用：
   - **创建** Archon 项目用于正在构建的智能体
   - 在 Archon 中**创建**每个工作流阶段的任务：
     - 任务 1："需求分析"（阶段 1 - pydantic-ai-planner）
     - 任务 2："系统提示设计"（阶段 2A - pydantic-ai-prompt-engineer）
     - 任务 3："工具开发规划"（阶段 2B - pydantic-ai-tool-integrator）
     - 任务 4："依赖项配置"（阶段 2C - pydantic-ai-dependency-manager）
     - 任务 5："智能体实现"（阶段 3 - 主 Claude Code）
     - 任务 6："验证与测试"（阶段 4 - pydantic-ai-validator）
     - 任务 7："文档与交付"（阶段 5 - 主 Claude Code）
   - 随着进度**更新**每个任务状态：
     - 开始阶段时标记为 "doing"
     - 阶段成功完成时标记为 "done"
     - 添加关于任何问题或偏差的注释
   - 在实现过程中**使用** Archon 的 RAG 进行文档查找
   - **指示**所有子智能体引用 Archon 项目 ID
3. 如果 Archon 不可用：继续但使用 TodoWrite 进行本地跟踪

**工作流强制执行**：你必须：
1. 从阶段 0 开始（澄清问题）
2. 在继续之前等待用户响应
3. 然后系统地进行所有阶段
4. 永远不要直接跳到实现

当你想要使用或调用子智能体时，必须调用子智能体，给它们一个提示并将控制权传递给它们。

---

## 🔄 完整工厂工作流

### 阶段 0：请求识别与澄清
**触发模式**（在以下任何情况下激活工厂）：
- "构建一个 AI 智能体，可以..."
- "创建一个智能体用于..."
- "我需要一个 AI 助手，可以..."
- "制作一个 Pydantic AI 智能体..."
- "开发一个 LLM 智能体..."
- 任何提到智能体/AI/LLM + 功能的请求

**立即行动**：
```
1. 确认智能体创建请求
2. 提出 2-3 个有针对性的澄清问题（在调用规划器之前）：
   - 主要功能和用例
   - 首选的 API 或集成（如适用）
   - 输出格式偏好
3. ⚠️ 关键：停止并等待用户响应
   - 等待用户回答后再进行步骤 4
   - 避免做出假设以"保持流程进行"
   - 避免创建文件夹或调用子智能体
   - 等待明确的用户输入后再继续
4. 只有在用户响应后：确定智能体文件夹名称（snake_case，例如 web_search_agent、asana_manager）
5. 创建 agents/[AGENT_FOLDER_NAME]/ 目录
6. 使用完全相同的文件夹名称调用所有子智能体
7. 告诉每个子智能体："输出到 agents/[AGENT_FOLDER_NAME]/"
```

### 阶段 1：需求文档 🎯
**子智能体**：`pydantic-ai-planner`
**触发**：在阶段 0 澄清收集后调用
**模式**：自主 - 无需用户交互即可工作
**理念**：简单、聚焦的需求 - MVP 思维
**Archon**：在调用子智能体之前将任务 1 更新为 "doing"

```
操作：
1. 将 Archon 任务 1"需求分析"更新为 status="doing"
2. 从主智能体接收用户请求 + 澄清 + 文件夹名称 + Archon 项目 ID
3. 分析需求，只关注核心功能
4. 做出简单、实用的假设（单一模型、基本错误处理）
5. 创建最小化的 INITIAL.md，最多 2-3 个核心功能
6. 输出：agents/[EXACT_FOLDER_NAME]/planning/INITIAL.md
   ⚠️ 关键：输出到 planning/ 子目录
7. 子智能体完成后将 Archon 任务 1 更新为 status="done"
```

**质量门禁**：INITIAL.md 必须包含：
- ✅ 智能体分类和类型
- ✅ 功能需求
- ✅ 技术需求
- ✅ 外部依赖项
- ✅ 成功标准

### 阶段 2：并行组件开发 ⚡
**同时执行**（所有三个子智能体并行工作）：
**Archon**：在并行调用之前将任务 2、3、4 更新为 "doing"

**关键：使用并行工具调用：** 在调用多个子智能体时，必须在单个消息中使用多个工具调用来调用所有三个 Task 工具。这确保了真正的并行执行。
- ❌ 错误：调用规划器，等待完成，然后调用提示词工程师
- ✅ 正确：在单个消息中进行三次 Task 工具调用
- 同时在并行调用之前将所有三个 Archon 任务（2、3、4）更新为 "doing"

#### 2A：系统提示词工程
**子智能体**：`pydantic-ai-prompt-engineer`
**理念**：简单、清晰的提示 - 通常 100-300 字
```
输入：planning/INITIAL.md + 主智能体的文件夹名称
输出：agents/[EXACT_FOLDER_NAME]/planning/prompts.md
⚠️ 关键：输出 MARKDOWN 文件，包含提示规范，而不是 Python 代码
内容：
- 一个简单的静态系统提示（100-300 字）
- 除非明确需要，否则跳过动态提示
- 只关注基本行为
```

#### 2B：工具开发规划
**子智能体**：`pydantic-ai-tool-integrator`
**理念**：最少工具 - 只有 2-3 个基本功能
```
输入：planning/INITIAL.md + 主智能体的文件夹名称
输出：agents/[EXACT_FOLDER_NAME]/planning/tools.md
⚠️ 关键：输出 MARKDOWN 文件，包含工具规范，而不是 Python 代码
内容：
- 只有 2-3 个基本工具规范
- 简单参数（每个工具 1-3 个）
- 基本错误处理
- 单一用途工具
```

#### 2C：依赖项配置规划
**子智能体**：`pydantic-ai-dependency-manager`
**理念**：最少配置 - 只有基本环境变量
```
输入：planning/INITIAL.md + 主智能体的文件夹名称
输出：agents/[EXACT_FOLDER_NAME]/planning/dependencies.md
⚠️ 关键：输出 MARKDOWN 文件，包含依赖项规范，而不是 Python 代码
内容：
- 只有基本环境变量
- 单一模型提供商（无备用）
- 简单的 dataclass 依赖项
- 最少的 Python 包
```

**阶段 2 完成条件**：所有三个子智能体报告完成

### 阶段 3：智能体实现 🔨
**执行者**：主 Claude Code（不是子智能体）
**Archon**：在开始实现之前将任务 5 更新为 "doing"

```
操作：
1. 将 Archon 任务 5"智能体实现"更新为 status="doing"
2. 标记 Archon 任务 2、3、4 为 "done"（在验证子智能体完成后）
3. 读取规划阶段的 4 个 markdown 文件：
   - agents/[folder]/planning/INITIAL.md
   - agents/[folder]/planning/prompts.md
   - agents/[folder]/planning/tools.md
   - agents/[folder]/planning/dependencies.md
4. 根据需要使用 Archon RAG 搜索 Pydantic AI 模式和示例
5. 根据规范实现实际的 Python 代码：
   - 将提示规范 → prompts.py
   - 将工具规范 → tools.py
   - 将依赖项规范 → settings.py、providers.py、dependencies.py
6. 创建完整的智能体实现：
   - 将所有组件组合到 agent.py
   - 连接依赖项和工具
   - 创建主执行文件
7. 实现完成时将 Archon 任务 5 更新为 status="done"
8. 构建最终项目：
   agents/[agent_name]/
   ├── agent.py           # 主智能体
   ├── settings.py        # 配置
   ├── providers.py       # 模型提供商
   ├── dependencies.py    # 依赖项
   ├── tools.py          # 工具实现
   ├── prompts.py        # 系统提示
   ├── __init__.py       # 包初始化
   ├── requirements.txt  # Python 依赖项
   ├── .env.example      # 环境模板
   └── README.md         # 使用文档
```

### 阶段 4：验证与测试 ✅
**子智能体**：`pydantic-ai-validator`
**触发**：实现后自动触发
**时长**：3-5 分钟
**Archon**：在调用验证器之前将任务 6 更新为 "doing"

```
操作：
1. 将 Archon 任务 6"验证与测试"更新为 status="doing"
2. 使用智能体文件夹和 Archon 项目 ID 调用验证器子智能体
3. 创建全面的测试套件
4. 根据 INITIAL.md 需求进行验证
5. 使用 TestModel 运行测试
6. 生成验证报告
7. 验证完成后将 Archon 任务 6 更新为 status="done"
8. 输出：agents/[agent_name]/tests/
   ├── test_agent.py
   ├── test_tools.py
   ├── test_integration.py
   ├── test_validation.py
   ├── conftest.py
   └── VALIDATION_REPORT.md
```

**成功标准**：
- 所有需求已验证
- 核心功能已测试
- 错误处理已验证
- 性能可接受

### 阶段 5：交付与文档 📦
**执行者**：主 Claude Code
**Archon**：在最终文档之前将任务 7 更新为 "doing"
**最终操作**：
```
1. 将 Archon 任务 7"文档与交付"更新为 status="doing"
2. 生成全面的 README.md
3. 创建使用示例
4. 记录 API 端点（如适用）
5. 提供部署说明
6. 将 Archon 任务 7 更新为 status="done"
7. 在 Archon 项目中添加关于智能体能力的最终注释
8. 向用户提供包含 Archon 项目链接的摘要报告
```

---

## 📋 Archon 任务管理协议

### 任务创建流程
当 Archon 可用时，在项目创建后立即创建所有工作流任务：
```python
# 创建 Archon 项目后
tasks = [
    {"title": "需求分析", "assignee": "pydantic-ai-planner"},
    {"title": "系统提示设计", "assignee": "pydantic-ai-prompt-engineer"},
    {"title": "工具开发规划", "assignee": "pydantic-ai-tool-integrator"},
    {"title": "依赖项配置", "assignee": "pydantic-ai-dependency-manager"},
    {"title": "智能体实现", "assignee": "Claude Code"},
    {"title": "验证与测试", "assignee": "pydantic-ai-validator"},
    {"title": "文档与交付", "assignee": "Claude Code"}
]
# 最初使用 status="todo" 创建所有任务
```

### 任务状态更新
- 在开始每个阶段之前立即设置为 "doing"
- 在阶段成功完成后立即设置为 "done"
- 如果阶段遇到问题或偏差，添加注释
- 永远不要有多个任务处于 "doing" 状态（除了并行阶段 2）

### 子智能体通信
始终将 Archon 项目 ID 传递给子智能体：
- 在提示中包含："使用 Archon 项目 ID：[project-id]"
- 子智能体应在其输出中引用此 ID 以便可追溯

## 🎭 子智能体调用规则

### 自动调用
子智能体根据工作流阶段自动调用：
```python
if user_request.contains(agent_creation_pattern):
    # 阶段 0 - 主 Claude Code 提出澄清问题
    clarifications = ask_user_questions()

    # 阶段 1 - 使用上下文调用规划器
    invoke("pydantic-ai-planner", context={
        "user_request": original_request,
        "clarifications": clarifications
    })

    # 阶段 2 - 自动并行
    parallel_invoke([
        "pydantic-ai-prompt-engineer",
        "pydantic-ai-tool-integrator",
        "pydantic-ai-dependency-manager"
    ])

    # 阶段 3 - 主 Claude Code
    implement_agent()

    # 阶段 4 - 自动
    invoke("pydantic-ai-validator")
```

### 手动覆盖
用户可以明确请求特定的子智能体：
- "使用规划器细化需求"
- "让工具集成器添加网页搜索"
- "再次运行验证器"

---

## 📁 输出目录结构

每次智能体工厂运行都会创建：
```
agents/
└── [agent_name]/
    ├── planning/              # 所有规划文档
    │   ├── INITIAL.md         # 需求（规划器）
    │   ├── prompts.md         # 提示规范（提示词工程师）
    │   ├── tools.md           # 工具规范（工具集成器）
    │   └── dependencies.md    # 依赖项规范（依赖项管理器）
    ├── agent.py               # 主实现
    ├── settings.py            # 配置
    ├── providers.py           # 模型提供商
    ├── dependencies.py        # 依赖项
    ├── tools.py              # 工具
    ├── prompts.py            # 提示
    ├── cli.py                # CLI 界面
    ├── requirements.txt      # Python 包
    ├── .env.example          # 环境模板
    ├── README.md             # 文档
    └── tests/                # 测试套件（如果创建）
        ├── test_agent.py
        └── test_tools.py
```

---

## 🔧 实现指南

### 对于简单的智能体请求
示例："构建一个可以搜索网页的智能体"
```
1. 规划器提出最少的问题（1-2 个）
2. 假设标准模式（Brave API、字符串输出）
3. 总共约 10 分钟完成
4. 交付具有基本测试的工作智能体
```

### 对于复杂的智能体请求
示例："构建一个具有数据库、缓存和工作流编排的多模态智能体"
```
1. 规划器提出全面的问题（4-5 个）
2. 可能需要多次迭代
3. 交付具有完整测试覆盖率的简单但完整的系统
```

### 错误处理协议
如果任何子智能体失败：
```
1. 记录带有上下文的错误
2. 尝试自动恢复
3. 如果恢复失败，向用户寻求指导
4. 如果可能，继续进行部分实现
5. 在 README 中记录限制
```

---

## 📝 主智能体澄清指南

当用户请求 AI 智能体时，主 Claude Code 智能体应该：

### 提出 2-3 个重点问题
保持问题简单和有针对性：
1. **核心功能**："此智能体应处理哪些特定任务？"
2. **集成需求**："它需要连接到任何外部服务或 API 吗？"
3. **输出格式**："它应该返回纯文本、结构化数据还是其他内容？"

### 避免过度提问
- 不要询问技术细节（规划器会处理这些）
- 不要询问实现细节
- 保持问题高层次和用户友好

### 将上下文传递给规划器
在调用规划器时，提供：
- 原始用户请求
- 用户对澄清问题的回答
- 对话中的任何额外上下文

## 🚀 快速入门示例

### 示例 1：网页搜索智能体
**用户**："我想构建一个可以搜索网页的 AI 智能体"

**Claude Code 响应**：
```
我将帮助你使用 Pydantic AI 框架构建一个网页搜索 AI 智能体。让我问几个快速问题以更好地了解你的需求：

1. 智能体主要搜索什么？（一般网页内容、特定域名、研究论文等）
2. 智能体应该总结结果还是返回原始搜索数据？
3. 你对使用哪个搜索 API 有偏好吗？（Brave、Google、Bing）

[在这里停止并等待用户响应]

[用户用答案响应后]

完美！根据你的需求 [总结他们的答案]，我现在将调用我们的需求规划器为你的网页搜索智能体创建全面的规范。

📋 创建需求文档...
[使用上下文调用 pydantic-ai-planner]

[规划器自主工作并创建 INITIAL.md]

⚙️ 构建智能体组件...
[并行调用 prompt-engineer、tool-integrator、dependency-manager]

🔨 实现你的智能体...
[主实现]

✅ 运行验证...
[调用 pydantic-ai-validator]

🎉 智能体完成！
你的网页搜索智能体已准备好：agents/web_search_agent/
```

### 示例 2：数据库查询智能体
**用户**："创建一个可以查询 PostgreSQL 数据库并解释结果的智能体"

**Claude Code 响应**：
```
我将创建一个具有解释功能的 PostgreSQL 查询智能体。让我先问几个快速问题：

1. 此智能体需要运行什么类型的查询？（仅 SELECT，还是也包括 INSERT/UPDATE/DELETE？）
2. 它应该连接到特定数据库还是处理多个数据库连接？
3. 解释应该多详细？（简要摘要还是详细分析？）

[在这里停止并等待用户响应]

[用户用答案响应后]

太好了！根据你的需求 [总结他们的答案]，我现在将为你的 PostgreSQL 智能体创建全面的需求文档。

📋 创建需求文档...
[使用上下文调用 pydantic-ai-planner]
[流程自主继续]
```

---

## 🔍 监控与调试

### 进度跟踪
Claude Code 应提供状态更新：
```
✅ 阶段 1：需求完成（已创建 INITIAL.md）
⏳ 阶段 2：构建组件（3 个子智能体工作中...）
  ✅ 提示：完成
  ✅ 工具：完成
  ⏳ 依赖项：进行中...
⏳ 阶段 3：实现待处理...
⏳ 阶段 4：验证待处理...
```

### 调试模式
使用以下命令启用："以调试模式构建智能体"
- 来自所有子智能体的详细日志
- 保留中间输出
- 逐步确认模式
- 收集性能指标

---

## 🛡️ 质量保证

### 每个智能体必须具有：
1. **全面的测试**，使用 TestModel/FunctionModel
2. **错误处理**，用于所有外部操作
3. **安全措施**，用于 API 密钥和输入
4. **文档**，用于使用和部署
5. **环境模板**（.env.example）

### 验证清单
在交付之前，确认：
- [ ] 实现了 INITIAL.md 中的所有需求
- [ ] 测试通过，覆盖率 >80%
- [ ] API 密钥正确管理
- [ ] 错误场景已处理
- [ ] 文档完整
- [ ] 提供了使用示例

---

## 🎨 自定义点

### 用户偏好
用户可以指定：
- 首选的 LLM 提供商（OpenAI、Anthropic、Gemini）
- 输出格式（字符串、结构化、流式）
- 测试深度（基本、全面、详尽）
- 文档风格（最小、标准、详细）

### 高级功能
对于高级用户：
- 自定义子智能体配置
- 替代工作流序列
- 与现有代码库集成
- CI/CD 流水线生成

---

## 📊 成功指标

跟踪工厂性能：
- **完成时间**：标准智能体目标 <15 分钟
- **测试覆盖率**：智能体最低 80%
- **验证通过率**：100% 的需求已测试
- **用户干预**：最小化到仅初始需求

---

## 🔄 持续改进

### 反馈循环
每次智能体创建后：
1. 分析哪些工作良好
2. 识别瓶颈
3. 如需要更新子智能体提示
4. 根据模式细化工作流

### 模式库
构建常见模式库：
- 搜索智能体
- 数据库智能体
- 工作流编排器
- 聊天界面
- API 集成

---

## 🚨 重要规则

### 始终：
- ✅ 使用 python-dotenv 进行环境管理
- ✅ 创建 .env.example
- ✅ 遵循 main_agent_reference 模式
- ✅ 创建全面的测试
- ✅ 记录所有内容
- ✅ 根据需求进行验证

### 始终避免的反模式：
- ❌ 硬编码 API 密钥或秘密
- ❌ 跳过测试阶段
- ❌ 忽略错误处理
- ❌ 创建过于复杂的智能体
- ❌ 忘记安全考虑

---

## 🎯 最终清单

在认为智能体完成之前：
- [ ] 需求已在 INITIAL.md 中捕获
- [ ] 所有组件由子智能体生成
- [ ] 智能体实现完整且功能正常
- [ ] 测试已编写并通过
- [ ] 文档全面
- [ ] 安全措施到位
- [ ] 向用户提供了清晰的后续步骤

---


## 🔄 Pydantic AI 核心原则

**重要：这些原则适用于所有 Pydantic AI 智能体开发：**

### AI 智能体的研究方法
- **广泛的网页搜索** - 始终研究 Pydantic AI 模式和最佳实践
- **研究官方文档** - ai.pydantic.dev 是权威来源
- **模式提取** - 识别可重用的智能体架构和工具模式
- **陷阱文档** - 记录异步模式、模型限制和上下文管理问题

## 📚 项目意识与上下文

- **使用虚拟环境**来运行所有代码和测试。如果需要时代码库中还没有，请创建它
- **使用一致的 Pydantic AI 命名约定**和智能体结构模式
- **遵循已建立的智能体目录组织**模式（agent.py、tools.py、models.py）
- **广泛利用 Pydantic AI 示例** - 在创建新智能体之前研究现有模式

## 🧱 智能体结构与模块化

- **永远不要创建超过 500 行的文件** - 接近限制时拆分为模块
- **将智能体代码组织成清晰分离的模块**，按职责分组：
  - `agent.py` - 主智能体定义和执行逻辑
  - `tools.py` - 智能体使用的工具函数
  - `models.py` - Pydantic 输出模型和依赖类
  - `dependencies.py` - 上下文依赖项和外部服务集成
- **使用清晰、一致的导入** - 适当地从 pydantic_ai 包导入
- **使用 python-dotenv 和 load_dotenv()** 管理环境变量 - 遵循 examples/main_agent_reference/settings.py 模式
- **永远不要硬编码敏感信息** - 始终使用 .env 文件存储 API 密钥和配置

## 🤖 Pydantic AI 开发标准

### 智能体创建模式
- **使用模型无关设计** - 支持多个提供商（OpenAI、Anthropic、Gemini）
- **实现依赖注入** - 使用 deps_type 用于外部服务和上下文
- **定义结构化输出** - 使用 Pydantic 模型进行结果验证
- **包含全面的系统提示** - 静态和动态指令

### 工具集成标准
- **使用 @agent.tool 装饰器**用于具有 RunContext[DepsType] 的上下文感知工具
- **使用 @agent.tool_plain 装饰器**用于没有上下文依赖项的简单工具
- **实现适当的参数验证** - 使用 Pydantic 模型进行工具参数验证
- **优雅地处理工具错误** - 实现重试机制和错误恢复

### 使用 python-dotenv 的环境变量配置
```python
# 使用 python-dotenv 和 pydantic-settings 进行适当的配置管理
from pydantic_settings import BaseSettings
from pydantic import Field, ConfigDict
from dotenv import load_dotenv
from pydantic_ai.providers.openai import OpenAIProvider
from pydantic_ai.models.openai import OpenAIModel

class Settings(BaseSettings):
    """具有环境变量支持的应用程序设置。"""

    model_config = ConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore"
    )

    # LLM 配置
    llm_provider: str = Field(default="openai", description="LLM 提供商")
    llm_api_key: str = Field(..., description="LLM 提供商的 API 密钥")
    llm_model: str = Field(default="gpt-4", description="要使用的模型名称")
    llm_base_url: str = Field(
        default="https://api.openai.com/v1",
        description="LLM API 的基础 URL"
    )

def load_settings() -> Settings:
    """使用适当的错误处理和环境加载来加载设置。"""
    # 从 .env 文件加载环境变量
    load_dotenv()

    try:
        return Settings()
    except Exception as e:
        error_msg = f"加载设置失败：{e}"
        if "llm_api_key" in str(e).lower():
            error_msg += "\n确保在你的 .env 文件中设置 LLM_API_KEY"
        raise ValueError(error_msg) from e

def get_llm_model():
    """获取配置的 LLM 模型，并进行适当的环境加载。"""
    settings = load_settings()
    provider = OpenAIProvider(
        base_url=settings.llm_base_url,
        api_key=settings.llm_api_key
    )
    return OpenAIModel(settings.llm_model, provider=provider)
```

### AI 智能体的测试标准
- **使用 TestModel 进行开发** - 无需 API 调用的快速验证
- **使用 FunctionModel 进行自定义行为** - 在测试中控制智能体响应
- **使用 Agent.override() 进行测试** - 在测试上下文中替换模型
- **测试同步和异步模式** - 确保与不同执行模式的兼容性
- **测试工具验证** - 验证工具参数模式和错误处理

## ✅ AI 开发的任务管理

- **将智能体开发分解为明确的步骤**，具有特定的完成标准
- **完成智能体实现后立即标记任务完成**
- **实时更新任务状态**，随着智能体开发的进展
- **在标记实现任务完成之前测试智能体行为**

## 📎 Pydantic AI 编码标准

### 智能体架构
```python
# 遵循 main_agent_reference 模式 - 除非需要结构化输出，否则不使用 result_type
from pydantic_ai import Agent, RunContext
from dataclasses import dataclass
from .settings import load_settings

@dataclass
class AgentDependencies:
    """智能体执行的依赖项"""
    api_key: str
    session_id: str = None

# 使用适当的 dotenv 处理加载设置
settings = load_settings()

# 具有字符串输出的简单智能体（默认）
agent = Agent(
    get_llm_model(),  # 内部使用 load_settings()
    deps_type=AgentDependencies,
    system_prompt="你是一个乐于助人的助手..."
)

@agent.tool
async def example_tool(
    ctx: RunContext[AgentDependencies],
    query: str
) -> str:
    """具有适当上下文访问的工具"""
    return await external_api_call(ctx.deps.api_key, query)
```