# Vue 3 Frontend Context Engineering Template

**现代化的 Vue 3 + TypeScript + Vuetify 前端开发上下文工程模板**

这个模板为 Vue 3 前端开发提供完整的上下文工程框架，支持快速、高质量的现代 Web 应用开发。

## 🚀 Quick Start - 复制模板优先

**⚡ 第一步：复制模板到你的项目目录**

```bash
# 复制模板到新项目目录
python copy_template.py /path/to/your/vue-project

# 进入项目目录
cd /path/to/your/vue-project

# 开始使用 PRP 工作流程
/generate-vue3-prp PRPs/INITIAL.md
```

这将复制完整的 Vue 3 模板包，包括所有开发规则、命令和示例。

## 📋 PRP Framework Workflow - 3步骤过程

Vue 3 前端开发遵循简单的 3 步上下文工程工作流程：

### 1️⃣ 功能请求 (Feature Request)
创建详细的功能需求文档，说明要构建的 Vue 3 功能：

```bash
# 示例：PRPs/INITIAL.md
# Vue 3 功能请求 - 用户任务管理系统
## 功能描述
开发一个现代化的任务管理系统...

## 技术要求
- Vue 3 Composition API + TypeScript
- Vuetify 3 Material Design
- Pinia 状态管理
- Vitest + Playwright 测试
```

### 2️⃣ 生成 PRP (Generate PRP)
使用专用命令分析需求并生成详细的项目需求文档：

```bash
/generate-vue3-prp PRPs/INITIAL.md
```

这将创建：
- 完整的组件设计规划
- TypeScript 接口和类型定义
- Vuetify 组件使用模式
- Pinia store 架构设计
- 测试策略和验证循环
- 基于 Web 研究的最佳实践

### 3️⃣ 执行实现 (Execute Implementation)
使用生成的 PRP 实现完整的 Vue 3 功能：

```bash
/execute-vue3-prp PRPs/vue3-task-management.md
```

自动创建：
- Vue 3 SFC 组件（`<script setup lang="ts">`）
- Pinia stores 和状态管理
- Vue Router 路由配置
- Vitest 组件测试
- Playwright E2E 测试
- 完整的 TypeScript 类型定义

## 📁 Template Structure - 模板结构

```
vue3-frontend/
├── 🔧 CLAUDE.md                           # Vue 3 开发全局规则和最佳实践
├── 📁 .claude/commands/
│   ├── 🚀 generate-vue3-prp.md          # Vue 3 PRP 生成命令
│   └── ⚡ execute-vue3-prp.md           # Vue 3 PRP 执行命令
├── 📁 PRPs/
│   ├── 📁 templates/
│   │   └── 📋 prp_vue3_base.md          # Vue 3 基础 PRP 模板
│   └── 📄 INITIAL.md                    # 功能请求示例（任务管理系统）
├── 📁 examples/
│   ├── 🎨 TaskCard.vue                  # Vue 3 组件示例（完整功能）
│   ├── 🏪 useTaskStore.ts               # Pinia store 示例（状态管理）
│   └── 🧪 TaskCard.test.ts              # Vitest 测试示例（全面覆盖）
├── 📦 copy_template.py                   # 模板复制脚本
└── 📖 README.md                          # 这个文件
```

### 文件说明

- **CLAUDE.md**: Vue 3 专用开发规则，包括 Composition API、TypeScript 集成、Vuetify 使用、测试策略
- **generate-vue3-prp.md**: 分析功能需求，进行 Vue 3 生态研究，生成详细 PRP
- **execute-vue3-prp.md**: 基于 PRP 实现完整的 Vue 3 功能，包括组件、状态管理、测试
- **prp_vue3_base.md**: 预配置的 Vue 3 PRP 模板，包含技术栈上下文和验证循环
- **INITIAL.md**: 任务管理系统功能请求示例，展示如何定义 Vue 3 功能需求

## 🎯 What You Can Build - 你能构建什么

使用这个模板，你可以快速构建：

