<template>
  <br>
  <br>
  <h1 style="text-align:center">{{ servicio.nombre }}</h1>
  <br>
  <h2> Detalles </h2>
  <div class="detalles">
    <ul> 
      <li> Descripcion: {{ servicio.descripcion }} </li>
      <li> Tipo: {{ servicio.tipo_servicio }} </li>
      <li v-if="servicio.habilitado"> Habilitado: Si </li>
      <li v-else> Habilitado: No </li>
    </ul>
    <br>
  </div>
  <br>
  <button @click="realizarAccion">Solicitar</button>
  <br>
  <h1 style="text-align:center">{{ institucion.nombre }}</h1>
  <div class="detalles">
    <ul> 
      <li> Informacion: {{ institucion.informacion }} </li>
      <li> Calle: {{ institucion.calle }} </li>
      <li> Numero: {{ institucion.numero }} </li>
      <li> Localización: {{ institucion.localizacion }} </li>
      <li> Horarios: {{ institucion.horarios }} </li>
      <li> Contacto: {{ institucion.contacto }} - va en mapa </li>
      <li v-if="institucion.habilitado"> - Habilitado: Si </li>
      <li v-else> Habilitado: No </li>
      <li>  Web: {{ institucion.web }} - va en mapa </li>
    </ul>
  </div>
  <br>
  <br>
  <div id="mapa" style="height: 400px;"></div>
</template>

<script>
import detalleServicio from './javascript/detalleServicio.js';

export default detalleServicio;
</script>

<style>
@import './css/detalleServicio.css';

</style>
