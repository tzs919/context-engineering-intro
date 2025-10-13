---
name: "LangGraph AI Agent Template Generator"
description: "Generate comprehensive context engineering templates for building intelligent AI agents with LangGraph, LangChain, and LangSmith"
complexity: "Beginner-friendly"
technology: "LangGraph + LangChain + LangSmith"
---

## Purpose

生成一个完整的上下文工程模板包,用于使用 LangGraph 构建智能 AI 代理,包括工具集成、对话处理和结构化数据验证。该模板针对初学者友好,同时包含生产就绪的最佳实践。

## Why

- **开发者加速**: 使开发者能够快速开始构建 LangGraph AI 代理
- **最佳实践集成**: 包含经过验证的架构模式和安全实践
- **完整的生态系统**: 涵盖 LangGraph、LangChain 和 LangSmith 的集成
- **避免常见陷阱**: 文档化常见的错误和边缘情况
- **可扩展框架**: 创建随技术演进而发展的可重用模板

## What

### 模板包组件

**完整的目录结构:**
```
use-cases/langgraph-agents/
├── CLAUDE.md                           # LangGraph 实现指南
├── .claude/commands/
│   ├── generate-langgraph-prp.md      # LangGraph PRP 生成命令
│   └── execute-langgraph-prp.md       # LangGraph PRP 执行命令
├── PRPs/
│   ├── templates/
│   │   └── prp_langgraph_base.md      # LangGraph 基础 PRP 模板
│   ├── ai_docs/                        # LangGraph 文档资源(可选)
│   └── INITIAL.md                      # 示例功能请求
├── examples/                           # 实际工作代码示例
│   ├── basic_chat_agent.py            # 基础聊天代理与记忆
│   ├── tool_enabled_agent.py          # 工具集成代理(搜索+计算)
│   ├── workflow_agent.py              # 多步骤工作流代理
│   ├── structured_output_agent.py     # Pydantic 结构化输出
│   └── testing_examples.py            # 代理测试模式
├── copy_template.py                   # 模板部署脚本
└── README.md                          # 综合使用指南
```

### 成功标准

- [ ] 完整的模板包结构生成
- [ ] 所有必需文件存在且格式正确
- [ ] 特定领域内容准确代表 LangGraph 模式
- [ ] 上下文工程原则正确适配到 LangGraph
- [ ] 验证循环适当且可执行
- [ ] 模板可立即用于创建 LangGraph 项目
- [ ] 与基础上下文工程框架的集成得以维护
- [ ] 包含综合文档和示例

## All Needed Context

### 技术文档研究 (已完成的 Web 研究)

**LangGraph 核心概念:**

1. **什么是 LangGraph**
   - LangGraph 是 LangChain 生态系统中的库,提供框架用于定义、协调和执行多个 LLM 代理
   - Python 框架,设计用于使用基于图的结构构建有状态的 AI 工作流
   - MIT 许可的开源库,免费使用
   - 官方仓库: https://github.com/langchain-ai/langgraph

2. **核心架构组件**
   - **Nodes (节点)**: 执行工作单元的图中的步骤,接受输入并产生输出
   - **Edges (边)**: 连接节点,定义图的流程
   - **State (状态)**: 流经图的共享内存对象,存储消息、变量、中间结果和决策历史
   - **Checkpointer (检查点)**: 用于持久化状态和实现时间旅行调试

3. **关键特性**
   - 持久化状态管理
   - 多代理协调
   - 内置人工监督支持
   - 并行化、流式传输、检查点、追踪和任务队列

**代理架构模式:**

1. **Tool-Calling Agents (ReAct 模式)**
   - LLM 在 while 循环中重复调用
   - 每步决定调用哪些工具及使用什么输入
   - 最适合需要工具使用或复杂规划的任务

2. **Router Agents (路由代理)**
   - 允许 LLM 从指定选项集中选择单个步骤

3. **Reflection/Self-Critique Agents (反思/自我批评代理)**
   - 使用循环让代理审查自己的工作并根据反馈采取行动

4. **Multi-Agent 架构**
   - **Supervisor (监督者)**: 单个监督代理接收输入并委派工作给子代理
   - **Collaboration (协作)**: 不同代理在共享消息草稿板上协作
   - **Sequential (顺序)**: 代理之间的顺序交接
   - **Hub-and-Spoke (轮辐式)**: 中央协调器向专家代理分派任务

**状态管理和内存:**

1. **短期内存 (Thread-Scoped)**
   - 通过维护会话内的消息历史跟踪持续对话
   - 使用检查点器(如 InMemorySaver)持久化到数据库
   - 线程可以随时恢复

2. **长期内存 (Cross-Thread)**
   - 允许系统在不同对话或会话之间保留信息
   - 保存在自定义"命名空间"中
   - LangGraph 提供存储来保存和回忆长期记忆

3. **上下文窗口管理**
   - 通过删除前 N 或后 N 条消息来修剪消息
   - 永久删除消息
   - 总结早期消息
   - 管理检查点

**工具集成模式:**

1. **基础工具创建**
```python
from langchain_core.tools import tool

@tool
def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b
```

2. **使用 create_react_agent**
```python
from langgraph.prebuilt import create_react_agent

agent = create_react_agent(
    model="anthropic:claude-3-7-sonnet-latest",
    tools=[get_weather],
    prompt="You are a helpful assistant"
)
```

3. **ToolNode 组件**
   - LangChain Runnable,在 LangGraph 架构中编排工具调用
   - 接受当前图状态作为输入

**模型提供商集成:**

