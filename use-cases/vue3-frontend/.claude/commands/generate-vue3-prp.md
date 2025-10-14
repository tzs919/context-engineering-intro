# Generate Vue 3 PRP

## 功能文件: {feature_file}

为 Vue 3 前端功能请求生成全面的 PRP（项目需求文档），包含组件架构、状态管理、路由配置、测试策略和 Material Design 实现。

**关键：Web 搜索和文档研究是最佳伙伴。在整个过程中广泛使用。**

## 研究过程

1. **读取并理解需求**
   - 彻底阅读指定的功能请求文件
   - 理解 Vue 3 组件需求和用户界面规范
   - 注意任何特定的 Vuetify 组件、状态管理或路由需求
   - 识别功能的范围和复杂性

2. **Vue 3 生态系统研究（关键）**
   - **Web 搜索 Vue 3 最新最佳实践** - 这是必需的
   - 研究官方 Vue 3 文档、Composition API 和 TypeScript 集成
   - 找到 Vuetify 3 组件使用模式和 Material Design 指南
   - 研究 Pinia 状态管理模式和 Vue Router 配置
   - 识别 Vitest 组件测试和 Playwright E2E 测试策略
   - 查找常见的陷阱、边缘情况和性能优化技巧

3. **前端架构分析**
   - 检查成功的 Vue 3 应用实现通过 web 搜索发现
   - 识别组件结构和文件组织模式
   - 提取可复用的 TypeScript 模式和配置模板
   - 记录 Vue 3 特定的开发工作流程和构建过程
   - 注意测试框架和验证方法

4. **Vue 3 上下文工程适配**
   - 将发现的 Vue 3 模式映射到上下文工程原理
   - 规划如何为此特定功能调整 PRP 框架
   - 设计前端特定的验证要求和成功标准
   - 规划组件包结构和依赖关系

## PRP 生成

使用 PRPs/templates/prp_vue3_base.md 作为基础：

### 包含来自 Web 搜索的关键上下文

**Vue 3 技术文档（来自 web 搜索）**:
- Vue 3 Composition API 官方文档 URL 和特定部分
- TypeScript 集成指南和最佳实践
- Vuetify 3 组件库文档和 Material Design 指南
- Pinia 状态管理模式和组合式 API 集成
- Vue Router SPA 导航和路由守卫

**实现模式（来自研究）**:
- 组件架构和文件组织约定
- 状态管理和数据流模式
- 路由配置和导航策略
- 测试策略和 E2E 用户流程

**真实示例**:
- 链接到成功的 Vue 3 实现在线找到的
- 组件模式和配置示例
- 常见集成模式和部署过程

### 实现蓝图

基于 web 搜索发现:
- **Vue 3 组件分析**: 记录组件特性和交互模式
- **状态管理设计**: 规划完整的 Pinia store 结构
- **路由架构**: 设计 Vue Router 配置和导航流
- **测试策略**: 组件测试和 E2E 测试方法

### 验证门（必须可执行）

```bash
# Vue 3 项目结构验证
ls -la src/components/ src/views/ src/stores/
find . -name "*.vue" -o -name "*.ts" | wc -l  # 应该有所需文件

# Vue 3 依赖验证
pnpm list vue typescript vuetify pinia
grep -r "script setup" src/ | wc -l  # 应该使用现代语法

# Vue 3 功能测试
pnpm dev  # 测试开发服务器
pnpm build  # 测试生产构建
pnpm test:unit  # 测试 Vitest 组件测试
pnpm test:e2e  # 测试 Playwright E2E 测试
```

*** 关键：在编写 PRP 之前进行广泛的 web 搜索 ***
*** 广泛使用 WebSearch 工具深入了解 Vue 3 生态系统 ***

## 输出

保存为: `PRPs/vue3-{功能描述}.md`

## Vue 3 质量检查清单

- [ ] 在目标 Vue 3 技术上完成广泛的 web 研究
- [ ] 彻底审查官方 Vue 3 和 Vuetify 文档
- [ ] 识别真实世界的示例和模式
- [ ] 完成组件包结构规划
- [ ] 设计前端特定的验证
- [ ] 所有 web 搜索发现记录在 PRP 中
- [ ] Vue 3 特定的陷阱和模式捕获

根据彻底的技术研究，为 Vue 3 前端功能创建全面、立即可用的 PRP，打分 1-10（创建基于彻底 Vue 3 研究的全面、立即可用功能的信心级别）。

记住：目标是创建完整、专门的 Vue 3 功能实现，通过全面的研究和文档使上下文工程应用到前端开发变得轻松。