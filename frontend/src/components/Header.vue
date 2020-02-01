<template>
  <div class="header">
    <div class="left-menu"></div>
    <div class="center-menu">
      <a href="/" class="button-link">
        <div class="logo">GOODREADS</div>
      </a>
    </div>
    <div class="right-menu"></div>
  </div>
</template>

<style lang="scss" scoped>
.header {
  top: 0;
  position: fixed;
  display: flex;
  align-items: center;
  -webkit-box-pack: justify;
  justify-content: space-between;
}
.header .left-menu {
  flex: 1 0 25%;
  text-align: center;
  display: flex;
}
.header .center-menu {
  position: absolute;
  left: 0;
  right: 0;
  top: 0;
  bottom: 0;
  margin: 0 auto;
  padding: 0 1rem;
  cursor: pointer;
  display: flex;
  -webkit-box-pack: center;
  justify-content: center;
  -webkit-box-align: center;
  align-items: center;
}
.header .right-menu {
  flex: 1 0 25%;
  text-align: right;
  display: flex;
  -webkit-box-align: center;
  align-items: center;
  -webkit-box-pack: end;
  justify-content: flex-end;
}
</style>
