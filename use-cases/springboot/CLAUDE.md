# Spring Boot 上下文工程 - 全局规则

本文件包含 Spring Boot 3.x 项目开发的全局规则和最佳实践,这些规则适用于所有 Spring Boot 上下文工程工作。

## 🔄 Spring Boot 核心原则

**重要提示: 这些原则适用于所有 Spring Boot 开发工作:**

### 分层架构模式
- **严格遵守 Controller-Service-Repository 分层** - 每一层都有明确的职责
- **Controller 层只处理 HTTP 请求和响应** - 不包含业务逻辑
- **Service 层包含所有业务逻辑** - 这是核心逻辑所在
- **Repository 层负责数据访问** - 使用 Spring Data JPA
- **使用 DTO 在层之间传输数据** - Entity 仅用于 JPA 映射

### 配置管理
- **始终使用 YAML 格式** - application.yml 而不是 application.properties
- **使用 profile-specific 配置** - application-dev.yml, application-prod.yml
- **永远不要硬编码敏感信息** - 使用环境变量或配置服务器
- **使用 @ConfigurationProperties** - 类型安全的配置绑定

### 测试策略
- **为每一层编写测试** - 单元测试和集成测试
- **使用 @WebMvcTest** - 测试 Controller 层
- **使用 @DataJpaTest** - 测试 Repository 层
- **使用 MockMvc** - 模拟 HTTP 请求
- **避免过度模拟** - 测试真实行为,不是模拟行为

## 📚 项目感知和上下文

### Maven 项目结构
```
src/main/java/com/example/demo/
├── controller/          # REST 控制器
│   ├── UserController.java
│   └── ProductController.java
├── service/             # 业务服务
│   ├── UserService.java
│   └── ProductService.java
├── repository/          # 数据仓库
│   ├── UserRepository.java
│   └── ProductRepository.java
├── model/               # JPA 实体
│   ├── User.java
│   └── Product.java
├── dto/                 # 数据传输对象
│   ├── UserDTO.java
│   └── ProductDTO.java
├── config/              # 配置类
│   ├── SecurityConfig.java
│   └── DatabaseConfig.java
├── exception/           # 自定义异常
│   ├── ResourceNotFoundException.java
│   └── GlobalExceptionHandler.java
└── DemoApplication.java # 主应用类

src/main/resources/
├── application.yml      # 主配置文件
├── application-dev.yml  # 开发环境配置
├── application-prod.yml # 生产环境配置
└── data.sql             # 初始化数据(可选)

src/test/java/com/example/demo/
├── controller/          # Controller 测试
├── service/             # Service 测试
├── repository/          # Repository 测试
└── integration/         # 集成测试
```

### 依赖管理
```xml
<!-- 始终使用 spring-boot-starter-parent -->
<parent>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-parent</artifactId>
    <version>3.2.x</version>
</parent>

<!-- 核心 starters -->
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

## 🧱 代码结构和模块化

### Controller 层最佳实践
```java
@RestController
@RequestMapping("/api/users")
public class UserController {

    private final UserService userService;

    // 使用构造器注入(推荐)
    public UserController(UserService userService) {
        this.userService = userService;
    }

    @GetMapping
    public ResponseEntity<List<UserDTO>> getAllUsers() {
        return ResponseEntity.ok(userService.getAllUsers());
    }

    @GetMapping("/{id}")
    public ResponseEntity<UserDTO> getUserById(@PathVariable Long id) {
        return ResponseEntity.ok(userService.getUserById(id));
    }

    @PostMapping
    public ResponseEntity<UserDTO> createUser(@Valid @RequestBody UserDTO userDTO) {
        return ResponseEntity.status(HttpStatus.CREATED)
            .body(userService.createUser(userDTO));
    }
}
```

### Service 层最佳实践
```java
@Service
public class UserService {

    private final UserRepository userRepository;

    public UserService(UserRepository userRepository) {
        this.userRepository = userRepository;
    }

    @Transactional(readOnly = true)
    public List<UserDTO> getAllUsers() {
        return userRepository.findAll().stream()
            .map(this::convertToDTO)
            .collect(Collectors.toList());
    }

    @Transactional
    public UserDTO createUser(UserDTO userDTO) {
        User user = convertToEntity(userDTO);
        User savedUser = userRepository.save(user);
        return convertToDTO(savedUser);
    }

    private UserDTO convertToDTO(User user) {
        // 转换逻辑
    }
}
```

### Repository 层最佳实践
```java
@Repository
public interface UserRepository extends JpaRepository<User, Long> {

    Optional<User> findByEmail(String email);

    @Query("SELECT u FROM User u WHERE u.active = true")
    List<User> findAllActiveUsers();

