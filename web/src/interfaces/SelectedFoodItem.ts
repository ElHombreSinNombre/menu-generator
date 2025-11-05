import type { FoodItem } from './FoodItem' // O la ruta correcta

export interface SelectedFoodItem extends FoodItem {
  number: number
}
