# Execute Spring Boot PRP

执行 Spring Boot PRP 以创建完整的、可立即运行的 Spring Boot 应用程序,遵循分层架构和最佳实践。

## PRP 文件: PRPs/{feature-name}.md

## 执行流程

### 1. 加载 Spring Boot PRP
- 完整读取指定的 PRP 文件
- 理解所有 Spring Boot 要求和架构
- 审查 PRP 中记录的所有网络研究发现
- 遵循项目结构和实现的所有说明

### 2. 创建 Maven 项目结构
```bash
# 创建标准 Maven/Spring Boot 目录结构
src/main/java/com/{groupId}/{artifactId}/
├── controller/
├── service/
├── repository/
├── model/
├── dto/
├── config/
└── {Artifact}Application.java

src/main/resources/
├── application.yml
└── application-dev.yml

src/test/java/com/{groupId}/{artifactId}/
├── controller/
├── service/
└── repository/
```

### 3. 生成 Maven POM
基于 PRP 研究创建 `pom.xml`:
```xml
<parent>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-parent</artifactId>
    <version>3.2.x</version>
</parent>

<dependencies>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
    </dependency>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-data-jpa</artifactId>
    </dependency>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-security</artifactId>
    </dependency>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-test</artifactId>
        <scope>test</scope>
    </dependency>
    <dependency>
        <groupId>com.h2database</groupId>
        <artifactId>h2</artifactId>
        <scope>runtime</scope>
    </dependency>
</dependencies>
```

### 4. 实现分层架构

**Model 层 (Entity)**:
```java
@Entity
@Table(name = "entities")
public class EntityName {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    // 字段、关系、getters/setters
}
```

**Repository 层**:
```java
@Repository
public interface EntityRepository extends JpaRepository<EntityName, Long> {
    // 自定义查询方法
}
```

**Service 层**:
```java
@Service
public class EntityService {
    private final EntityRepository repository;

    public EntityService(EntityRepository repository) {
        this.repository = repository;
    }

    @Transactional(readOnly = true)
    public List<EntityDTO> findAll() {
        // 实现
    }
}
```

**Controller 层**:
```java
@RestController
@RequestMapping("/api/entities")
public class EntityController {
    private final EntityService service;

    public EntityController(EntityService service) {
        this.service = service;
    }

    @GetMapping
    public ResponseEntity<List<EntityDTO>> getAll() {
        return ResponseEntity.ok(service.findAll());
    }
}
```

### 5. 配置文件

**application.yml**:
```yaml
spring:
  application:
    name: application-name
  h2:
    console:
      enabled: true
  datasource:
    url: jdbc:h2:mem:testdb
    username: sa
    password:
  jpa:
    hibernate:
      ddl-auto: create-drop
    show-sql: true
```

### 6. 实现测试

**Controller 测试**:
```java
@WebMvcTest(EntityController.class)
class EntityControllerTest {
    @Autowired private MockMvc mockMvc;
    @MockBean private EntityService service;

    @Test
    void shouldGetAllEntities() throws Exception {
        mockMvc.perform(get("/api/entities"))
            .andExpect(status().isOk());
    }
}
```

**Service 测试**:
```java
@ExtendWith(MockitoExtension.class)
class EntityServiceTest {
    @Mock private EntityRepository repository;
    @InjectMocks private EntityService service;

    @Test
    void shouldFindAll() {
        // 测试实现
    }
}
```

**Repository 测试**:
```java
@DataJpaTest
class EntityRepositoryTest {
    @Autowired private EntityRepository repository;

    @Test
    void shouldSaveEntity() {
        // 测试实现
    }
}
```

## 验证循环

### Level 1: 项目结构验证
```bash
# 验证 Maven 项目结构
test -f pom.xml && echo "✓ POM 存在"
test -d src/main/java && echo "✓ 源代码目录存在"
test -d src/main/resources && echo "✓ 资源目录存在"
test -d src/test/java && echo "✓ 测试目录存在"
```

### Level 2: 编译验证
```bash
# Maven 验证和编译
mvn validate
mvn clean compile
```

### Level 3: 测试验证
```bash
# 运行所有测试
mvn test

# 检查测试覆盖率
# 确保所有层都有测试
```

### Level 4: 应用程序验证
```bash
# 构建应用程序
mvn clean package

# 运行应用程序
mvn spring-boot:run

# 验证端点 (在另一个终端)
curl http://localhost:8080/api/entities
```

## 成功标准

- [ ] Maven 项目结构完整且正确
- [ ] 所有依赖正确配置在 pom.xml
- [ ] 遵循 Controller-Service-Repository 分层架构
- [ ] 所有实体正确定义 JPA 注解
- [ ] 仓库扩展 JpaRepository
- [ ] 服务包含业务逻辑和事务管理
- [ ] 控制器正确处理 HTTP 请求
- [ ] application.yml 配置完整
- [ ] 为所有层实现测试
- [ ] 项目成功编译: `mvn compile`
- [ ] 所有测试通过: `mvn test`
- [ ] 应用程序成功运行: `mvn spring-boot:run`
- [ ] API 端点可访问并返回正确响应

注意: 如果任何验证失败,分析错误,修复代码,并重新验证,直到所有标准通过。应用程序必须是生产就绪的,并立即可用。