### 🎨 Vue 3 现代组件
- **响应式单文件组件**: 使用 `<script setup lang="ts">` 语法
- **Material Design UI**: 基于 Vuetify 3 组件库
- **类型安全**: 完整的 TypeScript 接口和类型定义
- **组合式 API**: 现代的状态管理和逻辑复用

### 🏪 状态管理系统
- **Pinia Stores**: 使用 Composition API 语法
- **响应式状态**: 正确的响应性模式和 `storeToRefs()`
- **异步操作**: API 调用和错误处理
- **类型化 Actions**: TypeScript 类型安全的状态操作

### 🧭 路由和导航
- **Vue Router 4**: SPA 路由配置和导航守卫
- **类型化路由**: TypeScript 路由参数和查询字符串
- **懒加载**: 组件和路由的代码分割
- **导航保护**: 权限控制和页面保护

### 🧪 完整测试覆盖
- **Vitest 组件测试**: 组件行为和交互测试
- **Playwright E2E**: 用户流程和跨浏览器测试
- **API 模拟**: MSW 或 Vitest mocks
- **视觉回归**: UI 截图和变化检测

## 📚 Key Features - 核心特性

### ⚡ 现代技术栈 (2025 最佳实践)
- **Vue 3.4+**: 最新的 Composition API 和性能优化
- **TypeScript 5+**: 严格类型检查和最新语言特性
- **Vuetify 3**: Material Design 3 组件和主题系统
- **Vite 5**: 极快的构建工具和 HMR
- **pnpm**: 高效的包管理和 workspace 支持

### 🔧 开发工具集成
- **ESLint + Prettier**: 代码质量和格式化
- **Vue DevTools**: 组件和状态调试
- **TypeScript Language Service**: IDE 智能提示
- **Git Hooks**: 提交前的代码检查

### 🎨 UI/UX 优化
- **响应式设计**: 移动优先，支持所有设备
- **Material Design 3**: 现代化的设计语言
- **明暗主题**: 内置主题切换支持
- **无障碍访问**: ARIA 标签和键盘导航

### 🚀 性能优化
- **代码分割**: 路由和组件懒加载
- **Tree Shaking**: Vuetify 组件按需引入
- **缓存策略**: 智能缓存和更新机制
- **Bundle 分析**: 构建产物大小优化

## 🔍 Examples Included - 包含的示例

### 📱 TaskCard.vue - 完整的 Vue 3 组件
- **Composition API**: `<script setup lang="ts">` 语法
- **Material Design**: Vuetify 3 组件使用
- **交互功能**: 拖拽、动画、状态切换
- **类型安全**: 完整的 TypeScript 接口定义

### 🏪 useTaskStore.ts - Pinia 状态管理
- **Composition Store**: 使用 `defineStore(() => {})`语法
- **响应式状态**: `ref()` 和 `computed()` 模式
- **异步操作**: API 调用和错误处理
- **类型定义**: 完整的 TypeScript 接口

### 🧪 TaskCard.test.ts - 综合测试
- **组件测试**: Vue Test Utils + Vitest
- **用户交互**: 点击、输入、表单提交
- **可访问性**: ARIA 标签和键盘导航测试
- **边缘情况**: 错误处理和异常情况

## 📖 Documentation References - 文档引用

