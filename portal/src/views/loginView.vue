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
  computed: {
    loggedIn() {
      // Usa la información de inicio de sesión para determinar si el usuario ha iniciado sesión
      const store = useAuthStore();
      return store.isLoggedIn;
    }
  },
  methods: {
    async logout() {  
      const store = useAuthStore();
      try {
         const response = await apiService.get('sesion/logout_jwt',{
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${localStorage.getItem('jwt')}`
          }})
         localStorage.removeItem('jwt');
         console.log(response);
         store.logoutUser()
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

        const response = await apiService.post('sesion/login_jwt', userData, {
          headers: {
            'Content-Type': 'application/json'
          }
        });

        console.log(response);
        const store = useAuthStore();
        store.setUser(response);
        console.log('User stored in Pinia:', store.getUser);
        localStorage.setItem('jwt', response.data.token);
        console.log(localStorage.getItem('jwt'));
      } catch (error) {
        console.error(error);
        this.error = true;
      }
    }
  }
};
</script>

<style scoped>
.login-container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
}

.login-form {
  max-width: 400px;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
  background-color: #f5f5f5;
}

.form-title {
  text-align: center;
  font-size: 24px;
  margin-bottom: 20px;
}

.form-group {
  margin: 10px 0;
}

.form-label {
  font-weight: bold;
}

.form-control {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.btn:hover {
  background-color: #0056b3;
}.success-message {
  color: green; /* Color de texto verde para éxito */
  font-weight: bold; /* Texto en negrita */
  margin-top: 10px; /* Espacio superior */
}
</style>
