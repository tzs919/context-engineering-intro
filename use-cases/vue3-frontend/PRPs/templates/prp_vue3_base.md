---
name: "Vue 3 Feature PRP"
description: "Vue 3 + TypeScript + Vuetify + pnpm + Playwright 前端功能实现"
---

## Purpose

为 **Vue 3 前端应用** 实现一个功能，使用现代技术栈: Vue 3 Composition API + TypeScript + Vuetify Material Design + pnpm + Vitest + Playwright，遵循 2025 年最佳实践和 MVVM 架构模式。

## Core Principles

1. **Composition API 优先**: 使用 Vue 3 的 `<script setup lang="ts">` 语法
2. **类型安全**: 全面的 TypeScript 集成和严格类型检查
3. **Material Design**: 使用 Vuetify 3 组件保持设计一致性
4. **测试覆盖**: Vitest 组件测试 + Playwright E2E 测试
5. **性能优化**: 代码分割、懒加载和构建优化

---

## Goal

实现一个生产就绪的 Vue 3 前端功能，包括:

- 响应式 Vue 3 单文件组件使用 Composition API
- Pinia 状态管理集成和类型化 stores
- Vue Router 导航和路由配置
- Vuetify Material Design 组件集成
- 全面的测试覆盖：组件测试和 E2E 测试

## Why

- **现代前端开发**: 使用 Vue 3 生态系统的最新功能和模式
- **开发效率**: TypeScript 类型安全和 Vite 快速构建
- **用户体验**: Material Design 组件和响应式设计
- **代码质量**: 全面测试和 ESLint/Prettier 代码规范
- **可维护性**: 清晰的组件架构和状态管理模式

## What

### 功能实现组件

**Vue 3 单文件组件**:
```vue
<!-- 主组件结构 -->
<template>
  <v-container>
    <v-card>
      <v-card-title>{{ title }}</v-card-title>
      <v-card-text>
        <!-- Vuetify 组件内容 -->
      </v-card-text>
      <v-card-actions>
        <v-btn @click="handleAction">{{ actionText }}</v-btn>
      </v-card-actions>
    </v-card>
  </v-container>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'
import { useFeatureStore } from '@/stores/feature'

// TypeScript 接口定义
interface Props {
  title: string
  actionText?: string
}

// 定义 props 和 emits
const props = withDefaults(defineProps<Props>(), {
  actionText: '确认'
})

const emit = defineEmits<{
  action: [value: string]
}>()

// 响应式状态
const featureStore = useFeatureStore()
const { state } = storeToRefs(featureStore)

// 计算属性
const computedValue = computed(() => {
  return `处理后的值: ${state.value}`
})

// 方法
const handleAction = () => {
  featureStore.performAction()
  emit('action', computedValue.value)
}
</script>

<style scoped>
.v-card {
  margin: 1rem;
}
</style>
```

**Pinia Store 实现**:
```typescript
// stores/feature.ts
import { defineStore } from 'pinia'
import { ref, computed } from 'vue'

export interface FeatureState {
  items: FeatureItem[]
  loading: boolean
  error: string | null
}

export interface FeatureItem {
  id: string
  name: string
  active: boolean
}

export const useFeatureStore = defineStore('feature', () => {
  // State
  const state = ref<FeatureState>({
    items: [],
    loading: false,
    error: null
  })

  // Getters
  const activeItems = computed(() =>
    state.value.items.filter(item => item.active)
  )

  const itemCount = computed(() => state.value.items.length)

  // Actions
  const fetchItems = async () => {
    state.value.loading = true
    try {
      // API 调用逻辑
      const response = await fetch('/api/feature-items')
      const data = await response.json()
      state.value.items = data
    } catch (error) {
      state.value.error = error.message
    } finally {
      state.value.loading = false
    }
  }

  const addItem = (item: FeatureItem) => {
    state.value.items.push(item)
  }

  const performAction = () => {
    // 业务逻辑
    console.log('执行功能操作')
  }

  return {
    state: readonly(state),
    activeItems,
    itemCount,
    fetchItems,
    addItem,
    performAction
  }
})
```

**路由配置**:
```typescript
// router/feature.ts
import type { RouteRecordRaw } from 'vue-router'

export const featureRoutes: RouteRecordRaw[] = [
  {
    path: '/feature',
    name: 'Feature',
    component: () => import('@/views/FeatureView.vue'),
    meta: {
      title: '功能页面',
      requiresAuth: false
    }
  },
  {
    path: '/feature/:id',
    name: 'FeatureDetail',
    component: () => import('@/views/FeatureDetailView.vue'),
    props: true,
    meta: {
      title: '功能详情'
    }
  }
]
```

