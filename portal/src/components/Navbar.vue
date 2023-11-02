<template>
    <nav>
      <ul>
        <li><router-link to="/">Inicio</router-link></li>
        <li><router-link to="/about">Acerca de</router-link></li>
        <li><router-link to="/login">Iniciar sesión</router-link></li>
      </ul>
    </nav>
  </template>
  
  <script>
  export default {
    name: 'Navbar'
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