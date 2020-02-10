<template>
  <div @click="go('/')" class="quote-wrapper">
    <h1 class="book-quote">
      "So Many Books,
      <br />
      <span style="padding-left:100px">So Little Time."</span>
    </h1>
    <span class="quote-by">― Frank Zappa</span>
  </div>
</template>

<script>
export default {
  data() {
    return {};
  },
  methods: {
    go: function(url) {
      location.href = "/";
    }
  },
  created() {
    window.setTimeout(this.go, 2000);
  }
};
</script>

<style lang="scss" scoped>
body {
  height: 100%;
}
.quote-wrapper {
  overflow: hidden;
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-flow: column;
  width: 100%;
  height: 100%;
}

.book-quote {
  padding: 0.3em 1em 0.25em;
  font-weight: 400;
  font-size: 40px;
  color: $black;
  font-family: "Bellefair", serif;
  position: relative;
  line-height: 1.3;
  text-shadow: 0 0 3px #000;
  animation-name: appear;
  animation-duration: 3s;
}

.quote-by {
  color: $black;
  opacity: 0.6;
  font-family: "Bellefair", serif;
  text-shadow: 0 0 1px #000;
  animation-name: appear-2;
  animation-duration: 4.5s;
}

@keyframes appear {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

@keyframes appear-2 {
  from {
    opacity: 0;
  }
  to {
    opacity: 0.6;
  }
}
</style>
