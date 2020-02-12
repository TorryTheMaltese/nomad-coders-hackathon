<template>
  <router-view></router-view>
</template>

<script>
import router from "./routes/routes.js";
import store from "./stores/store";

export default {
  router,
  store
};
</script>

<style lang="scss" scoped></style>
