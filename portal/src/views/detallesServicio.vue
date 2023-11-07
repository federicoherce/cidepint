<template>
    <div>
      <h2>{{ servicio.nombre }}</h2>
      <p>{{ servicio.descripcion }}</p>
      <p>{{ servicio.keywords }}</p>
      <p>{{ servicio.habilitado }}</p>
      <br>
      <h1> Boton de solicitar </h1>
      <h1> Informacion de la institucion</h1>
      <h1> Mapa </h1>
    </div>
  </template>
  
  <script>
  
  import { apiService } from '@/api';  
  export default {
    props: ['id'],
    data() {
      return {
        servicio: {},
      };
    },
    created() {
      this.obtenerServicio();
    },
    methods: {
      async obtenerServicio() {
        try {
          const respuesta = await apiService.get(`/api/services/${this.id}`);
          this.servicio = respuesta.data;
        } catch (error) {
          console.error('Error al obtener la información del servicio', error);
        }
      }
    },
  };
  </script>
  