1. **OpenAI 集成**
```python
from langchain.chat_models import init_chat_model
import os

os.environ["OPENAI_API_KEY"] = "sk-..."
llm = init_chat_model("openai:gpt-4.1")
```

2. **Anthropic 集成**
```python
from langchain_anthropic import ChatAnthropic

model = ChatAnthropic(
    model="claude-3-7-sonnet-latest",
    temperature=0,
    max_tokens=2048
)
```

3. **多提供商选择器**
```python
def select_model(state: AgentState, runtime: Runtime) -> BaseChatModel:
    if runtime.context.provider == "anthropic":
        return anthropic_model
    elif runtime.context.provider == "openai":
        return openai_model
```

**结构化输出与 Pydantic:**

1. **with_structured_output() 方法**
   - 推荐方法,自动绑定模式到模型并解析输出
   - 模式可以是 TypedDict 类、JSON Schema 或 Pydantic 类

2. **PydanticOutputParser**
   - 利用 Pydantic 库进行 JSON 解析
   - 提供结构化方式表示语言模型输出
   - 模型生成的输出将被验证

3. **验证优势**
   - 如果缺少任何必需字段或字段类型错误,Pydantic 将引发错误

**错误处理和重试机制:**

1. **重试策略配置**
   - LangGraph 允许设置 retry_policy 以指导图重试引发特定类型异常的节点
   - 只重试失败的分支
   - 可配置最大尝试次数、指数退避参数

2. **RunnableRetry**
   - 所有 Runnables 上的 .with_retry() 方法
   - 仅对可能是暂时性的异常重试(网络错误、429 Too Many Requests)

3. **最佳实践**
   - 将重试范围保持尽可能小
   - ToolNode 自动捕获工具错误并报告给模型

**测试模式:**

1. **测试级别**
   - 单个节点的单元测试
   - 验证状态流的系统测试
   - 一些开发者推荐模拟 LLM 行为的纯软件单元测试

2. **Pytest 集成**
   - 测试框架与标准 pytest 执行模式集成
   - 支持通过配置的 anyio 后端进行异步操作

3. **验证模式**
   - 验证响应结构、状态码和预期数据类型的断言
   - 在具有已知期望行为的多个示例上测试代理
   - Human Ground Truth Evaluation (人工真实评估)
   - LLM-as-a-Judge 方法评估正确性

4. **LangGraph Studio 中的评估**
   - 现在允许直接从 UI 运行评估
   - 跨不同输入测试代理性能

**项目结构最佳实践:**

```
my-app/
├── my_agent                  # 所有项目代码
│   ├── utils                 # 图的实用工具
│   │   ├── __init__.py
│   │   ├── tools.py          # 图的工具
│   │   ├── nodes.py          # 图的节点函数
│   │   └── state.py          # 图的状态定义
│   ├── __init__.py
│   └── agent.py              # 构建图的代码
├── .env                      # 环境变量
├── requirements.txt          # 包依赖
└── langgraph.json            # LangGraph 配置文件
```

**核心配置文件:**
- **langgraph.json**: 指定依赖、图、环境变量和部署设置的 JSON 文件

**安全最佳实践:**

1. **API 密钥管理**
   - 安全存储 API 密钥和凭据
   - 避免在脚本中硬编码
   - 使用环境变量或密钥管理工具(如 AWS Secrets Manager)
   - 实施访问控制(OAuth2 scopes、API 密钥轮换)
   - 自动密钥检测和编辑(使用 CodeGate 等工具)

2. **提示注入防护**
   - 在系统提示中提供关于模型角色、功能和限制的具体说明
   - 强制执行严格的上下文遵守
   - 验证和净化所有用户输入和 LLM 输出
   - 使用白名单阻止恶意提示
   - 将输出格式限制为预定义模板
   - 实施输入过滤以删除特殊字符或代码片段

3. **权限限制**
   - 限制权限并专门针对应用程序的需求进行范围限定
   - 使用只读凭据
   - 不允许访问敏感资源
   - 使用沙盒技术(在容器内运行)
   - 为代理提供只读 API 密钥

4. **深度防御**
   - 没有安全技术是完美的
   - 结合多个分层安全方法
   - 微调和良好的链设计可以减少但不能消除错误几率

**常见陷阱和 Gotchas:**

1. **Token 限制和上下文窗口问题**
   - 使用文档检索器时,整个对话和检索到的文档都作为上下文传递给 LLM
   - 使用检查点提供对话历史时,可能导致上下文窗口超过最大 token 限制
   - 长对话的完整历史可能不适合 LLM 的上下文窗口
   - 即使 LLM 支持完整上下文长度,大多数 LLM 在长上下文中表现仍然较差

2. **InvalidUpdateError(并行执行中)**
   - 在并行执行场景中常见的陷阱
   - 当多个节点尝试更新相同的 State 键而没有正确定义的 reducer 函数时出现
   - Reducers 对于解决 State 更新冲突是强制性的

3. **递归限制问题**
   - recursion_limit 参数作为关键安全机制
   - 防止失控的图执行和资源耗尽
   - 工作流应该根据明确的退出条件优雅地终止
   - 达到限制通常表示存在潜在的设计缺陷

4. **Human-in-the-Loop 陷阱**
   - 绝对避免在节点内的 interrupt(value) 函数调用之前放置有副作用的代码
   - 副作用包括外部 API 调用、数据库写入、发送电子邮件等
   - 这可能由于重新执行而导致意外和有害的后果

5. **模型提供商速率限制**
   - 处理模型提供商速率限制和错误
   - 实施适当的重试机制和退避策略

