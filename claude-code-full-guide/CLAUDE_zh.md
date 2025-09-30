# CLAUDE.md

本文件为 Claude Code 在此代码库中处理 Python 代码时提供全面指导。

## 核心开发哲学

### KISS(保持简单、愚蠢)

简单性应该是设计的关键目标。只要可能,就选择直接的解决方案而不是复杂的方案。简单的解决方案更容易理解、维护和调试。

### YAGNI(你不会需要它)

避免基于推测构建功能。仅在需要时实现功能,而不是在你预期可能有用时实现。

### 设计原则

- **依赖倒置**:高层模块不应依赖低层模块。两者都应依赖抽象。
- **开闭原则**:软件实体应对扩展开放,但对修改关闭。
- **单一职责**:每个函数、类和模块应该有一个明确的目的。
- **快速失败**:及早检查潜在错误,并在出现问题时立即抛出异常。

## 🧱 代码结构与模块化

### 文件和函数限制

- **永远不要创建超过500行代码的文件**。如果接近此限制,通过拆分为模块进行重构。
- **函数应少于50行**,具有单一、明确的职责。
- **类应少于100行**,代表单一概念或实体。
- **将代码组织成清晰分离的模块**,按功能或职责分组。
- **行长度最多100个字符** pyproject.toml 中的 ruff 规则
- **使用 venv_linux**(虚拟环境)执行所有 Python 命令,包括单元测试。

### 项目架构

遵循严格的垂直切片架构,测试与被测试的代码放在一起:

```
src/project/
    __init__.py
    main.py
    tests/
        test_main.py
    conftest.py

    # 核心模块
    database/
        __init__.py
        connection.py
        models.py
        tests/
            test_connection.py
            test_models.py

    auth/
        __init__.py
        authentication.py
        authorization.py
        tests/
            test_authentication.py
            test_authorization.py

    # 功能切片
    features/
        user_management/
            __init__.py
            handlers.py
            validators.py
            tests/
                test_handlers.py
                test_validators.py

        payment_processing/
            __init__.py
            processor.py
            gateway.py
            tests/
                test_processor.py
                test_gateway.py
```

## 🛠️ 开发环境

### UV 包管理

本项目使用 UV 进行超快的 Python 包和环境管理。

```bash
# 安装 UV(如果尚未安装)
curl -LsSf https://astral.sh/uv/install.sh | sh

# 创建虚拟环境
uv venv

# 同步依赖项
uv sync

# 添加包 ***永远不要直接在 PYPROJECT.toml 中更新依赖项***
# 始终使用 UV ADD
uv add requests

# 添加开发依赖项
uv add --dev pytest ruff mypy

# 删除包
uv remove requests

# 在环境中运行命令
uv run python script.py
uv run pytest
uv run ruff check .

# 安装特定 Python 版本
uv python install 3.12
```

### 开发命令

```bash
# 运行所有测试
uv run pytest

# 运行特定测试并显示详细输出
uv run pytest tests/test_module.py -v

# 运行测试并生成覆盖率报告
uv run pytest --cov=src --cov-report=html

# 格式化代码
uv run ruff format .

# 检查代码规范
uv run ruff check .

# 自动修复代码规范问题
uv run ruff check --fix .

# 类型检查
uv run mypy src/

# 运行 pre-commit 钩子
uv run pre-commit run --all-files
```

## 📋 风格与约定

### Python 风格指南

- **遵循 PEP8**,具体选择如下:
  - 行长度:100个字符(由 pyproject.toml 中的 Ruff 设置)
  - 字符串使用双引号
  - 多行结构使用尾随逗号
- **始终使用类型提示**用于函数签名和类属性
- **使用 `ruff format` 格式化**(更快的 Black 替代方案)
- **使用 `pydantic` v2** 进行数据验证和设置管理

### 文档字符串标准

为所有公共函数、类和模块使用 Google 风格的文档字符串:

```python
def calculate_discount(
    price: Decimal,
    discount_percent: float,
    min_amount: Decimal = Decimal("0.01")
) -> Decimal:
    """
    计算产品的折扣价格。

    Args:
        price: 产品的原价
        discount_percent: 折扣百分比(0-100)
        min_amount: 允许的最终价格下限

    Returns:
        应用折扣后的最终价格

    Raises:
        ValueError: 如果 discount_percent 不在 0 到 100 之间
        ValueError: 如果最终价格低于 min_amount

    Example:
        >>> calculate_discount(Decimal("100"), 20)
        Decimal('80.00')
    """
```

### 命名约定

- **变量和函数**: `snake_case`
- **类**: `PascalCase`
- **常量**: `UPPER_SNAKE_CASE`
- **私有属性/方法**: `_leading_underscore`
- **类型别名**: `PascalCase`
- **枚举值**: `UPPER_SNAKE_CASE`

