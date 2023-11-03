import { createRouter, createWebHistory } from 'vue-router'
import Home from '../components/Home.vue'
import Navbar from '../components/Navbar.vue' 
import loginView from '../views/loginView.vue'

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
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router