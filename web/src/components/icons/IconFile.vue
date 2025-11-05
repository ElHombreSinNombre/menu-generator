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
    <path
      d="M6 22a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h8a2.4 2.4 0 0 1 1.704.706l3.588 3.588A2.4 2.4 0 0 1 20 8v12a2 2 0 0 1-2 2z"
    />
    <path d="M14 2v5a1 1 0 0 0 1 1h5" />
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
