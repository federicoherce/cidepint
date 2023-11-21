import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Navbar from '../components/Navbar.vue' 
import loginView from '../views/loginView.vue'
import contacto from '../components/contacto.vue'
import servicios from '../views/ServiciosView.vue'
import detallesServicio from '../components/detallesServicio.vue'
import solicitud from '../views/solicitud.vue'
import logout from '../components/logout.vue'
import estadisticas from '../views/EstadisticasView.vue'
import solicitudesPorEstado from '../components/SolicitudesPorEstado.vue'
import topInstituciones from '../components/TopInstituciones.vue'
import rankingServicios from '../components/RankingServicios.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/navbar',
    name: "Navbar",
    component: Navbar
  },
  {
    path: '/login',
    name: "loginView",
    component: loginView
  },
  {
    path: '/contacto',
    name: "contacto",
    component: contacto
  },
  {
    path: '/servicios',
    name: "ServiciosView",
    component: servicios
  },
  {
    path: '/servicios/:id',
    name: "detallesServicio",
    component: detallesServicio,
    props: true
  },
  {
    path: '/solicitud/:id/:institucion_id', 
    name: 'solicitud',
    component: solicitud, 
  }
  ,
  {
    path: '/logout',
    name: 'logout',
    component: logout, 
  },
  {
    path: '/estadisticas',
    name: 'EstadisticasView',
    component: estadisticas,
  },
  {
    path: '/top-10-instituciones',
    name: 'TopInstituciones',
    component: topInstituciones
  },
  {
    path: '/solicitudes-por-estado',
    name: 'SolicitudesPorEstado',
    component: solicitudesPorEstado
  },
  {
    path: '/ranking-servicios',
    name: 'RankingServicios',
    component: rankingServicios
  }



]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router