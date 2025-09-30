---
name: "PydanticAI 智能体 PRP 模板"
description: "用于为 PydanticAI 智能体开发项目生成全面 PRP 的模板"
---

## 目的

[简要描述要构建的 PydanticAI 智能体及其主要目的]

## 核心原则

1. **PydanticAI 最佳实践**：深度集成 PydanticAI 模式，用于智能体创建、工具和结构化输出
2. **生产就绪**：包含用于生产部署的安全性、测试和监控
3. **类型安全优先**：在整个过程中利用 PydanticAI 的类型安全设计和 Pydantic 验证
4. **Context Engineering 集成**：将经过验证的 Context Engineering 工作流应用于 AI 智能体开发
5. **全面测试**：使用 TestModel 和 FunctionModel 进行彻底的智能体验证

## ⚠️ 实现指南：不要过度工程化

**重要**：保持你的智能体实现专注和实用。不要构建不必要的复杂性。

### 不要做什么：
- ❌ **不要创建几十个工具** - 只构建智能体实际需要的工具
- ❌ **不要过度复杂化依赖项** - 保持依赖注入简单和专注
- ❌ **不要添加不必要的抽象** - 直接遵循 main_agent_reference 模式
- ❌ **不要构建复杂的工作流**，除非特别需要
- ❌ **不要添加结构化输出**，除非特别需要验证（默认使用字符串）
- ❌ **不要在 examples/ 文件夹中构建**

### 要做什么：
- ✅ **从简单开始** - 构建满足需求的最小可行智能体
- ✅ **增量添加工具** - 只实现智能体运行所需的内容
- ✅ **遵循 main_agent_reference** - 使用经过验证的模式，不要重新发明
- ✅ **默认使用字符串输出** - 只有在需要验证时才添加 result_type
- ✅ **尽早且经常测试** - 在构建时使用 TestModel 进行验证

### 关键问题：
**"这个智能体真的需要这个功能来完成其核心目的吗？"**

如果答案是否定的，就不要构建它。保持简单、专注和功能性。

---

## 目标

[详细描述智能体应该完成什么]

## 为什么

[解释为什么需要这个智能体以及它解决什么问题]

## 什么

### 智能体类型分类
- [ ] **聊天智能体**：具有记忆和上下文的对话界面
- [ ] **工具启用智能体**：具有外部工具集成能力的智能体
- [ ] **工作流智能体**：多步骤任务处理和编排
- [ ] **结构化输出智能体**：复杂的数据验证和格式化

### 模型提供商需求
- [ ] **OpenAI**：`openai:gpt-4o` 或 `openai:gpt-4o-mini`
- [ ] **Anthropic**：`anthropic:claude-3-5-sonnet-20241022` 或 `anthropic:claude-3-5-haiku-20241022`
- [ ] **Google**：`gemini-1.5-flash` 或 `gemini-1.5-pro`
- [ ] **备用策略**：支持多个提供商并自动故障转移

### 外部集成
- [ ] 数据库连接（指定类型：PostgreSQL、MongoDB 等）
- [ ] REST API 集成（列出所需服务）
- [ ] 文件系统操作
- [ ] 网页抓取或搜索功能
- [ ] 实时数据源

### 成功标准
- [ ] 智能体成功处理指定的用例
- [ ] 所有工具都能正确工作，并具有适当的错误处理
- [ ] 结构化输出根据 Pydantic 模型进行验证
- [ ] 使用 TestModel 和 FunctionModel 的全面测试覆盖率
- [ ] 实现了安全措施（API 密钥、输入验证、速率限制）
- [ ] 性能满足要求（响应时间、吞吐量）

## 所有需要的上下文

### PydanticAI 文档与研究