## 🧪 测试策略

### 测试驱动开发(TDD)

1. **首先编写测试** - 在实现之前定义预期行为
2. **观察它失败** - 确保测试实际测试了某些东西
3. **编写最少代码** - 刚好足以使测试通过
4. **重构** - 在保持测试通过的同时改进代码
5. **重复** - 一次一个测试

### 测试最佳实践

```python
# 始终使用 pytest fixtures 进行设置
import pytest
from datetime import datetime

@pytest.fixture
def sample_user():
    """提供用于测试的示例用户。"""
    return User(
        id=123,
        name="Test User",
        email="test@example.com",
        created_at=datetime.now()
    )

# 使用描述性测试名称
def test_user_can_update_email_when_valid(sample_user):
    """测试用户可以使用有效输入更新其电子邮件。"""
    new_email = "newemail@example.com"
    sample_user.update_email(new_email)
    assert sample_user.email == new_email

# 测试边界情况和错误条件
def test_user_update_email_fails_with_invalid_format(sample_user):
    """测试拒绝无效的电子邮件格式。"""
    with pytest.raises(ValidationError) as exc_info:
        sample_user.update_email("not-an-email")
    assert "Invalid email format" in str(exc_info.value)
```

### 测试组织

- 单元测试:独立测试单个函数/方法
- 集成测试:测试组件交互
- 端到端测试:测试完整的用户工作流
- 将测试文件放在被测试代码旁边
- 使用 `conftest.py` 存放共享的 fixtures
- 目标覆盖率 80%+,但重点关注关键路径

## 🚨 错误处理

### 异常最佳实践

```python
# 为你的域创建自定义异常
class PaymentError(Exception):
    """支付相关错误的基础异常。"""
    pass

class InsufficientFundsError(PaymentError):
    """账户资金不足时抛出。"""
    def __init__(self, required: Decimal, available: Decimal):
        self.required = required
        self.available = available
        super().__init__(
            f"Insufficient funds: required {required}, available {available}"
        )

# 使用特定的异常处理
try:
    process_payment(amount)
except InsufficientFundsError as e:
    logger.warning(f"Payment failed: {e}")
    return PaymentResult(success=False, reason="insufficient_funds")
except PaymentError as e:
    logger.error(f"Payment error: {e}")
    return PaymentResult(success=False, reason="payment_error")

# 使用上下文管理器进行资源管理
from contextlib import contextmanager

@contextmanager
def database_transaction():
    """为数据库操作提供事务作用域。"""
    conn = get_connection()
    trans = conn.begin_transaction()
    try:
        yield conn
        trans.commit()
    except Exception:
        trans.rollback()
        raise
    finally:
        conn.close()
```

### 日志策略

```python
import logging
from functools import wraps

# 配置结构化日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

# 为调试记录函数进入/退出
def log_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.debug(f"Entering {func.__name__}")
        try:
            result = func(*args, **kwargs)
            logger.debug(f"Exiting {func.__name__} successfully")
            return result
        except Exception as e:
            logger.exception(f"Error in {func.__name__}: {e}")
            raise
    return wrapper
```

## 🔧 配置管理

### 环境变量和设置

```python
from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    """带验证的应用设置。"""
    app_name: str = "MyApp"
    debug: bool = False
    database_url: str
    redis_url: str = "redis://localhost:6379"
    api_key: str
    max_connections: int = 100

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False

@lru_cache()
def get_settings() -> Settings:
    """获取缓存的设置实例。"""
    return Settings()

# 使用方式
settings = get_settings()
```

## 🏗️ 数据模型和验证

### Pydantic v2 严格模型示例

```python
from pydantic import BaseModel, Field, validator, EmailStr
from datetime import datetime
from typing import Optional, List
from decimal import Decimal

class ProductBase(BaseModel):
    """带公共字段的基础产品模型。"""
    name: str = Field(..., min_length=1, max_length=255)
    description: Optional[str] = None
    price: Decimal = Field(..., gt=0, decimal_places=2)
    category: str
    tags: List[str] = []

    @validator('price')
    def validate_price(cls, v):
        if v > Decimal('1000000'):
            raise ValueError('Price cannot exceed 1,000,000')
        return v

    class Config:
        json_encoders = {
            Decimal: str,
            datetime: lambda v: v.isoformat()
        }

class ProductCreate(ProductBase):
    """创建新产品的模型。"""
    pass

class ProductUpdate(BaseModel):
    """更新产品的模型 - 所有字段可选。"""
    name: Optional[str] = Field(None, min_length=1, max_length=255)
    description: Optional[str] = None
    price: Optional[Decimal] = Field(None, gt=0, decimal_places=2)
    category: Optional[str] = None
    tags: Optional[List[str]] = None

class Product(ProductBase):
    """带数据库字段的完整产品模型。"""
    id: int
    created_at: datetime
    updated_at: datetime
    is_active: bool = True

    class Config:
        from_attributes = True  # 启用 ORM 模式
```

