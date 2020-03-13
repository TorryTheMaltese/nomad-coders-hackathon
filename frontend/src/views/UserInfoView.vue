<template>
  <div>
    <header-nav></header-nav>
    <user-info></user-info>
  </div>
</template>

<script>
import axios from "axios";
import HeaderNav from "../components/Header";
import UserInfo from "../components/UserInfo";

export default {
  components: {
    HeaderNav,
    UserInfo
  },
  created() {}
};
</script>

<style lang="scss" scoped></style>
