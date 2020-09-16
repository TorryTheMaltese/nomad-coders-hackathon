<template>
  <div class="container">
    <div class="login-form-wrapper">
      <form class="login-form" @submit.prevent="onSubmitForm(email, password)">
        <span class="form-title">Welcome</span>

        <span class="form-input-title">이메일</span>
        <div class="form-input-wrapper">
          <input
            type="email"
            name="email"
            v-model="email"
            @keydown.enter.prevent="nextInput()"
            class="form-input"
            maxlength="30"
            placeholder="이메일을 입력해주세요"
          />
          <span class="form-input-focus"></span>
        </div>

        <span class="form-input-title">패스워드</span>
        <div class="form-input-wrapper">
          <input
            type="password"
            name="password"
            v-model="password"
            class="form-input"
            placeholder="패스워드를 입력해주세요"
          />
          <span class="form-input-focus"></span>
        </div>

        <div class="form-btn-wrapper">
          <button class="form-btn">LOGIN</button>
        </div>

        <router-link to="/join" tag="div" class="form-btn-wrapper">
          <button class="form-switch">가입하기</button>
        </router-link>
      </form>
    </div>
  </div>
</template>

<script>
import router from "../routes/routes";
import axios from "axios";

export default {
  router,
  data() {
    return {
      email: "",
      password: "",
      msg: "",
    };
  },
  methods: {
    nextInput() {
      event.target.parentElement.nextElementSibling.nextElementSibling.children[0].focus();
    },
    formCheck() {
      console.log("form check");
    },
    onSubmitForm(email, password) {
      this.formCheck();

      this.$store
        .dispatch("LOGIN", { email, password })
        .then(() => this.redirect())
        .catch(({ message }) => (this.msg = message));
    },
    redirect() {
      console.log("Login Success");
      router.push({ name: "main" });
    },
  },
};
</script>

<style lang="scss" scoped>
.container {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
  padding: 15px;
  font-family: "Noto Serif KR", serif;
}

.login-form-wrapper {
  width: 400px;
  padding: 50px;
  border: 1px solid $light-gray;
  border-radius: 30px;
  background-color: $white;
}

.login-form {
  width: 100%;
}

.form-title {
  display: block;
  color: $black;
  text-align: center;
  font-size: 2em;
  margin-bottom: 40px;
  font-weight: bold;
}

.form-input-wrapper {
  position: relative;
  width: 100%;
  border-bottom: 2px solid $gray;
  margin-bottom: 35px;
}

.form-input-wrapper .form-input-title {
  position: relative;
}

.form-input-wrapper .form-input {
  font-size: 18px;
  color: $black;
  line-height: 1.2;
  display: block;
  width: 100%;
  height: 52px;
  padding: 0 5px;
  outline: none;
  border: none;
  margin: 0;
}

.form-input::placeholder {
  color: $gray;
  font-size: 16px;
  line-height: 1.2;
  display: block;
  outline: none;
  border: none;
  margin: 0;
}

.form-input-wrapper .form-input-focus::before {
  content: "";
  display: block;
  position: absolute;
  bottom: -2px;
  left: 0;
  width: 0;
  height: 2px;
  transition: all 0.4s;
  background: $black;
}

.form-input-wrapper .form-input-focus::after {
  line-height: 1.2;
  display: block;
  width: 100%;
  position: absolute;
  top: 15px;
  left: 0;
  padding-left: 5px;
  transition: all 0.4s;
}

.form-input:focus + .form-input-focus::before {
  width: 100%;
}

.form-btn-wrapper {
  width: 100%;
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  margin-bottom: 20px;
}

.form-btn-wrapper .form-btn {
  font-family: "Noto Serif KR", serif;
  font-size: 14px;
  color: $black;
  line-height: 1.2;
  text-transform: uppercase;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 0 20px;
  width: 100%;
  height: 50px;
  background-color: $gray;
  outline: none;
  border-radius: 8px;

  box-shadow: 0 10px 30px 0px rgba(0, 0, 0, 0.1);
  transition: all 0.4s;
}

.form-btn:hover {
  background-color: $black;
  color: $white;
  box-shadow: 0 10px 30px 0px rgba(0, 0, 0, 0.5);
}

button {
  border: none;
  cursor: pointer;
}

.form-btn-wrapper .form-switch {
  font-family: "Noto Serif KR", serif;
  font-size: 14px;
  color: $black;
  line-height: 1.2;
  text-transform: uppercase;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 0 20px;
  width: 100%;
  height: 50px;
  background: transparent;
  outline: none;
}
</style>
