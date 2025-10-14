---
name: "Vue 3 Context Engineering Template"
description: "Complete context engineering template package for Vue 3 + TypeScript + Vuetify + pnpm + Playwright modern frontend development"
---

## Purpose

Generate a comprehensive context engineering template package for **Vue 3 + TypeScript + Vuetify + pnpm + Playwright** that enables rapid development of modern frontend applications following 2025 best practices, MVVM architecture patterns, and complete testing strategies.

## Core Principles

1. **Vue 3 Composition API First**: Leverage Vue 3's modern features with `<script setup>` syntax and TypeScript integration
2. **Material Design Excellence**: Use Vuetify 3 for consistent, accessible UI components following Material Design principles
3. **Developer Experience Focus**: Fast builds with Vite, efficient package management with pnpm, and comprehensive testing
4. **Type Safety Throughout**: Strong TypeScript integration across components, stores, and testing
5. **Production Ready**: Include E2E testing with Playwright and component testing with Vitest

---

## Goal

Generate a complete context engineering template package for **Vue 3 Frontend Development** that includes:

- Domain-specific CLAUDE.md implementation guide for Vue 3 development patterns
- Specialized PRP generation and execution commands for frontend features
- Vue 3 + TypeScript-appropriate base PRP template with Material Design considerations
- Comprehensive examples including components, state management, and testing
- Frontend-specific validation loops including component testing and E2E scenarios

## Why

- **Frontend Developer Acceleration**: Enable rapid application of context engineering to Vue 3 development
- **Modern Stack Integration**: Comprehensive support for 2025's recommended Vue 3 ecosystem tools
- **Quality Assurance**: Ensure comprehensive testing coverage with both unit and E2E testing
- **Best Practices Capture**: Document Vue 3 + TypeScript + Vuetify patterns and common gotchas
- **Beginner Friendly**: Create templates that new Vue developers can immediately understand and use

## What

### Template Package Components

**Complete Directory Structure:**
```
use-cases/vue3-frontend/
├── CLAUDE.md                      # Vue 3 development guide
├── .claude/commands/
│   ├── generate-vue3-prp.md      # Vue 3 PRP generation
│   └── execute-vue3-prp.md       # Vue 3 PRP execution
├── PRPs/
│   ├── templates/
│   │   └── prp_vue3_base.md      # Vue 3 base PRP template
│   ├── ai_docs/                  # Vue ecosystem documentation
│   └── INITIAL.md                # Example Vue feature request
├── examples/                     # Vue 3 code examples
├── copy_template.py              # Template deployment script
└── README.md                     # Comprehensive usage guide
```

**Vue 3 Technology Integration:**
- Vite build system with hot module replacement
- pnpm workspace configuration and efficient package management
- TypeScript configuration with strict type checking
- Vuetify 3 Material Design component system
- Pinia state management with composition API patterns
- Vue Router for SPA navigation
- Vitest for component and unit testing
- Playwright for E2E testing with real browser automation

**Context Engineering Adaptation:**
- Frontend-specific research processes including UI/UX pattern analysis
- Component-based validation loops with visual regression testing
- Vue ecosystem-specialized implementation blueprints
- Integration with modern frontend development workflows

### Success Criteria

- [ ] Complete Vue 3 template package structure generated with all required files
- [ ] Vue 3 + TypeScript + Vuetify patterns accurately documented and implemented
- [ ] Component testing with Vitest properly configured and working
- [ ] E2E testing with Playwright properly set up with example tests
- [ ] pnpm workspace configuration optimized for Vue 3 development
- [ ] Template immediately usable for creating production-ready Vue 3 applications
- [ ] Comprehensive documentation covering Vue 3 ecosystem and common patterns
- [ ] Real, working code examples that compile and run successfully

## All Needed Context

### Documentation & References (RESEARCHED)