```yaml
# MCP 服务器
- mcp: Archon
  query: "PydanticAI agent creation model providers tools dependencies"
  why: 核心框架理解和最新模式

# 必需的 PYDANTIC AI 文档 - 必须研究
- url: https://ai.pydantic.dev/
  why: 官方 PydanticAI 文档，带有入门指南
  content: 智能体创建、模型提供商、依赖注入模式

- url: https://ai.pydantic.dev/agents/
  why: 全面的智能体架构和配置模式
  content: 系统提示、输出类型、执行方法、智能体组合

- url: https://ai.pydantic.dev/tools/
  why: 工具集成模式和函数注册
  content: @agent.tool 装饰器、RunContext 使用、参数验证

- url: https://ai.pydantic.dev/testing/
  why: 特定于 PydanticAI 智能体的测试策略
  content: TestModel、FunctionModel、Agent.override()、pytest 模式

- url: https://ai.pydantic.dev/models/
  why: 模型提供商配置和认证
  content: OpenAI、Anthropic、Gemini 设置、API 密钥管理、备用模型

# 预构建示例
- path: examples/
  why: Pydantic AI 智能体的参考实现
  content: 一堆已经构建的简单 Pydantic AI 示例可供参考，包括如何设置模型和提供商

- path: examples/cli.py
  why: 展示与 Pydantic AI 智能体的真实世界交互
  content: 具有流式传输、工具调用可见性和对话处理的对话式 CLI - 演示用户实际如何与智能体交互
```

### 智能体架构研究

```yaml
# PydanticAI 架构模式（遵循 main_agent_reference）
agent_structure:
  configuration:
    - settings.py: 使用 pydantic-settings 的基于环境的配置
    - providers.py: 使用 get_llm_model() 的模型提供商抽象
    - API 密钥和模型选择的环境变量
    - 永远不要硬编码模型字符串，如 "openai:gpt-4o"

  agent_definition:
    - 默认使用字符串输出（除非需要结构化输出，否则不使用 result_type）
    - 使用 providers.py 中的 get_llm_model() 进行模型配置
    - 系统提示作为字符串常量或函数
    - 外部服务的 Dataclass 依赖项

  tool_integration:
    - @agent.tool 用于具有 RunContext[DepsType] 的上下文感知工具
    - 工具函数作为可以独立调用的纯函数
    - 工具实现中的适当错误处理和日志记录
    - 通过 RunContext.deps 进行依赖注入

  testing_strategy:
    - TestModel 用于快速开发验证
    - FunctionModel 用于自定义行为测试
    - Agent.override() 用于测试隔离
    - 使用模拟的全面工具测试
```

### 安全和生产考虑

```yaml
# PydanticAI 安全模式（需要研究）
security_requirements:
  api_management:
    environment_variables: ["OPENAI_API_KEY", "ANTHROPIC_API_KEY", "GEMINI_API_KEY"]
    secure_storage: "永远不要将 API 密钥提交到版本控制"
    rotation_strategy: "计划密钥轮换和管理"

  input_validation:
    sanitization: "使用 Pydantic 模型验证所有用户输入"
    prompt_injection: "实施提示注入预防策略"
    rate_limiting: "通过适当的节流防止滥用"

  output_security:
    data_filtering: "确保智能体响应中没有敏感数据"
    content_validation: "验证输出结构和内容"
    logging_safety: "安全记录，不暴露秘密"
```

### 常见 PydanticAI 陷阱（研究并记录）

```yaml
# 需要研究和解决的智能体特定陷阱
implementation_gotchas:
  async_patterns:
    issue: "不一致地混合同步和异步智能体调用"
    research: "PydanticAI async/await 最佳实践"
    solution: "[根据研究记录]"

  model_limits:
    issue: "不同的模型具有不同的能力和 token 限制"
    research: "模型提供商比较和能力"
    solution: "[根据研究记录]"

  dependency_complexity:
    issue: "复杂的依赖关系图可能难以调试"
    research: "PydanticAI 中的依赖注入最佳实践"
    solution: "[根据研究记录]"

  tool_error_handling:
    issue: "工具失败可能导致整个智能体运行崩溃"
    research: "工具的错误处理和重试模式"
    solution: "[根据研究记录]"
```

