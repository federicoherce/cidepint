<template>
  <div class="container mt-5">
    <div class="row justify-content-center">
      <div class="col-md-6">
        <div v-if="!loggedIn" class="card">
          <div class="card-body">
            <h2 class="card-title text-center">Iniciar sesión</h2>
            <form @submit.prevent="login">
              <div class="mb-3">
                <label for="email" class="form-label">Correo electrónico:</label>
                <input v-model="user.email" type="email" id="email" class="form-control" required>
              </div>
              <div class="mb-3">
                <label for="password" class="form-label">Contraseña:</label>
                <input v-model="user.password" type="password" id="password" class="form-control" required>
              </div>
              <button type="submit" class="btn btn-primary btn-block">Iniciar sesión</button>
            </form>
          </div>
        </div>
        <div v-else>
          <p class="success-message text-center">¡Sesión iniciada correctamente!</p>
        </div>
      </div>
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
