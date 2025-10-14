# Vue 3 Frontend Development - Context Engineering Rules

这个文件包含了为 Vue 3 + TypeScript + Vuetify + pnpm + Playwright 现代前端开发所定制的全局规则和最佳实践。

## 🔄 项目意识和上下文

- **始终遵循 Vue 3 Composition API** - 使用 `<script setup lang="ts">` 语法和现代 Vue 3 模式
- **理解项目架构** - 检查 package.json、vite.config.ts 和 tsconfig.json 了解项目配置
- **使用一致的文件结构** - 遵循 Vue 3 + Vite 项目的标准组织模式
- **TypeScript 优先** - 所有组件、store 和工具函数都应该使用 TypeScript

## 🧱 Vue 3 代码结构和模块化

### 组件组织
- **单文件组件 (SFC)**: 使用 `.vue` 文件，包含 `<template>`, `<script setup lang="ts">`, `<style scoped>`
- **组件大小限制**: 每个 Vue 组件不超过 200 行代码，复杂组件应拆分为子组件
- **Composition API 优先**: 使用 `<script setup>` 语法而不是 Options API
- **组件分类**:
  - `src/components/` - 可复用的基础组件
  - `src/views/` - 页面级组件
  - `src/layouts/` - 布局组件

### 状态管理 (Pinia)
- **Store 组织**: 按功能域组织 stores，每个 store 使用 Composition API 语法
- **类型安全**: 为 store 的 state、getters 和 actions 定义 TypeScript 接口
- **响应式解构**: 使用 `storeToRefs()` 保持响应性

### TypeScript 集成
- **严格模式**: 启用 TypeScript strict 模式进行类型检查
- **组件 Props**: 使用 `defineProps<T>()` 定义类型化的属性
- **组合式函数**: 为可复用逻辑创建类型化的 composables

## 🎨 Vuetify Material Design

### 组件使用
- **自动导入**: 利用 `vite-plugin-vuetify` 进行组件的自动导入
- **主题系统**: 使用 Vuetify 3 的主题系统处理明暗模式切换
- **响应式设计**: 使用 Vuetify 的断点系统和栅格布局
- **无障碍访问**: 利用 Vuetify 内置的 ARIA 属性和键盘导航

### 样式约定
- **Scoped CSS**: 在 Vue 组件中使用 `<style scoped>`
- **CSS 变量**: 使用 CSS 自定义属性进行主题定制
- **Material Design**: 遵循 Material Design 3 设计原则

## 🧪 测试和可靠性

### 组件测试 (Vitest)
- **测试文件位置**: 测试文件放在 `/tests` 文件夹中，镜像主应用结构
- **Vue Test Utils**: 使用 `@vue/test-utils` 挂载和测试 Vue 组件
- **测试覆盖**: 为每个组件包括至少:
  - 1 个预期行为测试
  - 1 个边缘情况测试
  - 1 个错误处理测试

### E2E 测试 (Playwright)
- **测试策略**: 使用 Playwright 测试用户工作流和关键路径
- **页面对象模式**: 为复杂的用户界面创建页面对象
- **视觉回归**: 使用 Playwright 的截图功能进行 UI 测试

### 验证循环
```bash
# 开发验证命令
pnpm dev          # 启动开发服务器
pnpm build        # 构建生产版本
pnpm test:unit    # 运行 Vitest 单元测试
pnpm test:e2e     # 运行 Playwright E2E 测试
pnpm lint         # ESLint 代码检查
pnpm type-check   # TypeScript 类型检查
```

## ✅ 任务完成规范

### 开发工作流
- **开发服务器**: 使用 `pnpm dev` 启动 Vite 开发服务器
- **类型检查**: 使用 `vue-tsc` 进行 TypeScript 类型检查
- **代码质量**: 运行 ESLint 和 Prettier 保持代码质量
- **测试驱动**: 为新功能编写测试用例

