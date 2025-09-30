# MCP 服务器构建器 - Context Engineering 用例

此用例演示如何使用 **Context Engineering** 和 **PRP（产品需求提示）流程**构建生产就绪的模型上下文协议（MCP）服务器。它提供了一个经过验证的模板和工作流，用于创建具有 GitHub OAuth 身份验证、数据库集成和 Cloudflare Workers 部署的 MCP 服务器。

> PRP 是 PRD + 精选代码库智能 + 智能体/运行手册——AI 在第一次尝试时就能合理交付生产就绪代码所需的最小可行数据包。

## 🚀 快速开始

### 先决条件

- 已安装 Node.js 和 npm
- Cloudflare 账户（免费层可用）
- 用于 OAuth 的 GitHub 账户
- PostgreSQL 数据库（本地或托管）

### 步骤 1：设置你的项目

```bash
# 克隆 Context Engineering 仓库
git clone https://github.com/coleam00/Context-Engineering-Intro.git
cd Context-Engineering-Intro/use-cases/mcp-server

# 将模板复制到新项目目录
python copy_template.py my-mcp-server-project

# 导航到新项目
cd my-mcp-server-project

# 安装依赖项
npm install

# 全局安装 Wrangler CLI
npm install -g wrangler

# 使用 Cloudflare 进行身份验证
wrangler login
```

**copy_template.py 的作用：**
- 复制所有模板文件，除了构建产物（遵守 .gitignore）
- 将 README.md 重命名为 README_TEMPLATE.md（以便你可以创建自己的 README）
- 包含所有源代码、示例、测试和配置文件
- 保留完整的 Context Engineering 设置

## 🎯 你将学到什么

此用例教你如何：

- **使用 PRP 流程**系统地构建复杂的 MCP 服务器
- **利用专门的 Context Engineering**进行 MCP 开发
- **遵循经过验证的模式**来自生产就绪的 MCP 服务器模板
- **实现安全身份验证**，使用 GitHub OAuth 和基于角色的访问
- **部署到 Cloudflare Workers**，具有监控和错误处理

## 📋 工作原理 - MCP 服务器的 PRP 流程

> **步骤 1 是上面的快速入门设置** - 克隆仓库、复制模板、安装依赖项、设置 Wrangler

### 步骤 2：定义你的 MCP 服务器

编辑 `PRPs/INITIAL.md` 来描述你的特定 MCP 服务器需求：

```markdown
## 功能：
我们想创建一个天气 MCP 服务器，提供实时天气数据，
具有缓存和速率限制功能。

## 附加功能：
- 与 OpenWeatherMap API 集成
- Redis 缓存以提高性能
- 每个用户的速率限制
- 历史天气数据访问
- 位置搜索和自动完成

## 其他考虑：
- 外部服务的 API 密钥管理
- API 失败的适当错误处理
- 位置查询的坐标验证
```

### 步骤 3：生成你的 PRP

使用专门的 MCP PRP 命令创建全面的实现计划：

```bash
/prp-mcp-create INITIAL.md
```

**这会做什么：**
- 读取你的功能请求
- 研究现有的 MCP 代码库模式
- 研究身份验证和数据库集成模式
- 在 `PRPs/your-server-name.md` 中创建全面的 PRP
- 包含所有上下文、验证循环和逐步任务

> 在生成 PRP 后验证所有内容非常重要！使用 PRP 框架，你应该成为流程的一部分，以确保所有上下文的质量！执行的好坏取决于你的 PRP。使用 /prp-mcp-create 作为一个可靠的起点。

### 步骤 4：执行你的 PRP

使用专门的 MCP 执行命令构建你的服务器：

```bash
/prp-mcp-execute PRPs/your-server-name.md
```

**这会做什么：**
- 加载包含所有上下文的完整 PRP
- 使用 TodoWrite 创建详细的实现计划
- 按照经过验证的模式实现每个组件
- 运行全面验证（TypeScript、测试、部署）
- 确保你的 MCP 服务器端到端工作

### 步骤 5：配置环境

```bash
# 创建环境文件
cp .dev.vars.example .dev.vars

# 使用你的凭据编辑 .dev.vars
# - GitHub OAuth 应用凭据
# - 数据库连接字符串
# - Cookie 加密密钥
```

### 步骤 6：测试和部署

```bash
# 本地测试
wrangler dev --config <your wrangler config (.jsonc)>

# 使用 MCP Inspector 测试
npx @modelcontextprotocol/inspector@latest
# 连接到：http://localhost:8792/mcp

# 部署到生产环境
wrangler deploy
```

