name: "基础 PRP 模板 v2 - 上下文丰富且带验证循环"
description: |

## 目的
为 AI 智能体优化的模板，用于实现功能，提供足够的上下文和自我验证能力，通过迭代改进实现可工作的代码。

## 核心原则
1. **上下文为王**：包含所有必要的文档、示例和注意事项
2. **验证循环**：提供 AI 可运行和修复的可执行测试/代码检查
3. **信息密集**：使用代码库中的关键字和模式
4. **渐进式成功**：从简单开始，验证，然后增强
5. **全局规则**：务必遵守 CLAUDE.md 中的所有规则

---

## 目标
[需要构建什么 - 具体说明最终状态和期望]

## 原因
- [业务价值和用户影响]
- [与现有功能的集成]
- [解决了什么问题以及为谁解决]

## 内容
[用户可见的行为和技术要求]

### 成功标准
- [ ] [具体可衡量的结果]

## 所有必需的上下文

### 文档与参考资料（列出实现功能所需的所有上下文）
```yaml
# 必读 - 将这些包含在你的上下文窗口中
- url: [官方 API 文档 URL]
  why: [你需要的特定章节/方法]

- file: [path/to/example.py]
  why: [要遵循的模式，要避免的陷阱]

- doc: [库文档 URL]
  section: [关于常见陷阱的特定章节]
  critical: [防止常见错误的关键见解]

- docfile: [PRPs/ai_docs/file.md]
  why: [用户粘贴到项目中的文档]

```

### 当前代码库结构树（在项目根目录运行 `tree` 命令）以获取代码库概览
```bash

```

### 期望的代码库结构树与待添加文件及文件职责
```bash

```

### 我们代码库的已知陷阱与库的特性
```python
# 关键：[库名称] 需要 [特定设置]
# 示例：FastAPI 需要异步函数作为端点
# 示例：此 ORM 不支持超过 1000 条记录的批量插入
# 示例：我们使用 pydantic v2 且
```

## 实现蓝图

### 数据模型和结构

创建核心数据模型，我们确保类型安全和一致性。
```python
示例：
 - orm 模型
 - pydantic 模型
 - pydantic schemas
 - pydantic validators

```

### 待完成任务列表，按应完成的顺序列出

```yaml
任务 1：
MODIFY src/existing_module.py:
  - FIND pattern: "class OldImplementation"
  - INJECT after line containing "def __init__"
  - PRESERVE existing method signatures

CREATE src/new_feature.py:
  - MIRROR pattern from: src/similar_feature.py
  - MODIFY class name and core logic
  - KEEP error handling pattern identical

...(...)

任务 N：
...

```


### 根据需要为每个任务添加伪代码
```python

# 任务 1
# 带有关键细节的伪代码，不要编写完整代码
async def new_feature(param: str) -> Result:
    # 模式：始终先验证输入（参见 src/validators.py）
    validated = validate_input(param)  # 抛出 ValidationError

    # 陷阱：此库需要连接池
    async with get_connection() as conn:  # 参见 src/db/pool.py
        # 模式：使用现有的重试装饰器
        @retry(attempts=3, backoff=exponential)
        async def _inner():
            # 关键：如果 >10 req/sec，API 返回 429
            await rate_limiter.acquire()
            return await external_api.call(validated)

        result = await _inner()

    # 模式：标准化响应格式
    return format_response(result)  # 参见 src/utils/responses.py
```

### 集成点
```yaml
DATABASE:
  - migration: "向 users 表添加列 'feature_enabled'"
  - index: "CREATE INDEX idx_feature_lookup ON users(feature_id)"

CONFIG:
  - add to: config/settings.py
  - pattern: "FEATURE_TIMEOUT = int(os.getenv('FEATURE_TIMEOUT', '30'))"

ROUTES:
  - add to: src/api/routes.py
  - pattern: "router.include_router(feature_router, prefix='/feature')"
```

## 验证循环

### 级别 1：语法与风格
```bash
# 首先运行这些 - 在继续之前修复任何错误
ruff check src/new_feature.py --fix  # 自动修复可能的问题
mypy src/new_feature.py              # 类型检查

# 预期：无错误。如果有错误，阅读错误并修复。
```

### 级别 2：每个新功能/文件/函数的单元测试，使用现有测试模式
```python
# 创建包含以下测试用例的 test_new_feature.py：
def test_happy_path():
    """基本功能正常工作"""
    result = new_feature("valid_input")
    assert result.status == "success"

def test_validation_error():
    """无效输入引发 ValidationError"""
    with pytest.raises(ValidationError):
        new_feature("")

def test_external_api_timeout():
    """优雅地处理超时"""
    with mock.patch('external_api.call', side_effect=TimeoutError):
        result = new_feature("valid")
        assert result.status == "error"
        assert "timeout" in result.message
```

```bash
# 运行并迭代直到通过：
uv run pytest test_new_feature.py -v
# 如果失败：阅读错误，理解根本原因，修复代码，重新运行（永远不要通过模拟来通过测试）
```

### 级别 3：集成测试
```bash
# 启动服务
uv run python -m src.main --dev

# 测试端点
curl -X POST http://localhost:8000/feature \
  -H "Content-Type: application/json" \
  -d '{"param": "test_value"}'

# 预期：{"status": "success", "data": {...}}
# 如果出错：检查 logs/app.log 中的日志以获取堆栈跟踪
```

## 最终验证清单
- [ ] 所有测试通过：`uv run pytest tests/ -v`
- [ ] 无代码检查错误：`uv run ruff check src/`
- [ ] 无类型错误：`uv run mypy src/`
- [ ] 手动测试成功：[特定的 curl/命令]
- [ ] 错误情况得到优雅处理
- [ ] 日志内容丰富但不冗长
- [ ] 必要时更新文档

---

## 要避免的反模式
- ❌ 当现有模式有效时，不要创建新模式
- ❌ 不要因为"应该可以工作"而跳过验证
- ❌ 不要忽略失败的测试 - 修复它们
- ❌ 不要在异步上下文中使用同步函数
- ❌ 不要硬编码应该是配置的值
- ❌ 不要捕获所有异常 - 要具体