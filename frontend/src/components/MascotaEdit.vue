<template>
  <section>
    <h2>Editar mascota</h2>

    <p v-if="cargando">Cargando...</p>
    <p v-if="error">{{ error }}</p>

    <form v-if="!cargando && !error" @submit.prevent="guardar">
      <label for="nombre">Nombre</label>
      <input
        id="nombre"
        v-model="form.nombre"
        type="text"
        maxlength="30"
        required
      />

      <label for="especie">Especie</label>
      <input
        id="especie"
        v-model="form.especie"
        type="text"
        maxlength="30"
        required
      />

      <label for="raza">Raza</label>
      <input
        id="raza"
        v-model="form.raza"
        type="text"
        maxlength="50"
        required
      />

      <label for="sexo">Sexo</label>
      <select id="sexo" v-model="form.sexo" required>
        <option value="" disabled>Seleccioná una opción</option>
        <option value="H">H</option>
        <option value="M">M</option>
      </select>

      <label for="fecha_nto">Fecha de nacimiento (opcional)</label>
      <input
        id="fecha_nto"
        v-model="form.fecha_nto"
        type="date"
      />

      <label for="dueno_id">Dueño</label>
      <select id="dueno_id" v-model="form.dueno_id" required>
        <option value="" disabled>Seleccioná un dueño</option>
        <option
          v-for="dueno in duenos"
          :key="dueno.id"
          :value="dueno.id"
        >
          {{ dueno.nombre }} {{ dueno.apellido }} - DNI {{ dueno.dni }}
        </option>
      </select>

      <button type="submit" :disabled="cargando">
        Guardar cambios
      </button>

      <button type="button" @click="emit('cancelar')">
        Cancelar
      </button>

      <p v-if="mensaje">{{ mensaje }}</p>
    </form>
  </section>
</template>

<script setup>
import { reactive, ref, watch, onMounted } from "vue";
import { storeToRefs } from "pinia";
import { useMascotaStore } from "../stores/mascota.js";
import { useDuenoStore } from "../stores/dueno.js";

const props = defineProps({
  id: {
    type: [Number, String],
    required: true,
  },
});

const emit = defineEmits(["actualizado", "cancelar"]);

const mascotaStore = useMascotaStore();
const duenoStore = useDuenoStore();
const { duenos } = storeToRefs(duenoStore);

const cargando = ref(false);
const mensaje = ref("");
const error = ref("");

const form = reactive({
  nombre: "",
  especie: "",
  raza: "",
  sexo: "",
  fecha_nto: "",
  dueno_id: "",
});

onMounted(async () => {
  await duenoStore.getAll();
});

watch(
  () => props.id,
  async (id) => {
    mensaje.value = "";
    error.value = "";
    cargando.value = true;

    const encontrado = await mascotaStore.findOne(id);

    if (encontrado && mascotaStore.mascota) {
      const mascota = mascotaStore.mascota;

      Object.assign(form, {
        nombre: mascota.nombre ?? "",
        especie: mascota.especie ?? "",
        raza: mascota.raza ?? "",
        sexo: mascota.sexo ?? "",
        fecha_nto: mascota.fecha_nto ?? "",
        dueno_id: mascota.dueno_id ?? mascota["dueño"]?.id ?? "",
      });
    } else {
      error.value = "No se pudieron cargar los datos de la mascota.";
    }

    cargando.value = false;
  },
  { immediate: true }
);

async function guardar() {
  cargando.value = true;
  mensaje.value = "";
  error.value = "";

  await mascotaStore.update(props.id, {
    nombre: form.nombre.trim(),
    especie: form.especie.trim(),
    raza: form.raza.trim(),
    sexo: form.sexo,
    fecha_nto: form.fecha_nto || null,
    dueno_id: Number(form.dueno_id),
  });

  if (mascotaStore.errors.length === 0) {
    mensaje.value = "Datos actualizados correctamente.";
    emit("actualizado");
  } else {
    error.value =
      mascotaStore.errors[0]?.message ||
      "No se pudieron actualizar los datos.";
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