6. **Token 计数和成本优化**
   - 实施 token 使用跟踪
   - 使用 UsageMetadataCallbackHandler 跟踪 token 使用
   - LangSmith 集成用于成本计算
   - 监控和调试使用 OpenTelemetry

**部署选项:**

1. **Cloud SaaS(完全托管)**
   - 作为 LangSmith 的一部分完全托管和托管
   - 自动更新和零维护
   - 一键部署应用

2. **Hybrid/BYOC(自带云)**
   - 在您自己的云中管理数据平面
   - LangGraph 处理控制平面
   - 在 AWS 上可用,提供 Terraform 模块

3. **Self-Hosted(自托管)**
   - 在您自己的云环境中完全运行所有组件
   - 支持使用 Docker 的独立容器部署
   - 适合部署到 Kubernetes 等环境

**生产配置:**
- 使用 python-dotenv 的环境管理
- 通过 Kubernetes secrets 进行生产环境变量管理
- 需要访问持久化存储后端(内存开发模式不适合生产)
- Docker Compose 用于本地复制生产环境

**监控与调试 - LangSmith:**

1. **什么是 LangSmith**
   - 统一的可观察性和评估平台
   - 用于调试、测试和监控 AI 应用性能
   - 与 LangChain 一起工作或独立使用

2. **关键功能**
   - **追踪和调试**: 逐步查看代理正在做什么
   - **监控能力**: 跟踪成本、延迟和响应质量
   - **完全可见性**: 追踪包含所有步骤的输入和输出的完整信息
   - **成本分析**: token 使用、响应时间和成本的详细分析

3. **为什么使用 LangSmith**
   - 允许查看代理内部并观察执行的所有步骤、工具调用、响应和决策点
   - 帮助调试意外的结果、确定代理循环的原因、找出链比预期慢的原因
   - 告诉您代理使用了多少 token

**示例项目和资源:**

1. **官方资源**
   - GitHub 主仓库: https://github.com/langchain-ai/langgraph
   - 示例代码仓库: https://github.com/langchain-ai/langgraph-example
   - LangChain Academy: 免费结构化课程学习基础知识

2. **社区资源**
   - jkmaina/LangGraphProjects: "The Complete LangGraph Blueprint: Build 50+ AI Agents for Business Success"官方配套仓库
   - von-development/awesome-LangGraph: LangChain + LangGraph 生态系统索引

**向量数据库集成:**

1. **Pinecone 集成**
   - LangGraph 可以查询 Pinecone 向量数据库以检索相关信息
   - 使用 langchain_pinecone 包中的 PineconeVectorStore
   - from_documents 和 from_texts 方法将记录添加到 Pinecone 索引

2. **Weaviate 集成**
   - LangChain 提供 langchain-weaviate 包与 Weaviate 向量存储集成
   - 可扩展的、生产就绪的向量存储

### Context Engineering 基础

```yaml
# 从基础框架继承
- file: ../../../README.md
  why: 核心上下文工程原则和工作流程

- file: ../../../.claude/commands/generate-prp.md
  why: 基础 PRP 生成模式

- file: ../../../.claude/commands/execute-prp.md
  why: 基础 PRP 执行模式

- file: ../../../PRPs/templates/prp_base.md
  why: 基础 PRP 模板结构

# 参考实现
- file: ../mcp-server/CLAUDE.md
  why: 领域特定实现指南模式的示例

- file: ../mcp-server/.claude/commands/prp-mcp-create.md
  why: 专门化 PRP 生成命令的示例
```

## Implementation Blueprint

### 阶段 1: 模板目录结构创建

**任务:**
```bash
# 创建完整的 use case 目录结构
mkdir -p use-cases/langgraph-agents/.claude/commands
mkdir -p use-cases/langgraph-agents/PRPs/templates
mkdir -p use-cases/langgraph-agents/PRPs/ai_docs
mkdir -p use-cases/langgraph-agents/examples
```

**验证:**
```bash
tree use-cases/langgraph-agents -L 2
# 预期: 显示所有必需的子目录
```

---

### 阶段 2: 生成领域特定 CLAUDE.md

**任务: 创建 `use-cases/langgraph-agents/CLAUDE.md`**

**内容必须包含:**

1. **项目概述**
   - LangGraph + LangChain + LangSmith 代理开发
   - 初学者友好的实现模式
   - 生产就绪的最佳实践

2. **包管理和工具**
   ```bash
   # 强制: 使用 uv 而不是 pip
   uv pip install langgraph langchain-anthropic langchain-openai
   uv pip install --dev pytest black mypy

   # 虚拟环境管理
   uv venv
   source .venv/bin/activate
   ```

3. **项目架构模式**
   ```
   my-agent/
   ├── my_agent/
   │   ├── utils/
   │   │   ├── tools.py      # 工具定义
   │   │   ├── nodes.py      # 节点函数
   │   │   └── state.py      # 状态定义
   │   └── agent.py          # 主代理逻辑
   ├── tests/                # Pytest 测试
   ├── .env                  # 环境变量
   ├── requirements.txt      # uv 生成的依赖
   └── langgraph.json        # LangGraph 配置
   ```

4. **开发工作流程**
   - 代理创建模式(ReAct、Router、Multi-Agent)
   - 工具集成最佳实践
   - 状态管理和记忆模式
   - 测试和验证方法

5. **安全和最佳实践**
   - API 密钥管理(使用 .env 和 python-dotenv)
   - 输入验证和净化
   - 提示注入防护
   - 成本控制和监控

6. **常见 Gotchas**
   - Token 限制和上下文窗口管理
   - 模型提供商速率限制处理
   - InvalidUpdateError 在并行执行中
   - 递归限制配置
   - Human-in-the-Loop 副作用避免

