# LangGraph AI Agent Template

一个全面的、生产就绪的模板,用于使用 LangGraph、LangChain 和 LangSmith 构建智能 AI 代理。

## 🎯 模板概述

此模板提供完整的框架和最佳实践,帮助你快速构建:
- **ReAct Agents**: 推理和行动代理,支持工具使用
- **Multi-Agent Systems**: 协作式多代理系统
- **Conversational Agents**: 带记忆的对话代理
- **Workflow Agents**: 多步骤工作流编排

**目标受众**: 初学者到高级开发者
**技术栈**: LangGraph + LangChain + LangSmith
**语言**: Python 3.11+

---

## 🚀 Quick Start - 首先复制模板!

### 步骤 1: 复制模板到你的项目

```bash
# 从 template-generator 目录运行
cd /path/to/context-engineering-intro/use-cases/template-generator

# 复制 LangGraph 模板到你的项目目录
python use-cases/langgraph-agents/copy_template.py /path/to/your-project

# 示例
python use-cases/langgraph-agents/copy_template.py ~/projects/my-agent
```

### 步骤 2: 设置环境

```bash
# 进入项目目录
cd /path/to/your-project

# 创建虚拟环境 (使用 uv)
uv venv
source .venv/bin/activate  # Linux/Mac
# .venv\Scripts\activate  # Windows

# 安装依赖
uv pip install langgraph langchain-anthropic langchain-openai
uv pip install langchain-core pydantic python-dotenv
uv pip install --dev pytest pytest-asyncio black mypy
```

### 步骤 3: 配置 API 密钥

```bash
# 复制环境变量示例
cp .env.example .env

# 编辑 .env 文件,添加你的 API 密钥
# ANTHROPIC_API_KEY=your-key-here
# OPENAI_API_KEY=your-key-here
# LANGSMITH_API_KEY=your-key-here (可选)
```

---

## 📋 PRP Framework Workflow (3 步流程)

此模板使用 **PRP (Plan-Research-Process)** 框架来构建 AI 代理:

### Step 1: 创建功能请求 (INITIAL.md)

描述你想要构建的代理功能:

```bash
# 编辑 PRPs/INITIAL.md
# 定义:
#   - 代理用途
#   - 核心功能
#   - 工具集成
#   - 测试要求
#   - 安全考虑
```

**示例 INITIAL.md**:
```markdown
# 代理用途
构建一个能够搜索网络并进行数学计算的智能助手

# 核心功能
- 网络搜索工具
- 计算器工具
- 对话记忆
- 结构化输出
```

### Step 2: 生成 PRP

使用专门化的命令生成详细的实现计划:

```bash
# 生成 PRP (在 Claude Code 中运行)
/generate-langgraph-prp PRPs/INITIAL.md
```

这将创建一个包含以下内容的详细 PRP:
- ✅ 完整的上下文和代码模式
- ✅ 逐步实现任务
- ✅ 验证循环和测试策略
- ✅ 安全最佳实践
- ✅ 常见陷阱和解决方案

### Step 3: 执行 PRP

执行 PRP 生成完整的代理实现:

```bash
# 执行 PRP (在 Claude Code 中运行)
/execute-langgraph-prp PRPs/prp_your_feature.md
```

这将自动:
- 📁 创建项目结构
- 🔧 生成代理代码
- 🛠️ 实现工具集成
- 🧪 创建测试套件
- 📝 生成文档

---

## 📁 模板结构

```
langgraph-agents/
├── CLAUDE.md                    # LangGraph 开发指南和最佳实践
├── .claude/commands/           # 专门化 PRP 命令
│   ├── generate-langgraph-prp.md  # PRP 生成命令
│   └── execute-langgraph-prp.md   # PRP 执行命令
├── PRPs/                       # PRP 文件
│   ├── templates/
│   │   └── prp_langgraph_base.md  # LangGraph PRP 基础模板
│   ├── ai_docs/                   # 可选文档资源
│   └── INITIAL.md                 # 功能请求示例
├── examples/                   # 工作代码示例
│   ├── basic_chat_agent.py        # 基础聊天代理
│   ├── tool_enabled_agent.py      # 工具集成代理
│   ├── workflow_agent.py          # 工作流代理
│   ├── structured_output_agent.py # 结构化输出
│   └── testing_examples.py        # 测试模式
├── copy_template.py            # 模板复制脚本
├── .env.example                # 环境变量示例
├── .gitignore                  # Git 忽略文件
└── README.md                   # 本文件
```

