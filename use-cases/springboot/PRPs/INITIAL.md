# Spring Boot 功能请求示例

## 技术栈
Java 21, Spring Boot 3.x, Spring Data JPA, Spring Security, H2 Database, Maven

## 功能描述
创建一个用户管理 REST API,支持 CRUD 操作和基本认证。

## 核心功能需求

### 1. 用户实体
- 用户 ID(自动生成)
- 用户名(唯一,必填)
- 邮箱(唯一,必填)
- 密码(加密存储)
- 角色(USER/ADMIN)
- 创建时间和更新时间

### 2. REST API 端点
- `GET /api/users` - 获取所有用户列表
- `GET /api/users/{id}` - 获取单个用户详情
- `POST /api/users` - 创建新用户
- `PUT /api/users/{id}` - 更新用户信息
- `DELETE /api/users/{id}` - 删除用户

### 3. 数据验证
- 用户名:最少 3 个字符,最多 50 个字符
- 邮箱:有效的邮箱格式
- 密码:最少 6 个字符

### 4. 安全要求
- 使用 Spring Security 基本认证
- 密码使用 BCrypt 加密
- `/api/users` GET 请求允许所有认证用户访问
- POST/PUT/DELETE 请求仅允许 ADMIN 角色访问

### 5. 数据库
- 使用 H2 内存数据库
- 启用 H2 控制台(开发环境)
- 自动创建表结构

### 6. 配置
- 使用 YAML 格式的配置文件
- 支持开发和生产环境配置
- 配置日志级别和格式

## 测试要求

### Controller 测试
- 使用 @WebMvcTest 测试所有 REST 端点
- 使用 MockMvc 模拟 HTTP 请求
- 验证响应状态码和内容

### Service 测试
- 使用 Mockito 模拟 Repository
- 测试业务逻辑和数据转换
- 测试异常处理

### Repository 测试
- 使用 @DataJpaTest 测试数据访问
- 验证自定义查询方法
- 测试实体关系

## 项目结构期望

```
src/main/java/com/example/usermanager/
├── controller/
│   └── UserController.java
├── service/
│   └── UserService.java
├── repository/
│   └── UserRepository.java
├── model/
│   ├── User.java
│   └── Role.java (enum)
├── dto/
│   └── UserDTO.java
├── config/
│   └── SecurityConfig.java
├── exception/
│   ├── ResourceNotFoundException.java
│   └── GlobalExceptionHandler.java
└── UserManagerApplication.java

src/main/resources/
├── application.yml
└── application-dev.yml

src/test/java/com/example/usermanager/
├── controller/
│   └── UserControllerTest.java
├── service/
│   └── UserServiceTest.java
└── repository/
    └── UserRepositoryTest.java
```

## 期望输出

1. 完整的 Maven 项目,可以直接运行
2. 所有 CRUD 端点都能正常工作
3. 通过所有单元测试和集成测试
4. 使用 `mvn spring-boot:run` 可以启动应用程序
5. 可以通过 H2 控制台查看数据库
6. API 文档或 README 说明如何测试端点

## 额外要求

- 遵循 Spring Boot 最佳实践
- 使用构造器注入而非字段注入
- 实现全局异常处理
- 使用 @Transactional 管理事务
- 避免 N+1 查询问题
- 使用 DTO 模式,不直接返回 Entity
