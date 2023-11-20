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

        <li v-if="tienePermisosDeEstadistica" class="nav-item">
          <router-link to="/estadisticas" class="nav-link">Estadísticas</router-link>
        </li>

        <li v-if="!loggedIn" class="nav-item">
          <router-link to="/login" class="nav-link">Iniciar sesión</router-link>
        </li>

        <li v-if="loggedIn" class="nav-item">
          <router-link to="/logout" class="nav-link">Cerrar sesión</router-link>
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
    },

    tienePermisosDeEstadistica() {
      const userPermissions = this.store.getUserPermissions;
      if (userPermissions) {
        return userPermissions.includes('statistics_index');
      } else {
        return false;
      }
    }
  },


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