### 成功标准

- [ ] Vue 3 组件使用 `<script setup>` 和 Composition API
- [ ] TypeScript 接口定义所有 props、emits 和状态
- [ ] Vuetify 3 组件正确集成和主题化
- [ ] Pinia store 使用 Composition API 语法
- [ ] Vue Router 配置包含类型化路由
- [ ] Vitest 组件测试覆盖主要功能
- [ ] Playwright E2E 测试覆盖用户工作流
- [ ] 响应式设计和移动端适配
- [ ] ESLint 和 TypeScript 检查通过
- [ ] 构建优化和性能检查通过

## All Needed Context

### Vue 3 生态系统文档

```yaml
# VUE 3 核心文档
- url: https://vuejs.org/guide/typescript/composition-api.html
  why: Composition API 与 TypeScript 集成模式

- url: https://vuejs.org/guide/components/props.html
  why: Vue 3 props 定义和验证模式

- url: https://vuejs.org/guide/components/events.html
  why: 组件事件定义和 emit 模式

# VUETIFY 3 MATERIAL DESIGN
- url: https://vuetifyjs.com/en/components/buttons/
  why: Vuetify 按钮组件和 Material Design 模式

- url: https://vuetifyjs.com/en/components/cards/
  why: Card 组件和布局模式

- url: https://vuetifyjs.com/en/features/theme/
  why: 主题系统和明暗模式切换

# PINIA 状态管理
- url: https://pinia.vuejs.org/core-concepts/state.html
  why: Pinia state 定义和 TypeScript 类型

- url: https://pinia.vuejs.org/core-concepts/getters.html
  why: Computed getters 和响应式计算

- url: https://pinia.vuejs.org/core-concepts/actions.html
  why: Actions 和异步操作模式

# VUE ROUTER 导航
- url: https://router.vuejs.org/guide/essentials/dynamic-matching.html
  why: 动态路由和参数处理

- url: https://router.vuejs.org/guide/advanced/navigation-guards.html
  why: 路由守卫和权限控制

# 测试框架
- url: https://vitest.dev/guide/
  why: Vitest 组件测试和模拟

- url: https://playwright.dev/docs/test-components
  why: Playwright 组件和 E2E 测试
```

### Vue 3 项目结构

```bash
# 当前 Vue 3 项目结构
src/
├── components/          # 可复用组件
├── views/              # 页面组件
├── stores/             # Pinia stores
├── composables/        # 组合式函数
├── router/             # Vue Router 配置
├── plugins/            # Vue 插件
├── types/              # TypeScript 类型
├── assets/             # 静态资源
└── utils/              # 工具函数

tests/
├── components/         # Vitest 组件测试
├── e2e/               # Playwright E2E 测试
├── fixtures/          # 测试数据
└── helpers/           # 测试工具
```

### Vue 3 技术栈分析

```typescript
// Vue 3 + TypeScript 模式
interface Vue3TechStack {
  // 组件架构
  components: {
    syntax: '<script setup lang="ts">'
    props: 'defineProps<Interface>()'
    emits: 'defineEmits<EventMap>()'
    composables: 'use[Feature]() pattern'
  }

  // 状态管理
  state: {
    store: 'Pinia with Composition API'
    reactivity: 'storeToRefs() for destructuring'
    typing: 'TypeScript interfaces for state'
  }

  // 路由系统
  routing: {
    definition: 'RouteRecordRaw[] with types'
    navigation: 'useRouter() and useRoute()'
    guards: 'beforeEach() and meta fields'
  }

  // UI 框架
  ui: {
    components: 'Vuetify 3 Material Design'
    theming: 'CSS custom properties'
    responsive: 'v-container and v-row/v-col'
    accessibility: 'Built-in ARIA attributes'
  }

  // 测试策略
  testing: {
    unit: 'Vitest + Vue Test Utils'
    e2e: 'Playwright with real browsers'
    mocking: 'vi.mock() and MSW'
    coverage: 'Built-in coverage reporting'
  }
}
```

### 已知 Vue 3 模式

