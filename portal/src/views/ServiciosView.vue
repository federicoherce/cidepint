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
        <tr v-for="servicio in servicios.data" :key="servicio.id">
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

    <nav aria-label="Page navigation">
      <ul class="pagination">
        <li class="page-item" v-if="servicios.page > 1">
          <a class="page-link" @click="cambiarPagina(servicios.page - 1)" aria-label="Previous">
            <span aria-hidden="true">&laquo;</span>
          </a>
        </li>
        <li class="page-item" v-for="pageNumber in servicios.pages" :key="pageNumber" :class="{ 'active': servicios.page == pageNumber }">
          <a class="page-link" @click="cambiarPagina(pageNumber)">{{ pageNumber }}</a>
        </li>
        <li class="page-item" v-if="servicios.page < servicios.pages">
          <a class="page-link" @click="cambiarPagina(servicios.page + 1)" aria-label="Next">
            <span aria-hidden="true">&raquo;</span>
          </a>
        </li>
      </ul>
    </nav>
  </div>
</template>
  
<script>
import { apiService } from '@/api';
import TiposDeServicios from '../components/TiposDeServicios.vue';

export default {
  data() {
    return {
      servicios: {
        items: [],
        page: 1,
        per_page: 1,
        total: 0,
        pages: 0
      },
      tipoServicioSeleccionado: ''
    };
  },
  components: {
    TiposDeServicios
  },
  methods: {
    async obtenerServicios() {
      try {
        const respuesta = await apiService.get('api/all_services', {
          params: {
            page: this.servicios.page,
            per_page: this.servicios.per_page
          }  
        });
        //const respuesta = await apiService.get('api/all_services');
        this.servicios = respuesta.data;
      } catch (error) {
        console.error('Error al obtener los servicios', error);
      }
    },
    cambiarPagina(pageNumber) {
      if (pageNumber >= 1 && pageNumber <= this.servicios.pages) {
        this.servicios.page = pageNumber
        this.obtenerServicios()
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