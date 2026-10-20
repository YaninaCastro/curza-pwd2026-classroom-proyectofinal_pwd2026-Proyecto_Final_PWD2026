<template>
  <section>
    <h2>Editar turno</h2>

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

      <p v-if="mensaje">{{ mensaje }}</p>

      <button type="submit" :disabled="cargando">
        {{ cargando ? "Guardando..." : "Guardar cambios" }}
      </button>

      <button type="button" @click="emit('cancelar')">
        Cancelar
      </button>
    </form>
  </section>
</template>


<script setup>
import { reactive, ref, onMounted } from "vue";
import { useTurnoStore } from "../stores/turno.js";
import { useMascotaStore } from "../stores/mascota.js";
import { useVeterinarioStore } from "../stores/veterinario.js";

const props = defineProps({
  id: {
    type: Number,
    required: true,
  },
});

const emit = defineEmits(["actualizado", "cancelar"]);

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

  const correcto = await turnoStore.findOne(props.id);

  if (!correcto || !turnoStore.turno) {
    mensaje.value = "No se pudo cargar el turno.";
    return;
  }

  const turno = turnoStore.turno;

  form.fecha = turno.fecha || "";
  form.hora = turno.hora || "";
  form.mascota_id = turno.mascota?.mascota_id ?? "";
  form.veterinario_id = turno.veterinario?.veterinario_id ?? "";
  form.motivo = turno.motivo || "";
  form.estado = turno.estado || "pendiente";
});

async function guardar() {
  cargando.value = true;
  mensaje.value = "";

  const correcto = await turnoStore.update(props.id, {
    fecha: form.fecha,
    hora: form.hora,
    mascota_id: Number(form.mascota_id),
    veterinario_id: Number(form.veterinario_id),
    motivo: form.motivo.trim(),
    estado: form.estado,
  });

  if (correcto) {
    emit("actualizado");
  } else {
    mensaje.value = turnoStore.errors
      .map(error => error.message || "No se pudo actualizar el turno.")
      .join(" ");
  }

  cargando.value = false;
}
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
