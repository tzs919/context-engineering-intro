---
name: "PydanticAI 模板生成器 PRP"
description: "为 PydanticAI agent 开发生成全面的上下文工程模板,包含工具、内存和结构化输出"
---

## 目的

为 **PydanticAI** 生成完整的上下文工程模板包,使开发者能够快速构建智能 AI agent,并支持工具集成、对话处理以及使用 PydanticAI 框架的结构化数据验证。

## 核心原则

1. **PydanticAI 专业化**: 深度集成 PydanticAI 模式,用于 agent 创建、工具和结构化输出
2. **完整包生成**: 创建包含工作示例和验证的完整模板生态系统
3. **类型安全优先**: 充分利用 PydanticAI 的类型安全设计和 Pydantic 验证
4. **生产就绪**: 包含安全性、测试和生产部署的最佳实践
5. **上下文工程集成**: 将经过验证的上下文工程工作流应用于 AI agent 开发

---

## 目标

为 **PydanticAI** 生成完整的上下文工程模板包,包括:

- 带有 agent 模式的 PydanticAI 专用 CLAUDE.md 实施指南
- 用于 AI agent 的专业化 PRP 生成和执行命令
- 带有 agent 架构模式的领域专用基础 PRP 模板
- 全面的工作示例(聊天 agent、工具集成、多步骤工作流)
- PydanticAI 专用验证循环和测试模式

## 原因

- **AI 开发加速**: 能够快速开发生产级 PydanticAI agent
- **模式一致性**: 维护已建立的 AI agent 架构模式和最佳实践
- **质量保证**: 确保对 agent 行为、工具和输出进行全面测试
- **知识捕获**: 记录 PydanticAI 特定模式、陷阱和集成策略
- **可扩展的 AI 框架**: 为各种 AI agent 用例创建可重用的模板

## 内容

### 模板包组件

**完整目录结构:**
```
use-cases/pydantic-ai/
├── CLAUDE.md                           # PydanticAI 实施指南
├── .claude/commands/
│   ├── generate-pydantic-ai-prp.md     # Agent PRP 生成
│   └── execute-pydantic-ai-prp.md      # Agent PRP 执行
├── PRPs/
│   ├── templates/
│   │   └── prp_pydantic_ai_base.md     # PydanticAI 基础 PRP 模板
│   ├── ai_docs/                        # PydanticAI 文档
│   └── INITIAL.md                      # 示例 agent 功能请求
├── examples/
│   ├── basic_chat_agent/               # 简单聊天 agent 带内存
│   ├── tool_enabled_agent/             # 网络搜索 + 计算器工具
│   ├── workflow_agent/                 # 多步骤工作流处理
│   ├── structured_output_agent/        # 自定义 Pydantic 模型
│   └── testing_examples/               # Agent 测试模式
├── copy_template.py                    # 模板部署脚本
└── README.md                           # 全面的使用指南
```

**PydanticAI 集成:**
- 使用多个模型提供商(OpenAI、Anthropic、Gemini)创建 agent
- 工具集成模式和函数注册
- 使用依赖项进行对话内存和上下文管理
- 使用 Pydantic 模型进行结构化输出验证
- 使用 TestModel 和 FunctionModel 的测试模式
- API 密钥管理和输入验证的安全模式

**上下文工程适配:**
- PydanticAI 专用研究流程和文档引用
- Agent 适用的验证循环和测试策略
- AI 框架专业化的实施蓝图
- 与 AI 开发的基础上下文工程原则集成

### 成功标准

- [ ] 生成完整的 PydanticAI 模板包结构
- [ ] 所有必需文件都包含 PydanticAI 专用内容
- [ ] Agent 模式准确表示 PydanticAI 最佳实践
- [ ] 上下文工程原则已适配 AI agent 开发
- [ ] 验证循环适用于测试 AI agent 和工具
- [ ] 模板可立即用于创建 PydanticAI 项目
- [ ] 保持与基础上下文工程框架的集成
- [ ] 包含全面的示例和测试文档

## 所需全部上下文

### 文档和参考资料(已研究)

