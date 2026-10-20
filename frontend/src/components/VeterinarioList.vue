<template>
  <section>
    <p v-if="cargando">Cargando veterinarios...</p>

    <p v-else-if="error">
      No se pudieron cargar los veterinarios.
    </p>

    <h3 v-else-if="veterinarios.length === 0">
      No hay veterinarios registrados.
    </h3>

    <template v-else>
      <DataTable
        :headers="[
          'ID',
          'NOMBRE',
          'APELLIDO',
          'TELEFONO',
          'EMAIL',
          'MATRICULA',
          'ESPECIALIDAD',
          'USUARIO_SISTEMA',
          'ACCIONES'
        ]"
        :data="veterinarios"
        :acciones="puedeEditar"
        @editar="edita"
        @eliminar="elimina"
      />
    </template>
  </section>
</template>

<script setup>
import { onMounted, ref } from "vue";
import { storeToRefs } from "pinia";
import { useVeterinarioStore } from "../stores/veterinario.js";
import { useAuthStore } from "../stores/auth.js";
import DataTable from "./DataTable.vue";

const veterinarioStore = useVeterinarioStore();
const authStore = useAuthStore();

const { veterinarios } = storeToRefs(veterinarioStore);
const cargando = ref(true);
const error = ref(false);

const emit = defineEmits(["editar"]);

const puedeEditar = [
  "Administrador/a",
  "recepcionista"
].includes(authStore.rol_user);

onMounted(async () => {
  const resultado = await veterinarioStore.getAll();
  error.value = !resultado;
  cargando.value = false;
});

function edita(id) {
  emit("editar", id);
}

async function elimina(id) {
  if (confirm("¿Seguro que querés eliminar este veterinario?")) {
    await veterinarioStore.destroy(id);
  }
}
</script>
