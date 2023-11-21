<template>
  <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <a class="navbar-brand" href="#">CIDEPINT</a>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav mr-auto">
        <li class="nav-item">
          <router-link to="/" class="nav-link">Inicio</router-link>
        </li>
        <li class="nav-item">
          <router-link to="/servicios" class="nav-link">Servicios</router-link>
        </li>
        <li class="nav-item">
          <router-link to="/contacto" class="nav-link">Contacto</router-link>
        </li>
        <li class="nav-item">
          <router-link to="/solicitudes" class="nav-link">Mis Solicitudes</router-link>
        </li>
        <li v-if="!loggedIn" class="nav-item">
          <router-link to="/login" class="nav-link">Iniciar sesión</router-link>
        </li>
        <li v-if="loggedIn" class="nav-item">
          <a href="#" class="nav-link" @click.prevent="logout">Cerrar sesión</a>
        </li>
      </ul>
    </div>
  </nav>
</template>
  
<script>
  import { useAuthStore } from '@/stores/modules/auth';
  import logout from '../components/logout.vue'



  export default {
    name: 'Navbar',

    components: {
      logout
  },
  created() {
    // Al crear el componente, almacena el store en una variable local
    this.store = useAuthStore();
  },
  
  computed: {
    loggedIn(){
      return this.store.getIsLoggedIn;
    }
  },
  methods: {
  async logout() {
      try {
        await this.store.logout();
        this.$router.push({ name: 'Home' });
      } catch (error) {
        this.$router.push({ name: 'loginView' });
        console.error(error);
      }
    }
  }
  }
  </script>
  
  <style scoped>
  nav {
    background-color: #333;
    color: #fff;
    width: 100%;
    position: fixed; 
    top: 0;
    left: 0;
    z-index: 1000; 
  } 
  ul {
    list-style-type: none;
    padding: 0;
  }
  li {
    display: inline-block;
    margin: 0 10px;
  }
  a {
    text-decoration: none;
    color: #fff;
  }
</style>