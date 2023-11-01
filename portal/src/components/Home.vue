<template>
  <div>
    <h1>Bienvenido a nuestro portal de servicios</h1>

    <!-- Descripción del servicio -->
    <p>
      Aquí encontrarás una amplia gama de servicios ofrecidos por diversas instituciones.
      Puedes explorar y solicitar los servicios que necesitas de manera fácil y rápida.
    </p>

    <!-- Acciones disponibles -->
    <div>
      <h2>Acciones disponibles:</h2>
      <ul>
        <li>Realizar búsqueda de servicios</li>
        <li>Explorar la lista de servicios por institución</li>
        <li>Iniciar una solicitud de servicio</li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Home'
}
</script>

<style scoped>
/* Estilos opcionales para el contenido */
h1 {
  font-size: 2em;
  margin-bottom: 10px;
}

p {
  font-size: 1.2em;
  margin-bottom: 20px;
}

ul {
  list-style-type: disc;
  margin-left: 20px;
  font-size: 1.1em;
}
</style>