```yaml
# 重要 - 使用 Archon MCP 服务器获取更多 Pydantic AI 文档!
- mcp: Archon
  why: 官方 Pydantic AI 文档,可用于 RAG 查询
  content: 所有 Pydantic AI 文档
# PYDANTIC AI 核心文档 - 基本框架理解
- url: https://ai.pydantic.dev/
  why: 官方 PydanticAI 文档,包含核心概念和入门指南
  content: Agent 创建、模型提供商、类型安全、依赖注入

- url: https://ai.pydantic.dev/agents/
  why: 全面的 agent 架构、系统提示、工具、结构化输出
  content: Agent 组件、执行方法、配置选项

- url: https://ai.pydantic.dev/models/
  why: 模型提供商配置、API 密钥管理、后备模型
  content: OpenAI、Anthropic、Gemini 集成模式和身份验证

- url: https://ai.pydantic.dev/tools/
  why: 函数工具注册、上下文使用、丰富返回、动态工具
  content: 工具装饰器、参数验证、文档模式

- url: https://ai.pydantic.dev/testing/
  why: 测试策略、TestModel、FunctionModel、pytest 模式
  content: 单元测试、agent 行为验证、模拟模型使用

- url: https://ai.pydantic.dev/examples/
  why: 各种 PydanticAI 用例的工作示例
  content: 聊天应用、RAG 系统、SQL 生成、FastAPI 集成

# 上下文工程基础 - 要适配的基础框架
- file: ../../../README.md
  why: 核心上下文工程原则和工作流,适配 AI agent

- file: ../../../.claude/commands/generate-prp.md
  why: 基础 PRP 生成模式,专业化用于 PydanticAI 开发

- file: ../../../.claude/commands/execute-prp.md
  why: 基础 PRP 执行模式,适配 AI agent 验证

- file: ../../../PRPs/templates/prp_base.md
  why: 基础 PRP 模板结构,专业化用于 PydanticAI 领域

# MCP SERVER 示例 - 参考实现
- file: ../mcp-server/CLAUDE.md
  why: 领域专用实施指南模式示例

- file: ../mcp-server/.claude/commands/prp-mcp-create.md
  why: 专业化 PRP 生成命令结构示例
```

### PydanticAI 框架分析(来自研究)

```typescript
// PydanticAI 架构模式(来自官方文档)
interface PydanticAIPatterns {
  // 核心 agent 模式
  agent_creation: {
    model_providers: ["openai:gpt-4o", "anthropic:claude-3-sonnet", "google:gemini-1.5-flash"];
    configuration: ["system_prompt", "deps_type", "output_type", "instructions"];
    execution_methods: ["run()", "run_sync()", "run_stream()", "iter()"];
  };

  // 工具集成模式
  tool_system: {
    registration: ["@agent.tool", "@agent.tool_plain", "tools=[]"];
    context_access: ["RunContext[DepsType]", "ctx.deps", "dependency_injection"];
    return_types: ["str", "ToolReturn", "structured_data", "rich_content"];
    validation: ["parameter_schemas", "docstring_extraction", "type_hints"];
  };

  // 测试和验证
  testing_patterns: {
    unit_testing: ["TestModel", "FunctionModel", "Agent.override()"];
    validation: ["capture_run_messages()", "pytest_fixtures", "mock_dependencies"];
    evals: ["model_performance", "agent_behavior", "production_monitoring"];
  };

  // 生产考虑因素
  security: {
    api_keys: ["environment_variables", "secure_storage", "key_rotation"];
    input_validation: ["pydantic_models", "parameter_validation", "sanitization"];
    monitoring: ["logfire_integration", "usage_tracking", "error_handling"];
  };
}
```

### 开发工作流分析(来自研究)

