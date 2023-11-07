<template>
    <div>
      <label for="seleccionTipoServicio">Tipo de Servicio:</label>
      <select id="seleccionTipoServicio" class="form-control" v-model="tipoServicioSeleccionado">
        <option value="">Todos</option>
        <option v-for="tipo in tiposDeServicios" :key="tipo">
          {{ tipo }}
        </option>
      </select>
    </div>
</template>
  
<script>
  import { apiService } from '@/api';
  
  export default {
    data() {
      return {
        tipoServicioSeleccionado: '',
        tiposDeServicios: [],
      };
    },
    async created() {
      await this.obtenerTiposDeServicio();
    },
    methods: {
      async obtenerTiposDeServicio() {
        try {
          const respuesta = await apiService.get('/api/services-type');
          this.tiposDeServicios = respuesta.data.data;
          console.log('Tipos de servicio obtenidos:', this.tiposDeServicios);
        } catch (error) {
          console.error('Error al obtener tipos de servicio:', error);
        }
      },
    },
  };
</script>

<style>
</style>
  