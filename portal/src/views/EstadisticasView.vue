<template>
<div class="container my-5">
    <h2 class="display-4 text-center">Estadísticas</h2>

    <div class="row mt-4">
        <div class="col-md-4">
            <router-link to="/solicitudes-por-estado">
            <div class="card">
                <div class="card-body text-center">
                    <font-awesome-icon icon="fa-solid fa-chart-column" />
                    <h5 class="card-title">Solicitudes realizadas por estado</h5>
                    
                </div>
            </div>
            </router-link>
        </div>

        <div class="col-md-4" v-if="tienePermiso('statistics_all_institutions')">
            <router-link to="/top-10-instituciones">
            <div class="card">
                <div class="card-body text-center">
                    <font-awesome-icon icon="fa-solid fa-stopwatch" />
                    <h5 class="card-title">Top 10 de instituciones con mejor tiempo de resolución</h5>
                </div>
            </div>
            </router-link>
        </div>

        <div class="col-md-4">
            <router-link to="/ranking-servicios">
                <div class="card">
                <div class="card-body text-center">
                    <font-awesome-icon icon="fa-solid fa-ranking-star" />
                    <h5 class="card-title">Ranking de servicios más solicitados</h5>
                </div>
            </div>
            </router-link>
        </div>
    </div>
</div>
</template>

<script>
import { useAuthStore } from '@/stores/modules/auth'

export default {
  methods: {
    tienePermiso(permission) {
      const authStore = useAuthStore();
      const userPermissions = authStore.getUserPermissions;

      return Array.isArray(userPermissions) && userPermissions.includes(permission);
    }
  
  }
};
</script>

<style>

</style>
  