```yaml
# PydanticAI 开发模式(从文档和示例中研究)
project_structure:
  basic_pattern: |
    my_agent/
    ├── agent.py          # 主要 agent 定义
    ├── tools.py          # 工具函数
    ├── models.py         # Pydantic 输出模型
    ├── dependencies.py   # 上下文依赖项
    └── tests/
        ├── test_agent.py
        └── test_tools.py

  advanced_pattern: |
    agents_project/
    ├── agents/
    │   ├── __init__.py
    │   ├── chat_agent.py
    │   └── workflow_agent.py
    ├── tools/
    │   ├── __init__.py
    │   ├── web_search.py
    │   └── calculator.py
    ├── models/
    │   ├── __init__.py
    │   └── outputs.py
    ├── dependencies/
    │   ├── __init__.py
    │   └── database.py
    ├── tests/
    └── examples/

package_management:
  installation: "pip install pydantic-ai"
  optional_deps: "pip install 'pydantic-ai[examples]'"
  dev_deps: "pip install pytest pytest-asyncio inline-snapshot dirty-equals"

testing_workflow:
  unit_tests: "pytest tests/ -v"
  agent_testing: "使用 TestModel 进行快速验证"
  integration_tests: "使用真实模型并进行速率限制"
  evals: "单独运行性能基准测试"

environment_setup:
  api_keys: ["OPENAI_API_KEY", "ANTHROPIC_API_KEY", "GEMINI_API_KEY"]
  development: "设置 ALLOW_MODEL_REQUESTS=False 用于测试"
  production: "配置适当的日志记录和监控"
```

### 安全性和最佳实践(来自研究)

```typescript
// PydanticAI 专用安全模式(来自研究)
interface PydanticAISecurity {
  // API 密钥管理
  api_security: {
    storage: "environment_variables_only";
    access_control: "minimal_required_permissions";
    monitoring: "usage_tracking_and_alerts";
  };

  // 输入验证和净化
  input_security: {
    validation: "pydantic_models_for_all_inputs";
    sanitization: "escape_user_content";
    rate_limiting: "prevent_abuse_patterns";
    content_filtering: "block_malicious_prompts";
  };

  // 提示注入预防
  prompt_security: {
    system_prompts: "clear_instruction_boundaries";
    user_input: "validate_and_sanitize";
    tool_calls: "parameter_validation";
    output_filtering: "structured_response_validation";
  };

  // 生产考虑因素
  production_security: {
    monitoring: "logfire_integration_recommended";
    error_handling: "no_sensitive_data_in_logs";
    dependency_injection: "secure_context_management";
    testing: "security_focused_unit_tests";
  };
}
```

### 常见陷阱和边缘情况(来自研究)

```yaml
# 通过研究发现的 PydanticAI 特定陷阱
agent_gotchas:
  model_limits:
    issue: "不同的模型有不同的 token 限制和功能"
    solution: "使用 FallbackModel 进行自动模型切换"
    validation: "使用多个模型提供商进行测试"

  async_patterns:
    issue: "混合同步和异步 agent 调用可能会导致问题"
    solution: "在整个过程中使用一致的 async/await 模式"
    validation: "测试同步和异步执行路径"

  dependency_injection:
    issue: "复杂的依赖关系图可能难以调试"
    solution: "保持依赖项简单且类型良好"
    validation: "单独进行单元测试依赖项"

tool_integration_gotchas:
  parameter_validation:
    issue: "工具可能会收到意外的参数类型"
    solution: "对工具参数使用严格的 Pydantic 模型"
    validation: "使用无效输入测试工具"

  context_management:
    issue: "RunContext 状态可能变得不一致"
    solution: "尽可能设计无状态工具"
    validation: "测试运行之间的上下文隔离"

  error_handling:
    issue: "工具错误可能会导致整个 agent 运行崩溃"
    solution: "实现重试机制和优雅降级"
    validation: "测试错误场景和恢复"

testing_gotchas:
  model_costs:
    issue: "真实模型测试可能很昂贵"
    solution: "使用 TestModel 和 FunctionModel 进行开发"
    validation: "将单元测试与昂贵的评估运行分开"

  async_testing:
    issue: "异步 agent 测试需要特殊设置"
    solution: "使用 pytest-asyncio 和适当的 fixture"
    validation: "测试同步和异步代码路径"

  deterministic_behavior:
    issue: "AI 响应本质上是非确定性的"
    solution: "专注于测试工具调用和结构化输出"
    validation: "使用 inline-snapshot 进行复杂断言"
```

