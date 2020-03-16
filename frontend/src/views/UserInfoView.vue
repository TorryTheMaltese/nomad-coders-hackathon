<template>
  <div style="margin: 0;">
    <header-nav></header-nav>
    <upload-component></upload-component>
    <!-- <user-info></user-info> -->
  </div>
</template>

<script>
import axios from "axios";
import HeaderNav from "../components/Header";
import UserInfo from "../components/UserInfo";
import UploadComponent from "../components/UploadComponent";

export default {
  components: {
    HeaderNav,
    UserInfo,
    UploadComponent
  },
  created() {}
};
</script>

<style lang="scss" scoped></style>
