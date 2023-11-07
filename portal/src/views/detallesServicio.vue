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
      <li> Direccion: {{ institucion.direccion }} </li>
      <li> Localización: {{ institucion.localizacion }} </li>
      <li> Horarios: {{ institucion.horarios }} </li>
      <li> Contacto: {{ institucion.contacto }} </li>
      <li v-if="institucion.habilitado"> Habilitado: Si </li>
      <li v-else> Habilitado: No </li>
      <li>  Web: {{ institucion.web }} </li>
    </ul>
  </div>
  <br>
  <br>
  <div id="mapa" style="height: 400px;"></div>
</template>

<script>
import { apiService } from '@/api';

export default {
  props: ['id'],
  data() {
    return {
      servicio: {},
      institucion: {},
    };
  },
  mounted() {
    this.obtenerServicio();
    const map = L.map('mapa').setView([51.505, -0.09], 13); // Coordenadas iniciales y zoom

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

  },
  methods: {
    async obtenerServicio() {
      try {
        const respuesta = await apiService.get(`/api/services/${this.id}`);
        this.servicio = respuesta.data;

        // Llama a la función para obtener la institución
        await this.obtenerInstitucion(this.servicio.institucion_id);
      } catch (error) {
        console.error('Error al obtener la información del servicio', error);
      }
    },
    async obtenerInstitucion(institucionId) {
      try {
        const respuesta = await apiService.get(`/api/instituciones/${institucionId}`);
        this.institucion = respuesta.data;
      } catch (error) {
        console.error('Error al obtener la información de la institución', error);
      }
    },
  },

};
</script>

<style>
.detalles {
max-width: 600px;
margin: 0 auto;
padding: 50px;
background-color: #ebdada;
border-radius: 10px;
box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.detalles h2 {
font-size: 1.5em;
margin-bottom: 10px;
}

.detalles li {
font-size: 1.2em;
line-height: 1.6;
}

button {
  font-size: 1em;
  padding: 10px 20px;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}
</style>
