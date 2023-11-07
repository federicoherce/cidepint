<template>
  <div class="login-container">
    <div v-if="!loggedIn" class="login-form">
      <h2 class="form-title">Iniciar Sesión</h2>
      <form action class = "form" @submit.prevent="login">
        <div class="form-group">
          <label for="email">Email:</label>
          <input v-model="user.email" placeholder="Email" class="form-control" type="email" id="email" required>
        </div>
        <div class="form-group">
          <label for="password">Password:</label>
          <input v-model="user.password" placeholder="Password" type="password" class="form-control" id="password" required>
        </div>
        <button class="btn btn-primary" type="submit">Login</button>
      </form>
      <p v-if="error" class="error-message">Error: Correo electrónico o contraseña incorrectos.</p>
    </div>
    <div v-else>
      <p class="success-message">¡Sesión iniciada correctamente!</p>
      <button class="btn btn-danger" type="button" @click="logout">Logout</button>

    </div>
  </div>
</template>

<script>
import { apiService } from '@/api';
import { useAuthStore } from '@/stores/modules/auth';

export default {
  data() {
    return {
      user: {
        email: '',
        password: ''
      },
      error: false
    };
  },
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

         
    async login() {
      try {
        const userData = {
          email: this.user.email,
          password: this.user.password
        };

        const response = await apiService.post('api/login_jwt', userData, {
          headers: {
            'Content-Type': 'application/json'
          }
        });
        console.log('login : ',response.status , response.statusText);
        localStorage.setItem('jwt', response.data.token);
        await this.store.axiosUser();

      } catch (error) {
        console.error(error);
        this.error = true;
      }
    }
  }
};
</script>

<style scoped>

.login-form {
  max-width: 400px;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
  background-color: #f5f5f5;
}

.success-message {
  color: green; /* Color de texto verde para éxito */
  font-weight: bold; /* Texto en negrita */
  margin-top: 10px; /* Espacio superior */
}
</style>