## 🔄 Git 工作流

### 分支策略

- `main` - 生产就绪代码
- `develop` - 功能集成分支
- `feature/*` - 新功能
- `fix/*` - Bug 修复
- `docs/*` - 文档更新
- `refactor/*` - 代码重构
- `test/*` - 测试添加或修复

### 提交消息格式

永远不要在提交消息中包含 claude code 或 written by claude code

```
<type>(<scope>): <subject>

<body>

<footer>
```

类型: feat, fix, docs, style, refactor, test, chore

示例:
```
feat(auth): add two-factor authentication

- Implement TOTP generation and validation
- Add QR code generation for authenticator apps
- Update user model with 2FA fields

Closes #123
```

## 🗄️ 数据库命名标准

### 实体特定主键
所有数据库表使用实体特定主键以提高清晰度和一致性:

```sql
-- ✅ 标准化:实体特定主键
sessions.session_id UUID PRIMARY KEY
leads.lead_id UUID PRIMARY KEY
messages.message_id UUID PRIMARY KEY
daily_metrics.daily_metric_id UUID PRIMARY KEY
agencies.agency_id UUID PRIMARY KEY
```

### 字段命名约定

```sql
-- 主键: {entity}_id
session_id, lead_id, message_id

-- 外键: {referenced_entity}_id
session_id REFERENCES sessions(session_id)
agency_id REFERENCES agencies(agency_id)

-- 时间戳: {action}_at
created_at, updated_at, started_at, expires_at

-- 布尔值: is_{state}
is_connected, is_active, is_qualified

-- 计数: {entity}_count
message_count, lead_count, notification_count

-- 持续时间: {property}_{unit}
duration_seconds, timeout_minutes
```

### 仓储模式自动推导

增强的 BaseRepository 自动推导表名和主键:

```python
# ✅ 标准化:基于约定的仓储
class LeadRepository(BaseRepository[Lead]):
    def __init__(self):
        super().__init__()  # 自动推导 "leads" 和 "lead_id"

class SessionRepository(BaseRepository[AvatarSession]):
    def __init__(self):
        super().__init__()  # 自动推导 "sessions" 和 "session_id"
```

**优势**:

- ✅ 自文档化的模式
- ✅ 清晰的外键关系
- ✅ 消除仓储方法覆盖
- ✅ 与实体命名模式一致

### 模型-数据库对齐

模型完全镜像数据库字段以消除字段映射复杂性:

```python
# ✅ 标准化:模型完全镜像数据库
class Lead(BaseModel):
    lead_id: UUID = Field(default_factory=uuid4)  # 匹配数据库字段
    session_id: UUID                               # 匹配数据库字段
    agency_id: str                                 # 匹配数据库字段
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))

    model_config = ConfigDict(
        use_enum_values=True,
        populate_by_name=True,
        alias_generator=None  # 使用精确字段名
    )
```

### API 路由标准

```python
# ✅ 标准化:RESTful 与一致的参数命名
router = APIRouter(prefix="/api/v1/leads", tags=["leads"])

@router.get("/{lead_id}")           # GET /api/v1/leads/{lead_id}
@router.put("/{lead_id}")           # PUT /api/v1/leads/{lead_id}
@router.delete("/{lead_id}")        # DELETE /api/v1/leads/{lead_id}

# 子资源
@router.get("/{lead_id}/messages")  # GET /api/v1/leads/{lead_id}/messages
@router.get("/agency/{agency_id}")  # GET /api/v1/leads/agency/{agency_id}
```

完整的命名标准,请参见 [NAMING_CONVENTIONS.md](./NAMING_CONVENTIONS.md)。

## 📝 文档标准

### 代码文档

- 每个模块都应有解释其目的的文档字符串
- 公共函数必须有完整的文档字符串
- 复杂逻辑应有带 `# Reason:` 前缀的内联注释
- 保持 README.md 更新,包含设置说明和示例
- 维护 CHANGELOG.md 记录版本历史

### API 文档

```python
from fastapi import APIRouter, HTTPException, status
from typing import List

router = APIRouter(prefix="/products", tags=["products"])

@router.get(
    "/",
    response_model=List[Product],
    summary="List all products",
    description="Retrieve a paginated list of all active products"
)
async def list_products(
    skip: int = 0,
    limit: int = 100,
    category: Optional[str] = None
) -> List[Product]:
    """
    检索产品并可选过滤。

    - **skip**: 要跳过的产品数量(用于分页)
    - **limit**: 返回的最大产品数量
    - **category**: 按产品类别过滤
    """
    # 实现在这里
```

