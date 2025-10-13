#!/usr/bin/env python3
"""
结构化输出代理示例

展示如何使用 Pydantic 模型实现结构化输出:
- Pydantic 模型定义
- with_structured_output() 方法
- 字段验证
- 类型安全

依赖:
    uv pip install langgraph langchain-anthropic langchain-core pydantic python-dotenv

使用:
    python examples/structured_output_agent.py

环境变量:
    ANTHROPIC_API_KEY: Anthropic API 密钥
"""

from pydantic import BaseModel, Field, field_validator
from langchain_anthropic import ChatAnthropic
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv
import os
from typing import Optional

# 加载环境变量
load_dotenv()


# 定义结构化输出模型
class MovieReview(BaseModel):
    """电影评论结构化输出。

    Attributes:
        movie_title: 电影标题
        director: 导演名字
        release_year: 上映年份
        rating: 评分 (1-10)
        summary: 简短总结
        strengths: 优点列表
        weaknesses: 缺点列表
        recommendation: 推荐级别
    """
    movie_title: str = Field(description="电影标题")
    director: Optional[str] = Field(default=None, description="导演名字")
    release_year: Optional[int] = Field(default=None, description="上映年份")
    rating: float = Field(ge=1.0, le=10.0, description="评分 (1-10)")
    summary: str = Field(description="一句话总结")
    strengths: list[str] = Field(
        default_factory=list,
        description="电影的优点"
    )
    weaknesses: list[str] = Field(
        default_factory=list,
        description="电影的缺点"
    )
    recommendation: str = Field(
        description="推荐级别: Highly Recommended, Recommended, Not Recommended"
    )

    @field_validator('rating')
    @classmethod
    def validate_rating(cls, v: float) -> float:
        """验证评分范围。"""
        if not 1.0 <= v <= 10.0:
            raise ValueError('评分必须在 1.0 到 10.0 之间')
        return v

    @field_validator('recommendation')
    @classmethod
    def validate_recommendation(cls, v: str) -> str:
        """验证推荐级别。"""
        valid_recommendations = [
            "Highly Recommended",
            "Recommended",
            "Not Recommended"
        ]
        if v not in valid_recommendations:
            raise ValueError(
                f'推荐级别必须是: {", ".join(valid_recommendations)}'
            )
        return v


class ProductAnalysis(BaseModel):
    """产品分析结构化输出。

    Attributes:
        product_name: 产品名称
        category: 产品类别
        price_estimate: 估计价格 (USD)
        target_audience: 目标受众
        key_features: 关键特性
        competitors: 竞争对手
        market_opportunity: 市场机会 (1-10)
    """
    product_name: str = Field(description="产品名称")
    category: str = Field(description="产品类别")
    price_estimate: Optional[float] = Field(
        default=None,
        ge=0,
        description="估计价格 (USD)"
    )
    target_audience: str = Field(description="目标受众描述")
    key_features: list[str] = Field(
        min_items=1,
        description="关键特性列表"
    )
    competitors: list[str] = Field(
        default_factory=list,
        description="主要竞争对手"
    )
    market_opportunity: int = Field(
        ge=1,
        le=10,
        description="市场机会评分 (1-10)"
    )


def create_structured_agent():
    """创建结构化输出代理。

    Returns:
        配置了结构化输出的模型

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
        temperature=0,
        max_tokens=2048,
        api_key=api_key
    )

    return model


def analyze_movie(model: ChatAnthropic, movie_description: str) -> MovieReview:
    """分析电影并返回结构化评论。

    Args:
        model: ChatAnthropic 模型
        movie_description: 电影描述或评论请求

    Returns:
        MovieReview: 结构化的电影评论

    Raises:
        ValidationError: 如果输出不符合 Pydantic 模型
    """
    # 配置结构化输出
    model_with_structure = model.with_structured_output(MovieReview)

    # 构建提示
    prompt = f"""请分析以下电影并提供详细评论:

{movie_description}