7. **验证要求**
   - Pytest 单元测试模式
   - 代理行为验证
   - 工具集成测试
   - LangSmith 追踪和调试

**验证:**
```bash
grep -c "langgraph\|langchain\|langsmith" use-cases/langgraph-agents/CLAUDE.md
# 预期: > 10 (确保包含 LangGraph 特定内容)

grep "uv pip install" use-cases/langgraph-agents/CLAUDE.md
# 预期: 找到 uv 命令而不是 pip
```

---

### 阶段 3: 创建专门化 PRP 命令

**任务 3.1: 创建 `generate-langgraph-prp.md`**

**内容必须包含:**

```markdown
---
name: "generate-langgraph-prp"
description: "为 LangGraph AI 代理功能生成综合 PRP"
Usage: /generate-langgraph-prp path/to/INITIAL.md
---

# Generate LangGraph Agent PRP

## 用户的功能用例: $ARGUMENTS

## Purpose

为 LangGraph AI 代理开发生成上下文丰富的 PRP,使用本代码库中经过验证的模式。

## Execution Process

1. **Research & Context Gathering**
   - 阅读 INITIAL.md 中的功能请求
   - 搜索代码库中的类似模式
   - 收集关于 LangGraph 工具、资源和代理架构的相关文档
   - 研究现有工具和代理模式

2. **Generate Comprehensive PRP**
   - 使用专门的 `PRPs/templates/prp_langgraph_base.md` 模板作为基础
   - 使用特定代理要求和功能定制模板
   - 包含来自代码库模式和 ai_docs 的所有必要上下文
   - 添加 LangGraph 代理开发的特定验证循环
   - 包含工具集成模式和安全考虑

3. **Enhance with AI docs**
   - 用户可能在 PRPs/ai_docs/ 目录中添加了文档
   - 如果 PRPs/ai_docs/ 目录中有文档,请审查它们并在构建 PRP 时考虑它们

## Research Areas

1. **LangGraph 代理模式**
   - 代理类型(ReAct、Router、Multi-Agent)
   - 状态管理和记忆模式
   - 工具注册和验证
   - 错误处理和日志记录

2. **模型提供商集成**
   - OpenAI、Anthropic 配置
   - 模型选择策略
   - Token 管理和成本优化
   - 结构化输出与 Pydantic

3. **测试和验证**
   - Pytest 单元测试模式
   - 代理行为验证
   - LangSmith 集成和追踪

## Output

在 PRPs/ 目录中创建包含以下内容的综合 PRP 文件:
- 所有必要的上下文和代码模式
- 逐步实现任务
- LangGraph 代理开发的验证循环

## Validation

命令确保:
- 所有引用的代码模式存在于代码库中
- 文档链接有效且可访问
- 实现任务具体且可操作
- 验证循环全面且可由 Claude Code 执行(重要)
```

**验证:**
```bash
test -f use-cases/langgraph-agents/.claude/commands/generate-langgraph-prp.md
echo $?  # 预期: 0
```

---

**任务 3.2: 创建 `execute-langgraph-prp.md`**

**内容必须包含:**

```markdown
---
name: "execute-langgraph-prp"
description: "执行 LangGraph AI 代理 PRP"
Usage: /execute-langgraph-prp path/to/prp.md
---

# Execute LangGraph Agent PRP

执行 PRPs/ 目录中的 LangGraph 代理 PRP。

## Purpose

遵循 PRP 中定义的实现蓝图,使用 LangGraph、LangChain 和 LangSmith 构建 AI 代理。

## Execution Process

1. **Read and Validate PRP**
   - 读取指定的 PRP 文件
   - 验证所有上下文引用和依赖项
   - 确认实现任务已明确定义

2. **Execute Implementation Blueprint**
   - 按照 PRP 中的任务顺序
   - 使用 LangGraph 模式创建代理代码
   - 实施工具集成和状态管理
   - 添加 Pydantic 模型用于结构化输出

3. **Run Validation Loops**
   - **Level 1 - 语法**: 使用 mypy 进行类型检查
   - **Level 2 - 单元测试**: 使用 pytest 运行测试
   - **Level 3 - 代理测试**: 验证代理行为
   - **Level 4 - 集成**: LangSmith 追踪和监控

4. **Documentation and Testing**
   - 创建 pytest 测试文件
   - 添加工具和代理的文档字符串
   - 包含 LangSmith 追踪示例

## Validation Commands

```bash
# Level 1: 语法和类型检查
mypy my_agent/

# Level 2: 单元测试
pytest tests/ -v

# Level 3: 代理行为测试
pytest tests/test_agent_behavior.py -v

# Level 4: LangSmith 集成
# 在运行代理时检查 LangSmith 追踪
```

## Output

- 完整的 LangGraph 代理实现
- 工具和节点函数
- 状态定义和配置
- Pytest 测试套件
- LangSmith 集成配置
```

**验证:**
```bash
test -f use-cases/langgraph-agents/.claude/commands/execute-langgraph-prp.md
echo $?  # 预期: 0
```

---

### 阶段 4: 开发领域特定基础 PRP 模板

**任务: 创建 `PRPs/templates/prp_langgraph_base.md`**

**内容必须包含:**

