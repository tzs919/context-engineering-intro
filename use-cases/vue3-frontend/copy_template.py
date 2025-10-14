#!/usr/bin/env python3
"""
Vue 3 Frontend Template Copier

This script copies the complete Vue 3 frontend template to a target directory,
including all necessary files for context engineering with Vue 3 development.

Usage:
    python copy_template.py /path/to/target/directory

Features:
- Copies entire template directory structure
- Preserves file permissions and timestamps
- Creates target directory if it doesn't exist
- Provides detailed progress feedback
- Error handling and validation
"""

import os
import sys
import shutil
import argparse
from pathlib import Path
from typing import Optional

# Template information
TEMPLATE_NAME = "Vue 3 Frontend Context Engineering Template"
TEMPLATE_VERSION = "1.0.0"
REQUIRED_FILES = [
    "CLAUDE.md",
    ".claude/commands/generate-vue3-prp.md",
    ".claude/commands/execute-vue3-prp.md",
    "PRPs/templates/prp_vue3_base.md",
    "PRPs/INITIAL.md",
    "README.md",
    "copy_template.py"
]

def print_header():
    """Print script header with template information."""
    print("=" * 60)
    print(f"🚀 {TEMPLATE_NAME}")
    print(f"📦 Version: {TEMPLATE_VERSION}")
    print("=" * 60)
    print()

def print_usage():
    """Print detailed usage instructions."""
    print("📖 使用方法:")
    print("  python copy_template.py <target_directory>")
    print()
    print("📝 示例:")
    print("  python copy_template.py /home/user/my-vue-project")
    print("  python copy_template.py ../new-frontend-project")
    print("  python copy_template.py ~/projects/vue-app")
    print()
    print("✨ 这将复制完整的 Vue 3 前端模板，包括:")
    print("  • Vue 3 + TypeScript + Vuetify 开发规则")
    print("  • 专用的 PRP 生成和执行命令")
    print("  • 预配置的基础 PRP 模板")
    print("  • 工作示例和测试模板")
    print("  • 完整的使用文档")
    print()

def validate_source_directory() -> Path:
    """Validate that we're running from the correct template directory."""
    script_dir = Path(__file__).parent.resolve()

    # Check if we're in a Vue 3 template directory
    required_files = [script_dir / file for file in REQUIRED_FILES]
    missing_files = [f for f in required_files if not f.exists()]

    if missing_files:
        print("❌ 错误: 模板文件不完整")
        print("缺失的文件:")
        for file in missing_files:
            print(f"  • {file.relative_to(script_dir)}")
        print()
        print("请确保在完整的 Vue 3 模板目录中运行此脚本。")
        sys.exit(1)

    print(f"✅ 源目录验证通过: {script_dir}")
    return script_dir

def validate_target_directory(target_path: str) -> Path:
    """Validate and prepare the target directory."""
    target = Path(target_path).resolve()

    # Check if target exists and is not empty
    if target.exists():
        if target.is_file():
            print(f"❌ 错误: 目标路径是一个文件: {target}")
            sys.exit(1)

        if list(target.iterdir()):
            response = input(f"⚠️  目标目录非空: {target}\n继续会覆盖现有文件。是否继续? [y/N]: ")
            if response.lower() not in ['y', 'yes', '是']:
                print("操作已取消。")
                sys.exit(0)

    # Create target directory if it doesn't exist
    target.mkdir(parents=True, exist_ok=True)
    print(f"✅ 目标目录准备完成: {target}")
    return target

def copy_template(source_dir: Path, target_dir: Path) -> None:
    """Copy the complete template to target directory."""
    print("\n📂 开始复制模板文件...")

    # Files and directories to exclude from copying
    exclude_patterns = {
        '__pycache__',
        '*.pyc',
        '.DS_Store',
        'Thumbs.db',
        '.git',
        '.gitignore',
        'node_modules',
        'dist',
        'build',
        '.vscode',
        '.idea'
    }

    def should_exclude(path: Path) -> bool:
        """Check if a path should be excluded from copying."""
        name = path.name
        for pattern in exclude_patterns:
            if pattern.startswith('*.') and name.endswith(pattern[1:]):
                return True
            elif name == pattern:
                return True
        return False

    copied_files = 0
    copied_dirs = 0

    try:
        # Walk through source directory and copy files
        for source_path in source_dir.rglob('*'):
            if should_exclude(source_path):
                continue

            # Calculate relative path from source
            relative_path = source_path.relative_to(source_dir)
            target_path = target_dir / relative_path

            if source_path.is_dir():
                # Create directory
                target_path.mkdir(parents=True, exist_ok=True)
                copied_dirs += 1
                print(f"📁 {relative_path}/")
            else:
                # Copy file
                shutil.copy2(source_path, target_path)
                copied_files += 1
                print(f"📄 {relative_path}")

    except Exception as e:
        print(f"\n❌ 复制过程中发生错误: {e}")
        sys.exit(1)

    print(f"\n✅ 复制完成! 共复制 {copied_files} 个文件，{copied_dirs} 个目录")