```yaml
# VUE 3 CORE DOCUMENTATION - Foundation framework understanding
- url: https://vuejs.org/guide/typescript/overview.html
  why: Vue 3 TypeScript integration patterns and best practices

- url: https://vuejs.org/guide/typescript/composition-api.html
  why: Composition API with TypeScript, defineProps, defineEmits patterns

- url: https://vuejs.org/guide/scaling-up/state-management.html
  why: State management patterns and Pinia integration guidance

# VUETIFY 3 MATERIAL DESIGN SYSTEM
- url: https://vuetifyjs.com/en/getting-started/installation/
  why: Vuetify 3 setup with Vite and TypeScript configuration

- url: https://vuetifyjs.com/en/introduction/why-vuetify/
  why: Material Design principles and component architecture patterns

# PINIA STATE MANAGEMENT PATTERNS
- url: https://pinia.vuejs.org/introduction.html
  why: Modern state management replacing Vuex, composition API integration

- url: https://pinia.vuejs.org/core-concepts/state.html
  why: State definition patterns with TypeScript interfaces

- url: https://pinia.vuejs.org/core-concepts/actions.html
  why: Action patterns for async operations and API calls

# VUE ROUTER NAVIGATION
- url: https://router.vuejs.org/guide/
  why: SPA routing patterns, guards, and navigation strategies

- url: https://router.vuejs.org/guide/essentials/dynamic-matching.html
  why: Dynamic routing and parameterized routes for frontend applications

# TESTING FRAMEWORKS INTEGRATION
- url: https://vitest.dev/guide/
  why: Component testing strategies with Vue Test Utils integration

- url: https://vitest.dev/api/mock.html
  why: Mocking patterns for API calls and external dependencies

- url: https://playwright.dev/docs/intro
  why: E2E testing setup for Vue applications with real browser automation

# PNPM PACKAGE MANAGEMENT
- url: https://pnpm.io/workspaces
  why: Efficient package management and workspace configuration
```

### Current Context Engineering Structure

```bash
# Base framework structure to extend for Vue 3
context-engineering-intro/
├── README.md                    # Core principles to adapt for frontend development
├── .claude/commands/            # Base commands to specialize for Vue 3 features
├── PRPs/templates/prp_base.md   # Base template to extend with Vue patterns
├── CLAUDE.md                    # Base rules to inherit and specialize
└── use-cases/
    ├── mcp-server/              # Reference specialization example
    ├── template-generator/      # This meta-template system
    └── vue3-frontend/           # New Vue 3 template package (to create)
```

### Vue 3 Technology Analysis (From Research)

```typescript
// Vue 3 + TypeScript patterns discovered through web research
interface Vue3TechnologyStack {
  // Core architecture (researched from official docs)
  architecture: {
    project_structure: [
      "src/components/", "src/views/", "src/composables/",
      "src/stores/", "src/router/", "src/assets/", "src/plugins/"
    ];
    configuration_files: [
      "vite.config.ts", "tsconfig.json", "tsconfig.app.json",
      "vitest.config.ts", "playwright.config.ts", "package.json"
    ];
    dependency_management: "pnpm with workspace support";
    module_organization: [
      "atomic_design", "feature_modules", "composition_api_composables"
    ];
  };

  // Development workflow (researched from community best practices)
  development: {
    package_manager: "pnpm";
    dev_server_commands: ["pnpm dev", "pnpm build", "pnpm preview"];
    build_process: ["vite build", "type checking with vue-tsc"];
    testing_frameworks: ["vitest for components", "playwright for e2e"];
  };

  // Best practices (from 2025 Vue community research)
  patterns: {
    code_organization: [
      "composition_api_with_script_setup", "feature_based_modules",
      "composables_for_reusable_logic", "pinia_stores_by_domain"
    ];
    state_management: [
      "pinia_composition_stores", "storeToRefs_for_reactivity",
      "typed_store_interfaces", "action_based_mutations"
    ];
    error_handling: [
      "try_catch_in_composables", "error_boundaries_in_components",
      "global_error_handling", "validation_with_vuelidate"
    ];
    performance_optimization: [
      "dynamic_imports", "component_lazy_loading",
      "virtual_scrolling", "image_optimization"
    ];
  };

  // Integration ecosystem (from technology research)
  ecosystem: {
    common_libraries: [
      "@vueuse/core", "vuelidate", "vue-i18n",
      "@vue/test-utils", "msw for api mocking"
    ];
    deployment_platforms: [
      "vercel", "netlify", "aws_amplify", "github_pages"
    ];
    monitoring_tools: [
      "vue_devtools", "vite_bundle_analyzer", "sentry"
    ];
    CI_CD_patterns: [
      "github_actions", "automated_testing", "build_verification"
    ];
  };
}
```

