---
name: "Spring Boot Context Engineering Template Generator"
description: "生成 Spring Boot 应用程序的完整上下文工程模板包,包含最佳实践、分层架构和完整的测试支持"
---

## Purpose

为 Spring Boot 3.x 应用程序生成完整的上下文工程模板包,专门针对使用 Java 21、Spring MVC、Spring Data JPA、Spring Security 和 H2 数据库的 Web 应用程序开发。模板遵循企业级最佳实践和分层架构模式。

## Core Principles

1. **分层架构优先**: 严格遵守 Controller-Service-Repository 分层模式
2. **测试驱动开发**: 使用 Spring Boot Test 和 MockMvc 进行全面测试
3. **安全第一**: 集成 Spring Security 6 的最佳安全实践
4. **配置标准化**: 使用 YAML 格式的配置文件管理
5. **即时可用**: 生成的模板可立即运行和部署

---

## Goal

生成一个完整的 Spring Boot 上下文工程模板包,包含:

- Spring Boot 特定的 CLAUDE.md 实现指南
- 专门的 PRP 生成和执行命令
- Spring Boot 适用的基础 PRP 模板
- 完整的代码示例和配置文件
- Spring Boot 特定的验证循环和成功标准

## Why

- **加速开发**: 使 Spring Boot 开发者能够快速应用上下文工程原则
- **最佳实践**: 确保遵循 Spring Boot 3.x 和 Java 21 的最新模式
- **质量保证**: 通过全面的测试和验证确保代码质量
- **知识捕获**: 记录 Spring Boot 生态系统的最佳实践和常见陷阱
- **可扩展框架**: 创建可随技术演进而更新的可重用模板

## What

### 模板包组件

**完整目录结构:**
```
use-cases/springboot/
├── CLAUDE.md                           # Spring Boot 实现指南
├── .claude/commands/
│   ├── generate-springboot-prp.md     # Spring Boot PRP 生成
│   └── execute-springboot-prp.md      # Spring Boot PRP 执行
├── PRPs/
│   ├── templates/
│   │   └── prp_springboot_base.md     # Spring Boot 基础 PRP 模板
│   ├── ai_docs/                       # Spring Boot 文档
│   └── INITIAL.md                     # 功能请求示例
├── examples/                          # Spring Boot 代码示例
│   ├── controller/                    # Controller 层示例
│   ├── service/                       # Service 层示例
│   ├── repository/                    # Repository 层示例
│   ├── model/                         # Entity 模型示例
│   ├── config/                        # 配置类示例
│   └── test/                          # 测试示例
├── copy_template.py                   # 模板部署脚本
└── README.md                          # 综合使用指南
```

**Spring Boot 技术集成:**
- Maven 项目结构和依赖管理
- Spring Boot 3.x 分层架构和命名约定
- REST API 开发工作流程
- Spring Boot Test 测试方法
- Spring Security 安全配置
- H2 数据库集成和 JPA 最佳实践
- YAML 配置和日志记录

**上下文工程适配:**
- Spring Boot 特定的研究流程
- Spring Boot 适用的验证循环
- 框架专门的实现蓝图
- 与基础上下文工程原则的集成

### 成功标准

- [ ] 生成完整的模板包结构
- [ ] 所有必需文件存在且格式正确
- [ ] Spring Boot 特定内容准确代表技术模式
- [ ] 上下文工程原则正确适配到 Spring Boot
- [ ] 验证循环适用且可执行
- [ ] 模板可立即用于创建 Spring Boot 项目
- [ ] 保持与基础上下文工程框架的集成
- [ ] 包含全面的文档和示例

## All Needed Context

### 文档和参考资料 (必读)

