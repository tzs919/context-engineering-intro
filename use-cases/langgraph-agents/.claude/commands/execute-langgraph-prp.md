---
name: "execute-langgraph-prp"
description: "执行 LangGraph AI 代理 PRP 并构建完整实现"
---

# Execute LangGraph Agent PRP

执行 PRPs/ 目录中的 LangGraph 代理 PRP,生成生产就绪的 AI 代理实现。

## Usage

```bash
/execute-langgraph-prp PRPs/prp_your_feature.md
```

## Purpose

遵循 PRP 中定义的实现蓝图,使用 LangGraph、LangChain 和 LangSmith 构建完整的 AI 代理,包括工具集成、状态管理、测试套件和文档。

## PRP 文件

**输入**: $ARGUMENTS (PRP 文件路径)

## Execution Process

### 1. 📖 Read and Validate PRP

```bash
# 读取 PRP 文件
cat $ARGUMENTS

# 验证 PRP 结构
# - Purpose 和 What 部分明确
# - Implementation Blueprint 包含具体任务
# - Validation Loop 定义清晰
# - 所有引用的文件存在
```

**检查项**:
- [ ] PRP 文件存在且可读
- [ ] 包含完整的 Implementation Blueprint
- [ ] 验证循环定义明确
- [ ] 成功标准可测量

### 2. 🏗️ Execute Implementation Blueprint

按照 PRP 中的 Task 顺序执行:

#### Task 1: 项目设置

```bash
# 创建项目结构
mkdir -p my_agent/utils tests scripts logs

# 创建 __init__.py 文件
touch my_agent/__init__.py
touch my_agent/utils/__init__.py
touch tests/__init__.py

# 安装依赖 (使用 uv)
uv venv
source .venv/bin/activate
uv pip install langgraph langchain-anthropic langchain-openai
uv pip install langchain-core pydantic python-dotenv
uv pip install --dev pytest pytest-asyncio black mypy

# 创建环境变量文件
cat > .env << 'EOF'
# API Keys (替换为实际密钥)
ANTHROPIC_API_KEY=your-anthropic-key-here
OPENAI_API_KEY=your-openai-key-here

# LangSmith (可选)
LANGSMITH_API_KEY=your-langsmith-key-here
LANGSMITH_TRACING=true
LANGSMITH_PROJECT=my-agent

# 其他配置
LOG_LEVEL=INFO
EOF

# 创建 .gitignore
cat > .gitignore << 'EOF'
.env
.venv/
__pycache__/
*.pyc
*.pyo
.pytest_cache/
.mypy_cache/
.coverage
logs/
*.log
EOF
```

#### Task 2: 状态定义

根据 PRP 中的状态要求创建 `my_agent/utils/state.py`:

```python
"""Agent state definitions."""
from typing import TypedDict, Annotated, Sequence
from langchain_core.messages import BaseMessage
from operator import add

class AgentState(TypedDict):
    """Agent state with conversation memory and context."""
    # 消息历史 (使用 add reducer 合并)
    messages: Annotated[Sequence[BaseMessage], add]

    # PRP 中定义的自定义状态字段
    # 根据具体需求添加
```

#### Task 3: 工具定义

根据 PRP 中的工具需求创建 `my_agent/utils/tools.py`:

```python
"""Tool definitions for the agent."""
from langchain_core.tools import tool
from pydantic import BaseModel, Field

# 根据 PRP 实现工具
# 示例:

@tool
def example_tool(query: str) -> str:
    """Tool description from PRP.

    Args:
        query: Input query

    Returns:
        str: Tool result
    """
    # 实现工具逻辑
    return f"Result: {query}"
```

#### Task 4: 节点函数 (如需要)

如果使用自定义图而非 create_react_agent,创建 `my_agent/utils/nodes.py`:

```python
"""Node functions for the agent graph."""
from langchain_core.messages import HumanMessage
from .state import AgentState

def agent_node(state: AgentState) -> AgentState:
    """Process agent logic.

    Args:
        state: Current agent state

    Returns:
        Updated state
    """
    # 实现节点逻辑
    return state
```

#### Task 5: 主代理逻辑

创建 `my_agent/agent.py`:

```python
"""Main agent implementation."""
from langgraph.prebuilt import create_react_agent
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
import os

from .utils.tools import example_tool  # 导入所有工具
from .utils.state import AgentState

# 加载环境变量
load_dotenv()

def create_agent():
    """Create and configure the LangGraph agent.

    Returns:
        Compiled agent graph ready for invocation
    """
    # 配置模型
    model = ChatAnthropic(
        model="claude-3-7-sonnet-latest",
        temperature=0,
        max_tokens=2048
    )

    # 系统提示 (根据 PRP)
    system_prompt = """You are a helpful AI assistant.

    Your capabilities:
    - [从 PRP 获取能力列表]

    Your constraints:
    - [从 PRP 获取约束]
    """

    # 创建代理
    agent = create_react_agent(
        model=model,
        tools=[example_tool],  # 添加所有工具
        state_modifier=system_prompt
    )

    return agent

# CLI 入口点
if __name__ == "__main__":
    agent = create_agent()

    print("Agent ready. Type 'quit' to exit.")

    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ['quit', 'exit', 'q']:
            break

        try:
            result = agent.invoke({"messages": [("user", user_input)]})
            print(f"\nAgent: {result['messages'][-1].content}")
        except Exception as e:
            print(f"Error: {e}")
```

