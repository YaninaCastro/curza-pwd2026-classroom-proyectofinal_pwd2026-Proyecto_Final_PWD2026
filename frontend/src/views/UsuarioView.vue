<template>
  <main>
    <CerrarSesion />

    <h1>Gestión de usuarios</h1>

    <template v-if="mostrarEdicion">
      <UsuarioEdit
        :id="usuarioId"
        @actualizado="vuelveAlListado"
        @cancelar="vuelveAlListado"
      />
    </template>

    <template v-else>
      <UsuarioCreate v-if="puedeCrear" />
      <UsuarioList
        :key="actualizarLista"
        @editar="edita"
      />
    </template>
  </main>
</template>

<script setup>
import { ref } from "vue";
import { useAuthStore } from "../stores/auth.js";
import CerrarSesion from "../components/CerrarSesion.vue";
import UsuarioCreate from "../components/UsuarioCreate.vue";
import UsuarioEdit from "../components/UsuarioEdit.vue";
import UsuarioList from "../components/UsuarioList.vue";

const authStore = useAuthStore();
const mostrarEdicion = ref(false);
const usuarioId = ref(null);
const actualizarLista = ref(0);

const puedeCrear = authStore.rol_user === "Administrador/a";

function edita(id) {
  usuarioId.value = id;
  mostrarEdicion.value = true;
}

function vuelveAlListado() {
  mostrarEdicion.value = false;
  usuarioId.value = null;
  actualizarLista.value++;
}
</script>