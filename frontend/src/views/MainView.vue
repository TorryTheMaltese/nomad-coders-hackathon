<template>
  <div style="margin: 0;">
    <header-nav></header-nav>
    <slide-carousel></slide-carousel>
    <card-carousel></card-carousel>
  </div>
</template>

<script>
import HeaderNav from "../components/Header";
import CardCarousel from "../components/CardCarousel";
import SlideCarousel from "../components/SlideCarousel";

export default {
  components: {
    HeaderNav,
    SlideCarousel,
    CardCarousel
  }
};
</script>

<style lang="scss" scoped>
div {
  user-select: none;
}
</style>
