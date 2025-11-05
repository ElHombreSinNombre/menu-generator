import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import tailwindVitePlugin from '@tailwindcss/vite'
import path from 'path'
import { fileURLToPath } from 'url'

const fileName = fileURLToPath(import.meta.url)
const dirName = path.dirname(fileName)

export default defineConfig({
  plugins: [vue(), tailwindVitePlugin()],
  resolve: {
    alias: {
      '@': path.resolve(dirName, './src'),
      '@components': path.resolve(dirName, './src/components'),
      '@interfaces': path.resolve(dirName, './src/interfaces'),
      '@services': path.resolve(dirName, './src/services'),
    },
  },
})
