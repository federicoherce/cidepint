<template>
      <button class="btn btn-danger" type="button" @click="logout">Logout</button>
</template>



<script>
import { apiService } from '@/api';
import { useAuthStore } from '@/stores/modules/auth';

export default {

  created() {
    // Al crear el componente, almacena el store en una variable local
    this.store = useAuthStore();
  },
  computed: {
    loggedIn() {
      // Usa la información de inicio de sesión para determinar si el usuario ha iniciado sesión
      return this.store.isLoggedIn;
    }
  },
  methods: {
    async logout() {  
      try {
         const response = await apiService.get('api/logout_jwt',{
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${localStorage.getItem('jwt')}`
          }})
         localStorage.removeItem('jwt');
         console.log(response.data.message);
         this.store.logoutUser()
         this.$router.push({ name: 'Home' });
    }
    catch (error) {
        console.error(error);
      }},


    }}
</script>