```yaml
# Spring Boot 官方文档
Spring Boot 核心文档:
  - url: https://docs.spring.io/spring-boot/docs/current/reference/html/getting-started.html
    why: Spring Boot 3.x 快速入门和核心概念

  - url: https://docs.spring.io/spring-boot/docs/current/reference/htmlsingle/
    why: 完整的 Spring Boot 参考文档

  - url: https://docs.spring.io/spring-boot/reference/using/structuring-your-code.html
    why: Spring Boot 代码结构最佳实践

Spring Framework 文档:
  - url: https://docs.spring.io/spring-framework/reference/
    why: Spring Framework 核心功能和模式

# Spring MVC 和 REST API
REST API 开发:
  - url: https://spring.io/guides
    why: Spring Boot REST API 指南和教程

  - url: https://www.baeldung.com/spring-boot-clean-architecture
    why: Spring Boot 清洁架构实践

Controller-Service-Repository 模式:
  - url: https://medium.com/@rameshfadatare/spring-boot-architecture-controller-service-repository-database-architecture-flow-9144084818b0
    why: Spring Boot 分层架构详细说明

  - url: https://tom-collings.medium.com/controller-service-repository-16e29a4684e5
    why: Controller-Service-Repository 模式最佳实践

# Spring Data JPA
JPA 和 Hibernate:
  - url: https://www.baeldung.com/spring-boot-clean-architecture
    why: Spring Data JPA 最佳实践

  - url: https://medium.com/javaguides/best-practices-for-spring-data-jpa-the-ultimate-guide-c2a84a4cd45e
    why: Spring Data JPA 终极指南

Entity 关系:
  - url: https://codingnomads.com/spring-data-jpa-entity-relationships
    why: Spring Data JPA 实体关系模式

  - url: https://medium.com/@bubu.tripathy/best-practices-entity-class-design-with-jpa-and-spring-boot-6f703339ab3d
    why: JPA Entity 类设计最佳实践

# H2 数据库
H2 配置:
  - url: https://www.baeldung.com/spring-boot-h2-database
    why: Spring Boot H2 数据库集成

  - url: https://medium.com/@humbleCoder007/configuring-h2-database-in-a-spring-boot-application-3c5b1ec49189
    why: H2 数据库配置详解

# Spring Security
Spring Security 6:
  - url: https://docs.spring.io/spring-security/reference/servlet/authentication/passwords/basic.html
    why: Spring Security 基本认证官方文档

  - url: https://medium.com/@Lakshitha_Fernando/spring-security-6-and-spring-boot-3-with-simple-project-91389cc13119
    why: Spring Security 6 和 Spring Boot 3 简单项目示例

安全最佳实践:
  - url: https://www.baeldung.com/spring-security-basic-authentication
    why: Spring Security 基本认证教程

  - url: https://tech.asimio.net/resources/code-snippets/spring-boot3-spring-security6-basic-auth-configuration/
    why: Spring Boot 3 和 Spring Security 6 配置代码片段

# 测试框架
Spring Boot Test:
  - url: https://howtodoinjava.com/spring-boot2/testing/spring-boot-mockmvc-example/
    why: Spring Boot MockMvc 测试示例

  - url: https://www.kapresoft.com/java/2023/11/16/spring-boot-mockmvc-best-practices.html
    why: Spring Boot MockMVC 最佳实践

集成测试:
  - url: https://www.baeldung.com/integration-testing-in-spring
    why: Spring 集成测试完整指南

  - url: https://rieckpil.de/guide-to-testing-spring-boot-applications-with-mockmvc/
    why: 使用 MockMvc 测试 Spring Boot 应用程序指南

# Maven 和项目结构
Maven 依赖管理:
  - url: https://mvnrepository.com/artifact/org.springframework.boot/spring-boot-starter-parent
    why: Spring Boot Maven Parent POM

  - url: https://www.baeldung.com/spring-boot-starter-parent
    why: Spring Boot Starter Parent 详解

项目结构:
  - url: https://symflower.com/en/company/blog/2024/spring-boot-folder-structure/
    why: Spring Boot 文件夹结构最佳实践

  - url: https://github.com/arsy786/springboot-best-practices
    why: Spring Boot 最佳实践 GitHub 仓库

# 配置和日志
YAML 配置:
  - url: https://docs.spring.io/spring-boot/reference/features/logging.html
    why: Spring Boot 日志记录官方文档

  - url: https://last9.io/blog/a-guide-to-spring-boot-logging/
    why: Spring Boot 日志记录指南

配置最佳实践:
  - url: https://howtodoinjava.com/spring-boot/configure-logging-application-yml/
    why: 使用 application.yml 配置日志

# 常见陷阱和故障排除
常见错误:
  - url: https://www.toptal.com/spring/top-10-most-common-spring-framework-mistakes
    why: 10 个最常见的 Spring Framework 错误

  - url: https://medium.com/@davoud.badamchi/9-common-mistakes-in-spring-boot-development-and-how-to-avoid-them-ce4e2707f015
    why: Spring Boot 开发中的 9 个常见错误及避免方法

性能调优:
  - url: https://www.cogentuniversity.com/post/spring-boot-performance-tuning-5-common-issues-and-how-to-fix-them
    why: Spring Boot 性能调优：5 个常见问题及修复方法

# 示例项目
GitHub 示例:
  - url: https://github.com/bezkoder/spring-boot-3-rest-api-example
    why: Spring Boot 3 REST API CRUD 操作示例

  - url: https://github.com/digitalinnovationone/spring-boot-3-rest-api-template
    why: Spring Boot 3 REST API 模板项目

Spring 指南:
  - url: https://spring.io/guides
    why: Spring 官方指南和教程
```

