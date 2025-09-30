## 功能：

[用你自己的上下文替换括号中的所有内容]
[提供你想要构建的智能体的概述。细节越多越好！]
[过于简单的示例：使用 Pydantic AI 构建一个简单的研究智能体，可以使用 Brave API 研究主题，并使用 Gmail 起草电子邮件来分享见解。]

## 工具：

[描述你想要为智能体使用的工具 - 功能、参数、返回内容等。尽可能具体 - 越具体越好。]

## 依赖项

[描述智能体工具所需的依赖项（用于 Pydantic AI RunContext）- 例如 API 密钥、数据库连接、HTTP 客户端等。]

## 系统提示

[在这里描述智能体的指令 - 你可以在这里创建完整的系统提示，或给出一般描述来指导编码助手]

## 示例：

[将过去项目或在线资源中的任何额外示例智能体/工具实现添加到 examples/ 文件夹中，并在此处引用它们。]
[模板已经包含以下 Pydantic AI 内容：]

- examples/basic_chat_agent - 具有对话记忆的基本聊天智能体
- examples/tool_enabled_agent - 具有网页搜索功能的工具启用智能体
- examples/structured_output_agent - 用于数据验证的结构化输出智能体
- examples/testing_examples - 使用 TestModel 和 FunctionModel 的测试示例
- examples/main_agent_reference - 构建 Pydantic AI 智能体的最佳实践

## 文档：

[添加你希望它引用的任何额外文档 - 这可以是你放在 PRPs/ai_docs 中的精选文档、URL 等。]

- Pydantic AI 官方文档：https://ai.pydantic.dev/
- 智能体创建指南：https://ai.pydantic.dev/agents/
- 工具集成：https://ai.pydantic.dev/tools/
- 测试模式：https://ai.pydantic.dev/testing/
- 模型提供商：https://ai.pydantic.dev/models/

## 其他考虑：

- 使用环境变量进行 API 密钥配置，而不是硬编码的模型字符串
- 保持智能体简单 - 默认使用字符串输出，除非特别需要结构化输出
- 遵循 main_agent_reference 模式进行配置和提供商设置
- 始终包含使用 TestModel 的全面测试用于开发

[为编码助手添加任何额外的考虑因素，特别是你希望它记住的"陷阱"。]