```typescript
// 关键：Vue 3 实现必须遵循这些模式

// 1. Composition API 最佳实践 (2025)
const compositionPatterns = {
  component: '<script setup lang="ts"> with defineProps<T>()',
  reactivity: 'ref(), reactive(), computed(), watch()',
  lifecycle: 'onMounted(), onUnmounted(), etc.',
  stores: 'storeToRefs() for reactive destructuring'
}

// 2. TypeScript 集成模式
const typescriptPatterns = {
  interfaces: 'Define interfaces for all data structures',
  generics: 'Use generics for reusable components',
  strict: 'Enable strict mode in tsconfig.json',
  validation: 'Runtime validation with schema libraries'
}

// 3. Vuetify 3 集成模式
const vuetifyPatterns = {
  components: 'v-btn, v-card, v-form, v-data-table',
  layout: 'v-app, v-main, v-container, v-row, v-col',
  theming: 'useTheme() composable for theme switching',
  icons: 'mdi icons with v-icon component'
}

// 4. 测试模式
const testingPatterns = {
  component: 'mount() with Vue Test Utils',
  stores: 'setActivePinia() for Pinia testing',
  mocking: 'vi.mock() for module mocking',
  e2e: 'page.goto() and page.click() patterns'
}

// 5. 常见陷阱
const commonPitfalls = {
  reactivity: 'Use storeToRefs() when destructuring',
  typescript: 'Avoid any type, use proper interfaces',
  performance: 'Use defineAsyncComponent for code splitting',
  testing: 'Mock external dependencies properly'
}
```

## 实现蓝图

### Vue 3 组件开发

**组件实现任务**:
```yaml
任务 1 - 创建主组件:
  创建 Vue 3 SFC 使用:
    - <script setup lang="ts"> 语法
    - TypeScript 接口定义 props 和 emits
    - Vuetify 3 组件用于 UI
    - 响应式状态和计算属性
    - 适当的生命周期钩子

任务 2 - 实现状态管理:
  创建 Pinia store 包含:
    - Composition API defineStore() 语法
    - TypeScript 类型化状态和 actions
    - 异步 actions 用于 API 调用
    - Getters 用于计算派生状态
    - 与组件的正确集成

任务 3 - 配置路由:
  设置 Vue Router 包含:
    - 类型化路由定义
    - 路由参数和查询处理
    - 路由守卫和元信息
    - 懒加载组件配置

任务 4 - 创建测试:
  实现测试覆盖包含:
    - Vitest 组件单元测试
    - Playwright E2E 用户流程测试
    - API 模拟和状态测试
    - 可访问性和响应式测试
```

### Vue 3 专业化详情

```typescript
// Vue 3 前端专业化模式
const vue3Specialization = {
  patterns: [
    'composition_api_components',
    'typescript_strict_types',
    'vuetify_material_design',
    'pinia_state_management',
    'vue_router_navigation'
  ],
  validation: [
    'vitest_component_testing',
    'playwright_e2e_flows',
    'typescript_type_checking',
    'eslint_code_quality',
    'build_performance_check'
  ],
  examples: [
    'responsive_vue3_app',
    'material_design_components',
    'pinia_store_integration',
    'router_navigation_flows',
    'form_validation_handling'
  ],
  gotchas: [
    'storeToRefs_reactivity',
    'typescript_component_typing',
    'vuetify_theme_customization',
    'vite_build_optimization',
    'testing_async_components'
  ]
}
```

## 验证循环

### Level 1: Vue 3 项目结构验证

```bash
# 验证 Vue 3 文件结构
find src/ -name "*.vue" -o -name "*.ts" | sort
ls -la src/components/ src/views/ src/stores/
test -f src/main.ts && echo "✓ 主入口文件存在"

# 验证 package.json 依赖
pnpm list vue typescript vuetify pinia @vue/test-utils vitest playwright
grep -q "\"type\": \"module\"" package.json && echo "✓ ES 模块配置"

# 预期: 所有必需文件和依赖存在
# 如果缺失: 创建缺失文件遵循 Vue 3 模式
```

### Level 2: Vue 3 代码质量验证

```bash
# 验证现代 Vue 3 语法使用
grep -r "script setup" src/ | wc -l  # 应该 > 0
grep -r "defineProps\|defineEmits" src/ | wc -l  # 应该 > 0
grep -r "Options API" src/ && echo "⚠ 发现旧语法" || echo "✓ 使用现代语法"

# 检查 TypeScript 类型覆盖
grep -r ": any" src/ | wc -l  # 应该 = 0
grep -r "interface\|type" src/ | wc -l  # 应该 > 0

# 验证 Vuetify 组件使用
grep -r "v-btn\|v-card\|v-form" src/ | wc -l  # 应该 > 0

# 预期: 现代 Vue 3 语法，强类型，Vuetify 集成
# 如果问题: 重构使用正确的 Vue 3 + TypeScript 模式
```

