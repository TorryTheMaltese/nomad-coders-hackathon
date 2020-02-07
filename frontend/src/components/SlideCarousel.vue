<template>
  <carousel
    class="carousel"
    :per-page="1"
    :mouse-drag="true"
    :autoplay="true"
    :loop="true"
    :paginationPadding="5"
  >
    <slide class="slide1">
      <div class="slide-content">slide 1</div>
    </slide>
    <slide class="slide2">
      <div class="slide-content">slide 2</div>
    </slide>
    <slide class="slide3">
      <div class="slide-content">slide 3</div>
    </slide>
  </carousel>
</template>

<script>
import { Carousel, Slide } from "vue-carousel";
export default {
  components: {
    Carousel,
    Slide
  }
};
</script>

<style lang="scss" scoped>
.carousel {
  width: 100%;
}

.slide1 {
  background-color: navy;
  align-items: center;
  display: flex;
  justify-content: center;
}
.slide2 {
  background-color: #ff8202;
  align-items: center;
  display: flex;
  justify-content: center;
}
.slide3 {
  background-color: rebeccapurple;
  align-items: center;
  display: flex;
  justify-content: center;
}

.slide-content {
  width: 100%;
  height: 400px;
  background-color: transparent;
  align-items: center;
  color: #fff;
  display: flex;
  font-size: 1.5rem;
  justify-content: center;
  cursor: pointer;
}
</style>