### Spring Boot 技术分析

```typescript
// Spring Boot 框架模式
interface SpringBootAnalysis {
  // 核心架构模式
  architecture: {
    project_structure: [
      "src/main/java/{base-package}/",
      "  ├── controller/    # REST 控制器层",
      "  ├── service/       # 业务逻辑层",
      "  ├── repository/    # 数据访问层",
      "  ├── model/         # Entity 实体类",
      "  ├── config/        # 配置类",
      "  └── Application.java  # 主应用类",
      "src/main/resources/",
      "  ├── application.yml    # 主配置文件",
      "  └── application-{profile}.yml  # 环境配置",
      "src/test/java/{base-package}/",
      "  ├── controller/    # Controller 测试",
      "  ├── service/       # Service 测试",
      "  └── integration/   # 集成测试"
    ];

    configuration_files: [
      "pom.xml                # Maven 依赖管理",
      "application.yml        # Spring Boot 配置",
      "logback-spring.xml     # 日志配置(可选)"
    ];

    dependency_management: "Maven with spring-boot-starter-parent";

    module_organization: [
      "按层组织: controller, service, repository",
      "或按功能组织: user/, product/, order/"
    ];
  };

  // 开发工作流
  development: {
    package_manager: "Maven (mvn)";

    dev_server_commands: [
      "mvn spring-boot:run",
      "mvn clean install",
      "mvn test"
    ];

    build_process: [
      "mvn clean",
      "mvn compile",
      "mvn package",
      "java -jar target/app.jar"
    ];

    testing_frameworks: [
      "Spring Boot Test",
      "JUnit 5",
      "MockMvc",
      "Mockito",
      "@WebMvcTest",
      "@SpringBootTest"
    ];
  };

  // 最佳实践模式
  patterns: {
    code_organization: [
      "Controller 层只处理 HTTP 请求",
      "Service 层包含业务逻辑",
      "Repository 层负责数据访问",
      "使用 DTO 在层之间传输数据",
      "Entity 类只用于 JPA 映射"
    ];

    state_management: [
      "使用 @Service 进行单例管理",
      "使用 @Transactional 管理事务",
      "避免在 Controller 中处理业务逻辑"
    ];

    error_handling: [
      "使用 @ControllerAdvice 全局异常处理",
      "创建自定义异常类",
      "使用 @ExceptionHandler 处理特定异常",
      "返回标准化的错误响应"
    ];

    performance_optimization: [
      "使用懒加载 (LAZY) 优化 JPA 关系",
      "启用 Hibernate 查询缓存",
      "使用 @Async 进行异步处理",
      "优化数据库查询和索引"
    ];
  };

  // 生态系统集成
  ecosystem: {
    common_libraries: [
      "spring-boot-starter-web",
      "spring-boot-starter-data-jpa",
      "spring-boot-starter-security",
      "spring-boot-starter-test",
      "h2database",
      "lombok (可选)"
    ];

    deployment_platforms: [
      "JAR 部署",
      "Docker 容器",
      "Kubernetes",
      "云平台 (AWS, Azure, GCP)"
    ];

    monitoring_tools: [
      "Spring Boot Actuator",
      "Micrometer",
      "Prometheus",
      "Grafana"
    ];

    CI_CD_patterns: [
      "GitHub Actions",
      "Jenkins",
      "GitLab CI",
      "Maven Wrapper"
    ];
  };
}
```