### 关键文件说明

| 文件 | 用途 |
|------|------|
| **CLAUDE.md** | LangGraph 实现指南,包含架构模式、工具集成、测试策略等 |
| **generate-langgraph-prp.md** | 生成 LangGraph 特定的 PRP,包含研究和规划 |
| **execute-langgraph-prp.md** | 执行 PRP 生成完整代理实现 |
| **prp_langgraph_base.md** | PRP 基础模板,包含所有必要部分 |
| **copy_template.py** | 将模板复制到新项目的脚本 |
| **examples/** | 5 个完整的工作示例,演示不同模式 |

---

## 🎯 你可以构建什么

### 1. ReAct Agents (推理和行动)

```python
from langgraph.prebuilt import create_react_agent

agent = create_react_agent(
    model="anthropic:claude-3-7-sonnet-latest",
    tools=[search_tool, calculator_tool],
    prompt="You are a helpful assistant"
)
```

**用例**:
- 研究助手 (搜索 + 分析)
- 数据分析代理 (查询 + 可视化)
- 客户支持机器人 (知识库 + 工具)

### 2. Multi-Agent Systems

- **Supervisor**: 单个监督者委派任务给专家代理
- **Collaboration**: 多个代理在共享工作区协作
- **Sequential**: 代理按顺序传递工作

**用例**:
- 内容创作流水线 (研究员 + 作家 + 编辑)
- 软件开发助手 (规划者 + 编码者 + 测试者)
- 数据处理流水线 (提取器 + 转换器 + 加载器)

### 3. Conversational Agents with Memory

```python
from langgraph.checkpoint.memory import MemorySaver

checkpointer = MemorySaver()
agent = create_react_agent(model, tools, checkpointer=checkpointer)
```

**用例**:
- 个人助理 (记住用户偏好)
- 教育辅导 (跟踪学习进度)
- 健康顾问 (维护健康历史)

### 4. Structured Output Agents

```python
from pydantic import BaseModel

class AgentResponse(BaseModel):
    answer: str
    sources: list[str]
    confidence: float

model_with_structure = model.with_structured_output(AgentResponse)
```

**用例**:
- API 集成 (需要特定格式)
- 数据提取 (结构化信息检索)
- 报告生成 (一致的输出格式)

---

## 📚 核心特性

### LangGraph 功能

- ✅ **状态管理**: TypedDict 定义,Annotated types,reducers
- ✅ **图编排**: 节点、边、条件边、子图
- ✅ **检查点器**: MemorySaver,PostgresSaver,持久化状态
- ✅ **并行执行**: 并发节点执行,InvalidUpdateError 处理
- ✅ **Human-in-the-Loop**: 中断和恢复支持

### LangChain 集成

- ✅ **多模型支持**: Anthropic Claude,OpenAI GPT,其他提供商
- ✅ **工具系统**: @tool 装饰器,ToolNode,工具链
- ✅ **结构化输出**: Pydantic 模型,with_structured_output()
- ✅ **向量存储**: Pinecone,Weaviate,检索增强生成 (RAG)
- ✅ **重试机制**: RunnableRetry,错误处理

### LangSmith 监控

- ✅ **追踪**: 完整的执行追踪,步骤级可见性
- ✅ **调试**: 输入/输出检查,错误诊断
- ✅ **性能**: Token 使用,延迟分析,成本计算
- ✅ **评估**: A/B 测试,质量评估

---

## 🔍 包含的示例

### 1. basic_chat_agent.py

基础对话代理,演示:
- 代理创建和配置
- 对话记忆 (MemorySaver)
- 系统提示配置
- 错误处理

**运行**:
```bash
python examples/basic_chat_agent.py
```

### 2. tool_enabled_agent.py

工具集成代理,演示:
- @tool 装饰器用法
- 网络搜索工具 (模拟)
- 计算器工具 (带 Pydantic 验证)
- 工具错误处理

**运行**:
```bash
python examples/tool_enabled_agent.py
```

### 3. workflow_agent.py

多步骤工作流,演示:
- 自定义状态定义
- 多个节点函数
- 条件边和流程控制
- 复杂工作流编排

**运行**:
```bash
python examples/workflow_agent.py
```

### 4. structured_output_agent.py

结构化输出,演示:
- Pydantic 模型定义
- with_structured_output() 方法
- 字段验证
- 类型安全输出

**运行**:
```bash
python examples/structured_output_agent.py
```

### 5. testing_examples.py

测试模式,演示:
- 单元测试 (工具测试)
- 集成测试 (代理测试)
- 行为测试 (记忆测试)
- Mock 和 Fixtures
- 参数化测试

**运行**:
```bash
pytest examples/testing_examples.py -v
```

---

## 📖 文档和学习资源

### 内部文档

- **CLAUDE.md**: 完整的 LangGraph 开发指南
  - 包管理 (uv)
  - 项目架构模式
  - 工具集成最佳实践
  - 状态管理策略
  - 安全和最佳实践
  - 常见 Gotchas

- **PRPs/templates/prp_langgraph_base.md**: PRP 模板示例
  - 完整的 PRP 结构
  - 实现蓝图
  - 验证循环
  - 测试策略

### 外部资源

- **LangGraph 官方文档**: https://langchain-ai.github.io/langgraph/
- **LangChain 文档**: https://python.langchain.com/
- **LangSmith**: https://smith.langchain.com
- **GitHub 仓库**: https://github.com/langchain-ai/langgraph
- **LangChain Academy**: 免费结构化课程

### 社区资源

- **awesome-LangGraph**: 社区资源索引
- **LangGraphProjects**: 50+ AI 代理蓝图
- **Discord**: LangChain 官方社区

---

## 🚫 常见陷阱 (Gotchas)

### 1. Token 限制和上下文窗口

**问题**: 长对话导致超出上下文窗口

**解决方案**:
```python
# 实现消息修剪
def trim_messages(state):
    if len(state["messages"]) > 20:
        state["messages"] = state["messages"][-20:]
    return state
```

### 2. InvalidUpdateError (并行执行)

**问题**: 多个节点并行更新同一状态键

**解决方案**:
```python
from typing import Annotated
from operator import add

class AgentState(TypedDict):
    # 使用 reducer 解决冲突
    results: Annotated[list[str], add]
```

### 3. 递归限制

**问题**: 代理陷入无限循环

**解决方案**:
```python
# 设置合理的递归限制
config = {"recursion_limit": 25}

# 实现退出条件
def should_continue(state):
    if len(state["messages"]) > 10:
        return "end"
    return "continue"
```

### 4. 工具执行错误

**问题**: 工具调用失败导致代理崩溃

**解决方案**:
```python
@tool
def robust_tool(query: str) -> str:
    try:
        return perform_operation(query)
    except Exception as e:
        return f"Error: {e}"
```

### 5. 速率限制

**问题**: 超过 API 速率限制

**解决方案**:
```python
from langchain_core.runnables import RunnableRetry

model_with_retry = model.with_retry(
    retry_if_exception_type=(RateLimitError,),
    wait_exponential_jitter=True,
    stop_after_attempt=3
)
```

---

## 🔒 安全最佳实践

### 1. API 密钥管理
- ✅ 使用 .env 文件存储密钥
- ✅ 将 .env 添加到 .gitignore
- ✅ 生产环境使用密钥管理服务
- ✅ 定期轮换密钥

### 2. 输入验证
- ✅ 使用 Pydantic 验证所有输入
- ✅ 限制输入长度
- ✅ 过滤特殊字符
- ✅ 拒绝恶意模式

### 3. 提示注入防护
- ✅ 系统提示明确角色限制
- ✅ 验证和净化用户输入
- ✅ 使用结构化输出限制格式
- ✅ 不允许覆盖系统指令

### 4. 权限限制
- ✅ 工具只有必要的权限
- ✅ 使用只读 API 密钥 (如可能)
- ✅ 不允许访问敏感资源
- ✅ 实施深度防御

---

## 🧪 测试策略

### 单元测试

```bash
# 测试工具
pytest tests/test_tools.py -v

# 测试状态管理
pytest tests/test_state.py -v
```

### 集成测试

```bash
# 测试代理行为
pytest tests/test_agent.py -v

# 测试工具集成
pytest tests/test_agent_integration.py -v
```

### 行为测试

```bash
# 测试对话记忆
pytest tests/test_agent_behavior.py -v

# 测试多轮对话
pytest tests/test_conversation.py -v
```

### 覆盖率报告

```bash
# 运行所有测试并生成覆盖率报告
pytest tests/ -v --cov=my_agent --cov-report=html

# 查看报告
open htmlcov/index.html
```

---

## 🛠️ 开发工作流程

### 1. 需求分析

- 阅读功能需求
- 确定代理类型
- 列出所需工具
- 定义成功标准

### 2. PRP 生成

```bash
# 创建 PRPs/INITIAL.md
# 运行 PRP 生成命令
/generate-langgraph-prp PRPs/INITIAL.md
```

### 3. 实现

```bash
# 运行 PRP 执行命令
/execute-langgraph-prp PRPs/prp_feature.md

# 这将创建:
# - 项目结构
# - 代理代码
# - 工具实现
# - 测试套件
```

### 4. 测试

```bash
# 运行单元测试
pytest tests/ -v

# 类型检查
mypy my_agent/

# 代码格式化
black my_agent/ tests/
```

### 5. 迭代优化

- 查看 LangSmith 追踪
- 优化提示和工具
- 改进错误处理
- 调整性能

### 6. 部署

- 配置生产环境变量
- 设置 LangGraph Cloud (可选)
- 配置监控和日志
- 实施 CI/CD

---

## 📈 性能优化

### Token 使用优化

```python
# 使用较小的模型用于简单任务
model_simple = ChatAnthropic(model="claude-3-haiku")

# 限制输出长度
model = ChatAnthropic(max_tokens=512)

# 实现消息修剪
def trim_context(messages):
    return messages[-10:]  # 只保留最近 10 条
```

### 并行处理

```python
# 并行执行独立节点
graph.add_node("node1", func1)
graph.add_node("node2", func2)
# node1 和 node2 将并行运行
```

### 缓存

```python
# 缓存工具结果
from functools import lru_cache

@lru_cache(maxsize=100)
@tool
def cached_search(query: str) -> str:
    return expensive_search(query)
```

---

## 🚀 部署选项

### 1. Local Development

```bash
# 本地运行
python my_agent/agent.py
```

### 2. Docker

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "-m", "my_agent.agent"]
```

### 3. LangGraph Cloud

```json
// langgraph.json
{
  "dependencies": ["requirements.txt"],
  "graphs": {
    "my_agent": "./my_agent/agent.py:create_agent"
  },
  "env": {
    "ANTHROPIC_API_KEY": null
  }
}
```

---

## 🤝 贡献和反馈

这个模板是一个活跃的、不断发展的项目。欢迎:

- 🐛 Bug 报告
- 💡 功能建议
- 📝 文档改进
- 🔧 代码贡献

---

## 📄 许可证

MIT License - 自由使用、修改和分发

---

## 🙏 致谢

此模板基于:
- **LangGraph**: LangChain 生态系统的图编排库
- **LangChain**: LLM 应用框架
- **LangSmith**: 可观察性和评估平台
- **Context Engineering**: PRP 框架和最佳实践

---

## 📞 支持

- **文档**: 查看 CLAUDE.md 和 examples/
- **问题**: 创建 GitHub issue
- **社区**: 加入 LangChain Discord
- **LangSmith**: https://smith.langchain.com 获取追踪支持

---

**开始构建你的 LangGraph AI 代理吧! 🚀**

```bash
# 1. 复制模板
python copy_template.py ~/my-awesome-agent

# 2. 设置环境
cd ~/my-awesome-agent
uv venv && source .venv/bin/activate
uv pip install -r requirements.txt

# 3. 创建功能请求
# 编辑 PRPs/INITIAL.md

# 4. 生成和执行 PRP
/generate-langgraph-prp PRPs/INITIAL.md
/execute-langgraph-prp PRPs/prp_your_feature.md

# 5. 开始构建! 🎉
```
