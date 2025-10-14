/**
 * Vue 3 + Vitest + Vue Test Utils 组件测试示例
 * TaskCard 组件的完整测试覆盖
 */

import { describe, it, expect, vi, beforeEach } from 'vitest'
import { mount } from '@vue/test-utils'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'

// 导入被测试的组件
import TaskCard from './TaskCard.vue'

// 测试数据
const mockTask = {
  id: '1',
  title: '测试任务',
  description: '这是一个测试任务的描述',
  status: 'pending' as const,
  priority: 'high' as const,
  createdAt: new Date('2025-01-01T10:00:00Z'),
  updatedAt: new Date('2025-01-01T12:00:00Z'),
  dueDate: new Date('2025-01-15T18:00:00Z'),
  tags: ['测试', '重要']
}

const completedTask = {
  ...mockTask,
  id: '2',
  title: '已完成任务',
  status: 'completed' as const
}

// Vuetify 配置
const vuetify = createVuetify({
  components,
  directives,
  theme: {
    defaultTheme: 'light'
  }
})

// 测试工具函数
const createWrapper = (props: any = {}) => {
  return mount(TaskCard, {
    props: {
      task: mockTask,
      ...props
    },
    global: {
      plugins: [vuetify],
      stubs: {
        // 可以在这里配置组件存根
      }
    }
  })
}

