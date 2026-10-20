<template>
  <div class="contenedor-cerrar-sesion">
    <button 
      type="button"
      class="btn-cerrar-sesion"
      @click="cerrarSesion">
      Cerrar sesión
    </button>
  </div>
</template>

<script setup>
import { useRouter } from "vue-router";
import { useAuthStore } from "../stores/auth.js";

const authStore = useAuthStore();
const router = useRouter();

function cerrarSesion() {
  authStore.logout();
  router.replace({ name: "Login" });
}
</script>




<style scoped>


.contenedor-cerrar-sesion {
  display: flex;
  justify-content: flex-end;
  margin: 0 20px 20px 15px;
  padding-top: 20px;
}

.btn-cerrar-sesion {
  background-color: #2563eb;
  color: white;
  border: none;
  border-radius: 8px;
  padding: 7px 12px;
  font-size: 12px;
  font-weight: 600;
  cursor: pointer;
  transition: background-color 0.2s ease;
}

.btn-cerrar-sesion:hover {
  background-color: #1d4ed8;
}

</style>
