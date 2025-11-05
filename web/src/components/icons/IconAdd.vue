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
    <path d="M5 12h14" />
    <path d="M12 5v14" />
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
