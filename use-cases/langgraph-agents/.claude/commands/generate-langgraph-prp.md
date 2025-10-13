---
name: "generate-langgraph-prp"
description: "为 LangGraph AI 代理功能生成综合 PRP"
---

# Generate LangGraph Agent PRP

为基于 LangGraph 的 AI 代理功能开发生成上下文丰富、生产就绪的 PRP (Plan-Research-Process)。

## Usage

```bash
/generate-langgraph-prp PRPs/INITIAL.md
```

## Purpose

根据功能请求生成详细的实现计划 (PRP),包含所有必要的上下文、代码模式和验证步骤,用于构建 LangGraph AI 代理。

## 用户的功能用例

**输入**: $ARGUMENTS (INITIAL.md 文件路径)

## Execution Process

### 1. 📖 Read Feature Request

- 读取 INITIAL.md 文件内容
- 理解代理的核心功能需求
- 识别所需的工具、架构模式和集成点
- 分析测试和验证要求

### 2. 🔍 Research & Context Gathering

#### 代码库模式研究

```bash
# 搜索相似的代理实现
grep -r "create_react_agent\|StateGraph" examples/

# 查找工具集成示例
grep -r "@tool" examples/

# 检查状态管理模式
grep -r "TypedDict\|AgentState" examples/

# 查看测试模式
find tests/ -name "test_*.py"
```

#### LangGraph 文档研究

收集以下方面的文档和最佳实践:

1. **代理架构模式**
   - ReAct agents (工具使用)
   - Multi-agent systems (多代理协作)
   - Router agents (路由选择)
   - Reflection agents (自我批评)

2. **工具集成**
   - @tool 装饰器用法
   - ToolNode 配置
   - 工具错误处理
   - 自定义工具开发

3. **状态管理**
   - TypedDict 定义
   - Reducer 函数使用
   - 短期记忆 (会话内)
   - 长期记忆 (跨会话)

4. **模型提供商集成**
   - Anthropic Claude 配置
   - OpenAI GPT 配置
   - 模型选择策略
   - Token 管理

5. **结构化输出**
   - Pydantic 模型定义
   - with_structured_output() 方法
   - 输出验证

6. **测试和验证**
   - Pytest 测试模式
   - 异步测试
   - Mock 和 fixtures
   - 行为验证

#### Web 研究 (如需要)

如果功能需要特定工具或集成:

```bash
# 使用 WebSearch 工具研究
# 示例: "LangGraph Tavily search integration example"
# 示例: "LangGraph Pinecone vector store tutorial"
```

### 3. 📋 Review AI Documentation

检查 `PRPs/ai_docs/` 目录:

```bash
# 列出可用文档
ls -la PRPs/ai_docs/

# 如果存在相关文档,读取并整合到 PRP 中
```

用户可能添加了:
- 特定工具的 API 文档
- 自定义集成指南
- 领域特定知识库

### 4. 🏗️ Generate Comprehensive PRP

使用 `PRPs/templates/prp_langgraph_base.md` 作为基础模板,生成定制化的 PRP:

#### PRP 结构要求

```markdown
---
name: "功能名称"
description: "简短描述"
complexity: "Beginner/Intermediate/Advanced"
---

## Purpose
[清晰说明要构建什么]

## Why
- 解决的问题
- 启用的功能
- 提供的价值

## What
### 代理架构
- 代理类型 (ReAct/Multi-Agent/Router)
- 核心组件列表
- 工具集成清单
- 状态定义
- 结构化输出模式

### 成功标准
- [ ] 具体的可验证标准

## All Needed Context

### LangGraph 文档
```yaml
# 相关文档和概念
```

### 代码库模式
```yaml
- file: examples/xxx.py
  why: 说明相关性
```

### 额外上下文 (来自 ai_docs/)
```yaml
- file: PRPs/ai_docs/xxx.md
  why: 提供的上下文
```

## Implementation Blueprint

### Task 1: 项目设置
[详细的设置步骤]

### Task 2-N: 实现步骤
[每个任务的具体步骤,包含代码示例]

## Validation Loop

### Level 1: 语法和类型检查
```bash
mypy my_agent/ --strict
# 预期: 无类型错误
# 如果失败: [修复指导]
```

### Level 2: 单元测试
```bash
pytest tests/ -v --cov=my_agent
# 预期: 所有测试通过
# 如果失败: [调试指导]
```

### Level 3: 代理行为测试
[具体的行为测试场景]

### Level 4: LangSmith 追踪
[验证追踪和监控]

## Security Checklist
- [ ] API 密钥管理
- [ ] 输入验证
- [ ] 输出净化
- [ ] 速率限制

## Common Gotchas
[功能特定的常见陷阱和解决方案]

## Final Checklist
- [ ] 所有验证项
```

### 5. 📝 Save PRP File

将生成的 PRP 保存到 `PRPs/` 目录:

```bash
# 文件命名: PRPs/prp_<feature_name>.md
# 示例: PRPs/prp_web_search_agent.md
```

## Validation

命令确保:

1. **上下文完整性**
   - 所有引用的代码模式存在于代码库中
   - 文档链接有效且可访问
   - ai_docs/ 中的内容已整合

2. **实现可行性**
   - 实现任务具体且可操作
   - 代码示例语法正确
   - 验证循环全面且可执行

3. **LangGraph 特异性**
   - 包含正确的 LangGraph 模式
   - 工具集成方法准确
   - 状态管理遵循最佳实践
   - 测试策略适合代理开发

4. **验证可执行性**
   - 所有验证命令可由 Claude Code 执行
   - 失败场景包含清晰的修复指导
   - 成功标准明确且可测量

## Research Areas Checklist

在生成 PRP 前,研究以下领域:

- [ ] **代理架构**: ReAct/Multi-Agent/Router/Reflection 模式
- [ ] **工具定义**: @tool 装饰器,参数验证,错误处理
- [ ] **状态管理**: TypedDict,reducers,记忆模式
- [ ] **模型集成**: Anthropic/OpenAI 配置,token 管理
- [ ] **结构化输出**: Pydantic 模型,验证策略
- [ ] **测试模式**: Pytest 单元测试,行为测试,async 测试
- [ ] **安全实践**: API 密钥管理,输入验证,提示注入防护
- [ ] **常见陷阱**: Token 限制,InvalidUpdateError,递归限制
- [ ] **部署模式**: langgraph.json 配置,环境变量
- [ ] **监控调试**: LangSmith 集成,追踪配置

## Output

在 `PRPs/` 目录中创建一个综合的 PRP 文件,包含:

- ✅ 完整的功能描述和目标
- ✅ 所有必要的上下文和代码模式
- ✅ 逐步的实现任务 (Task 1, 2, 3...)
- ✅ LangGraph 特定的验证循环
- ✅ 安全最佳实践
- ✅ 常见陷阱和解决方案
- ✅ 清晰的成功标准

生成的 PRP 应该是自包含的,提供实现功能所需的所有信息,无需额外的外部研究。

## Example Command Flow

```bash
# 1. 创建功能请求
cat > PRPs/INITIAL.md << 'EOF'
# 构建网络搜索和计算代理
...功能需求...
EOF

# 2. 生成 PRP
/generate-langgraph-prp PRPs/INITIAL.md

# 3. 生成的 PRP 保存在
# PRPs/prp_web_search_calculator_agent.md

# 4. 执行 PRP
/execute-langgraph-prp PRPs/prp_web_search_calculator_agent.md
```

---

**重要**: 此命令专注于**研究和规划**,不执行实现。实际的代码生成和测试由 `/execute-langgraph-prp` 命令完成。
