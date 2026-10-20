<script setup>
import { ref } from "vue";
import DuenoList from "../components/DuenoList.vue";
import DuenoCreate from "../components/DuenoCreate.vue";
import DuenoEdit from "../components/DuenoEdit.vue";
import CerrarSesion from "../components/CerrarSesion.vue";
import { useAuthStore } from "../stores/auth.js";


const mostrarEdicion = ref(false);
const duenoId = ref(null);
const actualizarLista = ref(0);

const authStore = useAuthStore();

const puedeCrear = ["Administrador/a", "recepcionista"].includes(
  authStore.rol_user
);

function edita(id) {
  duenoId.value = id;
  mostrarEdicion.value = true;
}

function vuelveAlListado() {
  mostrarEdicion.value = false;
  duenoId.value = null;
  actualizarLista.value++;
}
</script>

<template>
  <main>
    <CerrarSesion/>
    
    <h1>Gestión de dueños</h1>

    <template v-if="mostrarEdicion">
      <DuenoEdit
        :id="duenoId"
        @actualizado="vuelveAlListado"
        @cancelar="vuelveAlListado"
      />
    </template>

    <template v-else>
      <DuenoCreate v-if="puedeCrear" />
      <DuenoList :key="actualizarLista" @editar="edita"/>
    </template>
  </main>
</template>