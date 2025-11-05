import type { SelectedFoodItem } from '@interfaces/SelectedFoodItem'
import type { MenuItem } from '@interfaces/MenuItem'
const endpoint = import.meta.env.VITE_API_ENDPOINT
const token = import.meta.env.VITE_API_BEARER

interface MenuParams {
  foods: SelectedFoodItem[]
}

const generateMenu = async ({ foods }: MenuParams): Promise<MenuItem[]> => {
  const response = await fetch(`${endpoint}/generate`, {
    method: 'POST',
    headers: {
      Authorization: `Bearer ${token}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      language: navigator.language ?? 'es',
      elements: foods,
    }),
  })
  if (!response.ok) throw new Error('Failed to generate menu')
  const data = await response.json()
  return data.menu as MenuItem[]
}

export default generateMenu