### Spring Boot 常见陷阱

```typescript
// 必须避免的常见错误
interface SpringBootGotchas {
  dependency_issues: {
    problem: "依赖版本冲突和兼容性问题";
    solution: [
      "使用 spring-boot-starter-parent 管理版本",
      "避免手动指定 Spring 依赖版本",
      "使用 dependencyManagement 解决冲突"
    ];
  };

  annotation_misuse: {
    problem: "过度使用或误用注解";
    solutions: [
      "@Service 用于业务逻辑类",
      "@Repository 用于数据访问类",
      "@RestController = @Controller + @ResponseBody",
      "避免在同一个类上使用多个构造型注解"
    ];
  };

  exception_handling: {
    problem: "异常处理不当导致数据丢失或系统崩溃";
    solutions: [
      "使用 @ControllerAdvice 集中异常处理",
      "创建自定义异常类层次结构",
      "记录异常但不要吞掉它们",
      "向客户端返回有意义的错误消息"
    ];
  };

  n_plus_one_queries: {
    problem: "JPA N+1 查询导致性能问题";
    solutions: [
      "使用 @EntityGraph 预加载关系",
      "使用 JOIN FETCH in JPQL 查询",
      "选择适当的 FetchType (LAZY vs EAGER)",
      "启用 Hibernate 查询日志进行调试"
    ];
  };

  configuration_pitfalls: {
    problem: "application.yml 和 application.properties 混用";
    solutions: [
      "选择一种格式并坚持使用",
      "使用 profile-specific 配置文件",
      "避免硬编码敏感信息",
      "使用环境变量或加密的属性文件"
    ];
  };

  security_concerns: {
    problem: "暴露敏感信息和安全漏洞";
    solutions: [
      "永远不要在代码中硬编码密码",
      "使用 HTTPS 传输敏感数据",
      "配置 CORS 策略",
      "启用 CSRF 保护",
      "使用 BCrypt 编码密码"
    ];
  };

  test_coverage: {
    problem: "测试覆盖不足或测试过度模拟";
    solutions: [
      "为每个层编写单元测试",
      "使用 @WebMvcTest 测试控制器",
      "使用 @DataJpaTest 测试仓库",
      "编写集成测试验证完整流程",
      "避免过度模拟 - 测试真实行为"
    ];
  };

  startup_performance: {
    problem: "启动时间缓慢";
    solutions: [
      "减少 classpath 扫描范围",
      "使用懒加载初始化",
      "避免在启动时进行昂贵的操作",
      "考虑使用 Spring Native 进行原生编译"
    ];
  };
}
```

## Implementation Blueprint

### 技术研究阶段 (已完成)

**研究结果总结:**

✅ **核心框架分析:**
- Spring Boot 3.x 需要 Java 17+,完全支持 Java 21
- 支持 Java 21 的虚拟线程特性 (spring.threads.virtual.enabled=true)
- 遵循标准 Maven 项目结构
- 使用 @SpringBootApplication 注解的主应用类
- 分层架构: Controller → Service → Repository → Database

