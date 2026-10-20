<template>
  <section>
    <template v-if="cargando">
      <p>Cargando dueños...</p>
    </template>

    <template v-else-if="duenos.length === 0">
      <h3>SIN DATOS</h3>
    </template>

    <template v-else>
      <DataTable
        :headers="[
          'ID',
          'DNI',
          'NOMBRE',
          'APELLIDO',
          'TELEFONO',
          'EMAIL',
          'ACCIONES',
        ]"
        :data="duenos"
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
import { useDuenoStore } from "../stores/dueno.js";
import DataTable from "./DataTable.vue";
import { useAuthStore } from "../stores/auth.js";


const duenoStore = useDuenoStore();
const authStore = useAuthStore();
const { duenos } = storeToRefs(duenoStore); //storeToRefs() mantiene reactiva la lista guardada en Pinia.
const cargando = ref(true);
const emit = defineEmits(["editar"]);
const puedeEditar = ["Administrador/a", "recepcionista"].includes(
  authStore.rol_user
);

onMounted(async () => { //onMounted() carga los dueños cuando se muestra el componente.
  await duenoStore.getAll();
  cargando.value = false;
});

function edita(id) {
  emit("editar", id); //edita(id) por ahora muestra el ID en la consola; después lo conectamos con el formulario de edición
}

async function elimina(id) { //elimina(id) pide confirmación antes de llamar al store.
  if (confirm("¿Seguro que querés eliminar este dueño?")) {
    await duenoStore.destroy(id);
  }
}
</script>

//DataTable muestra las columnas y emite los eventos de edición y eliminación.