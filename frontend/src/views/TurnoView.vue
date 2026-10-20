<template>
  <main>
    <CerrarSesion />

    <h1>Gestión de turnos</h1>

    <template v-if="mostrarEdicion">
      <TurnoEdit
        :id="turnoId"
        @actualizado="vuelveAlListado"
        @cancelar="vuelveAlListado"
      />
    </template>

    <template v-else>
      <TurnoCreate v-if="puedeCrear" />
      <TurnoList :key="actualizarLista" @editar="edita" />
    </template>
  </main>
</template>

<script setup>
import { ref } from "vue";
import TurnoList from "../components/TurnoList.vue";
import TurnoCreate from "../components/TurnoCreate.vue";
import TurnoEdit from "../components/TurnoEdit.vue";
import CerrarSesion from "../components/CerrarSesion.vue";
import { useAuthStore } from "../stores/auth.js";

const mostrarEdicion = ref(false);
const turnoId = ref(null);
const actualizarLista = ref(0);

const authStore = useAuthStore();

const puedeCrear = ["Administrador/a", "recepcionista"].includes(
  authStore.rol_user
);

function edita(id) {
  turnoId.value = id;
  mostrarEdicion.value = true;
}

function vuelveAlListado() {
  mostrarEdicion.value = false;
  turnoId.value = null;
  actualizarLista.value++;
}
</script>