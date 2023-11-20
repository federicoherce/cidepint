<template>
  <div class="container-fluid mb-4">
    <br>
    <h1 class="mt-4">Mis Solicitudes</h1>

    <div class="form-group">
      <input type="text" class="form-control" v-model="estado" placeholder="Filtrar por Estado">
    </div>

    <div class="form-group">
      <label for="fechaInicio">Fecha Inicio:</label>
      <input type="date" class="form-control" v-model="fechaInicio">
    </div>

    <div class="form-group">
      <label for="fechaFin">Fecha Fin:</label>
      <input type="date" class="form-control" v-model="fechaFin">
    </div>

    <div class="form-group">
      <button class="btn btn-primary" @click="traerSolicitud">Buscar</button>
      <button v-if="busqueda" class="btn btn-secondary" @click="deshacerBusqueda">Deshacer Búsqueda</button>
    </div>

    <div class="btn-group">
      <button class="btn btn-secondary" @click="ordenarPorFecha('asc')">Ordenar por Fecha Ascendente</button>
      <button class="btn btn-secondary" @click="ordenarPorFecha('desc')">Ordenar por Fecha Descendente</button>
    </div>

    <table class="table table-striped table-bordered">
      <thead>
        <tr>
          <th @click="ordenarPor('nombre')">Título del Servicio</th>
          <th>Descripción</th>
          <th>Estado</th>
          <th>Fecha de Creación</th>
          <th>Fecha de Cambio de Estado</th>
          <th>Ultimo Comentario</th>
          <th></th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="solicitud in solicitudes" :key="solicitud.id">
          <td>{{ solicitud.servicio ? solicitud.servicio.nombre : 'Sin servicio' }}</td>
          <td>{{ solicitud.detalles }}</td>
          <td>{{ solicitud.estado }}</td>
          <td>{{ formatoFecha(solicitud.fecha_creacion) }}</td>
          <td>{{ formatoFecha(solicitud.fecha_cambio_estado) }}</td>
          <td>{{ solicitud.observacion_cambio_estado }}</td>
        </tr>
      </tbody>
    </table>

    <nav aria-label="Page navigation">
      <ul class="pagination">
        <li class="page-item" v-if="solicitudes.page > 1">
          <a class="page-link" @click="cambiarPagina(solicitudes.page - 1)" aria-label="Previous">
            <span aria-hidden="true">&laquo;</span>
          </a>
        </li>
        <li class="page-item" v-for="pageNumber in solicitudes.pages" :key="pageNumber" :class="{ 'active': solicitudes.page == pageNumber }">
          <a class="page-link" @click="cambiarPagina(pageNumber)">{{ pageNumber }}</a>
        </li>
        <li class="page-item" v-if="solicitudes.page < solicitudes.pages">
          <a class="page-link" @click="cambiarPagina(solicitudes.page + 1)" aria-label="Next">
            <span aria-hidden="true">&raquo;</span>
          </a>
        </li>
      </ul>
    </nav>
  </div>
</template>

<script>
import { apiService } from '@/api';

export default {
  data() {
    return {
      estado: '',
      fechaInicio: '',
      fechaFin: '',
      busqueda: false,
      solicitudes: [],
      currentPage: 1, // Agregamos una propiedad para rastrear la página actual
      sort: '', // Agregamos una propiedad para rastrear la columna de ordenamiento
      order: '', // Agregamos una propiedad para rastrear el orden (ascendente o descendente)
    };
  },
  methods: {
    buscarSolicitudes() {
      const jwtToken = localStorage.getItem('jwt')
      const params = {
        estado: this.estado,
        page: this.currentPage,
        per_page: '3',
        sort: this.sort,
        order: this.order
      };

      this.$axios.get('/api/me/requests', { params }, {headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${jwtToken}`
          }})
        .then(response => {
          this.solicitudes = response.data.data;
          this.busqueda = true;
        })
        .catch(error => {
          console.error('Error al obtener las solicitudes:', error);
        });
    },

    async traerSolicitud() {
      const params = {
        page: this.currentPage,
        per_page: '3',
        sort: this.sort,
        order: this.order,
      }
      try {
        const csrfToken = localStorage.getItem('csrfToken'); 
        const jwtToken = localStorage.getItem('jwt');
        if(localStorage.getItem('jwt') == null){
            alert("Debe iniciar sesión para enviar una solicitud");
            throw new Error("Debe iniciar sesión para enviar una solicitud");
        }
        const respuesta = await apiService.get('api/me/requests', { params
        }, 
        {
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${jwtToken}`,
            'X-CSRF-TOKEN': csrfToken,
          },
        });
        this.solicitudes = respuesta.data.data;
        this.busqueda = true;
        this.solicitudEnviada = true;
      } catch (error) {
        console.error('Error al enviar la solicitud', error);
        this.$router.push({ name: 'loginView' });
      }},

    deshacerBusqueda() {
      this.busqueda = false;
      this.estado = '';
      this.fechaInicio = '';
      this.fechaFin = '';
      this.sort = ''; // Reiniciar la columna de ordenamiento
      this.order = 'asc'; // Reiniciar el orden (ascendente por defecto)

      this.cargarSolicitudes();
    },

    ordenarPorFecha(order) {
      // Lógica para cambiar el orden por fecha
      this.order = order;
      this.sort = 'fecha_creacion'; // Ajusta esto según el nombre real del campo de fecha en tus datos
      this.cargarSolicitudes();
    },

    ordenarPor(columna) {
      // Si la columna ya está ordenada, invertir el orden
      if (this.sort === columna) {
        this.order = this.order === 'asc' ? 'desc' : 'asc';
      } else {
        // Si es una nueva columna, ordenar en ascendente por defecto
        this.sort = columna;
        this.order = 'asc';
      }

      this.cargarSolicitudes();
    },

    cambiarPagina(pageNumber) {
      this.currentPage = pageNumber;
      this.cargarSolicitudes();
    },

    formatoFecha(fecha) {
      const options = { year: 'numeric', month: 'long', day: 'numeric' };
      return new Date(fecha).toLocaleDateString('es-ES', options);
    },

    cargarSolicitudes() {
      const params = {
        estado: this.estado,
        fechaInicio: this.fechaInicio,
        fechaFin: this.fechaFin,
        page: this.currentPage,
        sort: this.sort,
        order: this.order,
      };

      this.$axios.get('/api/me/requests', { params })
        .then(response => {
          this.solicitudes = response.data.data;
        })
        .catch(error => {
          console.error('Error al obtener las solicitudes:', error);
        });
    },
  },
};
</script>

<style>
 .form-group {
    display: flex;
    justify-content: space-between;
  }
</style>