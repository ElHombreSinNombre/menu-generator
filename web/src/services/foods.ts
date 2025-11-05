import type { FoodItem } from '@interfaces/FoodItem'
const endpoint = import.meta.env.VITE_API_ENDPOINT
const token = import.meta.env.VITE_API_BEARER

const getAll = async (): Promise<FoodItem[]> => {
  const response = await fetch(`${endpoint}/foods`, {
    headers: {
      Authorization: `Bearer ${token}`,
      'Content-Type': 'application/json',
    },
  })
  if (!response.ok)
    throw new Error(`Failed to load foods. Status: ${response.status}`)
  const data = await response.json()
  return data as FoodItem[]
}

export default getAll
