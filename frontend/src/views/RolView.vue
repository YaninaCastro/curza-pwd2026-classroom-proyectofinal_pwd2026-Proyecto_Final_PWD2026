<template>
  <main>
    <h2>Gestión de roles</h2>

    <CerrarSesion />

    <RolCreate v-if="puedeAdministrar" />

    <RolList @editar="editar" />

    <RolEdit
      v-if="puedeAdministrar && mostrarEdicion"
      :id="idSeleccionado"
      @actualizado="finalizarEdicion"
      @cancelar="finalizarEdicion"
    />
  </main>
</template>

<script setup>
import { ref } from "vue";
import { useAuthStore } from "../stores/auth.js";
import CerrarSesion from "../components/CerrarSesion.vue";
import RolCreate from "../components/RolCreate.vue";
import RolList from "../components/RolList.vue";
import RolEdit from "../components/RolEdit.vue";

const authStore = useAuthStore();

const puedeAdministrar = authStore.rol_user === "Administrador/a";
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
