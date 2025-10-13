#!/usr/bin/env python3
"""
测试模式示例

展示 LangGraph 代理的测试最佳实践:
- 单元测试工具
- 集成测试代理
- 行为测试
- Mock 和 Fixtures
- 异步测试

注意: 这是一个可运行的测试套件示例。
      在实际项目中,应放在 tests/ 目录下。

依赖:
    uv pip install langgraph langchain-anthropic langchain-core pytest pytest-asyncio python-dotenv

使用:
    pytest examples/testing_examples.py -v

或直接运行:
    python examples/testing_examples.py
"""

import pytest
from typing import TypedDict, Annotated, Sequence
from operator import add
from unittest.mock import Mock, patch

from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver
from langchain_anthropic import ChatAnthropic
from langchain_core.tools import tool
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage
from dotenv import load_dotenv
import os

# 加载环境变量
load_dotenv()


# ============================================================================
# 测试用的工具和代理定义
# ============================================================================

@tool
def test_calculator(expression: str) -> str:
    """测试用计算器工具。

    Args:
        expression: 数学表达式

    Returns:
        str: 计算结果
    """
    try:
        result = eval(expression)
        return f"Result: {result}"
    except Exception as e:
        return f"Error: {e}"


@tool
def test_search(query: str) -> str:
    """测试用搜索工具。

    Args:
        query: 搜索查询

    Returns:
        str: 搜索结果
    """
    return f"Search results for: {query}"


class TestAgentState(TypedDict):
    """测试用代理状态。"""
    messages: Annotated[Sequence[BaseMessage], add]


def create_test_agent():
    """创建测试用代理。

    Returns:
        配置好的测试代理
    """
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        pytest.skip("ANTHROPIC_API_KEY not found")

    model = ChatAnthropic(
        model="claude-3-7-sonnet-latest",
        temperature=0,
        max_tokens=1024,
        api_key=api_key
    )

    tools = [test_calculator, test_search]
    checkpointer = MemorySaver()

    agent = create_react_agent(
        model=model,
        tools=tools,
        checkpointer=checkpointer
    )

    return agent


# ============================================================================
# 单元测试: 工具测试
# ============================================================================

class TestTools:
    """测试工具函数。"""

    def test_calculator_basic_addition(self):
        """测试基础加法。"""
        result = test_calculator("2 + 2")
        assert "Result: 4" in result

    def test_calculator_complex_expression(self):
        """测试复杂表达式。"""
        result = test_calculator("(10 + 5) * 2")
        assert "Result: 30" in result

    def test_calculator_error_handling(self):
        """测试错误处理。"""
        result = test_calculator("invalid")
        assert "Error" in result

    def test_search_tool(self):
        """测试搜索工具。"""
        result = test_search("Python tutorials")
        assert "Python tutorials" in result
        assert "Search results" in result


# ============================================================================
# 集成测试: 代理行为测试
# ============================================================================

class TestAgentBehavior:
    """测试代理行为。"""

    def test_agent_creation(self):
        """测试代理创建。"""
        agent = create_test_agent()
        assert agent is not None

    def test_agent_simple_response(self):
        """测试代理简单响应。"""
        agent = create_test_agent()

        result = agent.invoke({
            "messages": [("user", "Hello")]
        })

        assert "messages" in result
        assert len(result["messages"]) > 0
        last_message = result["messages"][-1]
        assert last_message.content

    def test_agent_with_calculator(self):
        """测试代理使用计算器工具。"""
        agent = create_test_agent()

        result = agent.invoke({
            "messages": [("user", "Calculate 5 + 3")]
        })

        assert result is not None
        # 检查是否有多个消息 (包括工具调用)
        assert len(result["messages"]) >= 2

    def test_agent_with_search(self):
        """测试代理使用搜索工具。"""
        agent = create_test_agent()

        result = agent.invoke({
            "messages": [("user", "Search for AI news")]
        })

        assert result is not None
        assert len(result["messages"]) >= 2


# ============================================================================
# 异步测试
# ============================================================================

class TestAsyncAgent:
    """测试异步代理操作。"""

    @pytest.mark.asyncio
    async def test_agent_async_invoke(self):
        """测试异步调用。"""
        agent = create_test_agent()

        result = await agent.ainvoke({
            "messages": [("user", "Hello")]
        })

        assert "messages" in result
        assert len(result["messages"]) > 0


# ============================================================================
# 行为测试: 对话记忆
# ============================================================================

