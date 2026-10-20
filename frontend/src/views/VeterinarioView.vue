<template>
  <main>
    <h2>Gestión de veterinarios</h2>

    <CerrarSesion />

    <VeterinarioEdit
      v-if="puedeEditar && mostrarEdicion"
      :id="idSeleccionado"
      @actualizado="finalizarEdicion"
      @cancelar="finalizarEdicion"
    />

    <VeterinarioCreate
      v-else-if="puedeEditar"
    />

    <VeterinarioList @editar="editar" />
  </main>
</template>


<script setup>
import { ref } from "vue";
import { useAuthStore } from "../stores/auth.js";
import CerrarSesion from "../components/CerrarSesion.vue";
import VeterinarioCreate from "../components/VeterinarioCreate.vue";
import VeterinarioList from "../components/VeterinarioList.vue";
import VeterinarioEdit from "../components/VeterinarioEdit.vue";

const authStore = useAuthStore();

const puedeEditar = [
  "Administrador/a",
  "recepcionista"
].includes(authStore.rol_user);

const mostrarEdicion = ref(false);
const idSeleccionado = ref(null);

function editar(id) {
  idSeleccionado.value = id;
  mostrarEdicion.value = true;
}

function finalizarEdicion() {
  mostrarEdicion.value = false;
  idSeleccionado.value = null;
}
</script>
