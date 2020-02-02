<template>
  <div>
    <header-nav></header-nav>
    <div class="head"></div>
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
  margin: 0;
}

.head {
  width: 100%;
  height: 60px;
  position: relative;
}
</style>
