// auth.js
import { defineStore } from 'pinia';

export const useAuthStore = defineStore({
  id: 'auth',
  state: () => ({
    user: null,
    isLoggedIn: false, // Asegúrate de que esta propiedad esté declarada aquí
  }),
  getters: {
    getUser: (state) => state.user,
    getIsLoggedIn: (state) => state.isLoggedIn,
  },
  actions: {
    setUser(user) {
      this.user = user;
      this.isLoggedIn = true;
    },
    logoutUser() {
      this.user = null;
      this.isLoggedIn = false;
    },
  },
});
