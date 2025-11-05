<template>
  <svg
    :width="size"
    :height="size"
    viewBox="0 0 24 24"
    fill="none"
    :stroke="stroke"
    stroke-width="2"
    stroke-linecap="round"
    stroke-linejoin="round"
    v-bind="$attrs"
    @click="$emit('click', $event)"
  >
    <title>{{ tooltip }}</title>
    <path d="M10 11v6" />
    <path d="M14 11v6" />
    <path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6" />
    <path d="M3 6h18" />
    <path d="M8 6V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2" />
  </svg>
</template>

<script setup lang="ts">
  import { withDefaults } from 'vue'
  withDefaults(
    defineProps<{
      size?: number | string
      stroke?: string
      tooltip?: string
    }>(),
    {
      size: 24,
      stroke: 'currentColor',
      tooltip: '',
    }
  )
  const emit = defineEmits<{
    (e: 'click', event: MouseEvent): void
  }>()
</script>
