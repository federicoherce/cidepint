// https://nominatim.openstreetmap.org/search?country=argentina&city=la+plata&street=1356+Calle+10&format=json

import { apiService } from '@/api';
import axios from 'axios';

export default {
  props: ['id'],
  data() {
    return {
      servicio: {},
      institucion: {},
    };
  },
  mounted() {
    this.obtenerServicio();
  },
  methods: {
    async obtenerServicio() {
      try {
        const respuesta = await apiService.get(`/api/services/${this.id}`);
        this.servicio = respuesta.data;

        this.obtenerInstitucion(this.servicio.institucion_id);
      } catch (error) {
        console.error('Error al obtener la información del servicio', error);
      }
    },
    async obtenerInstitucion(institucionId) {
      try {
        const respuesta = await apiService.get(`/api/instituciones/${institucionId}`);
        this.institucion = respuesta.data;
        this.infoMapa(this.institucion.calle, this.institucion.numero)
      } catch (error) {
        console.error('Error al obtener la información de la institución', error);
      }
    },
    async infoMapa(calle, nro) {
      try {
        const info = await axios.get(`https://nominatim.openstreetmap.org/search?country=argentina&city=la+plata&street=${nro}+Calle+${calle}&format=json`)
        const map = L.map('mapa').setView([-34.91895294495346, -57.95574638183875], 14);
        L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
        }).addTo(map);
        const marker = L.marker([info.data[0].lat, info.data[0].lon]).addTo(map);
      } catch(error) {
          console.error('Error al obtener la información de geocoding', error);
      }

    },
  },

};