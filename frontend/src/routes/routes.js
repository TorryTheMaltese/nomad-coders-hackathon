import Vue from "vue";
import Router from "vue-router";
import axios from "axios";
import MainView from "../views/MainView.vue";
import PreView from "../views/PreView";
import LoginView from "../views/LoginView";
import JoinView from "../views/JoinView";
import BookDetailView from "../views/BookDetailView";
import UserInfoView from "../views/UserInfoView";

Vue.use(Router);

const path = "http://localhost:5000/profile";

const requireAuth = () => (from, to, next) => {
  axios
    .get(path)
    .then(res => {
      // res.data: {exp: 000, userId: 0, username: "0000"}
      // or
      // res.data: {error: ""}
      console.log("res.data.error :", res.data.error);
      if (res.data.error) {
        return next({ path: "/" });
      } else {
        return next();
      }
    })
    .catch(error => {
      console.error(error);
      alert("로그인 해주세요");
      next({ path: "/" });
    });
};

export default new Router({
  mode: "history",
  base: process.env.BASE_URL,
  routes: [
    {
      path: "/welcome",
      name: "welcome",
      component: PreView
    },
    {
      path: "/",
      name: "main",
      component: MainView
    },
    {
      path: "/login",
      name: "login",
      component: LoginView
    },
    {
      path: "/join",
      name: "join",
      component: JoinView
    },
    {
      path: "/detail",
      name: "detail",
      component: BookDetailView
    },
    {
      path: "/profile",
      name: "profile",
      component: UserInfoView,
      beforeEnter: requireAuth()
    }
  ]
});
