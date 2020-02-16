import Vuex from "vuex";
import Vue from "vue";
import axios from "axios";

Vue.use(Vuex);
const resourceHost = "http://localhost:5000";

export default new Vuex.Store({
  state: {
    accessToken: null
  },
  getters: {},
  mutations: {
    LOGIN(state, { accessToken }) {
      state.accessToken = accessToken;
      localStorage.setItem("accessToken", state.accessToken);
      console.log("state.accessToken :", state.accessToken);
    },
    LOGOUT(state) {
      state.accessToken = null;
      delete localStorage.accessToken;
      console.log("state.accessToken :", state.accessToken);
    }
  },
  actions: {
    LOGIN({ commit }, { email, password }) {
      return axios
        .post(`${resourceHost}/login`, { email, password })
        .then(({ data }) => commit("LOGIN", data));
    },
    LOGOUT({ commit }) {
      commit("LOGOUT");
    }
  }
});
