import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import tailwindVitePlugin from '@tailwindcss/vite'
import path from 'path' // 👈 1. Importar el módulo 'path'

const __dirname = path.resolve()

export default defineConfig({
  plugins: [vue(), tailwindVitePlugin()],
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src'),
      '@components': path.resolve(__dirname, './src/components'),
      '@interfaces': path.resolve(__dirname, './src/interfaces'),
      '@services': path.resolve(__dirname, './src/services'),
    },
  },
})
