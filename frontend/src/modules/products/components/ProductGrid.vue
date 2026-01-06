<template>
  <div class="flex-1">
    <!-- Sorting Bar -->
    <div
      class="flex justify-between items-center mb-6 bg-white p-4 rounded-lg border border-gray-100 shadow-sm"
    >
      <span v-if="productList" class="text-slate-600 text-sm"
        >Showing
        <span class="font-semibold text-slate-900">{{ productList.count }}</span>
        results</span
      >
      <select
        class="border-none text-sm text-slate-700 font-medium focus:ring-0 cursor-pointer bg-transparent"
      >
        <option value="featured">Sort by: Featured</option>
        <option value="price-low">Price: Low to High</option>
        <option value="price-high">Price: High to Low</option>
        <option value="newest">Newest Arrivals</option>
      </select>
    </div>
    <template v-if="productList">
      <!-- Grid -->
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
        <ProductCard v-for="product in productList.results" :key="product.id" :product="product" />
      </div>

      <!-- Pagination -->
      <ButtonPagination :num-pages="productList.num_pages" :current-page="currentPage" />
    </template>
  </div>
</template>

<script lang="ts" setup>
import ButtonPagination from '@/modules/common/components/ButtonPagination.vue';
import type { ProductList } from '../interfaces/product.interface';
import ProductCard from './ProductCard.vue';

interface Props {
  productList: ProductList | undefined;
  currentPage: number;
}
defineProps<Props>();
</script>
