<template>
  <div class="container">
    <div class="wrapper">
      <div class="btn-wrapper">
        <button data-hover="See Ya !" class="logout-btn" @click="onLogoutBtn">
          <div>LOGOUT</div>
        </button>
      </div>

      <div class="profile-wrapper">
        <upload-component></upload-component>
        <!-- <img class="avatar" /> -->
        <!-- <p class="avatar-text">프로필 이미지 변경하기</p> -->
        <p class="profile-name">{{username}}</p>
      </div>
    </div>
  </div>
</template>
l
<script>
import router from "../routes/routes.js";
import axios from "axios";
import UploadComponent from "./UploadComponent";

export default {
  router,
  components: {
    UploadComponent
  },
  data() {
    return {
      username: ""
    };
  },
  methods: {
    onLogoutBtn() {
      this.$store
        .dispatch("LOGOUT")
        .then(() => this.redirect())
        .catch(({ message }) => (this.msg = message));
    },
    redirect() {
      console.log("Logout");
      router.push({ name: "main" });
    }
  },
  created() {
    axios
      .get("http://localhost:5000/profile")
      .then(({ data }) => (this.username = data.username));
  }
};
</script>

<style lang="scss" scoped>
.container {
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}

.wrapper {
  width: 1080px;
  height: 100%;
  display: flex;
  flex-direction: column;
}

/*[logout btn]********************************************************************************************************************************/

.btn-wrapper {
  display: flex;
  width: 100%;
  height: fit-content;
  flex-direction: row-reverse;
}

.logout-btn {
  // background: transparent;
  background: $black;
  padding: 10px 40px;
  position: relative;
  overflow: hidden;
  margin: 10px;
  border: 2px solid $black;
  outline: none;
  color: $white;
  letter-spacing: 3px;
  font-family: "Noto Serif KR", serif;
  cursor: pointer;
}

.logout-btn:hover::before {
  opacity: 1;
  transform: translate(0, 0);
}

.logout-btn::before {
  content: attr(data-hover);
  position: absolute;
  left: 0;
  width: 100%;
  letter-spacing: 3px;
  font-weight: 800;
  font-size: 0.8em;
  opacity: 0;
  transform: translate(-100%, 0);
  transition: all 0.2s ease-in-out;
}

button:hover div {
  opacity: 0;
  transform: translate(100%, 0);
}
button div {
  text-transform: uppercase;
  letter-spacing: 3px;
  font-weight: 800;
  font-size: 0.8em;
  transition: all 0.3s ease-in-out;
}

/*[user profile]********************************************************************************************************************************/

.profile-wrapper {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.avatar {
  width: 160px;
  height: 160px;
  border-radius: 50%;
  transform: scale(0.95);
  transition: all 0.5s;
  cursor: pointer;
  background-image: url(../images/profile.png);
  background-repeat: no-repeat;
  background-size: cover;
}
.avatar:hover {
  transform: scale(1);
  box-shadow: 0 37.125px 70px -12.125px rgba(0, 0, 0, 0.2);
  opacity: 0.5;
}

.avatar-text {
  visibility: hidden;
  font-family: "Noto Serif KR", serif;
  font-size: 30px;
}

.profile-name {
  font-family: "Noto Serif KR", serif;
  font-size: 30px;
  margin: 15px;
}
</style>
