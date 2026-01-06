<template>
  <div class="mt-12 flex justify-center">
    <nav class="flex items-center gap-2">
      <button
        @click="$router.push({ query: { page: currentPage - 1 } })"
        :disabled="currentPage === 1"
        class="p-2 rounded-lg border border-gray-200"
        :class="{
          'text-gray-300': currentPage === 1,
          'text-gray-600 hover:bg-gray-50 hover:border-gray-300': currentPage !== 1,
        }"
      >
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="16"
          height="16"
          viewBox="0 0 24 24"
          fill="none"
          stroke="currentColor"
          stroke-width="2"
          stroke-linecap="round"
          stroke-linejoin="round"
        >
          <path d="m15 18-6-6 6-6" />
        </svg>
      </button>
      <!-- Number of pages -->
      <button
        @click="$router.push({ query: { page: page } })"
        v-for="(page, index) in pageNumbers"
        :key="index"
        :disabled="page === '...'"
        class="w-10 h-10 rounded-lg font-medium transition-colors"
        :class="{
          'bg-indigo-600 text-white border border-indigo-600': page === currentPage,
          'text-gray-600 hover:bg-gray-50 border border-gray-200 hover:border-gray-300':
            page !== currentPage && page !== '...',
        }"
      >
        {{ page }}
      </button>

      <button
        @click="$router.push({ query: { page: currentPage + 1 } })"
        :disabled="currentPage === numPages"
        class="p-2 rounded-lg border border-gray-200"
        :class="{
          'text-gray-300': currentPage === numPages,
          'text-gray-600 hover:bg-gray-50 hover:border-gray-300': currentPage !== numPages,
        }"
      >
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="16"
          height="16"
          viewBox="0 0 24 24"
          fill="none"
          stroke="currentColor"
          stroke-width="2"
          stroke-linecap="round"
          stroke-linejoin="round"
        >
          <path d="m9 18 6-6-6-6" />
        </svg>
      </button>
    </nav>
  </div>
</template>

<script lang="ts" setup>
import { computed } from 'vue';

interface Props {
  currentPage: number;
  numPages: number;
}

const props = defineProps<Props>();

const pageNumbers = computed(() => {
  const pages = [];
  const current = props.currentPage;
  const total = props.numPages;

  // Siempre mostrar la primera página
  pages.push(1);

  // Calcular el rango visible (3 antes y 3 después)
  const start = Math.max(2, current - 3);
  const end = Math.min(total - 1, current + 3);

  // Agregar "0" si hay páginas ocultas al inicio
  if (start > 2) {
    pages.push('...');
  }

  // Agregar páginas del rango visible
  for (let i = start; i <= end; i++) {
    pages.push(i);
  }

  // Agregar "0" si hay páginas ocultas al final
  if (end < total - 1) {
    pages.push('...');
  }

  // Siempre mostrar la última página (si hay más de 1)
  if (total > 1) {
    pages.push(total);
  }
  console.log(pages);
  return pages;
});
</script>