#### Task 6: 结构化输出 (如 PRP 要求)

如果 PRP 要求 Pydantic 结构化输出,创建 `my_agent/utils/models.py`:

```python
"""Pydantic models for structured outputs."""
from pydantic import BaseModel, Field, field_validator

class AgentResponse(BaseModel):
    """Structured agent response."""
    answer: str = Field(description="The agent's answer")
    sources: list[str] = Field(default_factory=list, description="Source URLs")
    confidence: float = Field(ge=0.0, le=1.0, description="Confidence score")
    metadata: dict = Field(default_factory=dict)

    @field_validator('confidence')
    @classmethod
    def validate_confidence(cls, v):
        """Ensure confidence is between 0 and 1."""
        if not 0 <= v <= 1:
            raise ValueError('Confidence must be between 0 and 1')
        return v
```

#### Task 7: 测试套件

创建综合测试:

**tests/test_tools.py**:
```python
"""Unit tests for tools."""
import pytest
from my_agent.utils.tools import example_tool

def test_example_tool():
    """Test example tool basic functionality."""
    result = example_tool("test query")
    assert isinstance(result, str)
    assert len(result) > 0

def test_example_tool_edge_case():
    """Test tool with edge case input."""
    result = example_tool("")
    assert isinstance(result, str)
```

**tests/test_agent.py**:
```python
"""Integration tests for agent."""
import pytest
from my_agent.agent import create_agent

def test_agent_creation():
    """Test agent can be created."""
    agent = create_agent()
    assert agent is not None

@pytest.mark.asyncio
async def test_agent_responds():
    """Test agent generates responses."""
    agent = create_agent()
    result = agent.invoke({"messages": [("user", "Hello")]})

    assert "messages" in result
    assert len(result["messages"]) > 0

@pytest.mark.asyncio
async def test_agent_uses_tools():
    """Test agent can use tools."""
    agent = create_agent()
    result = agent.invoke({
        "messages": [("user", "Use the example tool")]
    })

    # 验证工具被调用
    assert result is not None
```

**tests/test_agent_behavior.py**:
```python
"""Behavioral tests for agent."""
import pytest
from my_agent.agent import create_agent

def test_conversation_memory():
    """Test agent maintains conversation context."""
    agent = create_agent()
    config = {"configurable": {"thread_id": "test-123"}}

    # 第一轮
    result1 = agent.invoke(
        {"messages": [("user", "My name is Alice")]},
        config
    )

    # 第二轮 - 测试记忆
    result2 = agent.invoke(
        {"messages": [("user", "What's my name?")]},
        config
    )

    assert "Alice" in result2["messages"][-1].content
```

#### Task 8: 运行脚本

创建 `scripts/` 中的运行脚本:

**scripts/run_agent.sh**:
```bash
#!/bin/bash
source .venv/bin/activate
python -m my_agent.agent
```

**scripts/test.sh**:
```bash
#!/bin/bash
source .venv/bin/activate
pytest tests/ -v --cov=my_agent --cov-report=term-missing
```

**scripts/type_check.sh**:
```bash
#!/bin/bash
source .venv/bin/activate
mypy my_agent/ --ignore-missing-imports
```

**scripts/format.sh**:
```bash
#!/bin/bash
source .venv/bin/activate
black my_agent/ tests/
```

```bash
# 使脚本可执行
chmod +x scripts/*.sh
```

### 3. 🧪 Run Validation Loops

按照 PRP 中定义的验证循环执行:

#### Level 1: 语法和类型检查

```bash
# 类型检查
./scripts/type_check.sh

# 代码格式化
./scripts/format.sh

# 预期: 无类型错误,代码格式规范
# 如果失败: 修复类型注释和格式问题
```

#### Level 2: 单元测试

```bash
# 运行所有测试
./scripts/test.sh

# 预期: 所有测试通过,覆盖率 > 80%
# 如果失败:
#   1. 查看失败的测试输出
#   2. 调试工具或代理逻辑
#   3. 修复代码
#   4. 重新运行测试
```

#### Level 3: 代理行为测试

```bash
# 运行行为测试
pytest tests/test_agent_behavior.py -v -s

# 预期: 代理正确响应,记忆工作,工具被调用
# 如果失败:
#   1. 检查代理配置
#   2. 验证工具集成
#   3. 调试状态管理
```

