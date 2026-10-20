<template>
  <section>
    <h2>Listado de turnos</h2>

    <p v-if="mensaje">{{ mensaje }}</p>

    <DataTable
      :headers="headers"
      :data="turnosTabla"
      :acciones="puedeModificar"
      :estado-editable="puedeModificar"
      @editar="emit('editar', $event)"
      @eliminar="eliminar"
      @cambiar-estado="cambiarEstado"
    />
  </section>
</template>


<script setup>
import { computed, onMounted, ref } from "vue";
import DataTable from "./DataTable.vue";
import { useTurnoStore } from "../stores/turno.js";
import { useAuthStore } from "../stores/auth.js";

const emit = defineEmits(["editar"]);

const turnoStore = useTurnoStore();
const authStore = useAuthStore();

const mensaje = ref("");

const puedeModificar = ["Administrador/a", "recepcionista"].includes(
  authStore.rol_user
);

const headers = [
  "ID",
  "FECHA",
  "HORA",
  "MASCOTA",
  "VETERINARIO",
  "MOTIVO",
  "ESTADO",
  "CAMBIAR ESTADO",
  "ACCIONES",
];

const turnosTabla = computed(() =>
  turnoStore.turnos.map((turno) => ({
    id: turno.id,
    fecha: turno.fecha.split("-").reverse().join("/"),
    hora: turno.hora,
    mascota: turno.mascota?.nombre || "",
    veterinario: turno.veterinario
      ? `${turno.veterinario.nombre} ${turno.veterinario.apellido}`
      : "",
    motivo: turno.motivo,
    estado: turno.estado,
  }))
);

async function cambiarEstado(id, estado) {
  mensaje.value = "";

  const correcto = await turnoStore.update(id, { estado });

  if (correcto) {
    mensaje.value = "Estado del turno actualizado.";
  } else {
    mensaje.value = turnoStore.errors
      .map(error => error.message || "No se pudo cambiar el estado.")
      .join(" ");
  }
}


onMounted(async () => {
  const correcto = await turnoStore.getAll();

  if (!correcto) {
    mensaje.value = "No se pudieron cargar los turnos.";
  } else if (turnoStore.turnos.length === 0) {
    mensaje.value = "No hay turnos registrados.";
  }
});

async function eliminar(id) {
  const confirmar = window.confirm(
    "¿Estás seguro de que querés eliminar este turno?"
  );

  if (!confirmar) return;

  const correcto = await turnoStore.destroy(id);

  if (correcto) {
    mensaje.value = turnoStore.turnos.length === 0
      ? "Turno eliminado. No hay turnos registrados."
      : "Turno eliminado correctamente.";
  } else {
    mensaje.value = turnoStore.errors
      .map(error => error.message || "No se pudo eliminar el turno.")
      .join(" ");
  }
}
</script>
