# Spring Boot 上下文工程模板

使用上下文工程原则快速构建企业级 Spring Boot 3.x 应用程序的完整模板,包含最佳实践、分层架构和全面的测试支持。

## 🚀 快速开始 - 首先复制模板

**在开始之前,使用复制脚本将此模板部署到你的项目目录:**

```bash
# 从模板目录运行
python copy_template.py /path/to/your/project

# 示例
python copy_template.py ~/projects/my-springboot-app
python copy_template.py ../my-new-api
```

这将复制所有必需的文件到你的项目:
- ✓ CLAUDE.md (Spring Boot 全局规则)
- ✓ .claude/commands/ (专门的斜杠命令)
- ✓ PRPs/ (模板和示例)
- ✓ examples/ (代码示例)
- ✓ README.md (本文档)

## 📋 PRP 框架工作流程

Spring Boot 上下文工程遵循标准的 3 步 PRP 流程:

### 步骤 1: 定义你的功能 (INITIAL.md)

在 `PRPs/INITIAL.md` 中描述你想要构建的功能:

```markdown
# 功能请求

## 技术栈
Java 21, Spring Boot 3.x, Spring Data JPA, H2 Database

## 功能描述
创建一个用户管理 REST API...

## 核心功能需求
- REST 端点: GET, POST, PUT, DELETE
- 数据验证
- Spring Security 认证
...
```

### 步骤 2: 生成 PRP (`/generate-springboot-prp`)

从你的功能请求生成全面的实现计划:

```bash
/generate-springboot-prp PRPs/INITIAL.md
```

这将:
- 📚 研究 Spring Boot 最佳实践和模式
- 🏗️ 规划完整的项目结构
- ✅ 定义验证标准
- 📝 创建详细的实现蓝图

输出: `PRPs/feature-{name}.md` - 包含所有上下文和步骤的完整计划

### 步骤 3: 执行 PRP (`/execute-springboot-prp`)

实现 PRP 中定义的功能:

```bash
/execute-springboot-prp PRPs/feature-{name}.md
```

这将:
- 🏗️ 创建 Maven 项目结构
- 📝 生成所有层的代码 (Controller, Service, Repository, Model)
- ⚙️ 配置 application.yml 和 pom.xml
- 🧪 创建全面的测试
- ✅ 验证所有内容编译和运行

输出: 完整的、可运行的 Spring Boot 应用程序!

## 📁 模板结构

```
springboot/
├── CLAUDE.md                          # Spring Boot 全局规则和最佳实践
├── .claude/commands/
│   ├── generate-springboot-prp.md    # PRP 生成命令
│   └── execute-springboot-prp.md     # PRP 执行命令
├── PRPs/
│   ├── templates/
│   │   └── prp_springboot_base.md    # 预填充的 PRP 模板
│   ├── ai_docs/                      # Spring Boot 文档 (可选)
│   └── INITIAL.md                    # 示例功能请求
├── examples/                         # 代码示例
│   ├── controller/
│   │   └── UserController.java       # REST 控制器示例
│   ├── service/
│   │   └── UserService.java          # 业务服务示例
│   ├── repository/
│   │   └── UserRepository.java       # JPA 仓库示例
│   ├── model/
│   │   └── User.java                 # Entity 模型示例
│   ├── config/
│   │   └── SecurityConfig.java       # Spring Security 配置
│   ├── test/
│   │   └── UserControllerTest.java   # 测试示例
│   ├── application.yml               # 配置文件模板
│   └── pom.xml                       # Maven POM 示例
├── copy_template.py                  # 模板复制脚本
└── README.md                         # 本文档
```

## 🎯 你可以构建什么

使用此模板,你可以快速创建:

### REST API
- ✅ 完整的 CRUD 端点
- ✅ 请求验证和错误处理
- ✅ 分页和排序
- ✅ 全局异常处理

### 数据层
- ✅ JPA Entity 和关系
- ✅ 自定义查询方法
- ✅ 事务管理
- ✅ H2 内存数据库

### 安全
- ✅ Spring Security 6 集成
- ✅ 基本认证
- ✅ 密码加密 (BCrypt)
- ✅ 角色基础访问控制

### 测试
- ✅ Controller 测试 (@WebMvcTest)
- ✅ Service 测试 (Mockito)
- ✅ Repository 测试 (@DataJpaTest)
- ✅ 集成测试 (@SpringBootTest)

## 📚 关键特性

### Controller-Service-Repository 架构
- **Controller 层**: 处理 HTTP 请求和响应
- **Service 层**: 包含所有业务逻辑
- **Repository 层**: 数据访问和持久化
- **Model 层**: JPA 实体定义
- **DTO 模式**: 安全的数据传输

### Maven 项目管理
- ✅ spring-boot-starter-parent
- ✅ 自动依赖管理
- ✅ Java 21 支持
- ✅ 标准项目结构

### Spring Data JPA
- ✅ Repository 接口
- ✅ 自定义查询方法
- ✅ Entity 关系 (@OneToMany, @ManyToOne 等)
- ✅ 懒加载优化
- ✅ N+1 查询解决方案

### Spring Security 6
- ✅ Lambda 风格配置
- ✅ SecurityFilterChain bean
- ✅ 密码编码器
- ✅ UserDetailsService