class TestConversationMemory:
    """测试对话记忆功能。"""

    def test_memory_across_turns(self):
        """测试多轮对话记忆。"""
        agent = create_test_agent()
        config = {"configurable": {"thread_id": "test-memory-123"}}

        # 第一轮: 告诉代理信息
        result1 = agent.invoke(
            {"messages": [("user", "My name is Alice")]},
            config
        )
        assert result1 is not None

        # 第二轮: 测试是否记住
        result2 = agent.invoke(
            {"messages": [("user", "What is my name?")]},
            config
        )

        last_message = result2["messages"][-1].content
        # 代理应该记住名字
        assert "Alice" in last_message or "alice" in last_message.lower()

    def test_different_threads_isolated(self):
        """测试不同线程的隔离。"""
        agent = create_test_agent()

        # 线程 1
        config1 = {"configurable": {"thread_id": "thread-1"}}
        agent.invoke(
            {"messages": [("user", "My favorite color is blue")]},
            config1
        )

        # 线程 2
        config2 = {"configurable": {"thread_id": "thread-2"}}
        result = agent.invoke(
            {"messages": [("user", "What is my favorite color?")]},
            config2
        )

        # 线程 2 不应该知道线程 1 的信息
        last_message = result["messages"][-1].content
        # 应该表示不知道
        assert any(word in last_message.lower() for word in [
            "don't know", "not sure", "haven't", "didn't mention"
        ])


# ============================================================================
# Mock 测试: 模拟外部依赖
# ============================================================================

class TestWithMocks:
    """使用 Mock 的测试。"""

    def test_tool_with_mock(self):
        """测试使用 mock 的工具。"""
        # 创建 mock 工具
        mock_tool = Mock()
        mock_tool.return_value = "Mocked result"
        mock_tool.name = "mock_tool"

        # 使用 mock
        result = mock_tool("test query")
        assert result == "Mocked result"
        mock_tool.assert_called_once_with("test query")

    @patch('langchain_anthropic.ChatAnthropic')
    def test_agent_with_mocked_model(self, mock_model_class):
        """测试使用 mocked 模型的代理。"""
        # 配置 mock
        mock_model = Mock()
        mock_model.invoke.return_value = AIMessage(
            content="Mocked response"
        )
        mock_model_class.return_value = mock_model

        # 这里可以测试代理逻辑,不实际调用 API
        # 注意: create_react_agent 内部逻辑复杂,完整 mock 较困难
        # 此示例仅展示 mock 模式


# ============================================================================
# Fixture 示例
# ============================================================================

@pytest.fixture
def agent():
    """提供测试用代理的 fixture。"""
    return create_test_agent()


@pytest.fixture
def test_config():
    """提供测试配置的 fixture。"""
    return {
        "configurable": {"thread_id": "test-fixture-thread"},
        "recursion_limit": 25
    }


class TestWithFixtures:
    """使用 fixtures 的测试。"""

    def test_with_agent_fixture(self, agent):
        """使用 agent fixture 的测试。"""
        result = agent.invoke({
            "messages": [("user", "Hello")]
        })
        assert result is not None

    def test_with_config_fixture(self, agent, test_config):
        """使用 config fixture 的测试。"""
        result = agent.invoke(
            {"messages": [("user", "Test")]},
            test_config
        )
        assert result is not None


# ============================================================================
# 参数化测试
# ============================================================================

class TestParameterized:
    """参数化测试示例。"""

    @pytest.mark.parametrize("expression,expected", [
        ("2 + 2", "4"),
        ("10 * 3", "30"),
        ("100 / 4", "25"),
    ])
    def test_calculator_multiple_cases(self, expression, expected):
        """测试多个计算案例。"""
        result = test_calculator(expression)
        assert expected in result

    @pytest.mark.parametrize("query", [
        "Python tutorials",
        "AI news",
        "Weather forecast",
    ])
    def test_search_multiple_queries(self, query):
        """测试多个搜索查询。"""
        result = test_search(query)
        assert query in result


# ============================================================================
# 性能测试 (简单示例)
# ============================================================================

class TestPerformance:
    """性能测试示例。"""

    def test_agent_response_time(self, agent):
        """测试代理响应时间。"""
        import time

        start_time = time.time()

        agent.invoke({
            "messages": [("user", "Hello")]
        })

        elapsed_time = time.time() - start_time

        # 响应应该在合理时间内 (例如 10 秒)
        assert elapsed_time < 10.0, f"Response took {elapsed_time}s"


# ============================================================================
# 运行测试 (如果直接执行此文件)
# ============================================================================

def main():
    """运行所有测试。"""
    print("🧪 LangGraph 代理测试示例")
    print("=" * 60)
    print("\n使用 pytest 运行此文件以查看完整测试结果:")
    print("  pytest examples/testing_examples.py -v\n")
    print("或使用 coverage:")
    print("  pytest examples/testing_examples.py -v --cov\n")

    # 运行一个简单的测试示例
    print("运行简单测试示例...\n")

    try:
        # 测试工具
        print("✓ 测试计算器工具")
        result = test_calculator("2 + 2")
        assert "Result: 4" in result
        print(f"  结果: {result}")

        print("\n✓ 测试搜索工具")
        result = test_search("Python")
        assert "Python" in result
        print(f"  结果: {result}")

        print("\n✅ 基础测试通过!")
        print("\n使用 pytest 运行完整测试套件以获取详细结果。")

    except Exception as e:
        print(f"\n❌ 测试失败: {e}")


if __name__ == "__main__":
    main()