## 实施蓝图

### 技术研究阶段(已完成)

**全面的 PydanticAI 分析已完成:**

✅ **核心框架分析:**
- PydanticAI 架构、agent 创建模式、模型提供商集成
- 来自官方文档和示例的项目结构约定
- 依赖注入系统和类型安全设计原则
- 带有 async/sync 模式和流式支持的开发工作流

✅ **工具系统调查:**
- 函数工具注册模式(@agent.tool vs @agent.tool_plain)
- 使用 RunContext 和依赖注入进行上下文管理
- 参数验证、文档字符串提取和架构生成
- 丰富的返回类型和多模态内容支持

✅ **测试框架分析:**
- TestModel 和 FunctionModel 用于无需 API 调用的单元测试
- Agent.override() 模式用于测试隔离
- Pytest 与异步测试和 fixture 的集成
- 模型性能评估策略 vs 单元测试

✅ **安全和生产模式:**
- 使用环境变量和安全存储的 API 密钥管理
- 使用 Pydantic 模型和参数架构进行输入验证
- 速率限制、监控和 Logfire 集成
- 常见安全漏洞和预防策略

### 模板包生成

基于研究结果创建完整的 PydanticAI 上下文工程模板:

```yaml
生成任务 1 - 创建 PydanticAI 模板目录结构:
  CREATE 完整的用例目录结构:
    - use-cases/pydantic-ai/
    - .claude/commands/ 带 PydanticAI 专用斜杠命令
    - PRPs/templates/ 带 agent 聚焦基础模板
    - examples/ 带工作 agent 实现
    - 每个模板包要求的所有子目录

生成任务 2 - 生成 PydanticAI 专用 CLAUDE.md:
  CREATE PydanticAI 全局规则文件,包括:
    - PydanticAI agent 创建和工具集成模式
    - 模型提供商配置和 API 密钥管理
    - Agent 架构模式(聊天、工作流、工具启用)
    - 使用 TestModel/FunctionModel 的测试策略
    - AI agent 和工具集成的安全最佳实践
    - 常见陷阱: async 模式、上下文管理、模型限制

生成任务 3 - 创建 PydanticAI PRP 命令:
  GENERATE 领域专用斜杠命令:
    - generate-pydantic-ai-prp.md 带 agent 研究模式
    - execute-pydantic-ai-prp.md 带 AI agent 验证循环
    - 包括 PydanticAI 文档引用和研究策略
    - Agent 专用成功标准和测试要求

生成任务 4 - 开发 PydanticAI 基础 PRP 模板:
  CREATE 专业化 prp_pydantic_ai_base.md 模板:
    - 预填充研究中的 agent 架构模式
    - PydanticAI 专用成功标准和验证关卡
    - 官方文档引用和模型提供商指南
    - 使用 TestModel 和验证策略的 agent 测试模式

生成任务 5 - 创建工作 PydanticAI 示例:
  GENERATE 全面的示例 agent:
    - basic_chat_agent: 简单对话带内存
    - tool_enabled_agent: 网络搜索和计算器集成
    - workflow_agent: 多步骤任务处理
    - structured_output_agent: 自定义 Pydantic 模型
    - testing_examples: 单元测试和验证模式
    - 包括配置文件和环境设置

生成任务 6 - 创建模板复制脚本:
  CREATE 用于模板部署的 Python 脚本:
    - copy_template.py 带命令行界面
    - 将整个 PydanticAI 模板结构复制到目标位置
    - 处理所有文件: CLAUDE.md、命令、PRP、示例等
    - 错误处理和成功反馈,包含后续步骤

生成任务 7 - 生成全面的 README:
  CREATE PydanticAI 专用 README.md:
    - 清晰描述: "PydanticAI 上下文工程模板"
    - 模板复制脚本使用(在顶部显著位置)
    - AI agent 开发的 PRP 框架工作流
    - 带 PydanticAI 专用说明的模板结构
    - 带 agent 创建示例的快速入门指南
    - 工作示例概述和测试模式
```

### PydanticAI 专业化细节

