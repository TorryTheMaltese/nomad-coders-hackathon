<template>
  <div class="container">
    <div class="join-form-wrapper">
      <form @submit.prevent="onSubmitForm" class="join-form">
        <span class="form-title">Join us!</span>
        <div class="form-input-title-wrapper">
          <span class="form-input-title">이메일</span>
          <span class="form-danger" v-if="errors.email">{{ errors.email }}</span>
        </div>
        <div class="form-input-wrapper">
          <input
            type="email"
            name="email"
            v-model="formData.email"
            @keydown.enter.prevent="nextInput()"
            class="form-input"
            maxlength="30"
            placeholder="이메일을 입력해주세요"
          />
          <span class="form-input-focus"></span>
        </div>

        <div class="form-input-title-wrapper">
          <span class="form-input-title">닉네임</span>
          <span class="form-danger" v-if="errors.username">{{ errors.username }}</span>
        </div>
        <div class="form-input-wrapper">
          <input
            type="text"
            name="username"
            @keydown.enter.prevent="nextInput()"
            @keyup="limitNameInput()"
            v-model="formData.username"
            class="form-input"
            maxlength="15"
            placeholder="닉네임을 입력해주세요"
          />
          <span class="form-input-focus"></span>
        </div>

        <div class="form-input-title-wrapper">
          <span class="form-input-title">패스워드</span>
          <span class="form-danger" v-if="errors.password">{{ errors.password }}</span>
        </div>
        <div class="form-input-wrapper">
          <input
            type="password"
            name="password"
            @keydown.enter.prevent="nextInput()"
            @keyup="limitPassword()"
            v-model="formData.password"
            class="form-input"
            placeholder="패스워드를 입력해주세요"
          />
          <span class="form-input-focus"></span>
        </div>

        <div class="form-input-title-wrapper">
          <span class="form-input-title">패스워드 확인</span>
          <span class="form-danger" v-if="errors.passwordCheck">{{ errors.passwordCheck }}</span>
        </div>
        <div class="form-input-wrapper">
          <input
            type="password"
            name="password-check"
            v-model="formData.passwordCheck"
            @blur="checkPasswordCheck()"
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
        password: "",
        passwordCheck: ""
      },
      errors: {
        email: "",
        username: "",
        password: "",
        passwordCheck: ""
      },
      len: 0
    };
  },
  methods: {
    nextInput() {
      event.target.parentElement.nextElementSibling.nextElementSibling.children[0].focus();
    },
    limitNameInput() {
      const pattern_username = /^[a-zA-Z가-힣0-9]{2,15}$/;
      try {
        if (!pattern_username.test(event.target.value))
          throw "한글, 영어, 숫자로 이루어진 2~15글자로 입력해주세요";
        else this.errors.username = "";
      } catch (error) {
        this.errors.username = error;
      }
    },
    limitPassword() {
      const pattern_password = /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d$@$!%*?&]{8,}$/;

      try {
        if (!pattern_password.test(event.target.value))
          throw "영어, 숫자를 혼용해 8자 이상으로 입력해주세요 (!@$%*& 사용가능)";
        else this.errors.password = "";
      } catch (error) {
        this.errors.password = error;
      }
    },
    checkPassword() {
      const pattern_password = /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d$@$!%*?&]{8,}$/;

      try {
        if (!pattern_password.test(this.formData.password))
          throw "영어, 숫자를 혼용해 8자 이상으로 입력해주세요 (!@$%*& 사용가능)";
        else this.errors.password = "";
      } catch (error) {
        this.errors.password = error;
      }
    },
    checkPasswordCheck() {
      try {
        if (this.formData.password !== this.formData.passwordCheck) {
          throw "패스워드를 확인해주세요";
        } else {
          this.errors.passwordCheck = "";
        }
      } catch (error) {
        this.errors.passwordCheck = error;
      }
    },
    checkUsername() {},
    checkRequired() {
      for (const item in this.formData) {
        try {
          if (!this.formData[item]) {
            throw "빈칸을 채워주세요";
          }
        } catch (error) {
          this.errors[item] = error;
        }
      }
    },
    validate() {
      this.errors.email = "";
      this.errors.username = "";
      this.errors.password = "";
      this.errors.passwordCheck = "";

      this.checkRequired();
      this.checkUsername();
      this.checkPassword();
      this.checkPasswordCheck();
    },
    onSubmitForm(e) {
      e.preventDefault();

      this.validate();
      if (
        !this.errors.email &&
        !this.errors.username &&
        !this.errors.password &&
        !this.errors.passwordCheck
      ) {
        const path = "http://localhost:5000/join";
        const payload = {
          email: this.formData.email,
          username: this.formData.username,
          password: this.formData.password
        };
        axios
          .post(path, payload)
          .then(res => {
            if (res.data.error) {
              this.errors.email = res.data.error;
            } else {
              router.push({ name: "login" });
            }
          })
          .catch(error => {
            console.error(error);
          });
      }
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