### 配置管理
- ✅ YAML 格式配置
- ✅ Profile-specific 配置 (dev, prod)
- ✅ H2 控制台集成
- ✅ 日志配置

### 测试策略
- ✅ MockMvc for Controllers
- ✅ Mockito for Services
- ✅ @DataJpaTest for Repositories
- ✅ Spring Security Test

## 🔍 包含的示例

### Controller 示例
`UserController.java` 展示:
- REST 端点定义 (@GetMapping, @PostMapping 等)
- 构造器注入
- ResponseEntity 使用
- 路径变量和请求体处理

### Service 示例
`UserService.java` 展示:
- 业务逻辑实现
- @Transactional 使用
- DTO 转换
- 异常处理

### Repository 示例
`UserRepository.java` 展示:
- JpaRepository 扩展
- 自定义查询方法
- @Query 注解
- 方法命名约定

### Entity 示例
`User.java` 展示:
- JPA 注解 (@Entity, @Table, @Column)
- 主键生成策略
- 生命周期回调 (@PrePersist, @PreUpdate)
- 时间戳字段

### Security 配置
`SecurityConfig.java` 展示:
- SecurityFilterChain 配置
- 端点授权规则
- 密码编码器 bean
- 内存用户管理

### 测试示例
`UserControllerTest.java` 展示:
- @WebMvcTest 使用
- MockMvc 设置
- @MockBean 模拟
- JSON 路径断言

### 配置文件
- `application.yml`: 完整的 Spring Boot 配置
- `pom.xml`: Maven 依赖和插件配置

## 📖 文档参考

### 官方文档
- [Spring Boot 文档](https://docs.spring.io/spring-boot/docs/current/reference/htmlsingle/)
- [Spring Data JPA](https://docs.spring.io/spring-data/jpa/docs/current/reference/html/)
- [Spring Security](https://docs.spring.io/spring-security/reference/index.html/)
- [Spring Guides](https://spring.io/guides)

### 最佳实践
- [Controller-Service-Repository 模式](https://tom-collings.medium.com/controller-service-repository-16e29a4684e5)
- [Spring Data JPA 最佳实践](https://medium.com/javaguides/best-practices-for-spring-data-jpa-the-ultimate-guide-c2a84a4cd45e)
- [Spring Boot 测试](https://www.baeldung.com/spring-boot-testing)

### 参考实现
- [Spring Boot REST API 示例](https://github.com/bezkoder/spring-boot-3-rest-api-example)
- [Spring Boot 最佳实践](https://github.com/arsy786/springboot-best-practices)

## 🚫 常见陷阱

### 架构陷阱
- ❌ **不要在 Controller 中编写业务逻辑** → 使用 Service 层
- ❌ **不要直接返回 Entity** → 使用 DTO 模式
- ❌ **不要在 Controller 中直接使用 Repository** → 通过 Service 访问

### 性能陷阱
- ❌ **不要忽视 N+1 查询问题** → 使用 @EntityGraph 或 JOIN FETCH
- ❌ **不要对所有关系使用 EAGER** → 默认使用 LAZY 加载
- ❌ **不要在循环中查询数据库** → 使用批量操作

### 安全陷阱
- ❌ **不要硬编码密码** → 使用环境变量
- ❌ **不要在生产环境禁用 CSRF** → 只在开发时禁用
- ❌ **不要使用明文密码** → 使用 BCrypt

### 配置陷阱
- ❌ **不要混用 .properties 和 .yml** → 选择一种格式
- ❌ **不要硬编码配置值** → 使用 application.yml
- ❌ **不要在代码中记录敏感信息** → 使用适当的日志级别

### 测试陷阱
- ❌ **不要跳过测试** → 测试是质量保证的关键
- ❌ **不要过度模拟** → 测试真实行为
- ❌ **不要在测试中使用生产数据库** → 使用 H2

## 💡 使用技巧

### 快速启动新项目
```bash
# 1. 复制模板
python copy_template.py ~/projects/my-api

# 2. 进入项目
cd ~/projects/my-api

# 3. 编辑功能需求
vim PRPs/INITIAL.md

# 4. 生成 PRP
/generate-springboot-prp PRPs/INITIAL.md

# 5. 执行实现
/execute-springboot-prp PRPs/feature-myapi.md
```

### 验证项目
```bash
# 编译
mvn clean compile

# 运行测试
mvn test

# 启动应用
mvn spring-boot:run

# 测试 API (在另一个终端)
curl -u user:password http://localhost:8080/api/users
```

### H2 控制台
访问 http://localhost:8080/h2-console 查看数据库:
- JDBC URL: `jdbc:h2:mem:testdb`
- Username: `sa`
- Password: (空)

## 🤝 贡献和反馈

这个模板是上下文工程框架的一部分。如果你有改进建议或发现问题:
- 查看主 README 了解更多信息
- 参考 CLAUDE.md 了解 Spring Boot 特定规则
- 参考示例了解最佳实践

## 📜 许可证

此模板是上下文工程框架的一部分,遵循相同的许可证。

---

**准备好使用 Spring Boot 和上下文工程开始构建了吗?** 🚀

从复制模板开始: `python copy_template.py /your/project/path`