### Known Vue 3 Template Generation Patterns

```typescript
// CRITICAL: Vue 3 template generation must follow these patterns (from research)

// 1. Vue 3 Composition API best practices (2025)
const vue3Patterns = {
  component_syntax: "<script setup lang='ts'> with defineProps<T>()",
  state_management: "Pinia stores with composition API syntax",
  routing: "Vue Router with typed routes and navigation guards",
  testing: "Vitest + Vue Test Utils + Playwright E2E"
};

// 2. TypeScript integration patterns (researched)
const typescriptIntegration = {
  strict_typing: "Enable strict mode in tsconfig.json",
  component_props: "Use interface definitions with defineProps<T>()",
  store_typing: "Type Pinia stores with TypeScript interfaces",
  route_typing: "Use typed route parameters and query strings"
};

// 3. Vuetify 3 Material Design patterns (from docs)
const vuetifyPatterns = {
  component_usage: "Auto-import with vite-plugin-vuetify",
  theming: "Light/dark theme with CSS custom properties",
  responsive_design: "Vuetify breakpoint system and grid layout",
  accessibility: "Built-in ARIA attributes and keyboard navigation"
};

// 4. Testing strategy patterns (from best practices)
const testingPatterns = {
  component_tests: "Vitest + Vue Test Utils for component behavior",
  e2e_tests: "Playwright for user workflow validation",
  api_mocking: "MSW or Vitest mocks for API responses",
  visual_testing: "Playwright screenshots for UI regression"
};

// 5. Common pitfalls to document (from research)
const vue3Gotchas = {
  reactivity: "Use storeToRefs() when destructuring Pinia stores",
  lifecycle: "onMounted in script setup vs options API differences",
  typescript: "Proper typing of component refs and template refs",
  build_optimization: "Tree shaking with Vuetify components"
};
```

## Implementation Blueprint

### Technology Research Phase (COMPLETED through Web Search)

**Research findings applied to template generation:**

```yaml
Vue 3 Framework Analysis Results:
  ✅ RESEARCHED Official Vue 3 documentation and TypeScript integration
  ✅ ANALYZED Composition API patterns with script setup syntax
  ✅ STUDIED Vuetify 3 Material Design integration with Vite
  ✅ INVESTIGATED Pinia state management with TypeScript
  ✅ EXAMINED Vue Router patterns for SPA navigation
  ✅ RESEARCHED Testing strategies with Vitest and Playwright
  ✅ ANALYZED pnpm workspace configuration for Vue projects

Development Workflow Analysis Results:
  ✅ DISCOVERED Vite as recommended build tool with HMR
  ✅ IDENTIFIED pnpm as preferred package manager for performance
  ✅ RESEARCHED Component testing with Vue Test Utils + Vitest
  ✅ ANALYZED E2E testing patterns with Playwright
  ✅ STUDIED Development tools integration and debugging

Best Practices Investigation Results:
  ✅ IDENTIFIED MVVM architecture patterns for Vue 3
  ✅ RESEARCHED Security best practices for frontend applications
  ✅ DOCUMENTED Common gotchas and TypeScript pitfalls
  ✅ ANALYZED Performance optimization techniques
  ✅ STUDIED Accessibility patterns with Vuetify components
```

### Template Package Generation

Create complete Vue 3 context engineering template package:

