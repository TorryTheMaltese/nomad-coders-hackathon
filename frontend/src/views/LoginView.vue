<template>
  <div style="margin: 0; height:100%; ">
    <header-nav></header-nav>
    <login></login>
  </div>
</template>

<script>
import HeaderNav from "../components/Header";
import Login from "../components/Login";

export default {
  components: {
    HeaderNav,
    Login
  }
};
</script>

<style lang="scss" scoped>
</style>