```typescript
// PydanticAI 的模板专业化
const pydantic_ai_specialization = {
  agent_patterns: [
    "chat_agent_with_memory",
    "tool_integrated_agent",
    "workflow_processing_agent",
    "structured_output_agent"
  ],

  validation: [
    "agent_behavior_testing",
    "tool_function_validation",
    "output_schema_verification",
    "model_provider_compatibility"
  ],

  examples: [
    "basic_conversation_agent",
    "web_search_calculator_tools",
    "multi_step_workflow_processing",
    "custom_pydantic_output_models",
    "comprehensive_testing_suite"
  ],

  gotchas: [
    "async_sync_mixing_issues",
    "model_token_limits",
    "dependency_injection_complexity",
    "tool_error_handling_failures",
    "context_state_management"
  ],

  security: [
    "api_key_environment_management",
    "input_validation_pydantic_models",
    "prompt_injection_prevention",
    "rate_limiting_implementation",
    "secure_tool_parameter_handling"
  ]
};
```

### 集成点

```yaml
CONTEXT_ENGINEERING_FRAMEWORK:
  - base_workflow: 继承 PRP 生成/执行,适配 AI agent 开发
  - validation_principles: 扩展 AI 专用测试(agent 行为、工具验证)
  - documentation_standards: 保持一致性,同时专业化 PydanticAI

PYDANTIC_AI_INTEGRATION:
  - agent_architecture: 包括聊天、工具启用和工作流 agent 模式
  - model_providers: 支持 OpenAI、Anthropic、Gemini 配置模式
  - testing_framework: 使用 TestModel/FunctionModel 进行开发验证
  - production_patterns: 包括安全性、监控和部署考虑因素

TEMPLATE_STRUCTURE:
  - directory_organization: 遵循带 AI 专用示例的用例模板模式
  - file_naming: generate-pydantic-ai-prp.md, prp_pydantic_ai_base.md
  - content_format: Markdown 带 agent 代码示例和配置
  - command_patterns: 扩展 AI agent 开发工作流的斜杠命令
```

## 验证循环

### 级别 1: PydanticAI 模板结构验证

```bash
# 验证完整的 PydanticAI 模板包结构
find use-cases/pydantic-ai -type f | sort
ls -la use-cases/pydantic-ai/.claude/commands/
ls -la use-cases/pydantic-ai/PRPs/templates/
ls -la use-cases/pydantic-ai/examples/

# 验证复制脚本和 agent 示例
test -f use-cases/pydantic-ai/copy_template.py
ls use-cases/pydantic-ai/examples/*/agent.py 2>/dev/null | wc -l  # 应该有 agent 文件
python use-cases/pydantic-ai/copy_template.py --help 2>/dev/null || echo "复制脚本需要帮助"

# 预期: 所有必需文件,包括工作 agent 示例
# 如果缺失: 使用 PydanticAI 模式生成缺失的组件
```

### 级别 2: PydanticAI 内容质量验证

```bash
# 验证 PydanticAI 专用内容准确性
grep -r "from pydantic_ai import Agent" use-cases/pydantic-ai/examples/
grep -r "@agent.tool" use-cases/pydantic-ai/examples/
grep -r "TestModel\|FunctionModel" use-cases/pydantic-ai/

# 检查 PydanticAI 模式并避免通用内容
grep -r "TODO\|PLACEHOLDER" use-cases/pydantic-ai/
grep -r "openai:gpt-4o\|anthropic:" use-cases/pydantic-ai/
grep -r "RunContext\|deps_type" use-cases/pydantic-ai/

# 预期: 真实的 PydanticAI 代码,无占位符,存在 agent 模式
# 如果有问题: 添加适当的 PydanticAI 专用模式和示例
```

### 级别 3: PydanticAI 功能验证

```bash
# 测试 PydanticAI 模板功能
cd use-cases/pydantic-ai

# 使用 agent 焦点测试 PRP 生成
/generate-pydantic-ai-prp INITIAL.md
ls PRPs/*.md | grep -v templates | head -1  # 应该生成 agent PRP

# 验证 agent 示例可以解析(语法检查)
python -m py_compile examples/basic_chat_agent/agent.py 2>/dev/null && echo "基本 agent 语法正常"
python -m py_compile examples/tool_enabled_agent/agent.py 2>/dev/null && echo "工具 agent 语法正常"

# 预期: PRP 生成工作,agent 示例具有有效语法
# 如果失败: 调试 PydanticAI 命令模式并修复 agent 代码
```