```yaml
Generation Task 1 - Create Vue 3 Template Directory Structure:
  CREATE complete use case directory:
    - use-cases/vue3-frontend/
    - .claude/commands/ with Vue-specific PRP commands
    - PRPs/templates/ with Vue 3 base PRP template
    - examples/ with working Vue 3 component examples
    - All required subdirectories per template package requirements

Generation Task 2 - Generate Vue 3-Specific CLAUDE.md:
  CREATE Vue 3 technology-specific global rules:
    - Vue 3 + Vite + pnpm development commands and workflows
    - Component architecture patterns and TypeScript integration
    - Vuetify Material Design component usage patterns
    - Pinia state management and Vue Router navigation patterns
    - Testing strategies with Vitest and Playwright
    - Common Vue 3 gotchas and performance considerations

Generation Task 3 - Create Vue 3 Template PRP Commands:
  GENERATE Vue 3-specific slash commands:
    - generate-vue3-prp.md with frontend research patterns
    - execute-vue3-prp.md with component and E2E validation loops
    - Commands reference Vue 3 ecosystem patterns from research
    - Include web search strategies for Vue/frontend development

Generation Task 4 - Develop Vue 3-Specific Base PRP Template:
  CREATE specialized prp_vue3_base.md template:
    - Pre-filled with Vue 3 + TypeScript + Vuetify context
    - Frontend-specific success criteria and validation gates
    - Vue ecosystem documentation references from research
    - Component testing and E2E testing validation loops

Generation Task 5 - Create Vue 3 Examples and INITIAL.md Template:
  GENERATE comprehensive Vue 3 template content:
    - INITIAL.md example for Vue 3 feature requests
    - Working Vue 3 component examples with TypeScript
    - Vuetify Material Design component demonstrations
    - Pinia store examples and Vue Router configuration
    - Vitest component tests and Playwright E2E test examples

Generation Task 6 - Create Template Copy Script:
  CREATE Python script for Vue 3 template deployment:
    - copy_template.py with target directory support
    - Copies complete Vue 3 template structure
    - Includes all files: CLAUDE.md, commands, PRPs, examples
    - Error handling and success feedback

Generation Task 7 - Generate Vue 3 Comprehensive README:
  CREATE Vue 3-specific README.md:
    - Vue 3 template purpose and modern frontend development focus
    - PRP framework workflow with Vue 3 examples
    - Template copy script usage (prominently featured)
    - Vue 3 + TypeScript + Vuetify quick start guide
    - Template structure with explanations of Vue patterns
    - Common Vue 3 gotchas and troubleshooting guide
```

### Vue 3 Specialization Details

```typescript
// Vue 3 frontend specialization patterns (from research)
const vue3Specialization = {
  patterns: [
    "component_composition_api", "typescript_integration",
    "material_design_vuetify", "reactive_state_management",
    "spa_routing", "responsive_design"
  ],
  validation: [
    "component_unit_testing", "e2e_user_flows",
    "accessibility_testing", "performance_testing",
    "type_checking", "build_optimization"
  ],
  examples: [
    "basic_vue3_app", "material_design_components",
    "pinia_state_integration", "router_navigation",
    "form_handling", "api_data_fetching"
  ],
  gotchas: [
    "reactivity_pitfalls", "typescript_component_typing",
    "vuetify_tree_shaking", "build_performance",
    "testing_async_components", "ssr_considerations"
  ]
};
```

## Validation Loop

### Level 1: Vue 3 Template Structure Validation

```bash
# CRITICAL: Verify complete Vue 3 template package structure
find use-cases/vue3-frontend -type f | sort
ls -la use-cases/vue3-frontend/.claude/commands/
ls -la use-cases/vue3-frontend/PRPs/templates/

# Verify Vue 3 copy script exists and is functional
test -f use-cases/vue3-frontend/copy_template.py
python use-cases/vue3-frontend/copy_template.py --help 2>/dev/null || echo "Copy script needs help option"

# Expected: All required files present including Vue 3 specialized content
# If missing: Generate missing files following Vue 3 patterns from research
```

### Level 2: Vue 3 Content Quality Validation

```bash
# Verify Vue 3-specific content accuracy (no placeholders)
grep -r "TODO\|PLACEHOLDER\|{vue3}" use-cases/vue3-frontend/
grep -r "TypeScript" use-cases/vue3-frontend/ | wc -l
grep -r "Vuetify" use-cases/vue3-frontend/ | wc -l
grep -r "Pinia" use-cases/vue3-frontend/ | wc -l

# Check for Vue 3 ecosystem patterns
grep -r "Composition API\|script setup" use-cases/vue3-frontend/
grep -r "vitest\|playwright" use-cases/vue3-frontend/.claude/commands/

# Expected: No placeholder content, Vue 3 patterns present throughout
# If issues: Research and add proper Vue 3-specific content
```

