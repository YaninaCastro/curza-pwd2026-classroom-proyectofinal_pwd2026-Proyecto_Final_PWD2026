<template>
  <section>
    <template v-if="cargando">
      <p>Cargando mascotas...</p>
    </template>

    <template v-else-if="mascotas.length === 0">
      <h3>SIN DATOS</h3>
    </template>

    <template v-else>
      <DataTable
        :headers="[
          'ID',
          'NOMBRE',
          'ESPECIE',
          'RAZA',
          'SEXO',
          'FECHA_NTO',
          'DUEÑO',
          'ACCIONES',
        ]"
        :data="datosTabla"
        :acciones="puedeEditar"
        @editar="edita"
        @eliminar="elimina"
      />
    </template>
  </section>
</template>

<script setup>
import { computed, onMounted, ref } from "vue";
import { storeToRefs } from "pinia";
import { useMascotaStore } from "../stores/mascota.js";
import DataTable from "./DataTable.vue";
import { useAuthStore } from "../stores/auth.js";

const mascotaStore = useMascotaStore();

const authStore = useAuthStore();

const puedeEditar = ["Administrador/a", "recepcionista"].includes(
  authStore.rol_user
);

const { mascotas } = storeToRefs(mascotaStore);
const cargando = ref(true);
const emit = defineEmits(["editar"]);

const datosTabla = computed(() =>
  mascotas.value.map((mascota) => ({
    ...mascota,
    fecha_nto: mascota.fecha_nto
      ? mascota.fecha_nto.split("-").reverse().join("/")
      : "Sin fecha",
    dueño: mascota["dueño"]
      ? `${mascota["dueño"].nombre} ${mascota["dueño"].apellido}`
      : "Sin dueño",
  }))
);

/*...mascota: copia las propiedades de la mascota.
map(): transforma cada elemento de una lista.
computed(): recalcula los datos preparados cuando cambian las mascotas.
Object.keys(): obtiene los nombres de las propiedades de un objeto.
toUpperCase(): permite comparar nombres ignorando diferencias entre mayúsculas y minúsculas */

onMounted(async () => {
  await mascotaStore.getAll();
  cargando.value = false;
});


function edita(id) {
  emit("editar", id);
}

async function elimina(id) {
  if (confirm("¿Seguro que querés eliminar esta mascota?")) {
    await mascotaStore.destroy(id);
  }
}


</script>