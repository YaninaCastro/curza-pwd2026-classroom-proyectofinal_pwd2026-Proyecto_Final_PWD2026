<template>
  <section>
    <template v-if="cargando">
      <p>Cargando roles...</p>
    </template>

    <template v-else-if="roles.length === 0">
      <h3>SIN DATOS</h3>
    </template>

    <template v-else>
      <DataTable
        :headers="['ID', 'NOMBRE', 'ACTIVO', 'ACCIONES']"
        :data="roles"
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
import { useRolStore } from "../stores/rol.js";
import DataTable from "./DataTable.vue";
import { useAuthStore } from "../stores/auth.js";

const rolStore = useRolStore();
const authStore = useAuthStore();
const { roles } = storeToRefs(rolStore);
const cargando = ref(true);
const emit = defineEmits(["editar"]);

const puedeEditar = authStore.rol_user === "Administrador/a";

onMounted(async () => {
  await rolStore.getAll();
  cargando.value = false;
});

function edita(id) {
  emit("editar", id);
}

async function elimina(id) {
  if (confirm("¿Seguro que querés eliminar este rol?")) {
    await rolStore.destroy(id);
  }
}
</script>