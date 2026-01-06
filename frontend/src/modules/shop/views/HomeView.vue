<template>
  <!-- Hero Section -->
  <div class="pt-28 pb-12 bg-white">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
      <h1 class="text-4xl md:text-6xl font-extrabold text-slate-900 tracking-tight mb-4">
        Productos <span class="text-indigo-600">Premium</span>
      </h1>
      <p class="text-lg text-slate-600 max-w-2xl mx-auto mb-8">
        Curated collection of high-quality essentials for your modern life. Elevate your everyday
        with our exclusive products.
      </p>
    </div>
  </div>

  <!-- Main Content -->
  <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
    <div class="flex justify-between items-end mb-8">
      <h2 class="text-3xl font-bold text-slate-900">Productos Destacados</h2>
      <RouterLink
        to="/shop"
        class="text-indigo-600 font-medium hover:text-indigo-700 flex items-center gap-1 group"
      >
        Ver más
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
          class="transform group-hover:translate-x-1 transition-transform"
        >
          <path d="M5 12h14" />
          <path d="m12 5 7 7-7 7" />
        </svg>
      </RouterLink>
    </div>
    <div v-if="isLoading">Cargando ...</div>
    <div v-else id="product-list" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-8">
      <ProductCard v-for="product in products" :key="product.id" :product="product" />
    </div>
  </main>
</template>

<script setup lang="ts">
import { useQuery } from '@tanstack/vue-query';

import { productsHomeAction } from '@/modules/products/actions';
import ProductCard from '@/modules/products/components/ProductCard.vue';

const { data: products, isLoading } = useQuery({
  queryKey: ['products-home'],
  queryFn: () => productsHomeAction(),
});
</script>