    // 使用 @EntityGraph 避免 N+1 问题
    @EntityGraph(attributePaths = {"roles", "profile"})
    Optional<User> findWithRolesAndProfileById(Long id);
}
```

### Entity 层最佳实践
```java
@Entity
@Table(name = "users")
public class User {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false, unique = true)
    private String email;

    @Column(nullable = false)
    private String password;

    // 使用懒加载优化性能
    @OneToMany(mappedBy = "user", fetch = FetchType.LAZY, cascade = CascadeType.ALL)
    private List<Order> orders = new ArrayList<>();

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "role_id")
    private Role role;

    // Getters and Setters
}
```

## 🧪 测试和可靠性

### Controller 测试
```java
@WebMvcTest(UserController.class)
class UserControllerTest {

    @Autowired
    private MockMvc mockMvc;

    @MockBean
    private UserService userService;

    @Test
    void shouldReturnAllUsers() throws Exception {
        List<UserDTO> users = Arrays.asList(new UserDTO(1L, "test@example.com"));
        when(userService.getAllUsers()).thenReturn(users);

        mockMvc.perform(get("/api/users"))
            .andExpect(status().isOk())
            .andExpect(jsonPath("$[0].email").value("test@example.com"));
    }
}
```

### Service 测试
```java
@ExtendWith(MockitoExtension.class)
class UserServiceTest {

    @Mock
    private UserRepository userRepository;

    @InjectMocks
    private UserService userService;

    @Test
    void shouldCreateUser() {
        User user = new User("test@example.com", "password");
        when(userRepository.save(any(User.class))).thenReturn(user);

        UserDTO result = userService.createUser(new UserDTO("test@example.com"));

        assertNotNull(result);
        assertEquals("test@example.com", result.getEmail());
    }
}
```

### Repository 测试
```java
@DataJpaTest
class UserRepositoryTest {

    @Autowired
    private UserRepository userRepository;

    @Test
    void shouldFindUserByEmail() {
        User user = new User("test@example.com", "password");
        userRepository.save(user);

        Optional<User> found = userRepository.findByEmail("test@example.com");

        assertTrue(found.isPresent());
        assertEquals("test@example.com", found.get().getEmail());
    }
}
```

## ✅ 开发工作流程

### 本地开发命令
```bash
# 运行应用程序
mvn spring-boot:run

# 编译项目
mvn clean compile

# 运行所有测试
mvn test

# 打包应用程序
mvn clean package

# 跳过测试打包(仅在必要时)
mvn clean package -DskipTests

# 运行打包的 JAR
java -jar target/application-name-0.0.1-SNAPSHOT.jar
```

### 配置文件管理
```yaml
# application.yml - 默认配置
spring:
  application:
    name: demo-app
  profiles:
    active: dev

---
# application-dev.yml - 开发环境
spring:
  h2:
    console:
      enabled: true
  datasource:
    url: jdbc:h2:mem:testdb
  jpa:
    show-sql: true
    hibernate:
      ddl-auto: create-drop

---
# application-prod.yml - 生产环境
spring:
  datasource:
    url: ${DB_URL}
    username: ${DB_USERNAME}
    password: ${DB_PASSWORD}
  jpa:
    hibernate:
      ddl-auto: validate
    show-sql: false
```

## 📎 样式和约定

### 命名约定
- **类名**: PascalCase (UserController, UserService)
- **方法名**: camelCase (getUserById, createUser)
- **包名**: 全小写 (com.example.demo.controller)
- **常量**: UPPER_SNAKE_CASE (MAX_RETRY_COUNT)

### 注解使用
```java
// Controller 注解
@RestController      // REST API 控制器
@RequestMapping      // 基础路径映射
@GetMapping          // HTTP GET
@PostMapping         // HTTP POST
@PutMapping          // HTTP PUT
@DeleteMapping       // HTTP DELETE
@PathVariable        // 路径变量
@RequestParam        // 查询参数
@RequestBody         // 请求体
@Valid               // 数据验证

// Service 注解
@Service             // 服务层组件
@Transactional       // 事务管理

// Repository 注解
@Repository          // 仓库层组件
@Query               // 自定义查询
@EntityGraph         // 解决 N+1 问题

// Entity 注解
@Entity              // JPA 实体
@Table               // 表名映射
@Id                  // 主键
@GeneratedValue      // 主键生成策略
@Column              // 列映射
@OneToMany           // 一对多关系
@ManyToOne           // 多对一关系
@JoinColumn          // 外键列
```

## 📚 文档和可解释性

### Javadoc 注释
```java
/**
 * 用户服务类,处理所有用户相关的业务逻辑
 *
 * @author Your Name
 * @version 1.0
 * @since 2024-01-01
 */
@Service
public class UserService {

    /**
     * 根据 ID 获取用户
     *
     * @param id 用户 ID
     * @return 用户 DTO
     * @throws ResourceNotFoundException 如果用户不存在
     */
    public UserDTO getUserById(Long id) {
        // 实现
    }
}
```

## 🧠 Spring Boot 行为规则

### 异常处理
```java
@ControllerAdvice
public class GlobalExceptionHandler {

