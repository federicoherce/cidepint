<template>
    <div>
      <h2>Información de Contacto</h2>
      <div>Email: {{ contacto.email }}</div>
      <div>Teléfono: {{ contacto.telefono }}</div>
      <div>Dirección: {{ contacto.direccion }}</div>
    </div>
  </template>
<script>
import { apiService } from '@/api';

export default {
  data() {
    return {
      contacto: {}
    };
  },
  methods: {
    async obtenerInformacionDeContacto() {
      try {
        const respuesta = await apiService.get('api/contacto');
        this.contacto = respuesta.data;
      } catch (error) {
        console.error('Error al obtener la información de contacto', error);
      }
    }
  },
  mounted() {
    this.obtenerInformacionDeContacto();
  }
}
</script>

<style>
</style>