<template>
  <carousel
    class="carousel"
    :per-page="1"
    :mouse-drag="true"
    :autoplay="true"
    :loop="true"
    :paginationPadding="5"
  >
    <slide class="slide">
      <div class="test">slide 1</div>
    </slide>
    <slide class="slide">
      <div class="test">slide 2</div>
    </slide>
    <slide class="slide">
      <div class="test">slide 3</div>
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

.test {
  width: 100%;
  height: 400px;
  background-color: $gray;
  align-items: center;
  color: #999;
  display: flex;
  font-size: 1.5rem;
  justify-content: center;
}
</style>
