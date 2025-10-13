# Generate Spring Boot PRP

从 INITIAL.md 功能请求生成 Spring Boot 特定的 PRP (Plan-Research-Prompt)。

## 功能文件: PRPs/INITIAL.md

根据 INITIAL.md 中的详细需求,生成一个全面的 Spring Boot PRP。这遵循标准的 PRP 框架工作流程: INITIAL.md → generate-springboot-prp → execute-springboot-prp。

**关键: 网络搜索和文档研究是你最好的朋友。在整个过程中广泛使用它们。**

## 研究流程

### 1. 读取并理解需求
- 彻底阅读指定的 INITIAL.md 文件
- 理解目标 Spring Boot 功能和具体要求
- 注意提到的任何特定功能、示例或文档
- 确定所需 Spring Boot 功能的范围和复杂性

### 2. 广泛的网络研究 (关键)
**Spring Boot 特定研究领域:**
- **官方文档**: 搜索 Spring Boot 3.x 官方文档和指南
- **分层架构**: 研究 Controller-Service-Repository 模式最佳实践
- **Spring Data JPA**: 调查 Entity 关系、查询方法和性能优化
- **Spring Security**: 搜索 Spring Security 6 配置和认证模式
- **测试策略**: 研究 MockMvc、@WebMvcTest、@DataJpaTest 测试模式
- **H2 数据库**: 查找 H2 配置和 application.yml 示例
- **Maven 配置**: 搜索 pom.xml 最佳实践和依赖管理
- **常见陷阱**: 识别 Spring Boot 常见错误和故障排除指南

### 3. 技术模式分析
- 检查通过网络研究找到的成功实现
- 确定项目结构和文件组织模式
- 提取可重用的代码模式和配置模板
- 记录特定于框架的开发工作流程
- 注意测试框架和验证方法

### 4. 上下文工程适配
- 将发现的 Spring Boot 模式映射到上下文工程原则
- 规划如何为 Spring Boot 适配 PRP 框架
- 设计特定于域的验证要求
- 规划分层架构实现蓝图

## PRP 生成

使用 PRPs/templates/prp_springboot_base.md 作为基础:

### 从网络研究中包含的关键上下文

**Spring Boot 文档 (来自网络搜索)**:
- 官方 Spring Boot 3.x 文档 URL 和具体章节
- Controller-Service-Repository 模式指南
- Spring Data JPA 最佳实践
- Spring Security 6 配置指南
- MockMvc 测试教程

**实现模式 (来自研究)**:
- 分层架构项目结构
- Maven pom.xml 依赖配置
- application.yml 配置模板
- Entity 关系注解模式
- REST API 控制器设计

**真实示例**:
- 在线找到的成功实现链接
- 代码片段和配置示例
- 常见集成模式
- 测试策略和验证方法

### 实现蓝图

基于网络研究发现:
- **Spring Boot 分析**: 记录框架特征和模式
- **项目结构**: 规划完整的 Maven 项目组件
- **验证设计**: Spring Boot 适当的测试和验证循环

### 验证门 (必须可执行)

```bash
# Maven 项目验证
test -f pom.xml && echo "✓ Maven POM 存在"
mvn validate

# 项目结构验证
test -d src/main/java && test -d src/main/resources
test -d src/test/java

# Spring Boot 配置验证
test -f src/main/resources/application.yml
grep -q "spring:" src/main/resources/application.yml

# 编译验证
mvn clean compile

# 测试验证
mvn test
```

*** 关键: 在编写 PRP 之前进行广泛的网络研究 ***
*** 广泛使用 WebSearch 工具深入理解 Spring Boot ***

## 输出

保存为: `PRPs/feature-{feature-name}.md`

## 质量检查表

- [ ] 完成了目标 Spring Boot 功能的广泛网络研究
- [ ] 彻底审查了官方 Spring Boot 和 Spring Data JPA 文档
- [ ] 识别了真实示例和 Maven 项目模式
- [ ] 规划了完整的分层架构项目结构
- [ ] 设计了 Spring Boot 特定的验证
- [ ] 所有网络研究发现都记录在 PRP 中
- [ ] 捕获了 Spring Boot 特定的陷阱和模式

在 1-10 的范围内对 PRP 进行评分(基于彻底的技术研究,创建全面、立即可用的 Spring Boot 实现的置信度)。

记住: 目标是创建完整的、专门的 Spring Boot PRP,通过全面的研究和文档使上下文工程应用变得简单。
