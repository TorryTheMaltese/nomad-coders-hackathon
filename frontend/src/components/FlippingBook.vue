<template>
  <div class="book-wrapper">
    <div class="book">
      <div class="back"></div>
      <div class="page6"></div>
      <div class="page5"></div>
      <div class="page4"></div>
      <div class="page3"></div>
      <div class="page2"></div>
      <div class="page1"></div>
      <div class="front"></div>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style lang="scss" scoped>
.book-wrapper {
  width: fit-content;
  display: flex;
}
.book {
  transform-style: preserve-3d;
  position: relative;
  height: 200px;
  cursor: pointer;
  backface-visibility: visible;
  margin: 10px;
}

.front,
.back,
.page1,
.page2,
.page3,
.page4,
.page5,
.page6 {
  transform-style: preserve-3d;
  position: absolute;
  width: 150px;
  height: 100%;
  top: 0;
  left: 0;
  transform-origin: left center;
  transition: transform 0.5s ease-in-out, box-shadow 0.35s ease-in-out;
}

.front,
.back {
  background: $dark-gray;
  background-size: cover;
}

.front,
.page1,
.page3,
.page5 {
  border-bottom-right-radius: 0.5em;
  border-top-right-radius: 0.5em;
}

.back,
.page2,
.page4,
.page6 {
  border-bottom-right-radius: 0.5em;
  border-top-right-radius: 0.5em;
}

.page1 {
  background: #efefef;
}

.page2 {
  background: #efefef;
}

.page3 {
  background: #f5f5f5;
}

.page4 {
  background: #f5f5f5;
}

.page5 {
  background: #fafafa;
}

.page6 {
  background: #fdfdfd;
}

.book:hover .front {
  transform: rotateY(-160deg) scale(1.1);
  box-shadow: 0 1em 3em 0 rgba(0, 0, 0, 0.2);
}

.book:hover .page1 {
  transform: rotateY(-150deg) scale(1.1);
  box-shadow: 0 1em 3em 0 rgba(0, 0, 0, 0.2);
}

.book:hover .page2 {
  transform: rotateY(-30deg) scale(1.1);
  box-shadow: 0 1em 3em 0 rgba(0, 0, 0, 0.2);
}

.book:hover .page3 {
  transform: rotateY(-140deg) scale(1.1);
  box-shadow: 0 1em 3em 0 rgba(0, 0, 0, 0.2);
}

.book:hover .page4 {
  transform: rotateY(-40deg) scale(1.1);
  box-shadow: 0 1em 3em 0 rgba(0, 0, 0, 0.2);
}

.book:hover .page5 {
  transform: rotateY(-130deg) scale(1.1);
  box-shadow: 0 1em 3em 0 rgba(0, 0, 0, 0.2);
}

.book:hover .page6 {
  transform: rotateY(-50deg) scale(1.1);
  box-shadow: 0 1em 3em 0 rgba(0, 0, 0, 0.2);
}

.book:hover .back {
  transform: rotateY(-20deg) scale(1.1);
}
</style>
