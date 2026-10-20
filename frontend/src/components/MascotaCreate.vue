<template>
  <section>
    <h2>Registrar mascota</h2>

    <form @submit.prevent="guardar">
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
        placeholder="Ej.: Perro, gato"
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

      <p v-if="duenos.length === 0">
        No hay dueños registrados. Primero tenés que registrar uno.
      </p>

      <button
        type="submit"
        :disabled="cargando || duenos.length === 0"
      >
        {{ cargando ? "Guardando..." : "Registrar mascota" }}
      </button>

      <p v-if="mensaje">{{ mensaje }}</p>
    </form>
  </section>
</template>

<script setup>
import { reactive, ref, onMounted } from "vue";
import { storeToRefs } from "pinia";
import { useMascotaStore } from "../stores/mascota.js";
import { useDuenoStore } from "../stores/dueno.js";

const mascotaStore = useMascotaStore();
const duenoStore = useDuenoStore();
const { duenos } = storeToRefs(duenoStore);

const cargando = ref(false);
const mensaje = ref("");

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

async function guardar() {
  cargando.value = true;
  mensaje.value = "";

  await mascotaStore.create({
    nombre: form.nombre.trim(),
    especie: form.especie.trim(),
    raza: form.raza.trim(),
    sexo: form.sexo,
    fecha_nto: form.fecha_nto || null,
    dueno_id: Number(form.dueno_id),
  });

  if (mascotaStore.errors.length === 0) {
    mensaje.value = "Mascota registrada.";
    form.nombre = "";
    form.especie = "";
    form.raza = "";
    form.sexo = "";
    form.fecha_nto = "";
    form.dueno_id = "";
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