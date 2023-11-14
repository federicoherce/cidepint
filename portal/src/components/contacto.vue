<template>
  <div class="container my-5">
    <h2 class="display-4 text-center">Información de Contacto</h2>
    
    <div class="card mt-3">
      <div class="card-body">
        <h5 class="card-title">Email</h5>
        <p class="card-text">{{ contacto.email }}</p>
      </div>
    </div>

    <div class="card mt-3">
      <div class="card-body">
        <h5 class="card-title">Teléfono</h5>
        <p class="card-text">{{ contacto.telefono }}</p>
      </div>
    </div>

    <div class="card mt-3">
      <div class="card-body">
        <h5 class="card-title">Dirección</h5>
        <p class="card-text">{{ contacto.direccion }}</p>
      </div>
    </div>
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