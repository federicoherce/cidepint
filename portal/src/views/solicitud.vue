<template>
    <div class="container">
      <h2 class="mt-4">Detalle solicitud</h2>
      <form @submit.prevent="enviarSolicitud" class="mt-4">
        <div class="form-group">
          <label for="detalle">Detalle:</label>
          <textarea id="detalle" v-model="detalle" class="form-control" required></textarea>
        </div>
        <button type="submit" class="btn btn-primary">Enviar Solicitud</button>
      </form>
      
      <!-- Mostrar mensaje de éxito -->
      <div v-if="solicitudEnviada" class="alert alert-success mt-4">
        Solicitud enviada con éxito al servicio : "{{ this.servicio.nombre}}"  
      </div>
    </div>
  </template>
  
<script>
import { apiService } from '@/api';


  export default {
    name: 'Solicitud',
    data() {
      return {
        detalle: "",
        solicitudEnviada: false,
        servicio : {},
      };
    },
    created() {
        this.obtenerServicio();
  },
    methods: {
    async enviarSolicitud() {
  try {
    const csrfToken = localStorage.getItem('csrfToken'); 
    const jwtToken = localStorage.getItem('jwt'); 
    const respuesta = await apiService.post('api/me/requests', {
      detalles: this.detalle,
      servicio_id: this.$route.params.id,
    }, 
    {
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${jwtToken}`,
        'X-CSRF-TOKEN': csrfToken,
      },
    });

    console.log(respuesta.data);
    this.solicitudEnviada = true;
  } catch (error) {
    console.error('Error al enviar la solicitud', error);
  }},

  async obtenerServicio() {
      try {
        const respuesta = await apiService.get(`/api/services/${this.$route.params.id}`);
        this.servicio = respuesta.data;
      } catch (error) {
        console.error('Error al obtener la información del servicio', error);
      }
    },

    },
  };
</script>
<style>
</style>
  