```markdown
---
name: "LangGraph Agent Base PRP"
description: "用于 LangGraph AI 代理开发的基础 PRP 模板"
---

## Purpose

构建一个使用 LangGraph、LangChain 和 LangSmith 的 AI 代理,具有 [SPECIFIC_CAPABILITY]。

## Why

- **解决问题**: [SPECIFIC_PROBLEM_TO_SOLVE]
- **启用功能**: [SPECIFIC_FUNCTIONALITY]
- **提高效率**: [HOW_IT_IMPROVES_WORKFLOW]

## What

### 代理架构

**代理类型**: [ReAct / Router / Multi-Agent / Workflow]

**核心组件:**
- State definition with typed fields
- Node functions for processing
- Tool definitions and integrations
- Model configuration (OpenAI/Anthropic)
- Memory and context management

**工具集成:**
- [Tool 1]: [Purpose and usage]
- [Tool 2]: [Purpose and usage]
- [Tool 3]: [Purpose and usage]

**结构化输出:**
```python
from pydantic import BaseModel, Field

class AgentOutput(BaseModel):
    """Agent response structure."""
    result: str = Field(description="The result")
    confidence: float = Field(description="Confidence score")
    metadata: dict = Field(default_factory=dict)
```

### 成功标准

- [ ] 代理正确响应用户查询
- [ ] 工具集成工作无错误
- [ ] 状态在交互中正确管理
- [ ] Pydantic 验证通过
- [ ] 所有 pytest 测试通过
- [ ] LangSmith 追踪显示预期行为

## All Needed Context

### LangGraph 文档

```yaml
# 核心概念
- 状态管理和内存模式
- 代理架构(ReAct、Multi-Agent)
- 工具集成最佳实践
- 错误处理和重试机制

# 模型集成
- OpenAI 和 Anthropic 配置
- 结构化输出与 Pydantic
- Token 管理和成本优化

# 测试和验证
- Pytest 测试模式
- 代理行为验证
- LangSmith 追踪和调试

# 安全考虑
- API 密钥管理
- 输入验证
- 提示注入防护
- 速率限制处理
```

### 代码库模式

```yaml
- file: examples/basic_chat_agent.py
  why: 基础代理创建模式

- file: examples/tool_enabled_agent.py
  why: 工具集成示例

- file: examples/structured_output_agent.py
  why: Pydantic 结构化输出

- file: examples/testing_examples.py
  why: 测试模式和验证
```

## Implementation Blueprint

### Task 1: 项目设置

```bash
# 创建项目结构
mkdir -p my_agent/utils tests

# 安装依赖 (使用 uv)
uv pip install langgraph langchain-anthropic langchain-openai pydantic
uv pip install --dev pytest black mypy

# 创建环境变量文件
cat > .env << EOF
OPENAI_API_KEY=your-key-here
ANTHROPIC_API_KEY=your-key-here
LANGSMITH_API_KEY=your-key-here
LANGSMITH_TRACING=true
EOF
```

### Task 2: 状态定义

```python
# my_agent/utils/state.py
from typing import TypedDict, Annotated, Sequence
from langchain_core.messages import BaseMessage
from operator import add

class AgentState(TypedDict):
    """Agent state definition."""
    messages: Annotated[Sequence[BaseMessage], add]
    # Add your custom state fields here
```

### Task 3: 工具定义

```python
# my_agent/utils/tools.py
from langchain_core.tools import tool

@tool
def example_tool(query: str) -> str:
    """Example tool description.

    Args:
        query: The query to process

    Returns:
        str: The result
    """
    # Implement tool logic
    return f"Processed: {query}"
```

### Task 4: 节点函数

```python
# my_agent/utils/nodes.py
from langchain_core.messages import HumanMessage
from .state import AgentState

def agent_node(state: AgentState) -> AgentState:
    """Process agent logic.

    Args:
        state: Current agent state

    Returns:
        Updated state
    """
    # Implement node logic
    return state
```

### Task 5: 主代理逻辑

```python
# my_agent/agent.py
from langgraph.graph import StateGraph, END
from langgraph.prebuilt import create_react_agent
from langchain_anthropic import ChatAnthropic
from .utils.tools import example_tool
from .utils.state import AgentState

def create_agent():
    """Create and configure the agent.

    Returns:
        Compiled agent graph
    """
    model = ChatAnthropic(model="claude-3-7-sonnet-latest")

    agent = create_react_agent(
        model=model,
        tools=[example_tool],
        state_modifier="You are a helpful assistant."
    )

    return agent
```

### Task 6: 测试套件

```python
# tests/test_agent.py
import pytest
from my_agent.agent import create_agent

def test_agent_creation():
    """Test agent can be created."""
    agent = create_agent()
    assert agent is not None

def test_agent_response():
    """Test agent responds correctly."""
    agent = create_agent()
    result = agent.invoke({
        "messages": [("user", "Hello")]
    })
    assert "messages" in result
    assert len(result["messages"]) > 0

@pytest.mark.asyncio
async def test_agent_with_tool():
    """Test agent uses tools correctly."""
    agent = create_agent()
    result = agent.invoke({
        "messages": [("user", "Use the example tool")]
    })
    # Add assertions for tool usage
    assert result is not None
```

## Validation Loop

### Level 1: 语法和类型检查

```bash
# 类型检查
mypy my_agent/ --strict

# 预期: 无类型错误
# 如果失败: 修复类型注释和导入
```

### Level 2: 单元测试

```bash
# 运行所有测试
pytest tests/ -v --cov=my_agent

# 预期: 所有测试通过,覆盖率 > 80%
# 如果失败: 修复代码逻辑和测试
```

### Level 3: 代理行为测试

```bash
# 测试代理行为
pytest tests/test_agent_behavior.py -v -s

# 预期: 代理正确响应并使用工具
# 如果失败: 调试代理逻辑和工具集成
```

### Level 4: LangSmith 追踪

```bash
# 运行代理并检查 LangSmith
python -m my_agent.agent

