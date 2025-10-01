---
name: "模板生成器 PRP 基础"
description: "用于为特定技术领域和用例生成上下文工程模板的元模板"
---

## 目的

优化 AI agent 以为特定技术领域(AI 框架、前端堆栈、后端技术等)生成完整的上下文工程模板包,具有全面的领域专业化和验证。

## 核心原则

1. **元上下文工程**: 应用上下文工程原则来生成领域专用模板
2. **技术专业化**: 与目标框架模式和约定深度集成
3. **完整包生成**: 创建整个模板生态系统,而不仅仅是单个文件
4. **验证驱动**: 包括全面的领域适用测试和验证循环
5. **可用性优先**: 生成开发者可立即使用的模板

---

## 目标

为 **[目标技术]** 生成完整的上下文工程模板包,包括:

- 领域专用 CLAUDE.md 实施指南
- 专业化 PRP 生成和执行命令
- 技术适用的基础 PRP 模板
- 全面的示例和文档
- 领域专用验证循环和成功标准

## 原因

- **开发者加速**: 能够快速将上下文工程应用于任何技术
- **模式一致性**: 在所有领域保持上下文工程原则
- **质量保证**: 确保每种技术的全面验证和测试
- **知识捕获**: 记录特定技术的最佳实践和模式
- **可扩展框架**: 创建随技术变化而演进的可重用模板

## 内容

### 模板包组件

**完整目录结构:**
```
use-cases/{technology-name}/
├── CLAUDE.md                      # 领域实施指南
├── .claude/commands/
│   ├── generate-{technology}-prp.md  # 领域 PRP 生成
│   └── execute-{technology}-prp.md   # 领域 PRP 执行
├── PRPs/
│   ├── templates/
│   │   └── prp_{technology}_base.md  # 领域基础 PRP 模板
│   ├── ai_docs/                      # 领域文档(可选)
│   └── INITIAL.md                    # 示例功能请求
├── examples/                         # 领域代码示例
├── copy_template.py                  # 模板部署脚本
└── README.md                         # 全面的使用指南
```

**技术集成:**
- 框架专用工具和命令
- 架构模式和约定
- 开发工作流集成
- 测试和验证方法
- 安全和性能考虑因素

**上下文工程适配:**
- 领域专用研究流程
- 技术适用的验证循环
- 框架专业化的实施蓝图
- 与基础上下文工程原则集成

### 成功标准

- [ ] 生成完整的模板包结构
- [ ] 所有必需文件都存在且格式正确
- [ ] 领域专用内容准确表示技术模式
- [ ] 上下文工程原则已适当适配技术
- [ ] 验证循环适用且可为框架执行
- [ ] 模板可立即用于在该领域创建项目
- [ ] 保持与基础上下文工程框架的集成
- [ ] 包含全面的文档和示例

## 所需全部上下文

### 文档和参考资料(必读)

```yaml
# 上下文工程基础 - 理解基础框架
- file: ../../../README.md
  why: 要适配的核心上下文工程原则和工作流

- file: ../../../.claude/commands/generate-prp.md
  why: 为领域专业化的基础 PRP 生成模式

- file: ../../../.claude/commands/execute-prp.md
  why: 为技术适配的基础 PRP 执行模式

- file: ../../../PRPs/templates/prp_base.md
  why: 为领域专业化的基础 PRP 模板结构

# MCP SERVER 示例 - 领域专业化的参考实现
- file: ../mcp-server/CLAUDE.md
  why: 领域专用实施指南模式示例

- file: ../mcp-server/.claude/commands/prp-mcp-create.md
  why: 专业化 PRP 生成命令示例

- file: ../mcp-server/PRPs/templates/prp_mcp_base.md
  why: 领域专业化基础 PRP 模板示例

# 目标技术研究 - 添加领域专用文档
- url: [OFFICIAL_FRAMEWORK_DOCS]
  why: 核心框架概念、API 和架构模式

- url: [BEST_PRACTICES_GUIDE]
  why: 技术的既定模式和约定

- url: [SECURITY_CONSIDERATIONS]
  why: 安全最佳实践和常见漏洞

- url: [TESTING_FRAMEWORKS]
  why: 技术的测试方法和验证模式

- url: [DEPLOYMENT_PATTERNS]
  why: 生产部署和监控考虑因素
```

### 当前上下文工程结构

```bash
# 要扩展的基础框架结构
context-engineering-intro/
├── README.md                    # 要适配的核心原则
├── .claude/commands/            # 要专业化的基础命令
├── PRPs/templates/prp_base.md   # 要扩展的基础模板
├── CLAUDE.md                    # 要继承的基础规则
└── use-cases/
    ├── mcp-server/              # 参考专业化示例
    └── template-generator/      # 此元模板系统
```

