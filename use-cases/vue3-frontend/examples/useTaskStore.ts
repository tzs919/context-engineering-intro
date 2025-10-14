/**
 * Vue 3 + Pinia 任务管理 Store 示例
 * 使用 Composition API 语法和完整的 TypeScript 类型定义
 */

import { defineStore } from 'pinia'
import { ref, computed, readonly } from 'vue'

// TypeScript 接口定义
export interface Task {
  id: string
  title: string
  description: string
  status: 'pending' | 'in_progress' | 'completed'
  priority: 'low' | 'medium' | 'high'
  createdAt: Date
  updatedAt: Date
  dueDate?: Date
  tags: string[]
}

export interface TaskFilter {
  status: string
  priority: string
  searchQuery: string
  sortBy: 'createdAt' | 'dueDate' | 'priority' | 'title'
  sortOrder: 'asc' | 'desc'
}

interface TaskState {
  tasks: Task[]
  loading: boolean
  error: string | null
  filter: TaskFilter
}

// API 模拟接口
interface TaskAPI {
  fetchTasks: () => Promise<Task[]>
  createTask: (task: Omit<Task, 'id' | 'createdAt' | 'updatedAt'>) => Promise<Task>
  updateTask: (id: string, updates: Partial<Task>) => Promise<Task>
  deleteTask: (id: string) => Promise<void>
}

// 模拟 API 服务
const taskAPI: TaskAPI = {
  async fetchTasks(): Promise<Task[]> {
    // 模拟 API 延迟
    await new Promise(resolve => setTimeout(resolve, 1000))

    return [
      {
        id: '1',
        title: '完成项目文档',
        description: '编写项目的技术文档和用户手册',
        status: 'in_progress',
        priority: 'high',
        createdAt: new Date('2025-01-01'),
        updatedAt: new Date('2025-01-02'),
        dueDate: new Date('2025-01-15'),
        tags: ['文档', '项目']
      },
      {
        id: '2',
        title: '代码审查',
        description: '审查新功能的代码实现',
        status: 'pending',
        priority: 'medium',
        createdAt: new Date('2025-01-02'),
        updatedAt: new Date('2025-01-02'),
        tags: ['代码', '审查']
      }
    ]
  },

  async createTask(taskData): Promise<Task> {
    await new Promise(resolve => setTimeout(resolve, 500))

    const newTask: Task = {
      ...taskData,
      id: Date.now().toString(),
      createdAt: new Date(),
      updatedAt: new Date()
    }

    return newTask
  },

  async updateTask(id: string, updates: Partial<Task>): Promise<Task> {
    await new Promise(resolve => setTimeout(resolve, 500))

    // 模拟更新任务
    const updatedTask: Task = {
      id,
      title: updates.title || '示例任务',
      description: updates.description || '',
      status: updates.status || 'pending',
      priority: updates.priority || 'medium',
      createdAt: updates.createdAt || new Date(),
      updatedAt: new Date(),
      dueDate: updates.dueDate,
      tags: updates.tags || []
    }

    return updatedTask
  },

  async deleteTask(id: string): Promise<void> {
    await new Promise(resolve => setTimeout(resolve, 500))
    // 删除操作完成
  }
}