def create_project_info(target_dir: Path) -> None:
    """Create a project information file in the target directory."""
    info_content = f"""# Vue 3 Frontend Project

This project was created using the Vue 3 Frontend Context Engineering Template.

## Template Information

- **Template**: {TEMPLATE_NAME}
- **Version**: {TEMPLATE_VERSION}
- **Created**: {Path().cwd()}
- **Target**: {target_dir}

## Quick Start

1. **Read the documentation**: Start with README.md
2. **Understand the workflow**: Review the 3-step PRP process
3. **Create your first feature**: Use `/generate-vue3-prp INITIAL.md`

## Next Steps

1. Install dependencies: `pnpm install`
2. Start development server: `pnpm dev`
3. Create your first Vue 3 component using the PRP workflow
4. Run tests: `pnpm test:unit` and `pnpm test:e2e`

## Important Files

- `CLAUDE.md`: Vue 3 development rules and best practices
- `.claude/commands/`: PRP generation and execution commands
- `PRPs/templates/prp_vue3_base.md`: Base template for Vue 3 features
- `PRPs/INITIAL.md`: Example feature request
- `examples/`: Working Vue 3 code examples

Happy coding with Vue 3! 🚀
"""

    info_file = target_dir / "PROJECT_INFO.md"
    info_file.write_text(info_content, encoding='utf-8')
    print(f"📋 项目信息文件已创建: {info_file.name}")

def print_completion_message(target_dir: Path) -> None:
    """Print completion message with next steps."""
    print("\n" + "=" * 60)
    print("🎉 Vue 3 前端模板复制成功!")
    print("=" * 60)
    print()
    print("📁 模板已复制到:")
    print(f"   {target_dir}")
    print()
    print("🚀 接下来的步骤:")
    print("1. 进入项目目录:")
    print(f"   cd {target_dir}")
    print()
    print("2. 阅读使用文档:")
    print("   cat README.md")
    print()
    print("3. 了解 PRP 工作流程:")
    print("   查看 3 步骤过程: 功能请求 → 生成 PRP → 执行实现")
    print()
    print("4. 开始你的第一个 Vue 3 功能:")
    print("   /generate-vue3-prp PRPs/INITIAL.md")
    print()
    print("📚 重要文件:")
    print("   • CLAUDE.md - Vue 3 开发规则")
    print("   • PRPs/templates/prp_vue3_base.md - 基础 PRP 模板")
    print("   • examples/ - Vue 3 代码示例")
    print()
    print("💡 提示: 这个模板专为 Vue 3 + TypeScript + Vuetify + pnpm + Playwright 优化")
    print("🎯 目标: 让 Vue 3 前端开发应用上下文工程变得简单而高效")
    print()
    print("Happy Vue 3 Development! ✨")

def main():
    """Main function to execute the template copying process."""
    parser = argparse.ArgumentParser(
        description=f'{TEMPLATE_NAME} - Copy template to target directory',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        'target_directory',
        nargs='?',
        help='Target directory to copy the template to'
    )
    parser.add_argument(
        '--version',
        action='version',
        version=f'Vue 3 Template Copier {TEMPLATE_VERSION}'
    )

    args = parser.parse_args()

    print_header()

    # If no target directory provided, show usage
    if not args.target_directory:
        print_usage()
        sys.exit(0)

    try:
        # Validate source directory
        source_dir = validate_source_directory()

        # Validate and prepare target directory
        target_dir = validate_target_directory(args.target_directory)

        # Copy template
        copy_template(source_dir, target_dir)

        # Create project information file
        create_project_info(target_dir)

        # Print completion message
        print_completion_message(target_dir)

    except KeyboardInterrupt:
        print("\n\n⚠️  操作被用户中断。")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ 发生未知错误: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()