<template>
  <div style="margin: 0px;height:100%;">
    <header-nav></header-nav>
    <transition name="fade" appear>
      <book-info></book-info>
    </transition>
  </div>
</template>

<script>
import HeaderNav from "../components/Header";
import BookInfo from "../components/BookInfo";

// 책정보(책표지,저자,출판사,출판년도 기타 등등)
// 후기 (별점평균, 후기 글)
// 후기 남기기
// 비슷한 책

export default {
  components: {
    HeaderNav,
    BookInfo
  }
};
</script>

<style lang="scss" scoped>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s;
}
.fade-enter,
.fade-leave-to {
  opacity: 0.3;
}
</style>