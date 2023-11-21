import './assets/main.css'
import 'bootstrap/dist/css/bootstrap.css';

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'

import { library } from '@fortawesome/fontawesome-svg-core';
import { fas } from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';

library.add(fas);
import { useAuthStore } from '@/stores/modules/auth';
const app = createApp(App)
const pinia = createPinia()
pinia.use(piniaPluginPersistedstate)
app.use(pinia)
app.use(router)
const store = useAuthStore();
router.beforeEach((to, from, next) => {
    if (to.matched.some((record) => record.meta.requiresAuth)) {
      if (store.getIsLoggedIn) {
        next();
      } else {
        alert("Debe iniciar sesión para acceder a esta página");
        next({ name:'loginView'});
      }
    } else {
      next();
    }
  });
app.component('font-awesome-icon', FontAwesomeIcon)
app.mount('#app')