### Level 3: Vue 3 Functional Validation

```bash
# Test Vue 3 template functionality
cd use-cases/vue3-frontend

# Test Vue 3 PRP generation command
/generate-vue3-prp INITIAL.md
ls PRPs/*.md | grep -v templates

# Test Vue 3 template completeness and specialization
grep -r "Context is King" . | wc -l  # Should inherit base principles
grep -r "vue3\|Vue 3" . | wc -l      # Should have Vue 3 specializations
grep -r "Material Design" . | wc -l   # Should include Vuetify patterns

# Expected: Vue 3 PRP generation works, content is specialized for frontend
# If failing: Debug Vue 3 command patterns and template structure
```

### Level 4: Vue 3 Integration Testing

```bash
# Verify integration with base context engineering framework
diff -r ../../.claude/commands/ .claude/commands/ | head -20
diff ../../CLAUDE.md CLAUDE.md | head -20

# Test Vue 3 template produces working results
cd examples/
# Verify Vue 3 examples can be validated (TypeScript compilation, etc.)

# Expected: Proper Vue 3 specialization without breaking base patterns
# If issues: Adjust Vue 3 specialization to maintain compatibility
```

## Final Validation Checklist

### Vue 3 Template Package Completeness

- [ ] Complete Vue 3 directory structure: `tree use-cases/vue3-frontend`
- [ ] All Vue 3 files present: CLAUDE.md, commands, base PRP, examples
- [ ] Vue 3 copy script present: `copy_template.py` with functionality
- [ ] Vue 3 README comprehensive: Copy script instructions and PRP workflow
- [ ] Vue 3-specific content: TypeScript + Vuetify + Pinia patterns documented
- [ ] Working Vue 3 examples: Components, stores, and tests compile successfully
- [ ] Vue 3 documentation complete: README and usage instructions clear

### Quality and Usability

- [ ] No placeholder content: `grep -r "TODO\|PLACEHOLDER"`
- [ ] Vue 3 specialization: Frontend patterns properly documented
- [ ] Testing validation loops: Vitest and Playwright commands executable
- [ ] Base framework integration: Works with context engineering principles
- [ ] Beginner ready: Vue 3 developers can immediately use template

### Framework Integration

- [ ] Inherits base principles: Context engineering workflow preserved
- [ ] Vue 3 specialization: Frontend-specific patterns included
- [ ] Command compatibility: Vue 3 slash commands work as expected
- [ ] Documentation consistency: Follows established patterns
- [ ] Maintainable structure: Easy to update as Vue ecosystem evolves

---

## Anti-Patterns to Avoid

### Vue 3 Template Generation

- ❌ Don't create generic frontend templates - specialize deeply for Vue 3 ecosystem
- ❌ Don't skip Vue 3 + TypeScript research - understand modern patterns thoroughly
- ❌ Don't use placeholder content - include real Vue 3 code and configurations
- ❌ Don't ignore testing strategies - include both Vitest and Playwright validation

### Vue 3 Content Quality

- ❌ Don't assume Vue knowledge - document Composition API and TypeScript patterns
- ❌ Don't skip Material Design - include comprehensive Vuetify component usage
- ❌ Don't ignore performance - document Vue 3 optimization and build strategies
- ❌ Don't forget accessibility - ensure Vuetify a11y patterns are documented

### Vue 3 Framework Integration

- ❌ Don't break context engineering - maintain compatibility with base workflow
- ❌ Don't duplicate base patterns - reuse and extend framework components
- ❌ Don't ignore Vue conventions - follow Vue 3 + TypeScript naming standards
- ❌ Don't skip validation - ensure Vue 3 templates actually compile and run

**Confidence Level: 9/10** - Comprehensive web research completed, Vue 3 ecosystem thoroughly understood, template will create immediately usable Vue 3 development environment following 2025 best practices.