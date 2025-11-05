<template>
  <div class="relative w-2xl">
    <select
      :value="modelValue"
      @change="
        $emit('update:modelValue', ($event.target as HTMLSelectElement).value)
      "
      class="appearance-none w-full p-2 border border-gray-300 rounded-md shadow-sm focus:outline-none"
    >
      <slot />
    </select>
  </div>
</template>

<script setup lang="ts">
  defineProps<{
    modelValue: string | number
  }>()
  defineEmits<{
    (e: 'update:modelValue', payload: string | number): void
  }>()
</script>