# 预期: 在 LangSmith UI 中看到追踪
# 如果失败: 检查 LANGSMITH_API_KEY 和 LANGSMITH_TRACING
```

## Security Checklist

- [ ] API 密钥存储在 .env 文件中(不提交到 git)
- [ ] 输入验证实施
- [ ] 输出净化实施
- [ ] 速率限制处理添加
- [ ] 错误消息不暴露敏感信息
- [ ] Pydantic 模型验证所有输入

## Common Gotchas

1. **Token 限制超出**
   - 实施消息修剪策略
   - 监控上下文窗口使用

2. **InvalidUpdateError**
   - 为并行更新的状态字段定义 reducers
   - 使用 Annotated[type, operator] 用于列表字段

3. **工具执行错误**
   - 添加适当的错误处理
   - 实施重试机制

4. **速率限制**
   - 使用 .with_retry() 进行暂时性错误
   - 实施指数退避

---

## Final Checklist

- [ ] 所有代码文件创建且语法正确
- [ ] Pydantic 模型定义并验证
- [ ] 工具正确集成
- [ ] 状态管理正确实现
- [ ] 所有 pytest 测试通过
- [ ] LangSmith 追踪工作
- [ ] 文档完整
- [ ] 安全最佳实践遵循
```

**验证:**
```bash
wc -l use-cases/langgraph-agents/PRPs/templates/prp_langgraph_base.md
# 预期: > 200 行(确保综合性)

grep -c "LangGraph\|LangChain\|LangSmith" use-cases/langgraph-agents/PRPs/templates/prp_langgraph_base.md
# 预期: > 15
```

---

### 阶段 5: 创建示例和 INITIAL.md

**任务 5.1: 创建 `PRPs/INITIAL.md` 示例**

**内容:**

```markdown
# LangGraph Agent Feature Request

## AGENT PURPOSE:
构建一个能够执行网络搜索并进行数学计算的智能助手代理

## CORE FEATURES:
- 网络搜索集成(使用 Tavily 或 DuckDuckGo)
- 数学计算工具
- 对话记忆和上下文跟踪
- 结构化响应输出使用 Pydantic

## AGENT ARCHITECTURE:
- Agent type: ReAct (Reasoning and Acting)
- Model provider: Anthropic Claude 3.7 Sonnet
- Memory: 短期对话记忆使用 InMemorySaver

## TOOLS TO INTEGRATE:
1. **Web Search Tool**
   - Search the web for current information
   - Return top 5 relevant results
   - Include source URLs

2. **Calculator Tool**
   - Perform basic arithmetic operations
   - Handle complex mathematical expressions
   - Return precise numeric results

## STRUCTURED OUTPUT:
```python
class AgentResponse(BaseModel):
    """Structured agent response."""
    answer: str = Field(description="The agent's answer")
    sources: list[str] = Field(default_factory=list, description="Source URLs")
    calculations: list[str] = Field(default_factory=list, description="Math performed")
    confidence: float = Field(ge=0, le=1, description="Confidence score")
```

## TESTING REQUIREMENTS:
- Test web search functionality
- Test calculator accuracy
- Test conversation memory
- Test structured output validation
- Test error handling for failed tool calls

## SECURITY CONSIDERATIONS:
- Validate web search queries for injection
- Sanitize calculator inputs
- Rate limit external API calls
- Secure API key management

## COMMON USAGE SCENARIOS:
1. "What's the weather in New York and what's 25 + 17?"
2. "Search for Python tutorials and calculate 15% of 200"
3. "Find recent AI news and compute the square root of 144"

## VALIDATION REQUIREMENTS:
- Agent responds within 5 seconds
- Web search returns valid results
- Calculator provides accurate computations
- Pydantic validation passes
- All pytest tests pass
```

**验证:**
```bash
test -f use-cases/langgraph-agents/PRPs/INITIAL.md
grep -c "LangGraph\|tool\|agent" use-cases/langgraph-agents/PRPs/INITIAL.md
# 预期: > 5
```

---

**任务 5.2: 创建工作代码示例**

创建以下示例文件:

1. **`examples/basic_chat_agent.py`** - 基础聊天代理与记忆
2. **`examples/tool_enabled_agent.py`** - 工具集成代理
3. **`examples/workflow_agent.py`** - 多步骤工作流
4. **`examples/structured_output_agent.py`** - Pydantic 输出
5. **`examples/testing_examples.py`** - 测试模式

**每个示例必须包含:**
- 完整的工作代码
- 文档字符串解释
- 使用说明
- 依赖要求

**验证:**
```bash
# 检查所有示例文件存在
ls -1 use-cases/langgraph-agents/examples/*.py | wc -l
# 预期: 5

# 验证代码语法
for file in use-cases/langgraph-agents/examples/*.py; do
    python -m py_compile "$file" || echo "Syntax error in $file"
done
# 预期: 无语法错误
```

---

### 阶段 6: 创建模板复制脚本

**任务: 创建 `copy_template.py`**

**内容:**

