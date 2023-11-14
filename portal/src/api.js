import axios from 'axios';
import { useAuthStore } from '@/stores/modules/auth';

const apiService = axios.create({
  baseURL: 'http://localhost:5000/',
  withCredentials: true,
  xsrfCookieName: 'csrf_access_token'
});

apiService.interceptors.response.use(
    
  (response) => {
    return response;
  },
  (error) => {
    if (error.response && error.response.status === 401) {
      alert('Su sesión ha excedido el tiempo límite. Por favor, acceda de nuevo.'); 
      const store = useAuthStore();
      store.logoutUser();
      localStorage.removeItem('jwt');
      console.log('Usuario no autorizado. Redirigiendo al inicio de sesión.');
    }
    return Promise.reject(error);
  }
);

export { apiService };
