import Vuex from "vuex";
import Vue from "vue";
import axios from "axios";

Vue.use(Vuex);
const resourceHost = "http://localhost:5000";

const enhanceAccessToken = () => {
  const { accessToken } = localStorage;
  if (!accessToken) return;
  axios.defaults.headers.common["Authorization"] = `${accessToken}`;
};

enhanceAccessToken();

export default new Vuex.Store({
  state: {
    accessToken: null
  },
  getters: {},
  mutations: {
    LOGIN(state, { accessToken }) {
      state.accessToken = accessToken;
      localStorage.accessToken = accessToken;
      console.log("state.accessToken :", state.accessToken);
      axios.defaults.headers.common["Authorization"] = `${accessToken}`;
    },
    LOGOUT(state) {
      state.accessToken = null;
      delete localStorage.accessToken;
      console.log("state.accessToken :", state.accessToken);
    }
  },
  actions: {
    LOGIN({ commit }, { email, password }) {
      return axios.post(`${resourceHost}/login`, { email, password }).then(({ data }) => {
        commit("LOGIN", data);
        axios.defaults.headers.common["Authorization"] = `${data.accessToken}`;
      });
    },
    LOGOUT({ commit }) {
      commit("LOGOUT");
    }
  }
});
