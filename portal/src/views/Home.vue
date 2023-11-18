<template>
  <section>
    <div class="container my-5">
      <h1 class="display-4 text-center">Bienvenido a CIDEPINT - Sitio público</h1>
      <div class="image-container">
        <img src="cidepint1.jpg">
        <img src="cidepint2.jpg">
        <img src="cidepint3.jpg">
        <img src="cidepint4.jpg">
      </div>
      <p class="lead text-center">
        Aquí encontrarás una amplia gama de servicios ofrecidos por diversas instituciones.
        Puedes explorar y solicitar los servicios que necesitas de manera fácil y rápida.
      </p>

      <ul class="list-group">
        <li class="list-group-item">
            <div>
                <h2 class="h4">Búsqueda de Servicios</h2>
                <p>Realiza búsquedas eficientes para encontrar los servicios que necesitas.</p>
            </div>
        </li>
        <li class="list-group-item">
            <div>
                <h2 class="h4">Informacion de los Servicios</h2>
                <p>Observa la información del servicio e institución que estés buscando.</p>
            </div>       
        </li>
        <li class="list-group-item">
            <div>
                <h2 class="h4">Solicitud de Servicio</h2>
                <p>Inicia fácilmente una solicitud de servicio.</p>
            </div>
        </li>
      </ul>
      <br>
      <div style="text-align: center;">
        <img src="/public/logo.jpg" style="max-width: 1000px; display: inline-block;">
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'Home'
}
</script>

<style scoped>
    .image-container {
      display: grid;
      grid-template-columns: repeat(2, 1fr); /* Dos columnas */
      gap: 10px; /* Espacio entre imágenes */
      max-width: 600px; /* Ancho máximo del contenedor */
      margin: 0 auto; /* Centrar el contenedor */
    }

    .image-container img {
      width: 100%; /* Ocupar el 100% del ancho del contenedor */
      height: auto; /* Mantener la proporción original */
      max-width: 100%; /* Evitar que las imágenes se amplíen más allá de su tamaño original */
      display: block; /* Eliminar el espacio adicional debajo de las imágenes */
    }
</style>