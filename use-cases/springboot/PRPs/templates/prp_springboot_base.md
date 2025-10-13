# Spring Boot 功能 PRP模板

用于 Spring Boot 3.x 应用程序功能开发的预填充 PRP 模板。

## All Needed Context

### Spring Boot 核心文档
```yaml
官方文档:
  - https://docs.spring.io/spring-boot/docs/current/reference/htmlsingle/
  - https://spring.io/guides
  - https://docs.spring.io/spring-boot/reference/using/structuring-your-code.html

分层架构:
  - https://tom-collings.medium.com/controller-service-repository-16e29a4684e5
  - Controller 层:处理 HTTP 请求
  - Service 层:业务逻辑
  - Repository 层:数据访问
```

### Spring Data JPA
```yaml
JPA 最佳实践:
  - https://medium.com/javaguides/best-practices-for-spring-data-jpa-the-ultimate-guide-c2a84a4cd45e
  - Entity 关系注解: @OneToMany, @ManyToOne, @OneToOne, @ManyToMany
  - 使用懒加载: FetchType.LAZY
  - 避免 N+1 查询: @EntityGraph, JOIN FETCH
```

### Spring Security 6
```yaml
安全配置:
  - https://docs.spring.io/spring-security/reference/servlet/authentication/passwords/basic.html
  - 使用 SecurityFilterChain bean
  - 密码编码: BCryptPasswordEncoder
  - Lambda 配置风格
```

### 测试策略
```yaml
测试框架:
  - @WebMvcTest: Controller 层测试
  - @DataJpaTest: Repository 层测试
  - @SpringBootTest: 集成测试
  - MockMvc: HTTP 请求模拟
```

## Implementation Blueprint

### Maven 项目结构
```
创建完整的 Spring Boot 项目结构:
  src/main/java/{package}/
  ├── controller/    # REST 控制器
  ├── service/       # 业务服务
  ├── repository/    # JPA 仓库
  ├── model/         # JPA 实体
  ├── dto/           # 数据传输对象
  ├── config/        # 配置类
  └── Application.java

  src/main/resources/
  ├── application.yml
  └── application-dev.yml

  src/test/java/{package}/
  ├── controller/
  ├── service/
  └── repository/
```

### 实现步骤
```yaml
步骤 1 - Maven POM:
  - 设置 spring-boot-starter-parent
  - 添加必需的 starters
  - 配置 Java 21

步骤 2 - Entity 层:
  - 定义 JPA 实体
  - 配置关系注解
  - 使用懒加载

步骤 3 - Repository 层:
  - 扩展 JpaRepository
  - 定义自定义查询方法
  - 使用 @EntityGraph 避免 N+1

步骤 4 - Service 层:
  - 实现业务逻辑
  - 使用 @Transactional
  - DTO 转换

步骤 5 - Controller 层:
  - 定义 REST 端点
  - 使用 @RestController
  - 处理请求和响应

步骤 6 - 配置:
  - application.yml 配置
  - Security 配置
  - H2 数据库配置

步骤 7 - 测试:
  - Controller 测试
  - Service 测试
  - Repository 测试
```

## Validation Loop

### 编译验证
```bash
mvn validate
mvn clean compile
```

### 测试验证
```bash
mvn test
```

### 运行验证
```bash
mvn spring-boot:run
# 在另一个终端测试 API
curl http://localhost:8080/api/endpoint
```

### 打包验证
```bash
mvn clean package
java -jar target/*.jar
```

## Spring Boot 常见陷阱

```yaml
必须避免:
  - 在 Controller 中编写业务逻辑
  - 直接返回 Entity 而非 DTO
  - 忽略 N+1 查询问题
  - 对所有关系使用 EAGER 加载
  - 硬编码配置值
  - 跳过测试
  - 混用 .properties 和 .yml
```

使用此模板作为创建 Spring Boot 特定 PRP 的起点。根据实际功能需求填充具体细节。
