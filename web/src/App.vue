<template>
  <main class="center">
    <template v-if="foods.length">
      <article class="card">
        <SelectMenu v-model="selectedFood" @change="addFood">
          <option v-for="food in foods" :key="food.ean" :value="food.ean">
            {{ food.name }}
          </option>
        </SelectMenu>
      </article>
    </template>
    <template v-else-if="isLoading && !foods.length">
      <IconDownload class="animate-ping" tooltip="Loading" />
    </template>
    <template v-else-if="!isLoading && !foods.length">
      <IconError stroke="#E7000b" size="64" tooltip="No data" />
    </template>
    <article class="card" v-if="selectedFoods.length">
      <header
        v-if="selectedFoods.length > 1"
        class="flex justify-between items-center mb-2"
      >
        <IconRemove
          :class="[
            'text-white p-1 rounded bg-red-500 transition-colors duration-300',
            !isLoading
              ? 'cursor-pointer hover:bg-red-700 '
              : 'opacity-50 cursor-not-allowed',
          ]"
          @click="!isLoading && clearAll()"
          tooltip="Remove All"
        />
      </header>
      <ul class="select-none">
        <li
          v-for="food in selectedFoods"
          :key="food.ean"
          class="flex items-center justify-between gap-3 py-1"
        >
          <article class="flex-1 truncate">
            <span class="font-semibold text-gray-800">
              {{ food.name }}
            </span>
            <span class="font-medium text-gray-500" v-if="food.number > 1">
              ({{ food.number }})</span
            >
          </article>
          <IconAdd
            :class="[
              'text-green-500 rounded transition-colors duration-300',
              !isLoading
                ? 'cursor-pointer hover:text-green-700 '
                : 'opacity-50 cursor-not-allowed',
            ]"
            tooltip="Add food"
            @click="!isLoading && addOne(food)"
          />
          <IconRemove
            :class="[
              'text-red-500 p-1 rounded transition-colors duration-300',
              !isLoading
                ? 'cursor-pointer hover:text-red-700 '
                : 'opacity-50 cursor-not-allowed',
            ]"
            tooltip="Delete food"
            @click="!isLoading && removeOne(food)"
          />
        </li>
      </ul>
      <template v-if="selectedFoods.length < 5">
        <div
          class="bg-orange-100 border-l-4 border-orange-500 text-orange-700 p-4"
          role="alert"
        >
          <p>You need to select more than 5 different items</p>
        </div>
      </template>
      <button
        @click="generate()"
        :disabled="isLoading"
        :class="[
          'button flex items-center justify-center',
          !isLoading
            ? 'cursor-pointer hover:bg-indigo-500'
            : 'opacity-50 cursor-not-allowed',
        ]"
      >
        <template v-if="isLoading">
          <span
            class="w-5 h-5 border-2 border-white border-t-transparent rounded-full animate-spin"
          ></span>
        </template>
        <template v-else> Create menu </template>
      </button>
    </article>
    <article class="card" v-if="weeklyMenu.length" ref="menuTable">
      <table
        class="w-full border border-collapse rounded-lg border-gray-200 shadow-md hover:shadow-lg transition-shadow duration-300"
      >
        <thead>
          <tr class="bg-gray-700 text-white text-center font-bold">
            <th class="px-4 py-5">Day</th>
            <th class="px-4 py-5">Breakfast</th>
            <th class="px-4 py-5">Lunch</th>
            <th class="px-4 py-5">Dinner</th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="(data, index) in weeklyMenu"
            :key="index"
            class="odd:bg-gray-100 even:bg-white hover:bg-gray-200 transition-colors duration-300 text-center"
          >
            <td class="px-4 py-4 bg-gray-700 text-white font-bold">
              {{ data.day }}
            </td>
            <td class="px-4 py-4 border">
              {{ data.breakfast }}
            </td>
            <td class="px-4 py-4 border">{{ data.lunch }}</td>
            <td class="px-4 py-4 border">{{ data.dinner }}</td>
          </tr>
        </tbody>
      </table>
      <span
        @click="exportToPDF()"
        class="cursor-pointer fixed bottom-4 right-4 z-50 p-2 bg-blue-500 hover:bg-blue-700 text-white rounded-full shadow-lg transition-all duration-300"
      >
        <IconFile tooltip="Generate PDF" />
      </span>
    </article>
  </main>
