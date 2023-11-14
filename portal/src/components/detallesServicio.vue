<template>
  <div class="container my-5">
    <h1 class="display-4 text-center">{{ servicio.nombre }}</h1>

    <div class="detalles mt-4">
      <h2>Detalles</h2>
      <ul class="list-group">
        <li class="list-group-item">Descripción: {{ servicio.descripcion }}</li>
        <li class="list-group-item">Tipo: {{ servicio.tipo_servicio }}</li>
        <li class="list-group-item" v-if="servicio.habilitado">Habilitado: Si</li>
        <li class="list-group-item" v-else>Habilitado: No</li>
      </ul>
    </div>

    <br>

    <router-link :to="{ name: 'solicitud', params: { id: servicio.id, institucion_id: `${institucion.id}` } }">
      <button class="btn btn-primary mt-3">Solicitar</button>
    </router-link>

    <br>

    <h1 class="display-4 text-center mt-4">{{ institucion.nombre }}</h1>

    <div class="detalles mt-4">
      <ul class="list-group">
        <li class="list-group-item">Información: {{ institucion.informacion }}</li>
        <li class="list-group-item">Calle: {{ institucion.calle }}</li>
        <li class="list-group-item">Número: {{ institucion.numero }}</li>
        <li class="list-group-item">Localización: {{ institucion.localizacion }}</li>
        <li class="list-group-item">Horarios: {{ institucion.horarios }}</li>
        <li class="list-group-item" v-if="institucion.habilitado">Habilitado: Si</li>
        <li class="list-group-item" v-else>Habilitado: No</li>
      </ul>
    </div>

    <br>
    <br>

    <div id="mapa" class="mt-4" style="height: 400px;"></div>
  </div>
</template>

<script>
import detalleServicio from './javascript/detalleServicio.js';

export default detalleServicio;
</script>

<style>
@import './css/detalleServicio.css';

</style>