```python
#!/usr/bin/env python3
"""
LangGraph Template Copy Script

Copies the entire LangGraph agent template to a target directory.

Usage:
    python copy_template.py /path/to/target

Example:
    python copy_template.py ~/projects/my-langgraph-agent
"""

import os
import shutil
import sys
from pathlib import Path


def copy_template(target_dir: str) -> None:
    """Copy the LangGraph template to target directory.

    Args:
        target_dir: Destination directory path
    """
    # Get current template directory
    template_dir = Path(__file__).parent
    target_path = Path(target_dir).resolve()

    # Validate target doesn't exist or is empty
    if target_path.exists() and any(target_path.iterdir()):
        print(f"Error: Target directory '{target_path}' exists and is not empty")
        sys.exit(1)

    # Create target directory
    target_path.mkdir(parents=True, exist_ok=True)

    # Files and directories to copy
    items_to_copy = [
        "CLAUDE.md",
        ".claude/",
        "PRPs/",
        "examples/",
        "README.md"
    ]

    print(f"Copying LangGraph template to: {target_path}")

    for item in items_to_copy:
        source = template_dir / item
        destination = target_path / item

        if not source.exists():
            print(f"Warning: {item} not found, skipping")
            continue

        if source.is_dir():
            shutil.copytree(source, destination, dirs_exist_ok=True)
            print(f"✓ Copied directory: {item}")
        else:
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, destination)
            print(f"✓ Copied file: {item}")

    print(f"\n✅ Template copied successfully!")
    print(f"\nNext steps:")
    print(f"1. cd {target_path}")
    print(f"2. uv venv && source .venv/bin/activate")
    print(f"3. uv pip install langgraph langchain-anthropic")
    print(f"4. Create PRPs/INITIAL.md with your feature request")
    print(f"5. Run: /generate-langgraph-prp PRPs/INITIAL.md")
    print(f"6. Run: /execute-langgraph-prp PRPs/your-prp.md")


def main():
    """Main entry point."""
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(1)

    target_dir = sys.argv[1]

    try:
        copy_template(target_dir)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
```

**验证:**
```bash
# 测试脚本存在且可执行
test -f use-cases/langgraph-agents/copy_template.py
python use-cases/langgraph-agents/copy_template.py --help 2>&1 | grep -q "Usage"
echo $?  # 预期: 0
```

---

### 阶段 7: 生成综合 README

**任务: 创建 `README.md`**

**内容必须包含:**

1. **标题和简要描述**
   - 模板用途的清晰描述
   - 目标受众(初学者友好)

2. **🚀 Quick Start - 首先复制模板(顶部突出显示)**
   ```bash
   python copy_template.py /path/to/your-project
   cd /path/to/your-project
   ```

3. **📋 PRP Framework Workflow(3步流程解释)**
   - Step 1: 创建 INITIAL.md 定义你想要构建的内容
   - Step 2: 生成 PRP `/generate-langgraph-prp INITIAL.md`
   - Step 3: 执行 PRP `/execute-langgraph-prp PRPs/your-prp.md`

4. **📁 Template Structure(带解释的目录树)**
   ```
   langgraph-agents/
   ├── CLAUDE.md                    # LangGraph 实现指南
   ├── .claude/commands/           # 专门化命令
   ├── PRPs/templates/             # PRP 模板
   ├── examples/                   # 工作代码示例
   ├── copy_template.py            # 模板部署脚本
   └── README.md                   # 本文件
   ```

5. **🎯 What You Can Build(技术特定示例)**
   - ReAct agents with tool integration
   - Multi-agent systems
   - Conversational agents with memory
   - Agents with structured Pydantic outputs

6. **📚 Key Features(框架功能)**
   - LangGraph state management
   - LangChain tool integration
   - LangSmith tracing and monitoring
   - Pydantic structured outputs

7. **🔍 Examples Included(提供的工作示例)**
   - basic_chat_agent.py
   - tool_enabled_agent.py
   - workflow_agent.py
   - structured_output_agent.py
   - testing_examples.py

8. **📖 Documentation References(研究来源)**
   - Official LangGraph docs
   - LangChain integration guides
   - LangSmith monitoring docs
   - Community resources

9. **🚫 Common Gotchas(技术特定陷阱)**
   - Token limit management
   - InvalidUpdateError in parallel execution
   - Recursion limit configuration
   - Rate limiting handling

**验证:**
```bash
# 验证 README 存在且全面
test -f use-cases/langgraph-agents/README.md
wc -l use-cases/langgraph-agents/README.md
# 预期: > 150 行

# 验证包含关键部分
grep -c "Quick Start\|PRP Framework\|copy_template\|Examples" use-cases/langgraph-agents/README.md
# 预期: >= 4
```

---

## Validation Loop

### Level 1: 模板结构验证

```bash
# 验证完整的模板包结构
find use-cases/langgraph-agents -type f | sort

# 验证所有必需文件
ls -la use-cases/langgraph-agents/CLAUDE.md
ls -la use-cases/langgraph-agents/.claude/commands/
ls -la use-cases/langgraph-agents/PRPs/templates/
ls -la use-cases/langgraph-agents/examples/
ls -la use-cases/langgraph-agents/copy_template.py
ls -la use-cases/langgraph-agents/README.md

# 验证复制脚本存在且可用
test -f use-cases/langgraph-agents/copy_template.py
python use-cases/langgraph-agents/copy_template.py 2>&1 | grep -q "Usage"

# 预期: 所有必需文件存在,包括 copy_template.py
# 如果缺少: 生成遵循既定模式的缺失文件
```

### Level 2: 内容质量验证

```bash
# 验证领域特定内容准确性
grep -r "TODO\|PLACEHOLDER\|{domain}" use-cases/langgraph-agents/
grep -r "WEBSEARCH_NEEDED" use-cases/langgraph-agents/

# 检查技术特定模式
grep -r "langgraph\|langchain\|langsmith" use-cases/langgraph-agents/ | wc -l
# 预期: > 50 (确保 LangGraph 特定内容)

grep -r "uv pip install" use-cases/langgraph-agents/
# 预期: 找到 uv 命令

# 检查验证命令
grep -r "pytest\|mypy" use-cases/langgraph-agents/.claude/commands/

# 预期: 无占位符内容,存在技术模式
# 如果有问题: 研究并添加适当的领域特定内容
```

