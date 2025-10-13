#!/usr/bin/env python3
"""
Spring Boot 模板复制脚本

将 Spring Boot 上下文工程模板复制到目标项目目录。
包含所有必需的文件:CLAUDE.md, 命令, PRPs, 示例等。

使用方法:
    python copy_template.py /path/to/target/directory
"""

import os
import sys
import shutil
from pathlib import Path


def print_usage():
    """打印使用说明"""
    print("用法: python copy_template.py <目标目录>")
    print()
    print("示例:")
    print("  python copy_template.py /home/user/my-springboot-project")
    print("  python copy_template.py ../my-new-project")


def copy_template(source_dir: Path, target_dir: Path):
    """
    复制模板到目标目录

    Args:
        source_dir: 模板源目录
        target_dir: 目标目录
    """
    # 要复制的文件和目录
    items_to_copy = [
        'CLAUDE.md',
        '.claude/',
        'PRPs/',
        'examples/',
        'README.md'
    ]

    # 创建目标目录
    target_dir.mkdir(parents=True, exist_ok=True)

    copied_count = 0

    for item in items_to_copy:
        source_path = source_dir / item
        target_path = target_dir / item

        if not source_path.exists():
            print(f"⚠️  跳过不存在的项: {item}")
            continue

        try:
            if source_path.is_file():
                # 复制文件
                shutil.copy2(source_path, target_path)
                print(f"✓ 已复制文件: {item}")
                copied_count += 1
            elif source_path.is_dir():
                # 复制目录
                if target_path.exists():
                    shutil.rmtree(target_path)
                shutil.copytree(source_path, target_path)
                print(f"✓ 已复制目录: {item}")
                copied_count += 1
        except Exception as e:
            print(f"✗ 复制失败 {item}: {e}")

    return copied_count


def main():
    """主函数"""
    # 检查命令行参数
    if len(sys.argv) < 2:
        print("错误: 缺少目标目录参数\n")
        print_usage()
        sys.exit(1)

    if sys.argv[1] in ['-h', '--help', 'help']:
        print_usage()
        sys.exit(0)

    # 获取源目录(脚本所在目录)
    source_dir = Path(__file__).parent.resolve()

    # 获取目标目录
    target_path = sys.argv[1]
    target_dir = Path(target_path).resolve()

    print("=" * 60)
    print("Spring Boot 上下文工程模板复制工具")
    print("=" * 60)
    print(f"源目录: {source_dir}")
    print(f"目标目录: {target_dir}")
    print()

    # 确认操作
    if target_dir.exists():
        print(f"⚠️  目标目录已存在: {target_dir}")
        response = input("是否继续? (y/N): ")
        if response.lower() != 'y':
            print("操作已取消")
            sys.exit(0)
        print()

    # 执行复制
    print("开始复制模板文件...")
    print()

    try:
        copied_count = copy_template(source_dir, target_dir)

        print()
        print("=" * 60)
        print(f"✓ 模板复制完成! 共复制 {copied_count} 个项目")
        print("=" * 60)
        print()
        print("下一步:")
        print(f"1. cd {target_dir}")
        print("2. 查看 README.md 了解如何使用模板")
        print("3. 编辑 PRPs/INITIAL.md 定义你的功能需求")
        print("4. 运行 /generate-springboot-prp PRPs/INITIAL.md")
        print()
        print("Happy coding! 🚀")

    except Exception as e:
        print()
        print("=" * 60)
        print(f"✗ 复制失败: {e}")
        print("=" * 60)
        sys.exit(1)


if __name__ == '__main__':
    main()