请提供:
- 电影标题、导演、年份
- 评分 (1-10)
- 简短总结
- 优点和缺点
- 推荐级别
"""

    # 调用模型
    result = model_with_structure.invoke([HumanMessage(content=prompt)])

    return result


def analyze_product(
    model: ChatAnthropic,
    product_description: str
) -> ProductAnalysis:
    """分析产品并返回结构化分析。

    Args:
        model: ChatAnthropic 模型
        product_description: 产品描述

    Returns:
        ProductAnalysis: 结构化的产品分析

    Raises:
        ValidationError: 如果输出不符合 Pydantic 模型
    """
    # 配置结构化输出
    model_with_structure = model.with_structured_output(ProductAnalysis)

    # 构建提示
    prompt = f"""请分析以下产品:

{product_description}

请提供:
- 产品名称和类别
- 估计价格
- 目标受众
- 关键特性
- 竞争对手
- 市场机会评分 (1-10)
"""

    # 调用模型
    result = model_with_structure.invoke([HumanMessage(content=prompt)])

    return result


def display_movie_review(review: MovieReview):
    """格式化显示电影评论。"""
    print("\n" + "=" * 60)
    print(f"🎬 电影评论: {review.movie_title}")
    print("=" * 60)

    if review.director:
        print(f"导演: {review.director}")
    if review.release_year:
        print(f"年份: {review.release_year}")

    print(f"\n⭐ 评分: {review.rating}/10")
    print(f"\n📝 总结: {review.summary}")

    if review.strengths:
        print(f"\n✅ 优点:")
        for strength in review.strengths:
            print(f"  • {strength}")

    if review.weaknesses:
        print(f"\n❌ 缺点:")
        for weakness in review.weaknesses:
            print(f"  • {weakness}")

    print(f"\n💡 推荐: {review.recommendation}")
    print("=" * 60)


def display_product_analysis(analysis: ProductAnalysis):
    """格式化显示产品分析。"""
    print("\n" + "=" * 60)
    print(f"📦 产品分析: {analysis.product_name}")
    print("=" * 60)

    print(f"类别: {analysis.category}")
    if analysis.price_estimate:
        print(f"估计价格: ${analysis.price_estimate}")

    print(f"\n👥 目标受众: {analysis.target_audience}")

    print(f"\n⚡ 关键特性:")
    for feature in analysis.key_features:
        print(f"  • {feature}")

    if analysis.competitors:
        print(f"\n🏆 竞争对手:")
        for competitor in analysis.competitors:
            print(f"  • {competitor}")

    print(f"\n📈 市场机会: {analysis.market_opportunity}/10")
    print("=" * 60)


def main():
    """运行结构化输出代理示例。"""
    print("📊 结构化输出代理")
    print("=" * 60)
    print("此代理返回验证过的结构化 Pydantic 输出")
    print("\n选项:")
    print("  1. 电影评论分析")
    print("  2. 产品分析")
    print("  quit - 退出\n")

    # 创建代理
    try:
        model = create_structured_agent()
    except ValueError as e:
        print(f"❌ 错误: {e}")
        return

    # 主循环
    while True:
        try:
            # 选择分析类型
            choice = input("\n👤 选择 (1/2/quit): ").strip()

            if choice.lower() in ['quit', 'exit', 'q']:
                print("\n👋 再见!")
                break

            if choice == '1':
                # 电影评论
                print("\n🎬 电影评论分析")
                movie_input = input("\n描述电影或提供评论请求: ").strip()

                if not movie_input:
                    continue

                print("\n🤔 分析中...")
                review = analyze_movie(model, movie_input)
                display_movie_review(review)

                # 显示原始 Pydantic 模型 (可选)
                print("\n💾 原始数据 (JSON):")
                print(review.model_dump_json(indent=2))

            elif choice == '2':
                # 产品分析
                print("\n📦 产品分析")
                product_input = input("\n描述产品: ").strip()

                if not product_input:
                    continue

                print("\n🤔 分析中...")
                analysis = analyze_product(model, product_input)
                display_product_analysis(analysis)

                # 显示原始 Pydantic 模型 (可选)
                print("\n💾 原始数据 (JSON):")
                print(analysis.model_dump_json(indent=2))

            else:
                print("❌ 无效选择。请输入 1, 2 或 quit。")

        except KeyboardInterrupt:
            print("\n\n👋 再见!")
            break
        except Exception as e:
            print(f"\n❌ 错误: {e}")
            print("请重试或输入 'quit' 退出。")


if __name__ == "__main__":
    main()