### Level 3: 功能验证

```bash
# 测试模板功能
cd use-cases/langgraph-agents

# 测试 PRP 生成命令(如果 INITIAL.md 存在)
if [ -f PRPs/INITIAL.md ]; then
    echo "Testing PRP generation..."
    # 在实际使用中会运行: /generate-langgraph-prp PRPs/INITIAL.md
fi

# 测试模板完整性
grep -r "Context is King\|PRP\|validation" . | wc -l
# 预期: > 20 (继承原则)

grep -r "LangGraph\|state\|agent" . | wc -l
# 预期: > 30 (有专门化)

# 验证示例语法
for file in examples/*.py; do
    [ -f "$file" ] && python -m py_compile "$file" || echo "Syntax error in $file"
done

# 预期: PRP 生成工作,内容专门化,示例语法正确
# 如果失败: 调试命令模式和模板结构
```

### Level 4: 集成测试

```bash
# 验证与基础上下文工程框架的集成
diff -r ../../.claude/commands/ .claude/commands/ | head -20
diff ../../CLAUDE.md CLAUDE.md | head -20

# 测试模板产生工作结果
cd examples/
# 运行任何示例验证命令

# 检查文档一致性
grep -c "PRP\|validation\|context" README.md
# 预期: > 10

# 预期: 正确的专门化,不破坏基础模式
# 如果有问题: 调整专门化以保持兼容性
```

---

## Final Validation Checklist

### 模板包完整性

- [ ] 完整的目录结构: `tree use-cases/langgraph-agents`
- [ ] 所有必需文件存在: CLAUDE.md, commands, base PRP, examples
- [ ] 复制脚本存在: `copy_template.py` 具有适当的功能
- [ ] README 全面: 包含复制脚本说明和 PRP 工作流程
- [ ] 领域特定内容: LangGraph 模式准确表示
- [ ] 工作示例: 所有示例编译/运行成功
- [ ] 文档完整: README 和使用说明清晰

### 质量和可用性

- [ ] 无占位符内容: `grep -r "TODO\|PLACEHOLDER\|WEBSEARCH_NEEDED"`
- [ ] 技术专门化: LangGraph 模式适当记录
- [ ] 验证循环工作: 所有命令可执行且功能正常
- [ ] 集成维护: 与基础上下文工程框架一起工作
- [ ] 准备使用: 开发者可以立即开始使用模板

### 框架集成

- [ ] 继承基础原则: 上下文工程工作流程得以保留
- [ ] 适当的专门化: 包含技术特定模式
- [ ] 命令兼容性: Slash 命令按预期工作
- [ ] 文档一致性: 遵循既定的文档模式
- [ ] 可维护结构: 随着技术演进易于更新

### LangGraph 特定验证

- [ ] 代理架构模式记录: ReAct、Multi-Agent、Router
- [ ] 工具集成示例: 工作代码示例与 @tool 装饰器
- [ ] 状态管理模式: TypedDict、reducers、annotated 字段
- [ ] Pydantic 集成: 结构化输出示例和验证
- [ ] 测试模式: Pytest 示例用于代理行为测试
- [ ] 安全最佳实践: API 密钥管理、输入验证、提示注入防护
- [ ] LangSmith 集成: 追踪和监控配置
- [ ] 常见 Gotchas 记录: Token 限制、InvalidUpdateError、递归限制
- [ ] 部署模式: 生产配置和环境管理
- [ ] 模型提供商集成: OpenAI 和 Anthropic 示例

---

## Anti-Patterns to Avoid

### 模板生成

- ❌ 不要创建通用模板 - 始终深入研究和专门化
- ❌ 不要跳过全面的技术研究 - 彻底理解 LangGraph
- ❌ 不要使用占位符内容 - 始终包含真实的、研究过的信息
- ❌ 不要忽略验证循环 - 包含 LangGraph 的综合测试

### 内容质量

- ❌ 不要假设知识 - 为 LangGraph 明确记录一切
- ❌ 不要跳过边缘情况 - 包含常见 gotchas(Token 限制、InvalidUpdateError)
- ❌ 不要忽略安全 - 始终包含 API 密钥管理和提示注入防护
- ❌ 不要忘记维护 - 确保模板可以随 LangGraph 变化而演进

### 框架集成

- ❌ 不要破坏基础模式 - 保持与上下文工程原则的兼容性
- ❌ 不要重复努力 - 重用和扩展基础框架组件
- ❌ 不要忽略一致性 - 遵循既定的命名和结构约定
- ❌ 不要跳过验证 - 确保模板在完成前实际工作

---

## Quality Score: 9/10

**Confidence Level**: 非常高

**Reasoning**:
- 进行了广泛的 Web 研究,涵盖官方文档、社区资源和最佳实践
- 全面理解 LangGraph、LangChain 和 LangSmith 生态系统
- 包含真实的架构模式、工具集成和状态管理策略
- 记录了常见陷阱和安全最佳实践
- 包含可执行的验证循环和测试模式
- 基于经过验证的上下文工程原则

**Areas for Improvement**:
- 可以从更多真实世界的生产部署案例中受益
- 随着 LangGraph 的发展,需要持续更新以获取新功能

该 PRP 为创建全面的、生产就绪的 LangGraph 代理模板提供了坚实的基础,使开发者能够快速开始构建智能 AI 代理,同时遵循最佳实践并避免常见陷阱。