    @ExceptionHandler(ResourceNotFoundException.class)
    public ResponseEntity<ErrorResponse> handleResourceNotFound(
            ResourceNotFoundException ex) {
        ErrorResponse error = new ErrorResponse(
            HttpStatus.NOT_FOUND.value(),
            ex.getMessage(),
            LocalDateTime.now()
        );
        return ResponseEntity.status(HttpStatus.NOT_FOUND).body(error);
    }

    @ExceptionHandler(Exception.class)
    public ResponseEntity<ErrorResponse> handleGlobalException(Exception ex) {
        ErrorResponse error = new ErrorResponse(
            HttpStatus.INTERNAL_SERVER_ERROR.value(),
            "Internal server error occurred",
            LocalDateTime.now()
        );
        return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body(error);
    }
}
```

### 安全配置
```java
@Configuration
@EnableWebSecurity
public class SecurityConfig {

    @Bean
    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
        http
            .csrf(csrf -> csrf.disable())  // 仅在开发时禁用
            .authorizeHttpRequests(auth -> auth
                .requestMatchers("/api/public/**").permitAll()
                .requestMatchers("/api/admin/**").hasRole("ADMIN")
                .anyRequest().authenticated()
            )
            .httpBasic(Customizer.withDefaults());

        return http.build();
    }

    @Bean
    public PasswordEncoder passwordEncoder() {
        return new BCryptPasswordEncoder();
    }
}
```

## 🚫 必须避免的反模式

### 代码组织
- ❌ **不要在 Controller 中编写业务逻辑** - 使用 Service 层
- ❌ **不要直接在 Controller 中使用 Repository** - 通过 Service 访问
- ❌ **不要混用 Entity 和 DTO** - 保持清晰的边界
- ❌ **不要在 Entity 中包含业务逻辑** - Entity 只是数据模型

### 依赖管理
- ❌ **不要手动指定 Spring 依赖版本** - 使用 starter parent 管理
- ❌ **不要混用不同版本的 Spring 依赖** - 保持版本一致性

### 性能
- ❌ **不要忽视 N+1 查询问题** - 使用 @EntityGraph 或 JOIN FETCH
- ❌ **不要对所有关系使用 EAGER 加载** - 默认使用 LAZY
- ❌ **不要在循环中执行数据库查询** - 使用批量操作

### 安全
- ❌ **不要硬编码密码或密钥** - 使用环境变量
- ❌ **不要在生产环境禁用 CSRF** - 除非有充分理由
- ❌ **不要记录敏感信息** - 密码、token 等

### 测试
- ❌ **不要跳过测试** - 测试是质量保证的关键
- ❌ **不要过度模拟** - 测试真实行为
- ❌ **不要在测试中使用真实的外部服务** - 使用模拟或测试容器

## 🔍 常见陷阱和解决方案

### 1. N+1 查询问题
**问题**: JPA 懒加载导致多次数据库查询
```java
// ❌ 错误 - 会产生 N+1 查询
List<User> users = userRepository.findAll();
users.forEach(user -> {
    System.out.println(user.getOrders().size());  // 每个用户一次查询
});

// ✅ 正确 - 使用 @EntityGraph
@EntityGraph(attributePaths = {"orders"})
List<User> findAllWithOrders();
```

### 2. 事务管理
**问题**: 忘记添加 @Transactional 导致懒加载失败
```java
// ❌ 错误 - LazyInitializationException
public UserDTO getUserWithOrders(Long id) {
    User user = userRepository.findById(id).orElseThrow();
    return convertToDTO(user);  // orders 懒加载失败
}

// ✅ 正确 - 添加 @Transactional
@Transactional(readOnly = true)
public UserDTO getUserWithOrders(Long id) {
    User user = userRepository.findById(id).orElseThrow();
    return convertToDTO(user);
}
```

### 3. 循环依赖
**问题**: 服务之间相互注入导致循环依赖
```java
// ❌ 错误 - 循环依赖
@Service
public class UserService {
    @Autowired
    private OrderService orderService;
}

@Service
public class OrderService {
    @Autowired
    private UserService userService;
}

// ✅ 正确 - 重构为单向依赖或提取共享服务
```

### 4. DTO 和 Entity 混用
**问题**: 直接返回 Entity 导致序列化问题
```java
// ❌ 错误 - 直接返回 Entity
@GetMapping("/{id}")
public User getUser(@PathVariable Long id) {
    return userRepository.findById(id).orElseThrow();
}

// ✅ 正确 - 使用 DTO
@GetMapping("/{id}")
public UserDTO getUser(@PathVariable Long id) {
    User user = userRepository.findById(id).orElseThrow();
    return convertToDTO(user);
}
```

这些全局规则确保 Spring Boot 项目遵循最佳实践,提高代码质量和可维护性。