### 目标技术分析要求

```typescript
// 技术专业化的研究领域
interface TechnologyAnalysis {
  // 核心框架模式
  architecture: {
    project_structure: string[];
    configuration_files: string[];
    dependency_management: string;
    module_organization: string[];
  };

  // 开发工作流
  development: {
    package_manager: string;
    dev_server_commands: string[];
    build_process: string[];
    testing_frameworks: string[];
  };

  // 最佳实践
  patterns: {
    code_organization: string[];
    state_management: string[];
    error_handling: string[];
    performance_optimization: string[];
  };

  // 集成点
  ecosystem: {
    common_libraries: string[];
    deployment_platforms: string[];
    monitoring_tools: string[];
    CI_CD_patterns: string[];
  };
}
```

### 已知模板生成模式

```typescript
// 关键: 模板生成必须遵循这些模式

// 1. 始终从基础上下文工程原则继承
const basePatterns = {
  prp_workflow: "INITIAL.md → generate-prp → execute-prp",
  validation_loops: "语法 → 单元 → 集成 → 部署",
  context_richness: "文档 + 示例 + 模式 + 陷阱"
};

// 2. 始终为目标技术专业化
const specialization = {
  tooling: "用框架专用命令替换通用命令",
  patterns: "包括框架架构约定",
  validation: "使用技术适用的测试和 linting",
  examples: "为领域提供真实的、工作的代码示例"
};

// 3. 始终保持可用性和完整性
const quality_gates = {
  immediate_usability: "模板开箱即用",
  comprehensive_docs: "所有模式和陷阱都已记录",
  working_examples: "示例编译并成功运行",
  validation_loops: "所有验证命令都可执行"
};

// 4. 要避免的常见陷阱
const anti_patterns = {
  generic_content: "不要使用占位符文本 - 研究实际模式",
  incomplete_research: "不要跳过技术专用文档",
  broken_examples: "不要包含非工作代码示例",
  missing_validation: "不要跳过领域适用的测试模式"
};
```

## 实施蓝图

### 技术研究阶段

**关键: 在任何模板生成之前进行广泛的网络搜索。这对成功至关重要。**

使用网络研究对目标技术进行全面分析:

```yaml
研究任务 1 - 核心框架分析(需要网络搜索):
  网络搜索并彻底研究官方文档:
    - 框架架构和设计模式
    - 项目结构约定和最佳实践
    - 配置文件模式和管理方法
    - 技术的包/依赖管理
    - 入门指南和设置程序

研究任务 2 - 开发工作流分析(需要网络搜索):
  网络搜索并分析开发模式:
    - 本地开发设置和工具
    - 构建过程和编译步骤
    - 此技术常用的测试框架
    - 调试工具和开发环境
    - CLI 命令和包管理工作流

研究任务 3 - 最佳实践调查(需要网络搜索):
  网络搜索并研究既定模式:
    - 代码组织和文件结构约定
    - 此技术专用的安全最佳实践
    - 常见陷阱、缺陷和边缘情况
    - 错误处理模式和策略
    - 性能考虑因素和优化技术

研究任务 4 - 模板包结构规划:
  计划如何为此技术创建上下文工程模板:
    - 如何为此特定技术适配 PRP 框架
    - 需要什么领域专用 CLAUDE.md 规则
    - 什么验证循环适用于此框架
    - 应该包含哪些示例和文档
```

### 模板包生成

基于网络研究结果创建完整的上下文工程模板包:

