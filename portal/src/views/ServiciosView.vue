<template>
  <div class="container-fluid mb-4">
    <br>
    <h1 class="mt-4">Servicios</h1>

    <TiposDeServicios/>

    <div class="form-group">
      <input type="text" class="form-control" v-model="titleSearch" placeholder="Buscar por título">
    </div>

    <div class="form-group">
      <input type="text" class="form-control" v-model="descriptionSearch" placeholder="Buscar por descripción">
    </div>

    <div class="form-group">
      <input type="text" class="form-control" v-model="institutionSearch" placeholder="Buscar por institución">
    </div>

    <div class="form-group">
      <input type="text" class="form-control" v-model="tagsSearch" placeholder="Buscar por palabras clave">
    </div>

    

    <table class="table table-striped table-bordered">
      <thead>
        <tr>
          <th>Título</th>
          <th>Descripción</th>
          <th>Institución</th>
          <th>Tags</th>
          <th>Tipo de Servicio</th>
          <th></th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="servicio in servicios" :key="servicio.id">
          <router-link :to="{name: 'detallesServicio', params: { id: servicio.id } }">
          <td>{{ servicio.nombre }}</td>
          </router-link>
          <td>{{ servicio.descripcion }}</td>
          <td>{{ servicio.institucion }}</td>
          <td>{{ servicio.keywords }}</td>
          <td>{{ servicio.tipo }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<!--<ul>
        <li v-for="servicio in servicios" :key="servicio.id">
            <router-link :to="{ name: 'detallesServicio', params: { id: servicio.id } }">
                {{ servicio.nombre }}
            </router-link>
        </li>
      </ul>
    </div>-->
  
<script>
import { apiService } from '@/api';
import TiposDeServicios from '../components/TiposDeServicios.vue';

export default {
  data() {
    return {
      servicios: {},
      tipoServicioSeleccionado: ''
    };
  },
  components: {
    TiposDeServicios
  },
  methods: {
    async obtenerServicios() {
      try {
        const respuesta = await apiService.get('api/all_services');
        this.servicios = respuesta.data;
      } catch (error) {
        console.error('Error al obtener los servicios', error);
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