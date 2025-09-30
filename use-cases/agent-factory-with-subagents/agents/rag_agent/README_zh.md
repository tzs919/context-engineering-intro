# 🔍 语义搜索智能体

一个由 Pydantic AI 和带有 PGVector 的 PostgreSQL 驱动的智能知识库搜索系统。该智能体提供语义搜索和混合搜索功能，具有自动策略选择和结果摘要功能。

## 功能特性

- **语义搜索**：使用嵌入向量的纯向量相似度搜索
- **混合搜索**：结合语义和关键词匹配以获得精确结果
- **智能策略选择**：智能体自动选择最佳搜索方法
- **结果摘要**：从搜索结果生成连贯的见解
- **交互式 CLI**：具有实时流式传输的丰富命令行界面
- **多提供商支持**：适用于任何 OpenAI 兼容 API（OpenAI、Gemini、Ollama 等）

## 先决条件

- Python 3.10+
- 带有 PGVector 扩展的 PostgreSQL
- LLM API 密钥（OpenAI、Gemini、Ollama、Groq 或任何 OpenAI 兼容提供商）
- 包含文档和块的现有数据库（提供了模式）

## 安装

1. **克隆或复制智能体目录**：
```bash
cd agents/rag_agent
```

2. **安装依赖项**：
```bash
pip install -r requirements.txt
```

3. **使用 PGVector 设置 PostgreSQL**：
```bash
# 最简单：如果你使用 Supabase/Postgres 等平台，在 SQL 编辑器中运行 SQL

# 或使用 psql 运行模式
psql -d your_database -f sql/schema.sql
```

4. **配置环境变量**：
```bash
cp .env.example .env
# 使用你的凭据编辑 .env
```

5. **将文档导入数据库**：
```bash
# 在运行智能体之前需要此步骤
# 它将处理文档并生成嵌入向量
python -m ingestion.ingest --documents documents/
```

## 配置

### 必需的环境变量

- `DATABASE_URL`：带有 PGVector 的 PostgreSQL 连接字符串
- `LLM_PROVIDER`：提供商名称（openai、anthropic、ollama 等）
- `LLM_API_KEY`：你的 LLM 提供商 API 密钥
- `LLM_MODEL`：要使用的模型（例如 gpt-4.1-mini、gemini-2.5-flash）
- `LLM_BASE_URL`：API 基础 URL（默认：https://api.openai.com/v1）
- `EMBEDDING_MODEL`：要使用的嵌入模型（例如 text-embedding-3-small、text-embedding-3-large）

## 使用

### 命令行界面

运行交互式 CLI：
```bash
python -m cli
```

CLI 提供：
- 实时流式响应
- 工具执行可见性
- 会话持久化
- 用户偏好管理

### 可用命令

- `help` - 显示可用命令
- `info` - 显示系统配置
- `clear` - 清除屏幕
- `set <key>=<value>` - 设置偏好（例如 `set text_weight=0.5`）
- `exit/quit` - 退出应用程序

## 搜索策略

智能体智能地在两种搜索策略之间选择：

### 语义搜索
最适合概念性查询和查找相关内容：
- "与机器学习相似的概念"
- "关于人工智能的想法"
- "与神经网络相关"

### 混合搜索
最适合特定事实和技术术语：
- "OpenAI GPT-4 规格"
- "NASDAQ:NVDA 股价"
- "Sam Altman 的具体引用"

智能体根据你的查询自动选择适当的策略，或者你可以在提示中明确请求特定的搜索类型。

## 数据库设置

### 模式概述

- **documents**：存储带有元数据的完整文档
- **chunks**：存储带有嵌入向量的文档块
- **match_chunks()**：用于语义搜索的函数
- **hybrid_search()**：用于组合搜索的函数

## 开发

### 运行测试
```bash
pytest tests/
```

### 代码格式化
```bash
black .
ruff check .
```

### 项目结构
```
semantic_search_agent/
├── agent.py           # 主智能体实现
├── cli.py            # 命令行界面
├── dependencies.py   # 智能体依赖项
├── providers.py      # 模型提供商
├── prompts.py        # 系统提示
├── settings.py       # 配置
├── tools.py          # 搜索工具
├── ingestion/        # 文档导入流水线
├── sql/              # 数据库模式
└── documents/        # 示例文档
```