```yaml
生成任务 1 - 创建模板目录结构:
  CREATE 完整的用例目录结构:
    - use-cases/{technology-name}/
    - .claude/commands/ 子目录
    - PRPs/templates/ 子目录
    - examples/ 子目录
    - 每个模板包要求的所有其他必需子目录

生成任务 2 - 生成领域专用 CLAUDE.md:
  CREATE 技术专用全局规则文件:
    - 技术专用工具和包管理命令
    - 来自网络研究的框架架构模式和约定
    - 此技术专用的开发工作流程序
    - 通过研究发现的安全和最佳实践
    - 在文档中找到的常见陷阱和集成点

生成任务 3 - 创建专业化模板 PRP 命令:
  GENERATE 领域专用斜杠命令:
    - generate-{technology}-prp.md 带技术研究模式
    - execute-{technology}-prp.md 带框架验证循环
    - 命令应引用研究中的技术专用模式
    - 包括此技术领域专用的网络搜索策略

生成任务 4 - 开发领域专用基础 PRP 模板:
  CREATE 专业化 prp_{technology}_base.md 模板:
    - 预填充来自网络研究的技术上下文
    - 技术专用成功标准和验证关卡
    - 通过研究找到的框架文档引用
    - 领域适用的实施模式和验证循环

生成任务 5 - 创建示例和 INITIAL.md 模板:
  GENERATE 全面的模板包内容:
    - INITIAL.md 示例,展示如何请求此技术的功能
    - 与技术相关的工作代码示例(来自研究)
    - 配置文件模板和模式

生成任务 6 - 创建模板复制脚本:
  CREATE 用于模板部署的 Python 脚本:
    - copy_template.py 脚本,接受目标目录参数
    - 将整个模板目录结构复制到指定位置
    - 包括所有文件: CLAUDE.md、命令、PRP、示例等
    - 处理目录创建和文件复制,带错误处理
    - 简单的命令行界面,易于使用

生成任务 7 - 生成全面的 README:
  CREATE 全面但简洁的 README.md:
    - 清晰描述此模板的用途和目的
    - PRP 框架工作流说明(3 步过程)
    - 模板复制脚本使用说明(在顶部显著位置)
    - 带具体示例的快速入门指南
    - 模板结构概述,显示所有生成的文件
    - 此技术领域专用的使用示例
```

### 复制脚本和 README 的实施细节

**复制脚本 (copy_template.py) 要求:**
```python
# 基本复制脚本功能:
# 1. 接受目标目录作为命令行参数
# 2. 将整个模板目录结构复制到目标位置
# 3. 包括所有文件: CLAUDE.md、.claude/、PRPs/、examples/、README.md
# 4. 处理目录创建和错误处理
# 5. 提供清晰的成功反馈和后续步骤
# 6. 简单使用: python copy_template.py /path/to/target
```

**README 结构要求:**
```markdown
# 必须按此顺序包含这些部分:
# 1. 模板目的的标题和简要说明
# 2. 🚀 快速入门 - 首先复制模板(在顶部显著位置)
# 3. 📋 PRP 框架工作流(3 步过程说明)
# 4. 📁 模板结构(带说明的目录树)
# 5. 🎯 您可以构建什么(技术专用示例)
# 6. 📚 主要功能(框架功能)
# 7. 🔍 包含的示例(提供的工作示例)
# 8. 📖 文档引用(研究来源)
# 9. 🚫 常见陷阱(技术专用陷阱)

# 复制脚本使用必须在顶部显著显示
# PRP 工作流必须清楚地显示带有实际命令的 3 个步骤
# 一切都应该是技术专用的,而不是通用的
```

### 领域专业化细节

```typescript
// 特定领域的模板专业化模式

// 对于 AI/ML 框架(Pydantic AI、CrewAI 等)
const ai_specialization = {
  patterns: ["agent_architecture", "tool_integration", "model_configuration"],
  validation: ["model_response_testing", "agent_behavior_validation"],
  examples: ["basic_agent", "multi_agent_system", "tool_integration"],
  gotchas: ["token_limits", "model_compatibility", "async_patterns"]
};

// 对于前端框架(React、Vue、Svelte 等)
const frontend_specialization = {
  patterns: ["component_architecture", "state_management", "routing"],
  validation: ["component_testing", "e2e_testing", "accessibility"],
  examples: ["basic_app", "state_integration", "api_consumption"],
  gotchas: ["bundle_size", "ssr_considerations", "performance"]
};

// 对于后端框架(FastAPI、Express、Django 等)
const backend_specialization = {
  patterns: ["api_design", "database_integration", "authentication"],
  validation: ["api_testing", "database_testing", "security_testing"],
  examples: ["rest_api", "auth_system", "database_models"],
  gotchas: ["security_vulnerabilities", "performance_bottlenecks", "scalability"]
};

// 对于数据库/数据框架(SQLModel、Prisma 等)
const data_specialization = {
  patterns: ["schema_design", "migration_management", "query_optimization"],
  validation: ["schema_testing", "migration_testing", "query_performance"],
  examples: ["basic_models", "relationships", "complex_queries"],
  gotchas: ["migration_conflicts", "n+1_queries", "index_optimization"]
};
```

### 集成点

```yaml
CONTEXT_ENGINEERING_FRAMEWORK:
  - base_workflow: 从基础框架继承核心 PRP 生成和执行模式
  - validation_principles: 使用技术的领域专用检查扩展基础验证
  - documentation_standards: 保持与基础上下文工程文档模式的一致性

TECHNOLOGY_INTEGRATION:
  - package_management: 包括框架专用包管理器和工具
  - development_tools: 包括技术专用开发和测试工具
  - framework_patterns: 使用技术适用的架构和代码模式
  - validation_approaches: 包括框架专用测试和验证方法

TEMPLATE_STRUCTURE:
  - directory_structure: 遵循基础框架的既定用例模板模式
  - file_naming: 保持一致的命名约定(generate-{tech}-prp.md 等)
  - content_format: 使用既定的 markdown 和文档格式
  - command_patterns: 为特定技术扩展基础斜杠命令功能
```