</template>

<script setup lang="ts">
  import { ref, onMounted } from 'vue'
  import SelectMenu from '@components/SelectMenu.vue'
  import IconRemove from '@components/icons/IconRemove.vue'
  import IconAdd from '@components/icons/IconAdd.vue'
  import IconDownload from '@components/icons/IconDownload.vue'
  import IconError from '@components/icons/IconError.vue'
  import IconFile from '@components/icons/IconFile.vue'
  import getAll from '@services/foods'
  import generateMenu from '@services/llama3'
  import type { FoodItem } from '@interfaces/FoodItem'
  import type { SelectedFoodItem } from '@interfaces/SelectedFoodItem'
  import type { MenuItem } from '@interfaces/MenuItem'
  import { toPng } from 'html-to-image'
  import { jsPDF } from 'jspdf'

  const foods = ref<FoodItem[]>([])
  const selectedFoods = ref<SelectedFoodItem[]>([])
  const selectedFood = ref<string>('')
  const weeklyMenu = ref(<MenuItem[]>[])
  const menuTable = ref(null)
  const isLoading = ref(false)

  const loadFoods = async () => {
    try {
      isLoading.value = true
      const data = await getAll()
      foods.value = data
      if (foods.value.length > 0) selectedFood.value = foods.value[0].ean
      return { success: true, data: data }
    } catch (error) {
      console.error('An error occurred loading foods:', error)
      return { success: false, data: error }
    } finally {
      isLoading.value = false
    }
  }

  onMounted(loadFoods)

  const addFood = () => {
    const food = foods.value.find(
      (item: FoodItem) => item.ean === selectedFood.value
    )
    if (food) {
      const foodExist = selectedFoods.value.find(
        (item: SelectedFoodItem) => item.ean === selectedFood.value
      )
      if (!foodExist)
        selectedFoods.value.push({
          ...food,
          number: 1,
        })
    }
  }

  const clearAll = () => {
    selectedFoods.value = []
    weeklyMenu.value = []
  }

  const addOne = (item: SelectedFoodItem) => {
    item.number++
  }

  const removeOne = (item: SelectedFoodItem) => {
    if (item.number >= 1) item.number--
    if (item.number == 0)
      selectedFoods.value = selectedFoods.value.filter(
        (item: SelectedFoodItem) => item.number !== 0
      )
  }

  const generate = async () => {
    try {
      isLoading.value = true
      const data = await generateMenu({ foods: selectedFoods.value })
      weeklyMenu.value = data
      return { success: true, data: data }
    } catch (error) {
      console.error('An error occurred creating menu', error)
      return { success: false, data: error }
    } finally {
      isLoading.value = false
    }
  }

  const exportToPDF = async () => {
    const doc = new jsPDF('l', 'mm', 'a4')
    const source = menuTable.value as unknown as HTMLElement
    if (!source) {
      console.warn('Table doesn´t exist')
      return
    }
    try {
      const imgData = await toPng(source)
      const pdfW = doc.internal.pageSize.getWidth()
      const pdfH = doc.internal.pageSize.getHeight()
      const { offsetWidth: elW, offsetHeight: elH } = source
      const ratio = Math.min(pdfW / elW, pdfH / elH)
      const imgW = elW * ratio
      const imgH = elH * ratio
      const x = (pdfW - imgW) / 2
      const y = (pdfH - imgH) / 2
      doc.addImage(imgData, 'PNG', x, y, imgW, imgH)
      doc.save('weekly-menu.pdf')
    } catch (error) {
      console.error('Error creating PDF', error)
    }
  }
</script>
