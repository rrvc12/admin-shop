<template>
  <div
    class="bg-white rounded-xl overflow-hidden shadow-sm card-hover border border-gray-100 flex flex-col"
  >
    <div class="relative h-48 overflow-hidden group">
      <img
        :src="product.image_url ?? ''"
        :alt="product.name"
        class="w-full h-full object-cover transform group-hover:scale-110 transition-transform duration-500"
      />
      <div
        class="absolute top-2 right-2 bg-white/90 backdrop-blur-sm px-2 py-1 rounded-md text-xs font-semibold text-gray-700"
      >
        Accesorios
      </div>
    </div>
    <div class="p-5 flex-1 flex flex-col justify-between">
      <div>
        <h3 class="text-lg font-bold text-gray-800 mb-1">{{ product.name }}</h3>
        <p class="text-2xl font-bold text-indigo-600">$ {{ product.sale_price }}</p>
      </div>
      <button
        class="mt-4 w-full bg-slate-900 hover:bg-indigo-600 text-white font-medium py-2.5 px-4 rounded-lg transition-colors duration-300 flex items-center justify-center gap-2"
      >
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="20"
          height="20"
          viewBox="0 0 24 24"
          fill="none"
          stroke="currentColor"
          stroke-width="2"
          stroke-linecap="round"
          stroke-linejoin="round"
          class="lucide lucide-shopping-cart"
        >
          <circle cx="8" cy="21" r="1" />
          <circle cx="19" cy="21" r="1" />
          <path
            d="M2.05 2.05h2l2.66 12.42a2 2 0 0 0 2 1.58h9.78a2 2 0 0 0 1.95-1.57l1.65-7.43H5.12"
          />
        </svg>
        Añadir al carrito
      </button>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { type Product } from '../interfaces/product.interface';

interface Props {
  product: Product;
}

defineProps<Props>();
</script>