## 🏗️ MCP 特定的 Context Engineering

此用例包含专门为 MCP 服务器开发设计的 Context Engineering 组件：

### 专门的斜杠命令

位于 `.claude/commands/`：

- **`/prp-mcp-create`** - 专门为 MCP 服务器生成 PRP
- **`/prp-mcp-execute`** - 使用全面验证执行 MCP PRP

这些是根目录 `.claude/commands/` 中通用命令的专门版本，但针对 MCP 开发模式进行了定制。

### 专门的 PRP 模板

模板 `PRPs/templates/prp_mcp_base.md` 包括：

- **MCP 特定模式**用于工具注册和身份验证
- **Cloudflare Workers 配置**用于部署
- **GitHub OAuth 集成**模式
- **数据库安全性**和 SQL 注入保护
- **全面的验证循环**，从 TypeScript 到生产

### AI 文档

`PRPs/ai_docs/` 文件夹包含：

- **`mcp_patterns.md`** - 核心 MCP 开发模式和安全实践
- **`claude_api_usage.md`** - 如何与 Anthropic 的 API 集成以实现 LLM 驱动的功能

## 🔧 模板架构

此模板提供了一个完整的、生产就绪的 MCP 服务器，具有：

### 核心组件

```
src/
├── index.ts                 # 主身份验证 MCP 服务器
├── index_sentry.ts         # 具有 Sentry 监控的版本
├── simple-math.ts          # 基本 MCP 示例（无身份验证）
├── github-handler.ts       # 完整的 GitHub OAuth 实现
├── database.ts             # 具有安全模式的 PostgreSQL
├── utils.ts                # OAuth 辅助函数和工具
├── workers-oauth-utils.ts  # HMAC 签名的 cookie 系统
└── tools/                  # 模块化工具注册系统
    └── register-tools.ts   # 中央工具注册表
```

### 示例工具

`examples/` 文件夹展示了如何创建 MCP 工具：

- **`database-tools.ts`** - 具有适当模式的示例数据库工具
- **`database-tools-sentry.ts`** - 具有 Sentry 监控的相同工具

### 关键功能

- **🔐 GitHub OAuth** - 完整的身份验证流程，具有基于角色的访问
- **🗄️ 数据库集成** - 具有连接池和安全性的 PostgreSQL
- **🛠️ 模块化工具** - 具有中央注册的清晰关注点分离
- **☁️ Cloudflare Workers** - 具有持久对象的全球边缘部署
- **📊 监控** - 可选的 Sentry 集成用于生产
- **🧪 测试** - 从 TypeScript 到部署的全面验证

## 🔍 要理解的关键文件

要完全理解此用例，请检查这些文件：

### Context Engineering 组件

- **`PRPs/templates/prp_mcp_base.md`** - 专门的 MCP PRP 模板
- **`.claude/commands/prp-mcp-create.md`** - MCP 特定的 PRP 生成
- **`.claude/commands/prp-mcp-execute.md`** - MCP 特定的执行

### 实现模式

- **`src/index.ts`** - 具有身份验证的完整 MCP 服务器
- **`examples/database-tools.ts`** - 工具创建和注册模式
- **`src/tools/register-tools.ts`** - 模块化工具注册系统

### 配置与部署

- **`wrangler.jsonc`** - Cloudflare Workers 配置
- **`.dev.vars.example`** - 环境变量模板
- **`CLAUDE.md`** - 实现指南和模式

## 📈 成功指标

当你成功使用此流程时，你将实现：

- **快速实现** - 以最少的迭代快速拥有 MCP 服务器
- **生产就绪** - 安全身份验证、监控和错误处理
- **可扩展架构** - 清晰的关注点分离和模块化设计
- **全面测试** - 从 TypeScript 到生产部署的验证

## 🤝 贡献

此用例展示了 Context Engineering 在复杂软件开发中的力量。要改进它：

1. **添加新的 MCP 服务器示例**以展示不同的模式
2. **增强 PRP 模板**，提供更全面的上下文
3. **改进验证循环**以更好地检测错误
4. **记录边缘情况**和常见陷阱

目标是通过全面的 Context Engineering 使 MCP 服务器开发可预测且成功。

---

**准备好构建你的 MCP 服务器了吗？** 按照上面的完整流程：使用复制模板设置你的项目，配置你的环境，在 `PRPs/INITIAL.md` 中定义你的需求，然后生成并执行你的 PRP 来构建你的生产就绪 MCP 服务器。