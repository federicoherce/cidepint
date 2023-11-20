<template>
    <div class="container my-5">
        <h2 class="display-4 text-center">Estadísticas</h2>
    
        <div class="row mt-4">
            <div class="col-md-4">
                <router-link to="estadisticas/solicitudes-por-estado">
                    <div class="card">
                        <div class="card-body text-center">
                            <font-awesome-icon icon="fa-solid fa-chart-column" />
                            <h5 class="card-title">Solicitudes realizadas por estado.</h5>
                        </div>
                    </div>
                </router-link>
            </div>
    
            <div class="col-md-4">
                <router-link to="estadisticas/top-10-instituciones">
                    <div class="card">
                        <div class="card-body text-center">
                            <font-awesome-icon icon="fa-solid fa-stopwatch" />
                            <h5 class="card-title">Top 10 de instituciones con mejor tiempo de resolución</h5>
                        </div>
                    </div>
                </router-link>
            </div>
    
            <div class="col-md-4">
                <router-link to="estadisticas/ranking-servicios">
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
    export default {
    
    };
    </script>
    
    <style>
    
    </style>