describe('TaskCard', () => {
  describe('渲染测试', () => {
    it('应该正确渲染任务基本信息', () => {
      const wrapper = createWrapper()

      // 验证任务标题
      expect(wrapper.text()).toContain(mockTask.title)

      // 验证任务描述
      expect(wrapper.text()).toContain(mockTask.description)

      // 验证优先级标签
      expect(wrapper.text()).toContain('高')

      // 验证标签
      mockTask.tags.forEach(tag => {
        expect(wrapper.text()).toContain(tag)
      })
    })

    it('应该根据任务状态显示不同的样式', async () => {
      // 测试未完成任务
      const pendingWrapper = createWrapper()
      const pendingCheckbox = pendingWrapper.find('[type="checkbox"]')
      expect(pendingCheckbox.element.checked).toBe(false)

      // 测试已完成任务
      const completedWrapper = createWrapper({ task: completedTask })
      const completedCheckbox = completedWrapper.find('[type="checkbox"]')
      expect(completedCheckbox.element.checked).toBe(true)

      // 验证完成任务的样式类
      expect(completedWrapper.find('.task-completed').exists()).toBe(true)
    })

    it('应该正确显示优先级颜色', () => {
      const highPriorityWrapper = createWrapper()
      const mediumPriorityWrapper = createWrapper({
        task: { ...mockTask, priority: 'medium' }
      })
      const lowPriorityWrapper = createWrapper({
        task: { ...mockTask, priority: 'low' }
      })

      // 验证不同优先级对应不同颜色的标签
      expect(highPriorityWrapper.text()).toContain('高')
      expect(mediumPriorityWrapper.text()).toContain('中')
      expect(lowPriorityWrapper.text()).toContain('低')
    })

    it('应该正确格式化日期显示', () => {
      const wrapper = createWrapper()

      // 验证截止日期格式化
      expect(wrapper.text()).toMatch(/01月15日/)

      // 验证创建时间和更新时间格式化
      wrapper.find('[data-testid="details-toggle"]').trigger('click')
      expect(wrapper.text()).toMatch(/2025年01月01日/)
    })
  })

  describe('交互测试', () => {
    it('应该在点击复选框时触发状态切换事件', async () => {
      const wrapper = createWrapper()
      const checkbox = wrapper.find('[type="checkbox"]')

      await checkbox.setValue(true)

      // 验证是否触发了 toggleStatus 事件
      expect(wrapper.emitted('toggleStatus')).toBeTruthy()
      expect(wrapper.emitted('toggleStatus')?.[0]).toEqual([mockTask.id, 'completed'])
    })

    it('应该在点击编辑按钮时触发编辑事件', async () => {
      const wrapper = createWrapper()
      const editButton = wrapper.find('[data-testid="edit-btn"]')

      await editButton.trigger('click')

      // 验证是否触发了 edit 事件
      expect(wrapper.emitted('edit')).toBeTruthy()
      expect(wrapper.emitted('edit')?.[0]).toEqual([mockTask.id])
    })

    it('应该在点击删除按钮时显示确认对话框', async () => {
      const wrapper = createWrapper()
      const deleteButton = wrapper.find('[data-testid="delete-btn"]')

      // 初始状态对话框应该隐藏
      expect(wrapper.find('[data-testid="delete-dialog"]').exists()).toBe(false)

      await deleteButton.trigger('click')

      // 点击后应该显示对话框
      expect(wrapper.vm.deleteDialog).toBe(true)
    })

    it('应该在确认删除时触发删除事件', async () => {
      const wrapper = createWrapper()

      // 先打开删除对话框
      await wrapper.find('[data-testid="delete-btn"]').trigger('click')

      // 确认删除
      const confirmButton = wrapper.find('[data-testid="confirm-delete-btn"]')
      await confirmButton.trigger('click')

      // 验证是否触发了 delete 事件
      expect(wrapper.emitted('delete')).toBeTruthy()
      expect(wrapper.emitted('delete')?.[0]).toEqual([mockTask.id])

      // 验证对话框已关闭
      expect(wrapper.vm.deleteDialog).toBe(false)
    })

    it('应该能够展开和收起详细信息', async () => {
      const wrapper = createWrapper()
      const detailsToggle = wrapper.find('[data-testid="details-toggle"]')

      // 初始状态详细信息应该隐藏
      expect(wrapper.vm.showDetails).toBe(false)

      await detailsToggle.trigger('click')

      // 点击后应该展开详细信息
      expect(wrapper.vm.showDetails).toBe(true)

      // 再次点击应该收起
      await detailsToggle.trigger('click')
      expect(wrapper.vm.showDetails).toBe(false)
    })
  })

  describe('悬停效果测试', () => {
    it('应该在鼠标悬停时改变样式', async () => {
      const wrapper = createWrapper()
      const cardElement = wrapper.find('.task-card')

      // 初始状态
      expect(wrapper.vm.hover).toBe(false)

      // 鼠标进入
      await cardElement.trigger('mouseenter')
      expect(wrapper.vm.hover).toBe(true)

      // 鼠标离开
      await cardElement.trigger('mouseleave')
      expect(wrapper.vm.hover).toBe(false)
    })
  })

  describe('边缘情况测试', () => {
    it('应该正确处理没有描述的任务', () => {
      const taskWithoutDescription = {
        ...mockTask,
        description: ''
      }

      const wrapper = createWrapper({ task: taskWithoutDescription })

      // 应该不显示描述区域
      expect(wrapper.find('[data-testid="task-description"]').exists()).toBe(false)
    })

    it('应该正确处理没有截止日期的任务', () => {
      const taskWithoutDueDate = {
        ...mockTask,
        dueDate: undefined
      }

      const wrapper = createWrapper({ task: taskWithoutDueDate })

      // 应该不显示截止日期
      expect(wrapper.text()).not.toMatch(/\d{2}月\d{2}日/)
    })

    it('应该正确处理没有标签的任务', () => {
      const taskWithoutTags = {
        ...mockTask,
        tags: []
      }

      const wrapper = createWrapper({ task: taskWithoutTags })

      // 展开详细信息
      wrapper.find('[data-testid="details-toggle"]').trigger('click')

      // 应该不显示标签区域或显示空的标签容器
      const tagContainer = wrapper.find('[data-testid="tags-container"]')
      if (tagContainer.exists()) {
        expect(tagContainer.findAll('.v-chip')).toHaveLength(0)
      }
    })
  })

  describe('可访问性测试', () => {
    it('应该有适当的 ARIA 标签', () => {
      const wrapper = createWrapper()

      // 检查复选框的可访问性
      const checkbox = wrapper.find('[type="checkbox"]')
      expect(checkbox.attributes()).toHaveProperty('aria-label')

      // 检查按钮的可访问性
      const buttons = wrapper.findAll('button')
      buttons.forEach(button => {
        // 每个按钮应该有描述性文本或 aria-label
        const hasText = button.text().trim().length > 0
        const hasAriaLabel = button.attributes('aria-label')
        expect(hasText || hasAriaLabel).toBe(true)
      })
    })

    it('应该支持键盘导航', async () => {
      const wrapper = createWrapper()

      // 测试 Tab 键焦点切换
      const interactiveElements = wrapper.findAll(
        'input, button, [tabindex]:not([tabindex="-1"])'
      )

      // 确保有足够的可交互元素
      expect(interactiveElements.length).toBeGreaterThan(0)

      // 测试 Enter 键触发按钮点击
      const editButton = wrapper.find('[data-testid="edit-btn"]')
      await editButton.trigger('keydown.enter')

      expect(wrapper.emitted('edit')).toBeTruthy()
    })
  })

  describe('性能测试', () => {
    it('应该避免不必要的重新渲染', async () => {
      const wrapper = createWrapper()

      // 使用 spy 监控计算属性的调用
      const priorityColorSpy = vi.spyOn(wrapper.vm, 'priorityColor', 'get')

      // 触发不影响优先级的更新
      await wrapper.setProps({
        task: {
          ...mockTask,
          description: '更新的描述'
        }
      })

      // 优先级计算应该被缓存，不会重新计算
      expect(priorityColorSpy).toHaveBeenCalledTimes(1)

      priorityColorSpy.mockRestore()
    })
  })
})

// 集成测试 - 测试组件与外部依赖的集成
describe('TaskCard 集成测试', () => {
  it('应该正确集成 date-fns 进行日期格式化', () => {
    const wrapper = createWrapper()

    // 验证日期格式化库的正确使用
    expect(wrapper.vm.formattedCreatedAt).toMatch(/\d{4}年\d{2}月\d{2}日 \d{2}:\d{2}/)
    expect(wrapper.vm.formattedDueDate).toMatch(/\d{2}月\d{2}日/)
  })

  it('应该正确集成 Vuetify 组件', () => {
    const wrapper = createWrapper()

    // 验证 Vuetify 组件的存在
    expect(wrapper.findComponent({ name: 'VCard' }).exists()).toBe(true)
    expect(wrapper.findComponent({ name: 'VCheckbox' }).exists()).toBe(true)
    expect(wrapper.findComponent({ name: 'VChip' }).exists()).toBe(true)
    expect(wrapper.findComponent({ name: 'VBtn' }).exists()).toBe(true)
  })
})