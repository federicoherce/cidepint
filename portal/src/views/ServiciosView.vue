<template>
  <div class="container mb-4">
    <h1 class="mt-4">Servicios</h1>

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

    <div class="form-group">
      <label for="serviceTypeSelect">Tipo de Servicio:</label>
      <select id="serviceTypeSelect" class="form-control" v-model="selectedServiceType">
        <option value="">Todos</option>
        <option value="Tipo 1">Tipo 1</option>
        <option value="Tipo 2">Tipo 2</option>
        <!-- Agrega más opciones de tipo de servicio aquí -->
      </select>
    </div>

    <table class="table table-striped table-bordered">
      <thead>
        <tr>
          <th>Título</th>
          <th>Descripción</th>
          <th>Institución</th>
          <th>Tags</th>
          <th>Tipo de Servicio</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="servicio in servicios" :key="servicio.id">
          <td>{{ servicio.title }}</td>
          <td>{{ servicio.description }}</td>
          <td>{{ servicio.institution }}</td>
          <td>{{ servicio.tags.join(', ') }}</td>
          <td>{{ servicio.serviceType }}</td>
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