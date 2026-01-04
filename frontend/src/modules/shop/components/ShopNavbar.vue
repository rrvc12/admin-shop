<template>
  <nav class="fixed w-full z-50 glass-nav transition-all duration-300">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex justify-between items-center h-20">
        <div class="shrink-0 flex items-center gap-2 cursor-pointer">
          <div class="bg-indigo-600 text-white p-1.5 rounded-lg">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="24"
              height="24"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              stroke-width="2"
              stroke-linecap="round"
              stroke-linejoin="round"
              class="lucide lucide-shopping-bag"
            >
              <path d="M6 2 3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4Z" />
              <path d="M3 6h18" />
              <path d="M16 10a4 4 0 0 1-8 0" />
            </svg>
          </div>
          <span class="font-bold text-xl tracking-tight text-slate-900">Shop</span>
        </div>

        <div class="hidden md:flex items-center space-x-8">
          <a href="#" class="text-slate-600 hover:text-indigo-600 font-medium transition-colors"
            >Inicio</a
          >
          <a href="#" class="text-slate-600 hover:text-indigo-600 font-medium transition-colors"
            >Tienda</a
          >
          <a href="#" class="text-slate-600 hover:text-indigo-600 font-medium transition-colors"
            >Contáctanos</a
          >
          <a href="#" class="text-slate-600 hover:text-indigo-600 font-medium transition-colors"
            >Acerca de nosotros</a
          >
        </div>

        <div class="flex items-center space-x-4">
          <a
            href="#"
            class="hidden md:block text-slate-600 hover:text-indigo-600 font-medium transition-colors"
            >Iniciar Sesión</a
          >
          <a
            href="#"
            class="bg-indigo-600 hover:bg-indigo-700 text-white px-5 py-2.5 rounded-full font-medium transition-colors shadow-lg shadow-indigo-200"
          >
            Registrarse
          </a>
        </div>
      </div>
    </div>
  </nav>
</template>