### Level 3: Vue 3 功能验证

```bash
# 测试 Vue 3 开发环境
pnpm dev &
DEV_PID=$!
sleep 5
curl -f http://localhost:5173 >/dev/null && echo "✓ 开发服务器响应" || echo "✗ 开发服务器失败"
kill $DEV_PID

# 测试构建过程
pnpm build
test -d dist && echo "✓ 构建成功" || echo "✗ 构建失败"

# 运行测试套件
pnpm test:unit && echo "✓ 组件测试通过" || echo "✗ 组件测试失败"
pnpm type-check && echo "✓ 类型检查通过" || echo "✗ 类型错误"

# 预期: 开发、构建、测试全部成功
# 如果失败: 调试和修复 Vue 3 配置和代码问题
```

### Level 4: Vue 3 集成测试

```bash
# 验证组件集成
grep -r "storeToRefs\|useRouter" src/ | wc -l  # 应该有状态和路由集成
grep -r "v-model\|@click" src/ | wc -l  # 应该有用户交互

# 测试 E2E 场景（如果配置了 Playwright）
pnpm test:e2e && echo "✓ E2E 测试通过" || echo "⚠ E2E 测试跳过或失败"

# 验证响应式设计
grep -r "v-col.*xs\|sm\|md\|lg" src/ | wc -l  # 应该有响应式布局

# 预期: 完整的 Vue 3 生态系统集成
# 如果问题: 改进组件间集成和用户体验
```

## 最终验证清单

### Vue 3 功能完整性

- [ ] Vue 3 组件使用 Composition API: `grep -r "script setup"`
- [ ] TypeScript 类型安全: `pnpm type-check`
- [ ] Vuetify Material Design: `grep -r "v-"`
- [ ] Pinia 状态管理集成: `grep -r "useStore\|storeToRefs"`
- [ ] Vue Router 导航: `grep -r "useRouter\|useRoute"`
- [ ] 响应式设计: Vuetify 断点和栅格系统
- [ ] 测试覆盖: Vitest 和 Playwright 测试存在

### 质量和可用性

- [ ] 无 TODO 占位符内容: `grep -r "TODO\|FIXME"`
- [ ] Vue 3 最佳实践: 现代语法和模式
- [ ] 性能优化: 懒加载和代码分割
- [ ] 可访问性: ARIA 属性和键盘导航
- [ ] 开发就绪: 立即可运行和构建

### 框架集成

- [ ] 继承上下文工程原则: PRP 工作流程保持
- [ ] Vue 3 专业化: 前端特定模式包含
- [ ] 命令兼容性: Vue 3 斜杠命令按预期工作
- [ ] 文档一致性: 遵循建立的模式
- [ ] 可维护结构: 随 Vue 生态系统演进易于更新

---

## Vue 3 反模式避免

### 组件开发

- ❌ 不要使用 Options API - 使用 Composition API 和 `<script setup>`
- ❌ 不要忽略 TypeScript - 为所有 props、state 和方法提供类型
- ❌ 不要混合响应式 API - 一致使用 ref/reactive 模式
- ❌ 不要忘记 storeToRefs - 解构 Pinia store 时保持响应性

### 状态管理

- ❌ 不要使用 Vuex - 使用 Pinia 作为推荐状态管理
- ❌ 不要跳过类型定义 - 为 store state 和 actions 提供接口
- ❌ 不要直接修改状态 - 使用 actions 进行状态更改
- ❌ 不要忘记错误处理 - 在异步 actions 中实现 try/catch

### UI 和样式

- ❌ 不要忽略 Material Design - 遵循 Vuetify 3 设计原则
- ❌ 不要跳过响应式设计 - 使用 Vuetify 断点系统
- ❌ 不要忘记可访问性 - 利用 Vuetify 内置的 a11y 功能
- ❌ 不要忽略主题 - 实现明暗模式支持

### 测试和质量

- ❌ 不要跳过测试 - 包含组件和 E2E 测试覆盖
- ❌ 不要忽略类型检查 - 运行 vue-tsc 进行类型验证
- ❌ 不要跳过构建验证 - 确保生产构建成功
- ❌ 不要忽略性能 - 实现代码分割和懒加载