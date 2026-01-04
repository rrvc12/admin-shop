<template>
  <footer class="bg-white border-t border-gray-200 mt-20">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
      <div class="grid grid-cols-1 md:grid-cols-4 gap-8">
        <div class="col-span-1 md:col-span-1">
          <div class="flex items-center gap-2 mb-4">
            <div class="bg-indigo-600 text-white p-1 rounded">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="18"
                height="18"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="2"
                stroke-linecap="round"
                stroke-linejoin="round"
              >
                <path d="M6 2 3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4Z" />
                <path d="M3 6h18" />
                <path d="M16 10a4 4 0 0 1-8 0" />
              </svg>
            </div>
            <span class="font-bold text-xl text-slate-900">Shop</span>
          </div>
          <p class="text-slate-500 text-sm">
            Experience the best in quality and design. We bring you the finest products to enhance
            your lifestyle.
          </p>
        </div>

        <div>
          <h3 class="font-bold text-slate-900 mb-4">Shop</h3>
          <ul class="space-y-2 text-sm text-slate-600">
            <li><a href="#" class="hover:text-indigo-600">New Arrivals</a></li>
            <li><a href="#" class="hover:text-indigo-600">Best Sellers</a></li>
            <li><a href="#" class="hover:text-indigo-600">Categories</a></li>
            <li><a href="#" class="hover:text-indigo-600">Sale</a></li>
          </ul>
        </div>

        <div>
          <h3 class="font-bold text-slate-900 mb-4">Company</h3>
          <ul class="space-y-2 text-sm text-slate-600">
            <li><a href="#" class="hover:text-indigo-600">About Us</a></li>
            <li><a href="#" class="hover:text-indigo-600">Careers</a></li>
            <li><a href="#" class="hover:text-indigo-600">Press</a></li>
            <li><a href="#" class="hover:text-indigo-600">Contact</a></li>
          </ul>
        </div>

        <div>
          <h3 class="font-bold text-slate-900 mb-4">Newsletter</h3>
          <p class="text-sm text-slate-500 mb-4">
            Subscribe to get special offers, free giveaways, and once-in-a-lifetime deals.
          </p>
          <div class="flex gap-2">
            <input
              type="email"
              placeholder="Enter your email"
              class="flex-1 px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-transparent"
            />
            <button
              class="bg-indigo-600 hover:bg-indigo-700 text-white px-4 py-2 rounded-lg font-medium transition-colors"
            >
              Join
            </button>
          </div>
        </div>
      </div>
      <div
        class="border-t border-gray-100 mt-12 pt-8 flex flex-col md:flex-row justify-between items-center"
      >
        <p class="text-sm text-slate-500">
          © {{ new Date().getFullYear() }} Raúl. All rights reserved.
        </p>
        <div class="flex space-x-6 mt-4 md:mt-0">
          <a href="#" class="text-slate-400 hover:text-indigo-600 transition-colors">Terms</a>
          <a href="#" class="text-slate-400 hover:text-indigo-600 transition-colors">Privacy</a>
          <a href="#" class="text-slate-400 hover:text-indigo-600 transition-colors">Cookies</a>
        </div>
      </div>
    </div>
  </footer>
</template>
