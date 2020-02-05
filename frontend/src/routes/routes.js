import Vue from "vue";
import Router from "vue-router";
import MainView from "../views/MainView.vue";
import PreView from "../views/PreView";
import LoginView from "../views/LoginView";
import JoinView from "../views/JoinView";
import SearchView from "../views/SearchView";

Vue.use(Router);

export default new Router({
  // mode: "history",
  base: process.env.BASE_URL,
  routes: [
    {
      path: "/welcome",
      component: PreView
    },
    {
      path: "/",
      component: MainView
    },
    {
      path: "/login",
      component: LoginView
    },
    {
      path: "/join",
      component: JoinView
    },
    {
      path: "/search",
      component: SearchView
    }
  ]
});
