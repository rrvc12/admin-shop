<template>
  <aside class="w-full lg:w-64 flex-shrink-0">
    <div class="bg-white p-6 rounded-xl shadow-sm border border-gray-100 sticky top-24">
      <div class="flex items-center justify-between mb-4">
        <h3 class="font-bold text-lg text-slate-900">Filters</h3>
        <button
          id="clear-filters"
          class="text-xs text-indigo-600 hover:text-indigo-700 font-medium"
        >
          Clear All
        </button>
      </div>

      <!-- Search -->
      <div class="mb-6">
        <div class="relative">
          <input
            type="text"
            id="search-input"
            placeholder="Search products..."
            class="w-full pl-9 pr-4 py-2 border border-gray-200 rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-transparent"
          />
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
            class="absolute left-3 top-2.5 text-gray-400"
          >
            <circle cx="11" cy="11" r="8" />
            <path d="m21 21-4.3-4.3" />
          </svg>
        </div>
      </div>

      <!-- Categories -->
      <div class="mb-6">
        <h4 class="font-semibold text-slate-800 mb-3 text-sm uppercase tracking-wider">
          Categories
        </h4>
        <div class="space-y-2">
          <label class="flex items-center space-x-2 cursor-pointer group">
            <input
              type="checkbox"
              value="All"
              class="category-filter form-checkbox h-4 w-4 text-indigo-600 border-gray-300 rounded focus:ring-indigo-500"
              checked
            />
            <span class="text-slate-600 group-hover:text-indigo-600 transition-colors"
              >All Categories</span
            >
          </label>
          <label class="flex items-center space-x-2 cursor-pointer group">
            <input
              type="checkbox"
              value="Accessories"
              class="category-filter form-checkbox h-4 w-4 text-indigo-600 border-gray-300 rounded focus:ring-indigo-500"
            />
            <span class="text-slate-600 group-hover:text-indigo-600 transition-colors"
              >Accessories</span
            >
          </label>
          <label class="flex items-center space-x-2 cursor-pointer group">
            <input
              type="checkbox"
              value="Electronics"
              class="category-filter form-checkbox h-4 w-4 text-indigo-600 border-gray-300 rounded focus:ring-indigo-500"
            />
            <span class="text-slate-600 group-hover:text-indigo-600 transition-colors"
              >Electronics</span
            >
          </label>
          <label class="flex items-center space-x-2 cursor-pointer group">
            <input
              type="checkbox"
              value="Furniture"
              class="category-filter form-checkbox h-4 w-4 text-indigo-600 border-gray-300 rounded focus:ring-indigo-500"
            />
            <span class="text-slate-600 group-hover:text-indigo-600 transition-colors"
              >Furniture</span
            >
          </label>
          <label class="flex items-center space-x-2 cursor-pointer group">
            <input
              type="checkbox"
              value="Clothing"
              class="category-filter form-checkbox h-4 w-4 text-indigo-600 border-gray-300 rounded focus:ring-indigo-500"
            />
            <span class="text-slate-600 group-hover:text-indigo-600 transition-colors"
              >Clothing</span
            >
          </label>
        </div>
      </div>

      <!-- Price Range -->
      <div class="mb-6">
        <h4 class="font-semibold text-slate-800 mb-3 text-sm uppercase tracking-wider">
          Price Range
        </h4>
        <div class="px-2">
          <input
            type="range"
            id="price-range"
            min="0"
            max="1000"
            step="10"
            class="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer accent-indigo-600"
          />
          <div class="flex justify-between text-sm text-slate-600 mt-2">
            <span>$0</span>
            <span id="price-value">$1000+</span>
          </div>
        </div>
      </div>
    </div>
  </aside>
</template>
