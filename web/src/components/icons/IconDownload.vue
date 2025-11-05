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
    @click="$emit('click', $event)"
  >
    <title>{{ tooltip }}</title>
    <path d="M12 13v8l-4-4" />
    <path d="m12 21 4-4" />
    <path d="M4.393 15.269A7 7 0 1 1 15.71 8h1.79a4.5 4.5 0 0 1 2.436 8.284" />
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
