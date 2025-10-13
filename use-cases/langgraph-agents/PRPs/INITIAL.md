# LangGraph Agent Feature Request - 示例

这是一个示例功能请求文件,展示如何描述你想要构建的 AI 代理。

## 代理用途

构建一个智能助手代理,能够执行网络搜索并进行数学计算,同时提供结构化的响应输出。

## 核心功能

### 1. 网络搜索集成

- 使用 Tavily 或 DuckDuckGo API 搜索网络信息
- 返回前 5 个最相关的结果
- 包含来源 URL 和摘要
- 处理搜索失败和网络错误

### 2. 数学计算工具

- 执行基础算术运算 (+, -, *, /)
- 处理复杂的数学表达式
- 支持括号和运算优先级
- 返回精确的数值结果
- 可配置小数精度

### 3. 对话记忆

- 短期记忆: 维护会话内的对话历史
- 上下文跟踪: 记住用户提供的信息
- 使用 MemorySaver 持久化状态
- 支持多轮对话

### 4. 结构化输出

- 使用 Pydantic 模型定义响应格式
- 确保输出符合预定义模式
- 包含字段验证

## 代理架构

**代理类型**: ReAct (Reasoning and Acting)

**推理模式**:
- 思考 → 行动 → 观察 → 思考 (循环)
- 决定何时使用工具
- 综合多个工具结果

**模型提供商**: Anthropic Claude 3.7 Sonnet

**为什么选择这个模型**:
- 强大的推理能力
- 优秀的工具使用
- 支持长上下文
- 快速响应时间

**记忆配置**:
- 短期记忆 (会话内): InMemorySaver
- Thread ID: 用于隔离不同用户会话
- 消息修剪: 保留最近 20 条消息

## 工具集成

### Tool 1: Web Search

```python
@tool
def web_search(query: str, max_results: int = 5) -> str:
    """在网络上搜索信息。

    Args:
        query: 搜索查询字符串
        max_results: 返回的最大结果数 (默认: 5)

    Returns:
        str: 格式化的搜索结果,包含标题、摘要和 URL
    """
    # 实现: 使用 Tavily API 或 DuckDuckGo
    pass
```

**功能要求**:
- 返回标题、摘要、URL
- 处理搜索失败
- 速率限制处理
- 结果排名和过滤

### Tool 2: Calculator

```python
class CalculatorInput(BaseModel):
    """计算器输入模式。"""
    expression: str = Field(description="数学表达式")
    precision: int = Field(default=2, ge=0, le=10)

@tool(args_schema=CalculatorInput)
def calculator(expression: str, precision: int = 2) -> float:
    """执行数学计算。

    Args:
        expression: 数学表达式 (例如: "2 + 2 * 3")
        precision: 小数精度 (0-10)

    Returns:
        float: 计算结果
    """
    # 实现: 使用安全的表达式求值
    pass
```

**安全要求**:
- 只允许安全的数学运算
- 拒绝执行代码
- 输入验证和净化
- 错误处理

## 结构化输出

```python
from pydantic import BaseModel, Field

class AgentResponse(BaseModel):
    """代理响应结构。"""
    answer: str = Field(description="代理的答案")
    sources: list[str] = Field(
        default_factory=list,
        description="来源 URL (如果使用了搜索)"
    )
    calculations: list[str] = Field(
        default_factory=list,
        description="执行的计算 (如果使用了计算器)"
    )
    confidence: float = Field(
        ge=0.0,
        le=1.0,
        description="置信度分数"
    )
    metadata: dict = Field(
        default_factory=dict,
        description="额外的元数据"
    )
```

**验证要求**:
- 所有必需字段都存在
- confidence 在 0-1 范围内
- sources 是有效的 URL
- 字段类型正确

## 测试要求

### 单元测试

1. **工具测试**
   - 测试搜索工具返回格式
   - 测试计算器准确性
   - 测试边缘情况和错误处理

2. **状态管理测试**
   - 测试消息历史保持
   - 测试线程隔离
   - 测试状态更新

### 集成测试

1. **代理行为测试**
   - 测试代理选择正确的工具
   - 测试多工具协调
   - 测试推理流程

2. **记忆测试**
   - 测试对话上下文保持
   - 测试多轮对话
   - 测试记忆修剪

### 端到端测试

1. **完整场景测试**
   - "搜索 Python 教程并计算 25 的平方根"
   - "我的名字是 Alice,搜索关于机器学习的信息"
   - "计算 (15 + 27) * 3,然后搜索结果的含义"

2. **错误恢复测试**
   - 搜索失败时的处理
   - 无效计算表达式的处理
   - 网络错误的处理

