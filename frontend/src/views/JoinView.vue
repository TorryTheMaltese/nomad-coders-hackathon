<template>
  <div style="margin: 0; height:100%; ">
    <header-nav></header-nav>
    <transition name="fade" appear>
      <join></join>
    </transition>
  </div>
</template>

<script>
import HeaderNav from "../components/Header";
import Join from "../components/Join";

export default {
  components: {
    HeaderNav,
    Join
  }
};
</script>

<style lang="scss" scoped>
div {
  background-color: $light-gray;
}
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s;
}
.fade-enter,
.fade-leave-to {
  opacity: 0;
}
</style>