## 🚀 性能考虑

### 优化指南

- 优化前先进行性能分析 - 使用 `cProfile` 或 `py-spy`
- 对昂贵的计算使用 `lru_cache`
- 对大数据集优先使用生成器
- 对 I/O 密集型操作使用 `asyncio`
- 对 CPU 密集型任务考虑使用 `multiprocessing`
- 适当缓存数据库查询

### 优化示例

```python
from functools import lru_cache
import asyncio
from typing import AsyncIterator

@lru_cache(maxsize=1000)
def expensive_calculation(n: int) -> int:
    """缓存昂贵计算的结果。"""
    # 复杂计算在这里
    return result

async def process_large_dataset() -> AsyncIterator[dict]:
    """处理大数据集而不将所有数据加载到内存。"""
    async with aiofiles.open('large_file.json', mode='r') as f:
        async for line in f:
            data = json.loads(line)
            # 处理并生成每个项
            yield process_item(data)
```

## 🛡️ 安全最佳实践

### 安全指南

- 永远不要提交密钥 - 使用环境变量
- 使用 Pydantic 验证所有用户输入
- 对数据库操作使用参数化查询
- 为 API 实现速率限制
- 使用 `uv` 保持依赖项更新
- 对所有外部通信使用 HTTPS
- 实现适当的身份验证和授权

### 安全实现示例

```python
from passlib.context import CryptContext
import secrets

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    """使用 bcrypt 散列密码。"""
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """验证密码与其散列值。"""
    return pwd_context.verify(plain_password, hashed_password)

def generate_secure_token(length: int = 32) -> str:
    """生成加密安全的随机令牌。"""
    return secrets.token_urlsafe(length)
```

## 🔍 调试工具

### 调试命令

```bash
# 使用 ipdb 进行交互式调试
uv add --dev ipdb
# 添加断点: import ipdb; ipdb.set_trace()

# 内存分析
uv add --dev memory-profiler
uv run python -m memory_profiler script.py

# 行分析
uv add --dev line-profiler
# 为函数添加 @profile 装饰器

# 使用 rich 回溯进行调试
uv add --dev rich
# 在代码中: from rich.traceback import install; install()
```

## 📊 监控和可观察性

### 结构化日志

```python
import structlog

logger = structlog.get_logger()

# 带上下文的日志
logger.info(
    "payment_processed",
    user_id=user.id,
    amount=amount,
    currency="USD",
    processing_time=processing_time
)
```

## 📚 有用资源

### 基本工具

- UV 文档: https://github.com/astral-sh/uv
- Ruff: https://github.com/astral-sh/ruff
- Pytest: https://docs.pytest.org/
- Pydantic: https://docs.pydantic.dev/
- FastAPI: https://fastapi.tiangolo.com/

### Python 最佳实践

- PEP 8: https://pep8.org/
- PEP 484(类型提示): https://www.python.org/dev/peps/pep-0484/
- Python 搭便车指南: https://docs.python-guide.org/

## ⚠️ 重要说明

- **永远不要假设或猜测** - 有疑问时,寻求澄清
- **在使用前始终验证文件路径和模块名称**
- **保持 CLAUDE.md 更新** - 添加新模式或依赖项时
- **测试你的代码** - 没有测试的功能不算完成
- **记录你的决定** - 未来的开发人员(包括你自己)会感谢你

## 🔍 搜索命令要求

**关键**:始终使用 `rg`(ripgrep)而不是传统的 `grep` 和 `find` 命令:

```bash
# ❌ 不要使用 grep
grep -r "pattern" .

# ✅ 使用 rg 替代
rg "pattern"

# ❌ 不要使用 find 与 name
find . -name "*.py"

# ✅ 使用 rg 与文件过滤
rg --files | rg "\.py$"
# 或
rg --files -g "*.py"
```

**执行规则:**

```
(
    r"^grep\b(?!.*\|)",
    "Use 'rg' (ripgrep) instead of 'grep' for better performance and features",
),
(
    r"^find\s+\S+\s+-name\b",
    "Use 'rg --files | rg pattern' or 'rg --files -g pattern' instead of 'find -name' for better performance",
),
```

## 🚀 GitHub Flow 工作流摘要

main (受保护) ←── PR ←── feature/your-feature
↓ ↑
deploy development

### 日常工作流:

1. git checkout main && git pull origin main
2. git checkout -b feature/new-feature
3. 进行更改 + 测试
4. git push origin feature/new-feature
5. 创建 PR → 审查 → 合并到 main

---

_本文档是一个活文档。随着项目发展和新模式出现而更新它。_