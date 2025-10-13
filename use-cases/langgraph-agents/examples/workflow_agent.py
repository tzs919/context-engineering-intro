#!/usr/bin/env python3
"""
多步骤工作流代理示例

展示如何使用 LangGraph 创建复杂的多步骤工作流:
- 自定义状态定义
- 多个节点函数
- 条件边和流程控制
- 工作流编排

依赖:
    uv pip install langgraph langchain-anthropic langchain-core python-dotenv

使用:
    python examples/workflow_agent.py

环境变量:
    ANTHROPIC_API_KEY: Anthropic API 密钥
"""

from typing import TypedDict, Annotated, Literal
from langgraph.graph import StateGraph, END
from langchain_anthropic import ChatAnthropic
from langchain_core.messages import HumanMessage, AIMessage
from dotenv import load_dotenv
import os

# 加载环境变量
load_dotenv()


# 定义工作流状态
class WorkflowState(TypedDict):
    """工作流状态定义。

    Attributes:
        user_query: 用户原始查询
        research_results: 研究阶段结果
        analysis_results: 分析阶段结果
        final_answer: 最终答案
        current_step: 当前步骤
    """
    user_query: str
    research_results: str
    analysis_results: str
    final_answer: str
    current_step: str


# 节点 1: 研究节点
def research_node(state: WorkflowState) -> WorkflowState:
    """执行研究阶段。

    模拟信息收集和研究过程。

    Args:
        state: 当前工作流状态

    Returns:
        更新后的状态
    """
    print("🔍 步骤 1: 研究阶段...")

    query = state["user_query"]

    # 模拟研究过程
    # 实际应用中,这里可能调用搜索 API、数据库查询等
    research_results = f"""
    研究主题: {query}

    发现:
    - 相关信息点 1: 关于 {query} 的基础概念
    - 相关信息点 2: {query} 的应用场景
    - 相关信息点 3: {query} 的最佳实践

    数据来源: [模拟来源]
    """

    return {
        **state,
        "research_results": research_results,
        "current_step": "research"
    }


# 节点 2: 分析节点
def analysis_node(state: WorkflowState) -> WorkflowState:
    """执行分析阶段。

    使用 LLM 分析研究结果。

    Args:
        state: 当前工作流状态

    Returns:
        更新后的状态
    """
    print("📊 步骤 2: 分析阶段...")

    # 验证 API 密钥
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        raise ValueError("ANTHROPIC_API_KEY not found")

    # 配置模型
    model = ChatAnthropic(
        model="claude-3-7-sonnet-latest",
        temperature=0,
        max_tokens=1024,
        api_key=api_key
    )

    # 使用 LLM 分析研究结果
    analysis_prompt = f"""基于以下研究结果,进行深入分析:

{state['research_results']}

请提供:
1. 关键洞察
2. 潜在问题
3. 推荐行动
"""

    response = model.invoke([HumanMessage(content=analysis_prompt)])
    analysis_results = response.content

    return {
        **state,
        "analysis_results": analysis_results,
        "current_step": "analysis"
    }


# 节点 3: 综合节点
def synthesis_node(state: WorkflowState) -> WorkflowState:
    """执行综合阶段。

    综合所有信息生成最终答案。

    Args:
        state: 当前工作流状态

    Returns:
        更新后的状态
    """
    print("✨ 步骤 3: 综合阶段...")

    # 验证 API 密钥
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        raise ValueError("ANTHROPIC_API_KEY not found")

    # 配置模型
    model = ChatAnthropic(
        model="claude-3-7-sonnet-latest",
        temperature=0.3,
        max_tokens=1024,
        api_key=api_key
    )

    # 综合所有信息
    synthesis_prompt = f"""基于研究和分析,回答用户查询:

用户查询: {state['user_query']}

研究结果:
{state['research_results']}

分析结果:
{state['analysis_results']}

请提供一个全面、清晰的答案。
"""

    response = model.invoke([HumanMessage(content=synthesis_prompt)])
    final_answer = response.content

    return {
        **state,
        "final_answer": final_answer,
        "current_step": "completed"
    }


# 条件函数: 决定下一步
def decide_next_step(
    state: WorkflowState
) -> Literal["analysis", "synthesis", "end"]:
    """决定工作流的下一步。

    Args:
        state: 当前工作流状态

    Returns:
        下一个节点名称或 END
    """
    current_step = state.get("current_step", "")

    if current_step == "research":
        return "analysis"
    elif current_step == "analysis":
        return "synthesis"
    elif current_step == "completed":
        return "end"
    else:
        return "analysis"


def create_workflow_agent():
    """创建多步骤工作流代理。

    Returns:
        编译后的工作流图
    """
    # 创建状态图
    workflow = StateGraph(WorkflowState)

    # 添加节点
    workflow.add_node("research", research_node)
    workflow.add_node("analysis", analysis_node)
    workflow.add_node("synthesis", synthesis_node)

    # 设置入口点
    workflow.set_entry_point("research")

    # 添加条件边
    workflow.add_conditional_edges(
        "research",
        decide_next_step,
        {
            "analysis": "analysis",
            "synthesis": "synthesis",
            "end": END
        }
    )

    workflow.add_conditional_edges(
        "analysis",
        decide_next_step,
        {
            "synthesis": "synthesis",
            "end": END
        }
    )

    workflow.add_conditional_edges(
        "synthesis",
        decide_next_step,
        {
            "end": END
        }
    )

    # 编译图
    app = workflow.compile()

    return app


def main():
    """运行工作流代理示例。"""
    print("⚙️  多步骤工作流代理")
    print("=" * 50)
    print("此代理执行三步骤工作流:")
    print("  1. 🔍 研究: 收集信息")
    print("  2. 📊 分析: 深入分析")
    print("  3. ✨ 综合: 生成答案\n")

    # 创建代理
    try:
        agent = create_workflow_agent()
    except Exception as e:
        print(f"❌ 错误: {e}")
        return

    # 对话循环
    while True:
        try:
            # 获取用户输入
            user_query = input("\n👤 输入你的查询 (或 'quit' 退出): ").strip()

            if user_query.lower() in ['quit', 'exit', 'q']:
                print("\n👋 再见!")
                break

            if not user_query:
                continue

            print("\n🚀 启动工作流...\n")

            # 初始状态
            initial_state = {
                "user_query": user_query,
                "research_results": "",
                "analysis_results": "",
                "final_answer": "",
                "current_step": ""
            }

            # 运行工作流
            result = agent.invoke(initial_state)

            # 显示结果
            print("\n" + "=" * 50)
            print("📝 最终答案:")
            print("=" * 50)
            print(result["final_answer"])
            print("=" * 50)

            # 显示工作流统计
            print(f"\n✅ 工作流完成!")
            print(f"   最终步骤: {result['current_step']}")

        except KeyboardInterrupt:
            print("\n\n👋 再见!")
            break
        except Exception as e:
            print(f"\n❌ 错误: {e}")
            print("请重试或输入 'quit' 退出。")


if __name__ == "__main__":
    main()