### 级别 4: PydanticAI 集成测试

```bash
# 验证 PydanticAI 专业化保持基础框架兼容性
diff -r ../../.claude/commands/ .claude/commands/ | head -10
grep -r "Context is King" . | wc -l  # 应该继承基础原则
grep -r "pydantic.ai.dev\|PydanticAI" . | wc -l  # 应该有专业化

# 测试 agent 示例具有适当的依赖项
grep -r "pydantic_ai" examples/ | wc -l  # 应该导入 PydanticAI
grep -r "pytest" examples/testing_examples/ | wc -l  # 应该有测试

# 预期: 适当的专业化,工作 agent 模式,包含测试
# 如果有问题: 调整以保持兼容性,同时添加 PydanticAI 功能
```

## 最终验证清单

### PydanticAI 模板包完整性

- [ ] 完整的目录结构: `tree use-cases/pydantic-ai`
- [ ] PydanticAI 专用文件: 带有 agent 模式的 CLAUDE.md、专业化命令
- [ ] 复制脚本存在: 带有适当 PydanticAI 功能的 `copy_template.py`
- [ ] README 全面: 包括 agent 开发工作流和复制说明
- [ ] Agent 示例工作: 所有示例使用真实的 PydanticAI 代码模式
- [ ] 测试模式包括: TestModel/FunctionModel 示例和验证
- [ ] 文档完整: PydanticAI 专用模式和陷阱已记录

### PydanticAI 的质量和可用性

- [ ] 无占位符内容: `grep -r "TODO\|PLACEHOLDER"` 返回空
- [ ] PydanticAI 专业化: Agent 模式、工具、测试已正确记录
- [ ] 验证循环工作: 所有命令可执行,具有 agent 专用功能
- [ ] 框架集成: 适用于 AI 开发的基础上下文工程
- [ ] 准备用于 AI 开发: 开发者可以立即创建 PydanticAI agent

### PydanticAI 框架集成

- [ ] 继承基础原则: 为 AI agent 保留上下文工程工作流
- [ ] 适当的 AI 专业化: 包括 PydanticAI 模式、安全性、测试
- [ ] 命令兼容性: 斜杠命令适用于 agent 开发工作流
- [ ] 文档一致性: 遵循模式,同时专业化 AI 开发
- [ ] 可维护结构: 随着 PydanticAI 框架的发展易于更新

---

## 要避免的反模式

### PydanticAI 模板生成

- ❌ 不要创建通用 AI 模板 - 彻底研究 PydanticAI 细节
- ❌ 不要跳过 agent 架构研究 - 理解工具、内存、验证
- ❌ 不要使用占位符 agent 代码 - 包括真实的、工作的 PydanticAI 示例
- ❌ 不要忽略测试模式 - TestModel/FunctionModel 对 AI 至关重要

### PydanticAI 内容质量

- ❌ 不要假设 AI 模式 - 明确记录 PydanticAI 专用陷阱
- ❌ 不要跳过安全研究 - API 密钥、输入验证、提示注入至关重要
- ❌ 不要忽略模型提供商 - 包括 OpenAI、Anthropic、Gemini 模式
- ❌ 不要忘记 async 模式 - PydanticAI 有特定的 async/sync 考虑因素

### PydanticAI 框架集成

- ❌ 不要破坏上下文工程 - 保持 AI 开发的 PRP 工作流
- ❌ 不要重复基础功能 - 适当地扩展和专业化
- ❌ 不要忽略 AI 专用验证 - agent 行为测试是独特要求
- ❌ 不要跳过真实示例 - 包括带有工具和验证的工作 agent

**信心分数: 9/10** - 全面的 PydanticAI 研究已完成,框架模式已理解,准备为 AI agent 开发生成专业化的上下文工程模板。
