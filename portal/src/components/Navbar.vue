<template>
    <nav>
      <ul>
        <li><router-link to="/">Inicio</router-link></li>
        <li><router-link to="/about">Acerca de</router-link></li>
        <li><div v-if="!loggedIn" class="login-form"><router-link to="/login">Iniciar sesión</router-link></div></li> 
      </ul>
    </nav>
  </template>
  
<script>
  import { useAuthStore } from '@/stores/modules/auth';
  export default {
    name: 'Navbar',


  computed: {
    loggedIn(){
      // Usa la información de inicio de sesión para determinar si el usuario ha iniciado sesión
      const store = useAuthStore();
      return store.isLoggedIn;
    }
  }
  }
  </script>
  
  <style scoped>
nav {
  background-color: #333;
  color: #fff;
  position: fixed;
  width: 100%;
  top: 0;
  left: 0;
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