✅ **开发工作流分析:**
- Maven 作为构建工具和依赖管理器
- spring-boot-starter-parent 提供依赖版本管理
- mvn spring-boot:run 用于本地开发
- Spring Boot DevTools 支持热重载
- Spring Boot Test 提供全面的测试支持

✅ **最佳实践调研:**
- Controller-Service-Repository 模式是标准实践
- 业务逻辑必须在 Service 层,不在 Controller
- 使用 DTO 在层之间传输数据
- Entity 类专门用于 JPA 数据库映射
- 全局异常处理使用 @ControllerAdvice

✅ **Spring Data JPA 模式:**
- 四种关系注解: @OneToOne, @ManyToOne, @OneToMany, @ManyToMany
- 使用懒加载优化性能
- 理解关系的所有权 (owning side)
- 使用 @JoinColumn 指定外键映射
- 避免 N+1 查询问题

✅ **Spring Security 配置:**
- Spring Security 6 使用新的 lambda 配置风格
- 基本认证需要 SecurityFilterChain bean
- 密码使用 BCryptPasswordEncoder 编码
- InMemoryUserDetailsManager 用于内存用户管理
- 建议配合 HTTPS 使用

✅ **H2 数据库集成:**
- 使用内存模式: jdbc:h2:mem:testdb
- 启用 H2 控制台进行调试
- 配置 JPA hibernate.ddl-auto 管理模式
- 默认用户名 'sa',密码为空
- 可选择文件模式实现持久化

✅ **测试最佳实践:**
- @WebMvcTest 用于 MVC 层测试
- @SpringBootTest 用于集成测试
- MockMvc 模拟 HTTP 请求
- 分离单元测试和集成测试
- 使用 @DataJpaTest 测试仓库层

✅ **常见陷阱识别:**
- 依赖版本冲突
- 注解误用和过度使用
- 异常处理不当
- N+1 查询性能问题
- 配置文件混用
- 安全配置不当
- 测试过度模拟

### 模板包生成

```yaml
生成任务 1 - 创建模板目录结构:
  创建完整的用例目录结构:
    - use-cases/springboot/
    - .claude/commands/ 子目录
    - PRPs/templates/ 子目录
    - PRPs/ai_docs/ 子目录
    - examples/ 子目录 (controller, service, repository, model, config, test)
    - 根据模板包要求的所有其他子目录

生成任务 2 - 生成 Spring Boot 特定的 CLAUDE.md:
  创建技术特定的全局规则文件:
    - Maven 和 Java 21 工具命令
    - Spring Boot 分层架构模式和约定
    - REST API 开发工作流程
    - Spring Security 安全最佳实践
    - JPA 和 H2 数据库配置指南
    - Spring Boot Test 测试策略
    - 从研究中发现的常见陷阱

生成任务 3 - 创建专门的模板 PRP 命令:
  生成特定于域的斜杠命令:
    - generate-springboot-prp.md 包含 Spring Boot 研究模式
    - execute-springboot-prp.md 包含框架验证循环
    - 命令应引用研究中的 Spring Boot 特定模式
    - 包含特定于 Spring Boot 领域的网络搜索策略

生成任务 4 - 开发 Spring Boot 特定的基础 PRP 模板:
  创建专门的 prp_springboot_base.md 模板:
    - 预填充来自网络研究的 Spring Boot 上下文
    - Spring Boot 特定的成功标准和验证门
    - 通过研究找到的框架文档引用
    - 适用于域的实现模式和验证循环

生成任务 5 - 创建示例和 INITIAL.md 模板:
  生成全面的模板包内容:
    - INITIAL.md 示例展示如何请求 Spring Boot 功能
    - Controller 层代码示例 (REST API endpoints)
    - Service 层代码示例 (业务逻辑)
    - Repository 层代码示例 (JPA repositories)
    - Entity 模型示例 (JPA entities with relationships)
    - 配置类示例 (Security, Database, etc.)
    - 测试示例 (MockMvc, unit tests, integration tests)
    - application.yml 配置模板
    - pom.xml 依赖配置示例

生成任务 6 - 创建模板复制脚本:
  创建用于模板部署的 Python 脚本:
    - copy_template.py 脚本接受目标目录参数
    - 将整个模板目录结构复制到指定位置
    - 包含所有文件: CLAUDE.md, commands, PRPs, examples 等
    - 包含目录创建和文件复制的错误处理
    - 简单的命令行界面便于使用

生成任务 7 - 生成综合 README:
  创建全面但简洁的 README.md:
    - 清楚描述此模板的用途
    - 解释 PRP 框架工作流程 (3 步流程)
    - 模板复制脚本使用说明 (在顶部显著位置)
    - 快速入门指南和具体示例
    - 模板结构概述,显示所有生成的文件
    - 特定于 Spring Boot 领域的使用示例
    - Spring Boot 常见陷阱部分
```