## 实现蓝图

### 技术研究阶段

**需要研究 - 在实现之前完成：**

✅ **PydanticAI 框架深入研究：**
- [ ] 智能体创建模式和最佳实践
- [ ] 模型提供商配置和备用策略
- [ ] 工具集成模式（@agent.tool vs @agent.tool_plain）
- [ ] 依赖注入系统和类型安全
- [ ] 使用 TestModel 和 FunctionModel 的测试策略

✅ **智能体架构调查：**
- [ ] 项目结构约定（agent.py、tools.py、models.py、dependencies.py）
- [ ] 系统提示设计（静态 vs 动态）
- [ ] 使用 Pydantic 模型的结构化输出验证
- [ ] 异步/同步模式和流式支持
- [ ] 错误处理和重试机制

✅ **安全和生产模式：**
- [ ] API 密钥管理和安全配置
- [ ] 输入验证和提示注入预防
- [ ] 速率限制和监控策略
- [ ] 日志记录和可观测性模式
- [ ] 部署和扩展考虑

### 智能体实现计划

```yaml
实现任务 1 - 智能体架构设置（遵循 main_agent_reference）：
  创建智能体项目结构：
    - settings.py: 使用 pydantic-settings 的基于环境的配置
    - providers.py: 使用 get_llm_model() 的模型提供商抽象
    - agent.py: 主智能体定义（默认字符串输出）
    - tools.py: 具有适当装饰器的工具函数
    - dependencies.py: 外部服务集成（dataclasses）
    - tests/: 全面的测试套件

实现任务 2 - 核心智能体开发：
  实现 agent.py，遵循 main_agent_reference 模式：
    - 使用 providers.py 中的 get_llm_model() 进行模型配置
    - 系统提示作为字符串常量或函数
    - 使用 dataclass 的依赖注入
    - 除非特别需要结构化输出，否则不使用 result_type
    - 错误处理和日志记录

实现任务 3 - 工具集成：
  开发 tools.py：
    - 具有 @agent.tool 装饰器的工具函数
    - RunContext[DepsType] 集成用于依赖访问
    - 使用适当类型提示的参数验证
    - 错误处理和重试机制
    - 工具文档和模式生成

实现任务 4 - 数据模型和依赖项：
  创建 models.py 和 dependencies.py：
    - 用于结构化输出的 Pydantic 模型
    - 用于外部服务的依赖类
    - 用于工具的输入验证模型
    - 自定义验证器和约束

实现任务 5 - 全面测试：
  实现测试套件：
    - TestModel 集成用于快速开发
    - FunctionModel 测试用于自定义行为
    - Agent.override() 模式用于隔离
    - 使用真实提供商的集成测试
    - 工具验证和错误场景测试

实现任务 6 - 安全和配置：
  设置安全模式：
    - API 密钥的环境变量管理
    - 输入清理和验证
    - 速率限制实现
    - 安全日志记录和监控
    - 生产部署配置
```

## 验证循环

### 级别 1：智能体结构验证

```bash
# 验证完整的智能体项目结构
find agent_project -name "*.py" | sort
test -f agent_project/agent.py && echo "Agent definition present"
test -f agent_project/tools.py && echo "Tools module present"
test -f agent_project/models.py && echo "Models module present"
test -f agent_project/dependencies.py && echo "Dependencies module present"

# 验证适当的 PydanticAI 导入
grep -q "from pydantic_ai import Agent" agent_project/agent.py
grep -q "@agent.tool" agent_project/tools.py
grep -q "from pydantic import BaseModel" agent_project/models.py

# 预期：所有必需的文件都具有适当的 PydanticAI 模式
# 如果缺失：使用正确的模式生成缺失的组件
```

### 级别 2：智能体功能验证