// Pinia Store 定义 - 使用 Composition API 语法
export const useTaskStore = defineStore('tasks', () => {
  // State - 使用 ref 定义响应式状态
  const tasks = ref<Task[]>([])
  const loading = ref(false)
  const error = ref<string | null>(null)
  const filter = ref<TaskFilter>({
    status: 'all',
    priority: 'all',
    searchQuery: '',
    sortBy: 'createdAt',
    sortOrder: 'desc'
  })

  // Getters - 使用 computed 定义计算属性
  const filteredTasks = computed(() => {
    let filtered = [...tasks.value]

    // 按状态过滤
    if (filter.value.status !== 'all') {
      filtered = filtered.filter(task => task.status === filter.value.status)
    }

    // 按优先级过滤
    if (filter.value.priority !== 'all') {
      filtered = filtered.filter(task => task.priority === filter.value.priority)
    }

    // 按搜索关键词过滤
    if (filter.value.searchQuery) {
      const query = filter.value.searchQuery.toLowerCase()
      filtered = filtered.filter(task =>
        task.title.toLowerCase().includes(query) ||
        task.description.toLowerCase().includes(query) ||
        task.tags.some(tag => tag.toLowerCase().includes(query))
      )
    }

    // 排序
    filtered.sort((a, b) => {
      const aValue = a[filter.value.sortBy]
      const bValue = b[filter.value.sortBy]

      if (aValue instanceof Date && bValue instanceof Date) {
        return filter.value.sortOrder === 'asc'
          ? aValue.getTime() - bValue.getTime()
          : bValue.getTime() - aValue.getTime()
      }

      if (typeof aValue === 'string' && typeof bValue === 'string') {
        return filter.value.sortOrder === 'asc'
          ? aValue.localeCompare(bValue)
          : bValue.localeCompare(aValue)
      }

      return 0
    })

    return filtered
  })

  const taskStats = computed(() => ({
    total: tasks.value.length,
    pending: tasks.value.filter(task => task.status === 'pending').length,
    inProgress: tasks.value.filter(task => task.status === 'in_progress').length,
    completed: tasks.value.filter(task => task.status === 'completed').length
  }))

  const completionRate = computed(() => {
    if (tasks.value.length === 0) return 0
    return Math.round((taskStats.value.completed / taskStats.value.total) * 100)
  })

  const overdueTasks = computed(() => {
    const now = new Date()
    return tasks.value.filter(task =>
      task.dueDate &&
      task.status !== 'completed' &&
      task.dueDate < now
    )
  })

  // Actions - 定义异步操作和状态修改方法
  const fetchTasks = async () => {
    loading.value = true
    error.value = null

    try {
      const fetchedTasks = await taskAPI.fetchTasks()
      tasks.value = fetchedTasks
    } catch (err) {
      error.value = err instanceof Error ? err.message : '获取任务失败'
      console.error('Failed to fetch tasks:', err)
    } finally {
      loading.value = false
    }
  }

  const createTask = async (taskData: Omit<Task, 'id' | 'createdAt' | 'updatedAt'>) => {
    loading.value = true
    error.value = null

    try {
      const newTask = await taskAPI.createTask(taskData)
      tasks.value.unshift(newTask) // 添加到开头
      return newTask
    } catch (err) {
      error.value = err instanceof Error ? err.message : '创建任务失败'
      console.error('Failed to create task:', err)
      throw err
    } finally {
      loading.value = false
    }
  }

  const updateTask = async (id: string, updates: Partial<Task>) => {
    loading.value = true
    error.value = null

    try {
      const updatedTask = await taskAPI.updateTask(id, {
        ...updates,
        updatedAt: new Date()
      })

      const index = tasks.value.findIndex(task => task.id === id)
      if (index !== -1) {
        tasks.value[index] = updatedTask
      }

      return updatedTask
    } catch (err) {
      error.value = err instanceof Error ? err.message : '更新任务失败'
      console.error('Failed to update task:', err)
      throw err
    } finally {
      loading.value = false
    }
  }

  const deleteTask = async (id: string) => {
    loading.value = true
    error.value = null

    try {
      await taskAPI.deleteTask(id)
      tasks.value = tasks.value.filter(task => task.id !== id)
    } catch (err) {
      error.value = err instanceof Error ? err.message : '删除任务失败'
      console.error('Failed to delete task:', err)
      throw err
    } finally {
      loading.value = false
    }
  }

  const toggleTaskStatus = async (id: string, status: Task['status']) => {
    const task = tasks.value.find(t => t.id === id)
    if (!task) return

    await updateTask(id, { status })
  }

  const setFilter = (newFilter: Partial<TaskFilter>) => {
    filter.value = { ...filter.value, ...newFilter }
  }

  const clearFilter = () => {
    filter.value = {
      status: 'all',
      priority: 'all',
      searchQuery: '',
      sortBy: 'createdAt',
      sortOrder: 'desc'
    }
  }

  const clearError = () => {
    error.value = null
  }

  // 批量操作
  const markAllAsCompleted = async () => {
    const pendingTasks = tasks.value.filter(task => task.status !== 'completed')

    for (const task of pendingTasks) {
      await updateTask(task.id, { status: 'completed' })
    }
  }

  const deleteCompletedTasks = async () => {
    const completedTasks = tasks.value.filter(task => task.status === 'completed')

    for (const task of completedTasks) {
      await deleteTask(task.id)
    }
  }

  // 返回 store 的公共接口
  return {
    // State (只读)
    tasks: readonly(tasks),
    loading,
    error,
    filter,

    // Getters
    filteredTasks,
    taskStats,
    completionRate,
    overdueTasks,

    // Actions
    fetchTasks,
    createTask,
    updateTask,
    deleteTask,
    toggleTaskStatus,
    setFilter,
    clearFilter,
    clearError,
    markAllAsCompleted,
    deleteCompletedTasks
  }
})

// 导出类型以供组件使用
export type TaskStore = ReturnType<typeof useTaskStore>