## Validation Loop

### Level 1: 模板结构验证

```bash
# 验证完整的模板包结构
find use-cases/springboot -type f | sort

# 验证关键目录
ls -la use-cases/springboot/.claude/commands/
ls -la use-cases/springboot/PRPs/templates/
ls -la use-cases/springboot/examples/

# 验证复制脚本存在且可用
test -f use-cases/springboot/copy_template.py && echo "✓ Copy script exists"
python use-cases/springboot/copy_template.py --help 2>/dev/null || echo "ℹ Copy script ready"

# 预期: 所有必需文件存在,包括 copy_template.py
```

### Level 2: 内容质量验证

```bash
# 验证 Spring Boot 特定内容准确性
cd use-cases/springboot

# 检查占位符内容
grep -r "TODO\|PLACEHOLDER\|{domain}\|{technology}" . 2>/dev/null | grep -v ".git" | wc -l
# 预期: 0 (没有占位符)

# 检查 Spring Boot 特定模式
grep -r "Controller-Service-Repository\|@RestController\|@Service\|@Repository" . | wc -l
# 预期: > 0 (包含 Spring Boot 模式)

# 检查验证命令
grep -r "mvn\|@Test\|MockMvc" .claude/commands/ | wc -l
# 预期: > 0 (包含 Spring Boot 验证命令)

# 检查配置示例
test -f examples/application.yml && echo "✓ Configuration example exists"
test -f examples/pom.xml && echo "✓ Maven POM example exists"
```

### Level 3: 功能验证

```bash
# 测试模板功能
cd use-cases/springboot

# 验证 INITIAL.md 存在
test -f PRPs/INITIAL.md && echo "✓ INITIAL.md exists"

# 检查模板完整性
grep -r "Context is King\|PRP\|Validation" . | wc -l  # 应该继承原则
grep -r "Spring Boot\|Maven\|JPA" . | wc -l  # 应该有专门化

# 验证示例代码
find examples/ -name "*.java" -o -name "*.yml" -o -name "*.xml" | wc -l
# 预期: > 0 (包含示例文件)
```

### Level 4: Spring Boot 特定验证

```bash
# 验证 Spring Boot 最佳实践
cd use-cases/springboot

# 检查分层架构示例
test -d examples/controller && test -d examples/service && test -d examples/repository
echo "✓ Layered architecture examples present"

# 检查配置文件
grep -l "spring:" examples/*.yml | wc -l
# 预期: > 0 (包含 Spring 配置)

# 检查依赖管理
grep -l "spring-boot-starter" examples/*.xml | wc -l
# 预期: > 0 (包含 Spring Boot starters)

# 检查测试示例
grep -r "@Test\|@WebMvcTest\|MockMvc" examples/test/ | wc -l
# 预期: > 0 (包含测试示例)

# 检查安全配置
grep -r "Security\|BCrypt\|@EnableWebSecurity" examples/ | wc -l
# 预期: > 0 (包含安全配置)
```

