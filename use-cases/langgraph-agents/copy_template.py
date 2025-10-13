#!/usr/bin/env python3
"""
LangGraph 模板复制脚本

将完整的 LangGraph 代理模板复制到目标目录,包括所有必要的文件和目录结构。

使用方法:
    python copy_template.py /path/to/target-directory

示例:
    python copy_template.py ~/projects/my-langgraph-agent
    python copy_template.py /home/user/ai-projects/search-agent

功能:
    - 复制完整的模板结构
    - 创建必要的目录
    - 复制所有配置文件
    - 提供下一步指导

依赖:
    标准库 (无需额外安装)
"""

import os
import shutil
import sys
from pathlib import Path
from typing import List


def print_banner():
    """打印横幅。"""
    print("=" * 70)
    print("🚀 LangGraph Agent Template Copy Script")
    print("=" * 70)


def validate_target_directory(target_path: Path) -> None:
    """验证目标目录。

    Args:
        target_path: 目标目录路径

    Raises:
        SystemExit: 如果目标目录存在且不为空
    """
    if target_path.exists():
        # 检查目录是否为空
        if any(target_path.iterdir()):
            print(f"\n❌ 错误: 目标目录 '{target_path}' 已存在且不为空")
            print("\n请选择:")
            print("  1. 删除现有目录")
            print("  2. 选择不同的目标目录")
            sys.exit(1)


def get_items_to_copy() -> List[str]:
    """获取要复制的文件和目录列表。

    Returns:
        要复制的项目列表
    """
    return [
        "CLAUDE.md",
        ".claude/",
        "PRPs/",
        "examples/",
        "README.md"
    ]


def copy_template(source_dir: Path, target_dir: Path) -> None:
    """复制模板到目标目录。

    Args:
        source_dir: 模板源目录
        target_dir: 目标目录

    Raises:
        FileNotFoundError: 如果源文件不存在
        PermissionError: 如果没有写权限
    """
    items_to_copy = get_items_to_copy()

    print(f"\n📂 复制模板: {source_dir}")
    print(f"📁 目标目录: {target_dir}")
    print()

    # 创建目标目录
    target_dir.mkdir(parents=True, exist_ok=True)
    print(f"✓ 创建目录: {target_dir}")

    # 复制每个项目
    copied_count = 0
    skipped_count = 0

    for item in items_to_copy:
        source_item = source_dir / item
        target_item = target_dir / item

        if not source_item.exists():
            print(f"⚠️  跳过 (不存在): {item}")
            skipped_count += 1
            continue

        try:
            if source_item.is_dir():
                # 复制目录
                shutil.copytree(source_item, target_item, dirs_exist_ok=True)
                # 统计文件数
                file_count = sum(1 for _ in target_item.rglob('*') if _.is_file())
                print(f"✓ 复制目录: {item} ({file_count} 文件)")
            else:
                # 复制文件
                target_item.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(source_item, target_item)
                print(f"✓ 复制文件: {item}")

            copied_count += 1

        except Exception as e:
            print(f"❌ 复制失败 {item}: {e}")
            skipped_count += 1

    print()
    print(f"✅ 复制完成: {copied_count} 项成功, {skipped_count} 项跳过")