#### Level 4: LangSmith 追踪 (如配置)

```bash
# 运行代理并检查 LangSmith
./scripts/run_agent.sh

# 在 https://smith.langchain.com 查看追踪
# 预期: 看到完整的追踪信息,包括:
#   - 所有节点执行
#   - 工具调用
#   - Token 使用
#   - 延迟分析

# 如果失败:
#   1. 检查 LANGSMITH_API_KEY
#   2. 确认 LANGSMITH_TRACING=true
#   3. 验证网络连接
```

### 4. 📝 Documentation and README

创建 `README.md`:

```markdown
# [Agent Name]

[从 PRP Purpose 获取简短描述]

## Features

- [从 PRP What 列出功能]

## Setup

```bash
# 克隆/进入项目目录
cd my-agent

# 创建虚拟环境
uv venv
source .venv/bin/activate

# 安装依赖
uv pip install -r requirements.txt

# 配置环境变量
cp .env.example .env
# 编辑 .env 添加 API 密钥
```

## Usage

```bash
# 运行代理
./scripts/run_agent.sh

# 运行测试
./scripts/test.sh

# 类型检查
./scripts/type_check.sh
```

## Architecture

[从 PRP 描述代理架构]

## Tools

[列出集成的工具及其用途]

## Testing

[从 PRP 描述测试策略]

## Security

[从 PRP Security Checklist 列出安全措施]

## Common Issues

[从 PRP Common Gotchas 列出常见问题和解决方案]

## License

MIT
```

创建 `requirements.txt`:

```bash
# 生成依赖列表
uv pip freeze > requirements.txt
```

### 5. ✅ Final Validation

运行 PRP 中的 Final Checklist:

```bash
# 文件结构检查
tree my_agent tests scripts

# 所有测试通过
./scripts/test.sh

# 类型检查通过
./scripts/type_check.sh

# 代理可运行
./scripts/run_agent.sh
```

**检查项** (from PRP):
- [ ] 所有代码文件创建且语法正确
- [ ] Pydantic 模型定义并验证 (如需要)
- [ ] 工具正确集成
- [ ] 状态管理正确实现
- [ ] 所有 pytest 测试通过
- [ ] LangSmith 追踪工作 (如配置)
- [ ] 文档完整
- [ ] 安全最佳实践遵循

## 常见执行模式

### 模式 1: ReAct Agent (最常见)

使用 `create_react_agent` 快速构建:

```python
from langgraph.prebuilt import create_react_agent

agent = create_react_agent(
    model=model,
    tools=[tool1, tool2, tool3],
    state_modifier=system_prompt
)
```

### 模式 2: Custom Graph

需要更多控制时:

```python
from langgraph.graph import StateGraph, END

graph = StateGraph(AgentState)
graph.add_node("agent", agent_node)
graph.add_node("tools", tool_node)
graph.add_edge("agent", "tools")
graph.add_conditional_edges("tools", should_continue, {
    "continue": "agent",
    "end": END
})
```

### 模式 3: Multi-Agent System

多个专门化代理协作:

```python
# 创建多个代理
researcher = create_react_agent(model, research_tools, "You are a researcher")
writer = create_react_agent(model, writing_tools, "You are a writer")

# 使用 supervisor 或协作模式
```

## 错误处理

### 常见错误和解决方案

**1. ImportError: No module named 'langgraph'**
```bash
# 确保在虚拟环境中
source .venv/bin/activate
uv pip install langgraph
```

**2. InvalidUpdateError in parallel execution**
```python
# 为并行更新的字段添加 reducer
from operator import add

class AgentState(TypedDict):
    results: Annotated[list[str], add]  # 使用 add reducer
```

**3. Token limit exceeded**
```python
# 实现消息修剪
def trim_messages(state):
    if len(state["messages"]) > 20:
        state["messages"] = state["messages"][-20:]
    return state
```

**4. API Key not found**
```bash
# 检查 .env 文件
cat .env | grep API_KEY

# 确保 load_dotenv() 被调用
```

## Success Criteria

执行成功当:

1. ✅ 所有代码文件已创建
2. ✅ 项目结构遵循最佳实践
3. ✅ 所有单元测试通过
4. ✅ 类型检查通过
5. ✅ 代理能正确响应查询
6. ✅ 工具集成工作正常
7. ✅ 文档完整准确
8. ✅ PRP 中的所有成功标准满足

## Output

完整的 LangGraph 代理实现,包括:

- 📁 **代码**: 代理、工具、状态、节点
- 🧪 **测试**: 单元测试、集成测试、行为测试
- 📜 **脚本**: 运行、测试、类型检查脚本
- 📖 **文档**: README、代码注释、使用说明
- ⚙️ **配置**: .env、requirements.txt、.gitignore

代理已准备好用于开发、测试和部署!
