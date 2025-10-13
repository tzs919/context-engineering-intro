#!/usr/bin/env python3
"""
工具集成代理示例

展示如何创建带工具的 LangGraph 代理:
- 网络搜索工具 (模拟)
- 计算器工具
- 工具错误处理
- ReAct 推理模式

依赖:
    uv pip install langgraph langchain-anthropic langchain-core python-dotenv

使用:
    python examples/tool_enabled_agent.py

环境变量:
    ANTHROPIC_API_KEY: Anthropic API 密钥
"""

from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver
from langchain_anthropic import ChatAnthropic
from langchain_core.tools import tool
from pydantic import BaseModel, Field
from dotenv import load_dotenv
import os
import re

# 加载环境变量
load_dotenv()


# 工具 1: 网络搜索 (模拟)
@tool
def web_search(query: str, max_results: int = 5) -> str:
    """在网络上搜索信息。

    这是一个模拟工具。在生产环境中,应该集成真实的搜索 API
    如 Tavily、DuckDuckGo 或 Google Search API。

    Args:
        query: 搜索查询字符串
        max_results: 返回的最大结果数 (默认: 5)

    Returns:
        str: 格式化的搜索结果
    """
    # 模拟搜索结果
    results = f"""搜索结果: "{query}"

1. [示例结果 1] - 这是关于 {query} 的相关信息
2. [示例结果 2] - 更多 {query} 相关内容
3. [示例结果 3] - {query} 的深入分析

注意: 这是模拟搜索结果。实际使用时应集成真实的搜索 API。
"""
    return results


# 工具 2: 计算器 (使用 Pydantic 验证)
class CalculatorInput(BaseModel):
    """计算器工具输入模式。"""
    expression: str = Field(description="要计算的数学表达式")
    precision: int = Field(
        default=2,
        ge=0,
        le=10,
        description="小数精度 (0-10)"
    )


@tool(args_schema=CalculatorInput)
def calculator(expression: str, precision: int = 2) -> str:
    """执行数学计算。

    Args:
        expression: 数学表达式 (例如: "2 + 2 * 3")
        precision: 小数位数

    Returns:
        str: 计算结果

    Raises:
        ValueError: 如果表达式无效
    """
    try:
        # 安全地评估数学表达式
        # 注意: eval() 有安全风险,生产环境应使用 ast.literal_eval 或 sympy
        # 只允许数字、运算符和括号
        allowed_chars = set('0123456789+-*/.()')
        if not all(c in allowed_chars or c.isspace() for c in expression):
            raise ValueError("表达式包含非法字符")

        result = eval(expression)
        rounded_result = round(result, precision)

        return f"计算结果: {expression} = {rounded_result}"

    except Exception as e:
        return f"计算错误: {str(e)}. 请检查表达式格式。"


# 工具 3: 当前时间 (实用工具示例)
@tool
def get_current_time() -> str:
    """获取当前日期和时间。

    Returns:
        str: 格式化的当前时间
    """
    from datetime import datetime
    now = datetime.now()
    return f"当前时间: {now.strftime('%Y年%m月%d日 %H:%M:%S')}"


def create_tool_agent():
    """创建带工具的代理。

    Returns:
        编译后的 ReAct 代理,支持工具调用

    Raises:
        ValueError: 如果缺少 ANTHROPIC_API_KEY
    """
    # 验证 API 密钥
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        raise ValueError("ANTHROPIC_API_KEY not found")

    # 配置模型
    model = ChatAnthropic(
        model="claude-3-7-sonnet-latest",
        temperature=0,  # 确定性输出,适合工具使用
        max_tokens=2048,
        api_key=api_key
    )

    # 系统提示
    system_prompt = """You are a helpful AI assistant with access to tools.

Your capabilities:
- Web search: Find information online
- Calculator: Perform mathematical calculations
- Time: Get current date and time

Guidelines:
- Think step-by-step before using tools
- Use tools when necessary to provide accurate information
- Explain your reasoning
- If a tool fails, try to help the user anyway
- Be clear about when you're using tools vs. your own knowledge
"""

    # 工具列表
    tools = [
        web_search,
        calculator,
        get_current_time
    ]

    # 创建检查点器
    checkpointer = MemorySaver()

    # 创建 ReAct 代理
    agent = create_react_agent(
        model=model,
        tools=tools,
        state_modifier=system_prompt,
        checkpointer=checkpointer
    )

    return agent


def main():
    """运行交互式工具代理会话。"""
    print("🛠️  工具集成代理")
    print("=" * 50)
    print("代理可以使用以下工具:")
    print("  • 网络搜索 (模拟)")
    print("  • 计算器")
    print("  • 当前时间")
    print("\n输入 'quit' 退出。\n")

    # 创建代理
    try:
        agent = create_tool_agent()
    except ValueError as e:
        print(f"❌ 错误: {e}")
        return

    # 会话配置
    thread_id = "tool-agent-session"
    config = {"configurable": {"thread_id": thread_id}}

    # 示例查询提示
    print("💡 试试这些查询:")
    print("  - 计算 (15 + 27) * 3")
    print("  - 搜索 Python tutorials")
    print("  - 现在几点了?")
    print("  - 搜索 AI news 并计算 100 除以 4\n")

    # 对话循环
    while True:
        try:
            # 获取用户输入
            user_input = input("\n👤 You: ").strip()

            if user_input.lower() in ['quit', 'exit', 'q']:
                print("\n👋 再见!")
                break

            if not user_input:
                continue

            # 调用代理
            print("\n🤔 思考中...")
            result = agent.invoke(
                {"messages": [("user", user_input)]},
                config
            )

            # 显示响应
            last_message = result["messages"][-1]
            print(f"\n🤖 Agent: {last_message.content}")

            # 显示使用的工具 (可选)
            tool_calls = [
                msg for msg in result["messages"]
                if hasattr(msg, 'tool_calls') and msg.tool_calls
            ]
            if tool_calls:
                print(f"\n📊 使用了 {len(tool_calls[0].tool_calls)} 个工具")

        except KeyboardInterrupt:
            print("\n\n👋 再见!")
            break
        except Exception as e:
            print(f"\n❌ 错误: {e}")
            print("请重试或输入 'quit' 退出。")


if __name__ == "__main__":
    main()
