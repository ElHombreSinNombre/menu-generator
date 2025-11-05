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
    <path d="M12 12v4" />
    <path d="M12 20h.01" />
    <path d="M17 18h.5a1 1 0 0 0 0-9h-1.79A7 7 0 1 0 7 17.708" />
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