## 安全考虑

### 1. API 密钥管理

- 所有密钥存储在 .env 文件中
- .env 文件添加到 .gitignore
- 使用 python-dotenv 加载
- 生产环境使用密钥管理服务

### 2. 输入验证

- 验证搜索查询长度
- 净化数学表达式
- 拒绝恶意输入
- 使用 Pydantic 验证所有参数

### 3. 提示注入防护

- 系统提示明确角色限制
- 验证用户输入
- 使用结构化输出限制格式
- 不允许覆盖系统指令

### 4. 速率限制

- 限制 API 调用频率
- 实现重试机制
- 处理速率限制错误
- 监控使用量

## 常见使用场景

### 场景 1: 研究和计算

```
用户: "搜索纽约的天气,如果温度超过 20°C,计算 20 * 1.8 + 32"
```

**预期行为**:
1. 使用搜索工具查找纽约天气
2. 提取温度信息
3. 判断是否需要计算
4. 使用计算器转换温度
5. 提供综合答案

### 场景 2: 连续查询

```
用户: "搜索 Python 教程"
用户: "计算完成该教程需要的天数,如果每天学习 2 小时,总共 40 小时"
```

**预期行为**:
1. 第一轮: 搜索并返回教程
2. 记住第一轮的上下文
3. 第二轮: 使用计算器计算天数
4. 综合两轮信息回答

### 场景 3: 复杂任务

```
用户: "搜索最新的 AI 新闻,计算 15% 的 200,告诉我两者之间的关系"
```

**预期行为**:
1. 并行或顺序使用两个工具
2. 综合结果
3. 提供有见解的答案

## 验证要求

### 功能验证

- [ ] 代理正确响应简单查询
- [ ] 搜索工具返回有效结果
- [ ] 计算器提供准确计算
- [ ] 代理能协调多个工具
- [ ] 对话记忆正常工作

### 性能验证

- [ ] 响应时间 < 5 秒 (大多数查询)
- [ ] 搜索结果相关性高
- [ ] 计算准确率 100%
- [ ] 内存使用合理
- [ ] Token 使用优化

### 质量验证

- [ ] 所有 Pytest 测试通过
- [ ] 代码覆盖率 > 80%
- [ ] 类型检查通过 (mypy)
- [ ] 无安全漏洞
- [ ] 文档完整

### 用户体验验证

- [ ] 错误消息清晰
- [ ] 响应格式一致
- [ ] 工具使用透明
- [ ] 推理过程可理解

## 期望输出示例

### 示例 1: 搜索和计算

```
用户: "搜索 Python 教程,并计算学习 100 小时需要多少周,如果每周学习 10 小时"

代理: 我会帮你搜索 Python 教程,并计算学习时间。

[使用搜索工具]
找到以下 Python 教程:
1. Python.org 官方教程
2. Real Python 完整指南
3. ...

[使用计算器]
计算: 100 / 10 = 10 周

综合答案: 我找到了几个优质的 Python 教程。如果你每周学习 10 小时,
完成 100 小时的学习需要 10 周时间。推荐从 Python.org 官方教程开始。
```

**结构化输出**:
```json
{
  "answer": "找到优质 Python 教程,100 小时学习需要 10 周...",
  "sources": [
    "https://python.org/tutorial",
    "https://realpython.com/..."
  ],
  "calculations": ["100 / 10 = 10"],
  "confidence": 0.95,
  "metadata": {
    "tools_used": ["web_search", "calculator"],
    "execution_time_ms": 2500
  }
}
```

## 成功标准

### 必须满足 (Must Have)

- ✅ 代理能正确使用搜索和计算工具
- ✅ 对话记忆工作正常
- ✅ 所有测试通过
- ✅ 安全措施实施
- ✅ 错误处理完善

### 应该满足 (Should Have)

- ✅ LangSmith 追踪集成
- ✅ 结构化输出验证
- ✅ 性能优化
- ✅ 日志记录
- ✅ 文档完整

### 可以满足 (Nice to Have)

- ⭕ 多语言支持
- ⭕ 向量数据库集成 (RAG)
- ⭕ 更多工具集成
- ⭕ Web UI
- ⭕ 流式输出

---

**下一步**:

1. 使用此 INITIAL.md 生成详细的 PRP:
   ```bash
   /generate-langgraph-prp PRPs/INITIAL.md
   ```

2. 执行生成的 PRP:
   ```bash
   /execute-langgraph-prp PRPs/prp_search_calculator_agent.md
   ```

3. 测试和验证代理功能

4. 根据需要迭代改进
