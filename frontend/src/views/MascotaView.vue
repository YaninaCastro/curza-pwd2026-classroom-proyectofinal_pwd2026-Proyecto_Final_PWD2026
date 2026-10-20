<template>
  <main>
    <CerrarSesion/>

    <h1>Gestión de mascotas</h1>

    <template v-if="mostrarEdicion">
      <MascotaEdit
        :id="mascotaId"
        @actualizado="vuelveAlListado"
        @cancelar="vuelveAlListado"
      />
    </template>

    <template v-else>
      <MascotaCreate  v-if="puedeCrear" />
      <MascotaList
        :key="actualizarLista"
        @editar="edita"
      />
    </template>
  </main>
</template>



<script setup>
import { ref } from "vue";
import MascotaCreate from "../components/MascotaCreate.vue";
import MascotaList from "../components/MascotaList.vue";
import MascotaEdit from "../components/MascotaEdit.vue";
import CerrarSesion from "../components/CerrarSesion.vue";
import { useAuthStore } from "../stores/auth.js";

const mostrarEdicion = ref(false);
const mascotaId = ref(null);
const actualizarLista = ref(0);

const authStore = useAuthStore();

const puedeCrear = ["Administrador/a", "recepcionista"].includes(
  authStore.rol_user
);

function edita(id) {
  mascotaId.value = id;
  mostrarEdicion.value = true;
}

function vuelveAlListado() {
  mostrarEdicion.value = false;
  mascotaId.value = null;
  actualizarLista.value++;
}
/*Qué cambiamos y por qué?
- edita(id) recibe el ID de la mascota seleccionada.
- mostrarEdicion decide si se muestra el listado o el formulario de edición.
- vuelveAlListado() vuelve al listado después de guardar o cancelar y lo actualiza para mostrar los cambios.
Ahora probalo
1. Entrá a /mascotas.
2. Presioná Editar en una mascota.
3. Cambiá su nombre y guardá.
Si aparece un error al guardar, pasame el mensaje exacto. Puede que tengamos que ajustar el update del backend, 
especialmente los campos fecha_nto y dueno_id. */

</script>