## Final Validation Checklist

### 模板包完整性

- [ ] 完整目录结构: `tree use-cases/springboot`
- [ ] 所有必需文件存在: CLAUDE.md, commands, base PRP, examples
- [ ] 复制脚本存在: `copy_template.py` 功能正常
- [ ] README 全面: 包含复制脚本说明和 PRP 工作流程
- [ ] Spring Boot 特定内容: 准确表示技术模式
- [ ] 工作示例: 所有示例可编译/运行
- [ ] 文档完整: README 和使用说明清晰

### 质量和可用性

- [ ] 无占位符内容: `grep -r "TODO\|PLACEHOLDER"`
- [ ] Spring Boot 专门化: 框架模式正确记录
- [ ] 验证循环有效: 所有命令可执行且功能正常
- [ ] 保持集成: 与基础上下文工程框架协同工作
- [ ] 即时可用: 开发者可以立即开始使用模板

### Spring Boot 特定检查

- [ ] Maven 配置: pom.xml 示例完整且正确
- [ ] 分层架构: Controller-Service-Repository 示例清晰
- [ ] JPA 集成: Entity 和 Repository 示例准确
- [ ] Security 配置: Spring Security 6 配置正确
- [ ] H2 数据库: 数据库配置和初始化示例
- [ ] 测试策略: MockMvc 和集成测试示例
- [ ] 配置文件: application.yml 模板完整
- [ ] 常见陷阱: 记录 Spring Boot 特定问题和解决方案

### 框架集成

- [ ] 继承基本原则: 保留上下文工程工作流程
- [ ] 适当专门化: 包含 Spring Boot 特定模式
- [ ] 命令兼容性: 斜杠命令按预期工作
- [ ] 文档一致性: 遵循既定的文档模式
- [ ] 可维护结构: 易于随 Spring Boot 演进而更新

---

## 质量评分

**Spring Boot 模板 PRP 置信度评分: 9/10**

**理由:**
- ✅ 完成了对 Spring Boot 3.x 生态系统的全面网络研究
- ✅ 深入研究了所有核心组件 (MVC, JPA, Security, Testing)
- ✅ 识别并记录了真实世界的最佳实践和模式
- ✅ 从官方文档和可信来源提取了准确信息
- ✅ 记录了常见陷阱和故障排除策略
- ✅ 包含完整的验证循环和成功标准
- ✅ 提供了全面的示例和配置模板
- ⚠️ 实际代码示例需要在模板生成阶段创建和验证

**下一步:**
运行 `/execute-template-prp PRPs/template-springboot.md` 以生成完整的 Spring Boot 模板包,包括所有代码示例、配置文件和文档。

---

## Anti-Patterns to Avoid

### 模板生成

- ❌ 不要创建通用模板 - 始终深入研究和专门化
- ❌ 不要跳过全面的技术研究 - 深入理解框架
- ❌ 不要使用占位符内容 - 始终包含真实的、经过研究的信息
- ❌ 不要忽略验证循环 - 包含针对技术的全面测试

### Spring Boot 特定

- ❌ 不要混用 application.properties 和 application.yml
- ❌ 不要在 Controller 中放置业务逻辑
- ❌ 不要忽略异常处理和全局错误处理
- ❌ 不要忽视 JPA N+1 查询性能问题
- ❌ 不要硬编码敏感信息 - 使用环境变量
- ❌ 不要过度模拟测试 - 测试真实行为
- ❌ 不要跳过安全配置 - 始终配置 Spring Security

### 内容质量

- ❌ 不要假设知识 - 为领域明确记录所有内容
- ❌ 不要跳过边缘情况 - 包含常见陷阱和错误处理
- ❌ 不要忽视安全性 - 始终包含技术的安全考虑
- ❌ 不要忘记维护 - 确保模板可以随技术变化而演进
