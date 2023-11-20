import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Navbar from '../components/Navbar.vue' 
import loginView from '../views/loginView.vue'
import contacto from '../components/contacto.vue'
import servicios from '../views/ServiciosView.vue'
import solicitudes from '../views/MisSolicitudes.vue'
import detallesServicio from '../components/detallesServicio.vue'
import solicitud from '../views/solicitud.vue'
import logout from '../components/logout.vue'

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
    path: '/solicitudes',
    name: 'solicitudes',
    component: solicitudes
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router