## 验证循环

### 级别 1: 模板结构验证

```bash
# 关键: 验证完整的模板包结构
find use-cases/{technology-name} -type f | sort
ls -la use-cases/{technology-name}/.claude/commands/
ls -la use-cases/{technology-name}/PRPs/templates/

# 验证复制脚本存在且功能正常
test -f use-cases/{technology-name}/copy_template.py
python use-cases/{technology-name}/copy_template.py --help 2>/dev/null || echo "复制脚本需要帮助选项"

# 预期: 所有必需文件都存在,包括 copy_template.py
# 如果缺失: 按照既定模式生成缺失的文件
```

### 级别 2: 内容质量验证

```bash
# 验证领域专用内容准确性
grep -r "TODO\|PLACEHOLDER\|{domain}" use-cases/{technology-name}/
grep -r "{technology}" use-cases/{technology-name}/ | wc -l

# 检查技术专用模式
grep -r "framework-specific-pattern" use-cases/{technology-name}/
grep -r "validation" use-cases/{technology-name}/.claude/commands/

# 预期: 无占位符内容,存在技术模式
# 如果有问题: 研究并添加适当的领域专用内容
```

### 级别 3: 功能验证

```bash
# 测试模板功能
cd use-cases/{technology-name}

# 测试 PRP 生成命令
/generate-prp INITIAL.md
ls PRPs/*.md | grep -v templates

# 测试模板完整性
grep -r "Context is King" . | wc -l  # 应该继承原则
grep -r "{technology-specific}" . | wc -l  # 应该有专业化

# 预期: PRP 生成工作,内容已专业化
# 如果失败: 调试命令模式和模板结构
```

### 级别 4: 集成测试

```bash
# 验证与基础上下文工程框架的集成
diff -r ../../.claude/commands/ .claude/commands/ | head -20
diff ../../CLAUDE.md CLAUDE.md | head -20

# 测试模板产生工作结果
cd examples/
# 运行任何技术专用的示例验证命令

# 预期: 适当的专业化,不破坏基础模式
# 如果有问题: 调整专业化以保持兼容性
```

## 最终验证清单

### 模板包完整性

- [ ] 完整的目录结构: `tree use-cases/{technology-name}`
- [ ] 所有必需文件都存在: CLAUDE.md、命令、基础 PRP、示例
- [ ] 复制脚本存在: 带有适当功能的 `copy_template.py`
- [ ] README 全面: 包括复制脚本说明和 PRP 工作流
- [ ] 领域专用内容: 技术模式准确表示
- [ ] 工作示例: 所有示例编译/运行成功
- [ ] 文档完整: README 和使用说明清晰

### 质量和可用性

- [ ] 无占位符内容: `grep -r "TODO\|PLACEHOLDER"`
- [ ] 技术专业化: 框架模式已正确记录
- [ ] 验证循环工作: 所有命令可执行且功能正常
- [ ] 保持集成: 适用于基础上下文工程框架
- [ ] 准备使用: 开发者可以立即开始使用模板

### 框架集成

- [ ] 继承基础原则: 保留上下文工程工作流
- [ ] 适当的专业化: 包括技术专用模式
- [ ] 命令兼容性: 斜杠命令按预期工作
- [ ] 文档一致性: 遵循既定的文档模式
- [ ] 可维护结构: 随着技术的发展易于更新

---

## 要避免的反模式

### 模板生成

- ❌ 不要创建通用模板 - 始终深入研究和专业化
- ❌ 不要跳过全面的技术研究 - 彻底理解框架
- ❌ 不要使用占位符内容 - 始终包含真实的、经过研究的信息
- ❌ 不要忽略验证循环 - 包括技术的全面测试

### 内容质量

- ❌ 不要假设知识 - 为领域明确记录所有内容
- ❌ 不要跳过边缘情况 - 包括常见陷阱和错误处理
- ❌ 不要忽略安全性 - 始终包括技术的安全考虑因素
- ❌ 不要忘记维护 - 确保模板可以随技术变化而演进

### 框架集成

- ❌ 不要破坏基础模式 - 保持与上下文工程原则的兼容性
- ❌ 不要重复工作 - 重用和扩展基础框架组件
- ❌ 不要忽略一致性 - 遵循既定的命名和结构约定
- ❌ 不要跳过验证 - 在完成之前确保模板实际工作
