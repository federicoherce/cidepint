// https://nominatim.openstreetmap.org/search?country=argentina&city=la+plata&street=1356+Calle+10&format=json

import { apiService } from '@/api';

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
    const map = L.map('mapa').setView([-34.91895294495346, -57.95574638183875], 14);

    L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
    }).addTo(map);

  },
  methods: {
    async obtenerServicio() {
      try {
        const respuesta = await apiService.get(`/api/services/${this.id}`);
        this.servicio = respuesta.data;

        await this.obtenerInstitucion(this.servicio.institucion_id);
      } catch (error) {
        console.error('Error al obtener la información del servicio', error);
      }
    },
    async obtenerInstitucion(institucionId) {
      try {
        const respuesta = await apiService.get(`/api/instituciones/${institucionId}`);
        this.institucion = respuesta.data;
      } catch (error) {
        console.error('Error al obtener la información de la institución', error);
      }
    },
  },

};