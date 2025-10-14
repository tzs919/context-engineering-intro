# Execute Vue 3 PRP

执行全面的 Vue 3 PRP 来实现现代前端功能，包括组件开发、状态管理、路由配置和完整测试覆盖。

## PRP 文件: {prp_file}

## 执行过程

1. **加载 Vue 3 PRP**
   - 完全读取指定的 Vue 3 PRP 文件
   - 理解组件需求和所有技术规范
   - 审查 PRP 中记录的所有 web 研究发现
   - 遵循组件实现和测试的所有指导

2. **ULTRATHINK - Vue 3 功能设计**
   - 创建全面的实现计划
   - 基于 PRP 研究规划完整的组件结构
   - 设计前端特定的上下文工程适配
   - 将 Vue 3 模式映射到上下文工程原理
   - 规划所有必需文件和它们的关系

3. **生成 Vue 3 功能实现**
   - 创建 Vue 3 SFC 组件使用 Composition API
   - 实现 Pinia stores 用于状态管理
   - 配置 Vue Router 路由和导航
   - 设置 Vitest 组件测试
   - 创建 Playwright E2E 测试用例

4. **验证 Vue 3 实现**
   - 运行 PRP 中指定的所有验证命令
   - 验证组件渲染和功能正确性
   - 测试 TypeScript 类型检查和编译
   - 检查与 Vue 3 上下文工程框架的集成

5. **质量保证**
   - 确保遵循所有 Vue 3 最佳实践
   - 验证组件模式准确表示 PRP 要求
   - 检查验证循环适当且可执行
   - 确认实现立即可用于前端开发

6. **完成实现**
   - 审查功能实现对所有 PRP 要求
   - 确保满足 PRP 的所有成功标准
   - 验证实现准备就绪用于生产

## Vue 3 实现要求

### 必需的文件结构
```
src/
├── components/
│   └── [FeatureName]/
│       ├── [FeatureName].vue           # 主组件
│       ├── [FeatureName]Item.vue       # 子组件
│       └── index.ts                    # 组件导出
├── views/
│   └── [FeatureName]View.vue           # 页面视图
├── stores/
│   └── [featureName].ts                # Pinia store
├── composables/
│   └── use[FeatureName].ts             # 组合式函数
├── types/
│   └── [featureName].ts                # TypeScript 类型
└── router/
    └── [featureName].ts                # 路由配置

tests/
├── components/
│   └── [FeatureName].test.ts           # Vitest 组件测试
└── e2e/
    └── [featureName].spec.ts           # Playwright E2E 测试
```

### 基于 PRP 研究的内容要求

**Vue 3 组件** 必须包括:
- `<script setup lang="ts">` 语法和 Composition API
- TypeScript 接口定义 props 和 emits
- Vuetify 3 Material Design 组件使用
- 响应式状态管理与 Pinia 集成
- 适当的生命周期钩子和错误处理

**Pinia Store** 必须包括:
- Composition API 语法 `defineStore(() => { ... })`
- TypeScript 接口定义 state 和 actions
- 响应式状态和计算属性
- 异步 actions 用于 API 调用
- 与组件的适当集成模式

**Vue Router 配置** 必须包括:
- 类型化路由定义和参数
- 路由守卫和导航逻辑
- 懒加载组件用于性能优化
- 嵌套路由和动态路由支持

**测试实现** 必须包括:
- Vitest + Vue Test Utils 组件测试
- Playwright E2E 测试覆盖用户工作流
- API 模拟和状态测试
- 可访问性和响应式测试

## 验证要求

### 结构验证
```bash
# 验证 Vue 3 文件存在
find src/ -name "*.vue" -o -name "*.ts" | sort
ls -la src/components/ src/views/ src/stores/
test -f tests/components/[FeatureName].test.ts
test -f tests/e2e/[featureName].spec.ts

# 检查 Vue 3 依赖
pnpm list vue @vue/test-utils vitest playwright
grep -r "script setup" src/ | wc -l  # 应该使用现代语法
```

### 内容验证
```bash
# 检查未完成内容
grep -r "TODO\|PLACEHOLDER\|FIXME" src/
grep -r "any\|unknown" src/ | wc -l  # 应该使用具体类型

# 验证 Vue 3 特定内容存在
grep -r "defineProps\|defineEmits" src/components/
grep -r "storeToRefs\|useStore" src/
grep -r "useRouter\|useRoute" src/
```

### 功能验证
```bash
# 测试 Vue 3 开发和构建
pnpm dev &  # 启动开发服务器
sleep 5 && curl -f http://localhost:5173 || echo "Dev server not responding"
pkill -f "vite"

pnpm build  # 测试生产构建
test -d dist/  # 验证构建输出

# 运行测试套件
pnpm test:unit  # Vitest 组件测试
pnpm test:e2e   # Playwright E2E 测试
pnpm lint       # ESLint 检查
pnpm type-check # TypeScript 验证
```

## 成功标准

- [ ] 完整的 Vue 3 功能实现结构完全按指定创建
- [ ] 所有必需文件存在并正确格式化
- [ ] 基于 PRP 研究的组件模式准确实现
- [ ] Vue 3 最佳实践在整个实现中遵循
- [ ] 适当和可执行的验证循环
- [ ] 功能立即可用于前端开发
- [ ] 与 Vue 3 上下文工程框架的集成维护
- [ ] 来自 PRP 的所有 web 研究发现正确集成到实现中
- [ ] 示例和测试全面且特定于 Vue 3 技术
- [ ] Vitest 组件测试和 Playwright E2E 测试功能齐全
- [ ] TypeScript 类型安全在整个实现中维护
- [ ] Vuetify Material Design 组件正确使用

注意：如果任何验证失败，分析错误，修复 Vue 3 实现组件，并重新验证直到所有标准通过。实现必须准备就绪用于生产，并且立即可用于使用 Vue 3 + TypeScript + Vuetify + pnpm + Playwright 技术栈的开发人员。