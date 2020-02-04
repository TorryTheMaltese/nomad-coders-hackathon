<template>
  <div style="margin: 0;">
    <header-nav></header-nav>
    <slide-carousel></slide-carousel>
    <card-carousel></card-carousel>
    <book-card></book-card>
  </div>
</template>

<script>
import HeaderNav from "../components/Header";
import CardCarousel from "../components/CardCarousel";
import SlideCarousel from "../components/SlideCarousel";
import BookCard from "../components/BookCard";

export default {
  components: {
    HeaderNav,
    SlideCarousel,
    CardCarousel,
    BookCard
  }
};
</script>

<style lang="scss" scoped>
</style>