### Vue 3 特定模式
- **Composition API**: 优先使用 Composition API 和 `<script setup>` 语法
- **响应式**: 正确使用 `ref()`, `reactive()`, `computed()`, `watch()`
- **生命周期**: 使用 `onMounted()`, `onUnmounted()` 等组合式 API
- **依赖注入**: 使用 `provide()` 和 `inject()` 进行组件间通信

## 📎 风格和约定

### Vue 3 组件规范
- **单文件组件**: 使用 `.vue` 文件扩展名
- **命名约定**: 组件使用 PascalCase, 文件名使用 kebab-case
- **Props 定义**: 使用 TypeScript 接口定义 props 类型
- **事件处理**: 使用 `defineEmits<T>()` 定义组件事件

### 包管理 (pnpm)
- **依赖管理**: 使用 pnpm 进行包管理，支持 workspace
- **脚本**: 在 package.json 中定义常用的开发脚本
- **依赖更新**: 定期更新依赖并测试兼容性

### 目录结构约定
```
src/
├── components/          # 可复用组件
├── views/              # 页面组件
├── layouts/            # 布局组件
├── stores/             # Pinia stores
├── composables/        # 组合式函数
├── plugins/            # Vue 插件配置
├── router/             # Vue Router 配置
├── assets/             # 静态资源
├── types/              # TypeScript 类型定义
└── utils/              # 工具函数
```

## 📚 文档和可解释性

### Vue 3 组件文档
- **组件注释**: 为每个组件编写用途和使用方法的注释
- **Props 文档**: 详细说明每个 prop 的类型和用途
- **事件文档**: 说明组件发出的自定义事件

### TypeScript 文档
- **接口定义**: 为复杂的数据结构定义 TypeScript 接口
- **泛型使用**: 合理使用 TypeScript 泛型提高代码复用性
- **类型断言**: 谨慎使用类型断言，优先使用类型守卫

## 🧠 AI 行为规则

### Vue 3 开发指导
- **不要假设缺失的上下文** - 对 Vue 3 特性不确定时询问详情
- **不要虚构库或功能** - 只使用已知的、经过验证的 Vue 3 生态系统包
- **始终确认组件模式** - 确保使用的是 Vue 3 Composition API 而不是 Vue 2 Options API
- **验证 Vuetify 组件** - 确保使用的是 Vuetify 3 组件语法

### 代码质量保证
- **TypeScript 优先**: 总是提供类型安全的解决方案
- **响应式最佳实践**: 正确使用 Vue 3 响应式系统
- **性能考虑**: 考虑组件懒加载和代码分割
- **测试覆盖**: 为复杂逻辑提供测试示例

## 🚀 Vue 3 特定最佳实践

### 性能优化
- **组件懒加载**: 使用动态导入进行路由级代码分割
- **虚拟滚动**: 对长列表使用 Vuetify 的虚拟滚动
- **图片优化**: 使用现代图片格式和懒加载
- **Bundle 分析**: 使用 Vite Bundle Analyzer 分析打包大小

### 常见陷阱避免
- **响应式陷阱**: 解构 Pinia store 时使用 `storeToRefs()`
- **生命周期差异**: 理解 `onMounted` 与 Options API `mounted` 的区别
- **TypeScript 类型**: 正确类型化组件 refs 和模板 refs
- **构建优化**: 正确配置 Vuetify 组件的 tree shaking

### 开发体验
- **Vue Devtools**: 使用 Vue Devtools 进行调试
- **TypeScript 服务**: 配置 IDE 的 TypeScript 语言服务
- **热重载**: 利用 Vite 的热模块替换功能
- **错误处理**: 实现全局错误处理和用户友好的错误显示

---

## 重要指令提醒

严格遵守上述 Vue 3 前端开发规范，确保所有代码都符合现代 Vue 3 + TypeScript + Vuetify + pnpm + Playwright 技术栈的最佳实践。优先考虑类型安全、组件复用性、测试覆盖率和用户体验。