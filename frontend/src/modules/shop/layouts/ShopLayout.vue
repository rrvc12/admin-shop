<template>
  <shop-navbar />
  <RouterView />
  <shop-footer />
</template>

<script setup lang="ts">
import ShopFooter from '../components/ShopFooter.vue';
import ShopNavbar from '../components/ShopNavbar.vue';
</script>
