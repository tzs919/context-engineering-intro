<template>
  <v-card
    :elevation="hover ? 8 : 2"
    :class="['task-card', { 'task-completed': task.status === 'completed' }]"
    @mouseenter="hover = true"
    @mouseleave="hover = false"
  >
    <v-card-title class="d-flex align-center">
      <v-checkbox
        v-model="isCompleted"
        :color="priorityColor"
        hide-details
        @change="toggleCompletion"
      />
      <span
        :class="{ 'text-decoration-line-through': task.status === 'completed' }"
        class="ml-2 flex-grow-1"
      >
        {{ task.title }}
      </span>
      <v-chip
        :color="priorityColor"
        size="small"
        variant="outlined"
      >
        {{ priorityText }}
      </v-chip>
    </v-card-title>

    <v-card-text v-if="task.description">
      <p class="text-body-2 mb-2">{{ task.description }}</p>
      <div v-if="task.dueDate" class="d-flex align-center">
        <v-icon size="small" class="mr-1">mdi-calendar</v-icon>
        <span class="text-caption">{{ formattedDueDate }}</span>
      </div>
    </v-card-text>

    <v-card-actions>
      <v-btn
        variant="text"
        color="primary"
        size="small"
        @click="$emit('edit', task.id)"
      >
        <v-icon start>mdi-pencil</v-icon>
        编辑
      </v-btn>

      <v-btn
        variant="text"
        color="error"
        size="small"
        @click="confirmDelete"
      >
        <v-icon start>mdi-delete</v-icon>
        删除
      </v-btn>

      <v-spacer />

      <v-btn
        :icon="showDetails ? 'mdi-chevron-up' : 'mdi-chevron-down'"
        variant="text"
        size="small"
        @click="showDetails = !showDetails"
      />
    </v-card-actions>

    <v-expand-transition>
      <div v-show="showDetails">
        <v-divider />
        <v-card-text>
          <div class="d-flex flex-wrap gap-1 mb-2">
            <v-chip
              v-for="tag in task.tags"
              :key="tag"
              size="x-small"
              variant="outlined"
            >
              {{ tag }}
            </v-chip>
          </div>
          <div class="text-caption text-medium-emphasis">
            <div>创建时间: {{ formattedCreatedAt }}</div>
            <div>更新时间: {{ formattedUpdatedAt }}</div>
          </div>
        </v-card-text>
      </div>
    </v-expand-transition>

    <!-- 删除确认对话框 -->
    <v-dialog v-model="deleteDialog" max-width="400">
      <v-card>
        <v-card-title>确认删除</v-card-title>
        <v-card-text>
          确定要删除任务 "{{ task.title }}" 吗？此操作不可撤销。
        </v-card-text>
        <v-card-actions>
          <v-spacer />
          <v-btn variant="text" @click="deleteDialog = false">
            取消
          </v-btn>
          <v-btn
            color="error"
            variant="text"
            @click="handleDelete"
          >
            删除
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-card>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'
import { format } from 'date-fns'
import { zhCN } from 'date-fns/locale'

// 类型定义
interface Task {
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

// Props 和 Emits 定义
interface Props {
  task: Task
}

interface Emits {
  edit: [taskId: string]
  delete: [taskId: string]
  toggleStatus: [taskId: string, status: Task['status']]
}

const props = defineProps<Props>()
const emit = defineEmits<Emits>()

// 响应式状态
const hover = ref(false)
const showDetails = ref(false)
const deleteDialog = ref(false)

// 计算属性
const isCompleted = computed({
  get: () => props.task.status === 'completed',
  set: (value: boolean) => {
    const newStatus = value ? 'completed' : 'pending'
    emit('toggleStatus', props.task.id, newStatus)
  }
})

const priorityColor = computed(() => {
  const colors = {
    low: 'success',
    medium: 'warning',
    high: 'error'
  }
  return colors[props.task.priority]
})

const priorityText = computed(() => {
  const texts = {
    low: '低',
    medium: '中',
    high: '高'
  }
  return texts[props.task.priority]
})

const formattedDueDate = computed(() => {
  if (!props.task.dueDate) return ''
  return format(props.task.dueDate, 'MM月dd日', { locale: zhCN })
})

const formattedCreatedAt = computed(() => {
  return format(props.task.createdAt, 'yyyy年MM月dd日 HH:mm', { locale: zhCN })
})

const formattedUpdatedAt = computed(() => {
  return format(props.task.updatedAt, 'yyyy年MM月dd日 HH:mm', { locale: zhCN })
})

// 方法
const toggleCompletion = () => {
  // 状态切换逻辑已在 computed 中处理
}

const confirmDelete = () => {
  deleteDialog.value = true
}

const handleDelete = () => {
  emit('delete', props.task.id)
  deleteDialog.value = false
}
</script>

<style scoped>
.task-card {
  transition: all 0.3s ease;
  margin-bottom: 1rem;
}

.task-card:hover {
  transform: translateY(-2px);
}

.task-completed {
  opacity: 0.7;
}

.task-completed .v-card-title {
  opacity: 0.8;
}

.gap-1 > * + * {
  margin-left: 0.25rem;
}
</style>