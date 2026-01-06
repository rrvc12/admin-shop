<template>
  <div class="pt-32 pb-12 bg-white border-b border-gray-200">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <h1 class="text-4xl font-extrabold text-slate-900 tracking-tight">Our Collection</h1>
      <p class="mt-4 text-slate-500 max-w-2xl">
        Browse our extensive range of premium products designed to elevate your lifestyle.
      </p>
    </div>
  </div>

  <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
    <div class="flex flex-col lg:flex-row gap-8">
      <!-- Sidebar / Filters -->
      <ProductFilters />

      <!-- Product Grid -->
      <ProductGrid :product-list="productList" :current-page="page" />
    </div>
  </main>
</template>

<script setup lang="ts">
import { productsListAction } from '@/modules/products/actions/products-list.action';
import ProductFilters from '@/modules/products/components/ProductFilters.vue';
import ProductGrid from '@/modules/products/components/ProductGrid.vue';
import { useQuery, useQueryClient } from '@tanstack/vue-query';
import { ref, watch, watchEffect } from 'vue';
import { useRoute } from 'vue-router';

const route = useRoute();
const page = ref(Number(route.query.page || 1));
const queryClient = useQueryClient();

const { data: productList } = useQuery({
  queryKey: ['products', page],
  queryFn: () => productsListAction(page.value),
});

watch(
  () => route.query.page,
  (newPage) => {
    page.value = Number(newPage || 1);

    window.scrollTo({ top: 0, behavior: 'smooth' });
  },
);

watchEffect(() => {
  // Hacemos prefetch de la siguiente página
  queryClient.prefetchQuery({
    queryKey: ['products', page.value + 1],
    queryFn: () => productsListAction(page.value + 1),
  });
});
</script>
