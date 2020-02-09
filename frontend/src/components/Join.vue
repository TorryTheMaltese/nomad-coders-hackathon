<template>
  <div class="container">
    <div class="join-form-wrapper">
      <form @submit.prevent="onSubmitForm" class="join-form">
        <span class="form-title">Join us!</span>
        <div class="form-input-title-wrapper">
          <span class="form-input-title">이메일</span>
          <span class="form-danger">에러메세지</span>
        </div>
        <div class="form-input-wrapper">
          <input
            type="email"
            name="email"
            v-model="formData.email"
            class="form-input"
            maxlength="30"
            placeholder="이메일을 입력해주세요"
          />
          <span class="form-input-focus"></span>
        </div>

        <div class="form-input-title-wrapper">
          <span class="form-input-title">닉네임</span>
          <span class="form-danger">에러메세지</span>
        </div>
        <div class="form-input-wrapper">
          <input
            type="text"
            name="username"
            v-model="formData.username"
            class="form-input"
            maxlength="20"
            placeholder="닉네임을 입력해주세요"
          />
          <span class="form-input-focus"></span>
        </div>

        <div class="form-input-title-wrapper">
          <span class="form-input-title">패스워드</span>
          <span class="form-danger">에러메세지</span>
        </div>
        <div class="form-input-wrapper">
          <input
            type="password"
            name="password"
            v-model="formData.password"
            class="form-input"
            placeholder="패스워드를 입력해주세요"
          />
          <span class="form-input-focus"></span>
        </div>

        <div class="form-input-title-wrapper">
          <span class="form-input-title">패스워드 확인</span>
          <span class="form-danger">에러메세지</span>
        </div>
        <div class="form-input-wrapper">
          <input
            type="password"
            name="password-check"
            v-model="formData.passwordCheck"
            class="form-input"
            placeholder="패스워드를 한 번 더 입력해주세요"
          />
          <span class="form-input-focus"></span>
        </div>

        <div class="form-btn-wrapper">
          <button type="submit" class="form-btn">가입하기</button>
        </div>

        <router-link to="/login" tag="div" class="form-btn-wrapper">
          <button class="form-switch">이미 회원이신가요?</button>
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
      formData: {
        email: "",
        username: "",
        password: ""
      }
    };
  },
  methods: {
    checkPassword() {},
    checkUsername() {},
    onSubmitForm(e) {
      e.preventDefault();
      this.checkPassword();
      this.checkUsername();

      const path = "http://localhost:5000/join";
      const payload = {
        email: this.formData.email,
        username: this.formData.username,
        password: this.formData.password
      };

      axios
        .post(path, payload)
        .then(res => {})
        .catch(error => {
          console.error(error);
        });
    }
  }
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

.join-form-wrapper {
  width: 400px;
  padding: 50px;
  border: 1px solid $light-gray;
  border-radius: 30px;
  background-color: $white;
}

.join-form {
  width: 100%;
  display: flex;
  flex-direction: column;
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

.form-danger {
  font-family: "Noto Serif KR", serif;
  font-size: 12px;
  color: red;
}
</style>
