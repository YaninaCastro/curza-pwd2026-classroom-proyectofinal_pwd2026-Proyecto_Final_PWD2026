<template>
  <section>
    <h2>Registrar turno</h2>

    <form @submit.prevent="guardar">
      <label for="fecha">Fecha</label>
      <input
        id="fecha"
        v-model="form.fecha"
        type="date"
        required
      />

      <label for="hora">Hora</label>
      <input
        id="hora"
        v-model="form.hora"
        type="time"
        required
      />

      <label for="mascota">Mascota</label>
      <select id="mascota" v-model="form.mascota_id" required>
        <option value="" disabled>Seleccioná una mascota</option>
        <option
          v-for="mascota in mascotaStore.mascotas"
          :key="mascota.id"
          :value="mascota.id"
        >
          {{ mascota.nombre }} — {{ mascota.especie }}
          ({{ mascota.dueño?.apellido }})
        </option>
      </select>

      <label for="veterinario">Veterinario</label>
      <select
        id="veterinario"
        v-model="form.veterinario_id"
        required
      >
        <option value="" disabled>Seleccioná un veterinario</option>
        <option
          v-for="veterinario in veterinarioStore.veterinarios"
          :key="veterinario.id"
          :value="veterinario.id"
        >
          {{ veterinario.nombre }} {{ veterinario.apellido }}
        </option>
      </select>

      <label for="motivo">Motivo</label>
      <input
        id="motivo"
        v-model="form.motivo"
        type="text"
        maxlength="200"
        required
      />

      <label for="estado">Estado</label>
      <select id="estado" v-model="form.estado" required>
        <option value="pendiente">Pendiente</option>
        <option value="cancelado">Cancelado</option>
        <option value="atendido">Atendido</option>
      </select>

      <button type="submit" :disabled="cargando">
        {{ cargando ? "Guardando..." : "Registrar turno" }}
      </button>

      <p v-if="mensaje">{{ mensaje }}</p>
    </form>
  </section>
</template>


<script setup>
import { reactive, ref, onMounted } from "vue";
import { useTurnoStore } from "../stores/turno.js";
import { useMascotaStore } from "../stores/mascota.js";
import { useVeterinarioStore } from "../stores/veterinario.js";

const turnoStore = useTurnoStore();
const mascotaStore = useMascotaStore();
const veterinarioStore = useVeterinarioStore();

const cargando = ref(false);
const mensaje = ref("");

const form = reactive({
  fecha: "",
  hora: "",
  mascota_id: "",
  veterinario_id: "",
  motivo: "",
  estado: "pendiente",
});

onMounted(async () => {
  await mascotaStore.getAll();
  await veterinarioStore.getAll();
});

async function guardar() {
  cargando.value = true;
  mensaje.value = "";

  await turnoStore.create({
    fecha: form.fecha,
    hora: form.hora,
    mascota_id: Number(form.mascota_id),
    veterinario_id: Number(form.veterinario_id),
    motivo: form.motivo.trim(),
    estado: form.estado,
  });

  if (turnoStore.errors.length === 0) {
    mensaje.value = "Turno registrado.";
    form.fecha = "";
    form.hora = "";
    form.mascota_id = "";
    form.veterinario_id = "";
    form.motivo = "";
    form.estado = "pendiente";
  } else {
    mensaje.value = turnoStore.errors
      .map(error => error.message || "Error al registrar el turno.")
      .join(" ");
  }

  cargando.value = false;
}

/*onMounted() carga las mascotas y los veterinarios al abrir el formulario.
Los selectores muestran nombres, pero guardan los IDs necesarios para las relaciones de la base de datos.
Number() convierte los IDs seleccionados a números.
required evita enviar campos vacíos desde el formulario.
guardar() llama al store, muestra el resultado y limpia los campos si salió bien. */

</script>

<style scoped>
section {
  max-width: 450px;
  margin: 24px auto;
}

form {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

input,
select {
  padding: 9px;
  margin-bottom: 8px;
}

button {
  padding: 10px;
  cursor: pointer;
}
</style>