def create_additional_files(target_dir: Path) -> None:
    """创建额外的必要文件。

    Args:
        target_dir: 目标目录
    """
    print("\n📝 创建额外文件...")

    # 创建 .env.example
    env_example_content = """# LangGraph Agent 环境变量配置

# API Keys (替换为你的实际密钥)
ANTHROPIC_API_KEY=your-anthropic-api-key-here
OPENAI_API_KEY=your-openai-api-key-here

# LangSmith 配置 (可选,用于追踪和监控)
LANGSMITH_API_KEY=your-langsmith-api-key-here
LANGSMITH_TRACING=true
LANGSMITH_PROJECT=my-agent-project

# 工具 API Keys (根据需要)
# TAVILY_API_KEY=your-tavily-api-key
# PINECONE_API_KEY=your-pinecone-api-key

# 应用配置
LOG_LEVEL=INFO
MAX_RECURSION_LIMIT=25
"""

    env_example_path = target_dir / ".env.example"
    env_example_path.write_text(env_example_content, encoding='utf-8')
    print(f"✓ 创建文件: .env.example")

    # 创建 .gitignore
    gitignore_content = """# 环境文件
.env
.venv/
venv/
env/

# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python

# 测试
.pytest_cache/
.coverage
htmlcov/
.tox/

# 类型检查
.mypy_cache/
.dmypy.json
dmypy.json

# 日志
logs/
*.log

# IDE
.vscode/
.idea/
*.swp
*.swo

# 操作系统
.DS_Store
Thumbs.db

# 其他
*.egg-info/
dist/
build/
"""

    gitignore_path = target_dir / ".gitignore"
    gitignore_path.write_text(gitignore_content, encoding='utf-8')
    print(f"✓ 创建文件: .gitignore")


def print_next_steps(target_dir: Path) -> None:
    """打印下一步指导。

    Args:
        target_dir: 目标目录
    """
    print("\n" + "=" * 70)
    print("🎉 模板复制成功!")
    print("=" * 70)

    print(f"\n📍 模板位置: {target_dir}")

    print("\n🚀 下一步:")
    print(f"\n1️⃣  进入项目目录:")
    print(f"   cd {target_dir}")

    print(f"\n2️⃣  创建虚拟环境:")
    print(f"   uv venv")
    print(f"   source .venv/bin/activate  # Linux/Mac")
    print(f"   # .venv\\Scripts\\activate  # Windows")

    print(f"\n3️⃣  安装依赖:")
    print(f"   uv pip install langgraph langchain-anthropic langchain-openai")
    print(f"   uv pip install langchain-core pydantic python-dotenv")
    print(f"   uv pip install --dev pytest pytest-asyncio black mypy")

    print(f"\n4️⃣  配置环境变量:")
    print(f"   cp .env.example .env")
    print(f"   # 编辑 .env 文件,添加你的 API 密钥")

    print(f"\n5️⃣  创建功能请求:")
    print(f"   # 编辑 PRPs/INITIAL.md 描述你想构建的代理")

    print(f"\n6️⃣  生成 PRP:")
    print(f"   /generate-langgraph-prp PRPs/INITIAL.md")

    print(f"\n7️⃣  执行 PRP:")
    print(f"   /execute-langgraph-prp PRPs/prp_your_feature.md")

    print("\n📚 文档:")
    print("   - README.md: 模板使用指南")
    print("   - CLAUDE.md: LangGraph 开发指南")
    print("   - examples/: 工作代码示例")

    print("\n💡 提示:")
    print("   - 查看 examples/ 目录获取代码示例")
    print("   - 参考 PRPs/templates/prp_langgraph_base.md 了解 PRP 结构")
    print("   - 使用 LangSmith 追踪和调试你的代理")

    print("\n" + "=" * 70)


def main():
    """主函数。"""
    print_banner()

    # 检查参数
    if len(sys.argv) != 2:
        print("\n使用方法:")
        print("  python copy_template.py <target-directory>")
        print("\n示例:")
        print("  python copy_template.py ~/projects/my-langgraph-agent")
        print("  python copy_template.py /home/user/ai-projects/search-agent")
        print()
        sys.exit(1)

    # 获取路径
    template_dir = Path(__file__).parent.resolve()
    target_dir = Path(sys.argv[1]).resolve()

    print(f"\n📂 模板源: {template_dir}")
    print(f"📁 目标: {target_dir}")

    try:
        # 验证目标目录
        validate_target_directory(target_dir)

        # 复制模板
        copy_template(template_dir, target_dir)

        # 创建额外文件
        create_additional_files(target_dir)

        # 打印下一步指导
        print_next_steps(target_dir)

    except KeyboardInterrupt:
        print("\n\n❌ 操作已取消")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ 错误: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
