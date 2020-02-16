import Vue from "vue";
import Router from "vue-router";
import MainView from "../views/MainView.vue";
import PreView from "../views/PreView";
import LoginView from "../views/LoginView";
import JoinView from "../views/JoinView";
import BookDetailView from "../views/BookDetailView";
import UserInfoView from "../views/UserInfoView";

Vue.use(Router);

const requireAuth = () => (from, to, next) => {
  let isAuthenticated = false;

  if (localStorage.getItem("accessToken")) {
    isAuthenticated = true;
  }
  if (isAuthenticated) return next();
  next("/");
};

export default new Router({
  // mode: "history",
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
      path: "/user",
      name: "user",
      component: UserInfoView,
      beforeEnter: requireAuth()
    }
  ]
});