```bash
# 测试智能体可以导入和实例化
python -c "
from agent_project.agent import agent
print('Agent created successfully')
print(f'Model: {agent.model}')
print(f'Tools: {len(agent.tools)}')
"

# 使用 TestModel 进行验证测试
python -c "
from pydantic_ai.models.test import TestModel
from agent_project.agent import agent
test_model = TestModel()
with agent.override(model=test_model):
    result = agent.run_sync('Test message')
    print(f'Agent response: {result.output}')
"

# 预期：智能体实例化工作，工具已注册，TestModel 验证通过
# 如果失败：调试智能体配置和工具注册
```

### 级别 3：全面测试验证

```bash
# 运行完整的测试套件
cd agent_project
python -m pytest tests/ -v

# 测试特定的智能体行为
python -m pytest tests/test_agent.py::test_agent_response -v
python -m pytest tests/test_tools.py::test_tool_validation -v
python -m pytest tests/test_models.py::test_output_validation -v

# 预期：所有测试通过，实现全面覆盖
# 如果失败：根据测试失败修复实现
```

### 级别 4：生产就绪验证

```bash
# 验证安全模式
grep -r "API_KEY" agent_project/ | grep -v ".py:" # 不应暴露密钥
test -f agent_project/.env.example && echo "Environment template present"

# 检查错误处理
grep -r "try:" agent_project/ | wc -l  # 应该有错误处理
grep -r "except" agent_project/ | wc -l  # 应该有异常处理

# 验证日志设置
grep -r "logging\|logger" agent_project/ | wc -l  # 应该有日志记录

# 预期：安全措施到位，错误处理全面，日志已配置
# 如果有问题：实现缺失的安全和生产模式
```

## 最终验证清单

### 智能体实现完整性

- [ ] 完整的智能体项目结构：`agent.py`、`tools.py`、`models.py`、`dependencies.py`
- [ ] 使用适当的模型提供商配置进行智能体实例化
- [ ] 使用 @agent.tool 装饰器和 RunContext 集成的工具注册
- [ ] 使用 Pydantic 模型验证的结构化输出
- [ ] 依赖注入已正确配置和测试
- [ ] 使用 TestModel 和 FunctionModel 的全面测试套件

### PydanticAI 最佳实践

- [ ] 在整个过程中使用适当的类型提示和验证实现类型安全
- [ ] 实现了安全模式（API 密钥、输入验证、速率限制）
- [ ] 错误处理和重试机制以实现稳健操作
- [ ] 异步/同步模式一致且适当
- [ ] 文档和代码注释以提高可维护性

### 生产就绪

- [ ] 使用 .env 文件和验证的环境配置
- [ ] 日志记录和监控设置以实现可观测性
- [ ] 性能优化和资源管理
- [ ] 具有适当配置管理的部署就绪
- [ ] 维护和更新策略已记录

---

## 要避免的反模式

### PydanticAI 智能体开发

- ❌ 不要跳过 TestModel 验证 - 在开发期间始终使用 TestModel 进行测试
- ❌ 不要硬编码 API 密钥 - 对所有凭据使用环境变量
- ❌ 不要忽略异步模式 - PydanticAI 有特定的异步/同步要求
- ❌ 不要创建复杂的工具链 - 保持工具专注和可组合
- ❌ 不要跳过错误处理 - 实现全面的重试和备用机制

### 智能体架构

- ❌ 不要混合智能体类型 - 清楚地分离聊天、工具、工作流和结构化输出模式
- ❌ 不要忽略依赖注入 - 使用适当的类型安全依赖管理
- ❌ 不要跳过输出验证 - 始终对结构化响应使用 Pydantic 模型
- ❌ 不要忘记工具文档 - 确保所有工具都有适当的描述和模式

### 安全和生产

- ❌ 不要暴露敏感数据 - 验证所有输出和日志的安全性
- ❌ 不要跳过输入验证 - 清理和验证所有用户输入
- ❌ 不要忽略速率限制 - 为外部服务实现适当的节流
- ❌ 不要在没有监控的情况下部署 - 从一开始就包含适当的可观测性

**研究状态：[待完成]** - 在实现开始之前完成全面的 PydanticAI 研究。