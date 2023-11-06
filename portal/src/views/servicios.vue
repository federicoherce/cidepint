<template>
    <div>
      <ul>
        <li v-for="servicio in servicios" :key="servicio.id">
            <router-link :to="{ name: 'detallesServicio', params: { id: servicio.id } }">
                {{ servicio.nombre }}
            </router-link>
        </li>
      </ul>
    </div>
  </template>
  
<script>
import { apiService } from '@/api';

export default {
  data() {
    return {
      servicios: {}
    };
  },
  methods: {
    async obtenerServicios() {
      try {
        const respuesta = await apiService.get('api/all_services');
        this.servicios = respuesta.data;
      } catch (error) {
        console.error('Error al obtener la información de contacto', error);
      }
    }
  },
  mounted() {
    this.obtenerServicios();
  }
}
</script>

<style>
</style>