## FEATURE:

- Pydantic AI 代理,将另一个 Pydantic AI 代理作为工具。
- 主代理的研究代理,然后子代理的电子邮件草稿代理。
- 用于与代理交互的 CLI。
- 电子邮件草稿代理使用 Gmail,研究代理使用 Brave API。

## EXAMPLES:

在 `examples/` 文件夹中,有一个 README 供您阅读,以了解示例的全部内容以及在为上述功能创建文档时如何构建您自己的 README。

- `examples/cli.py` - 使用此作为创建 CLI 的模板
- `examples/agent/` - 通读这里的所有文件,了解创建支持不同提供商和 LLM 的 Pydantic AI 代理、处理代理依赖关系以及向代理添加工具的最佳实践。

不要直接复制这些示例中的任何内容,它们是完全不同的项目。但使用它们作为灵感和最佳实践。

## DOCUMENTATION:

Pydantic AI 文档: https://ai.pydantic.dev/

## OTHER CONSIDERATIONS:

- 包括 .env.example,README 以及设置说明,包括如何配置 Gmail 和 Brave。
- 在 README 中包括项目结构。
- 虚拟环境已经设置了必要的依赖项。
- 使用 python_dotenv 和 load_env() 处理环境变量