### 官方文档
- [Vue 3 官方指南](https://vuejs.org/guide/) - Vue 3 核心概念
- [Vuetify 3 文档](https://vuetifyjs.com/) - Material Design 组件
- [Pinia 文档](https://pinia.vuejs.org/) - 现代状态管理
- [Vitest 文档](https://vitest.dev/) - 单元测试框架
- [Playwright 文档](https://playwright.dev/) - E2E 测试工具

### 最佳实践资源
- [Vue 3 TypeScript 指南](https://vuejs.org/guide/typescript/overview.html)
- [Vue 3 性能优化](https://vuejs.org/guide/best-practices/performance.html)
- [Material Design 3](https://m3.material.io/) - 设计规范
- [pnpm 工作空间](https://pnpm.io/workspaces) - 包管理

## 🚫 Common Gotchas - 常见陷阱

### ⚠️ Vue 3 响应性陷阱
```javascript
// ❌ 错误：解构会丢失响应性
const { count } = store

// ✅ 正确：使用 storeToRefs 保持响应性
const { count } = storeToRefs(store)
```

### ⚠️ TypeScript 组件类型
```vue
<!-- ❌ 错误：使用 any 类型 -->
<script setup lang="ts">
const props = defineProps({
  data: Object as any
})

// ✅ 正确：定义具体接口 -->
interface Props {
  data: TaskData
}
const props = defineProps<Props>()
</script>
```

### ⚠️ Vuetify Tree Shaking
```javascript
// ❌ 错误：导入整个 Vuetify
import Vuetify from 'vuetify'

// ✅ 正确：使用 vite-plugin-vuetify 自动导入
// vite.config.ts 中配置 vuetify() 插件
```

### ⚠️ 异步组件测试
```javascript
// ❌ 错误：没有等待异步操作
it('should load data', () => {
  wrapper.vm.loadData()
  expect(wrapper.vm.loading).toBe(false) // 可能失败
})

// ✅ 正确：等待异步操作完成
it('should load data', async () => {
  await wrapper.vm.loadData()
  expect(wrapper.vm.loading).toBe(false)
})
```

## 🛠️ Development Commands - 开发命令

```bash
# 安装依赖
pnpm install

# 启动开发服务器
pnpm dev

# 构建生产版本
pnpm build

# 运行单元测试
pnpm test:unit

# 运行 E2E 测试
pnpm test:e2e

# 类型检查
pnpm type-check

# 代码检查和修复
pnpm lint
pnpm lint:fix

# 格式化代码
pnpm format
```

## 🔄 Workflow Integration - 工作流程集成

### CI/CD Pipeline
```yaml
# .github/workflows/ci.yml 示例
name: Vue 3 CI
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: pnpm/action-setup@v2
      - run: pnpm install
      - run: pnpm type-check
      - run: pnpm test:unit
      - run: pnpm build
```

### Git Hooks
```json
{
  "husky": {
    "hooks": {
      "pre-commit": "lint-staged",
      "commit-msg": "commitlint -E HUSKY_GIT_PARAMS"
    }
  },
  "lint-staged": {
    "*.{vue,ts,js}": ["eslint --fix", "prettier --write"]
  }
}
```

## 🎯 Success Metrics - 成功指标

使用这个模板，你的 Vue 3 项目将达到：

- ✅ **类型安全**: 100% TypeScript 覆盖，零 `any` 类型
- ✅ **测试覆盖**: 80%+ 代码覆盖率
- ✅ **性能优化**: Lighthouse 90+ 分数
- ✅ **代码质量**: ESLint 零错误，Prettier 格式化
- ✅ **响应式设计**: 移动端和桌面端完美适配
- ✅ **可访问性**: WCAG 2.1 AA 标准合规

## 💡 Tips for Success - 成功提示

1. **始终从功能请求开始**: 使用 `PRPs/INITIAL.md` 作为模板定义清晰的需求
2. **充分利用 Web 研究**: PRP 生成过程会进行广泛的技术研究
3. **遵循 Vue 3 最佳实践**: 使用 Composition API 和 `<script setup>` 语法
4. **保持类型安全**: 为所有数据结构定义 TypeScript 接口
5. **测试驱动开发**: 为每个组件编写测试，确保质量
6. **性能优先**: 使用懒加载和代码分割优化应用性能

## 🤝 Contributing - 贡献

这个模板是开源的，欢迎贡献！请遵循以下指南：

1. Fork 项目并创建功能分支
2. 确保所有测试通过
3. 更新文档（如果需要）
4. 提交 Pull Request

## 📄 License - 许可证

MIT License - 详见 LICENSE 文件

## 🎉 Happy Vue 3 Development!

这个模板将 Vue 3 前端开发的上下文工程应用变得简单而高效。通过遵循 3 步 PRP 工作流程，你可以快速构建高质量、类型安全、经过全面测试的现代 Web 应用。

立即开始你的 Vue 3 之旅：

```bash
python copy_template.py /your/awesome/vue-project
cd /your/awesome/vue-project
/generate-vue3-prp PRPs/INITIAL.md
```

✨ **让上下文工程为你的 Vue 3 开发加速！**