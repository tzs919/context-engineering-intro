#!/usr/bin/env python3
"""
基础聊天代理示例

展示如何创建一个简单的 LangGraph 聊天代理,具有:
- 对话记忆 (使用 MemorySaver)
- 系统提示
- 基础错误处理

依赖:
    uv pip install langgraph langchain-anthropic python-dotenv

使用:
    python examples/basic_chat_agent.py

环境变量:
    ANTHROPIC_API_KEY: Anthropic API 密钥
"""

from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
import os

# 加载环境变量
load_dotenv()


def create_basic_agent():
    """创建基础聊天代理。

    Returns:
        编译后的代理图,支持对话记忆

    Raises:
        ValueError: 如果缺少 ANTHROPIC_API_KEY
    """
    # 验证 API 密钥
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        raise ValueError(
            "ANTHROPIC_API_KEY not found. "
            "Please set it in .env file or environment"
        )

    # 配置模型
    model = ChatAnthropic(
        model="claude-3-7-sonnet-latest",
        temperature=0.7,  # 稍高温度使对话更自然
        max_tokens=1024,
        api_key=api_key
    )

    # 系统提示
    system_prompt = """You are a friendly and helpful AI assistant.

Your personality:
- Warm and conversational
- Patient and understanding
- Concise but thorough

Guidelines:
- Keep responses natural and engaging
- Use examples when helpful
- Admit when you don't know something
- Remember context from the conversation
"""

    # 创建检查点器用于记忆
    checkpointer = MemorySaver()

    # 创建代理 (不使用工具,纯对话)
    agent = create_react_agent(
        model=model,
        tools=[],  # 无工具,纯聊天
        state_modifier=system_prompt,
        checkpointer=checkpointer
    )

    return agent


def main():
    """运行交互式聊天会话。"""
    print("🤖 基础聊天代理")
    print("=" * 50)
    print("与 AI 助手对话。输入 'quit' 退出。\n")

    # 创建代理
    try:
        agent = create_basic_agent()
    except ValueError as e:
        print(f"❌ 错误: {e}")
        return

    # 会话配置 (使用固定的 thread_id 保持记忆)
    thread_id = "basic-chat-session"
    config = {"configurable": {"thread_id": thread_id}}

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
            result = agent.invoke(
                {"messages": [("user", user_input)]},
                config
            )

            # 显示响应
            last_message = result["messages"][-1]
            print(f"\n🤖 Agent: {last_message.content}")

        except KeyboardInterrupt:
            print("\n\n👋 再见!")
            break
        except Exception as e:
            print(f"\n❌ 错误: {e}")
            print("请重试或输入 'quit' 退出。")


if __name__ == "__main__":
    main()
