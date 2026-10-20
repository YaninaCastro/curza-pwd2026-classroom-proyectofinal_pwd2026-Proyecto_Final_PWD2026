<template>
  <section>
    <h2>Registrar dueño</h2>

    <form @submit.prevent="guardar">
      <label for="dni">DNI</label>
      <input
        id="dni"
        v-model="form.dni"
        type="text"
        maxlength="8"
        pattern="[0-9]{7,8}"
        title="Ingresá un DNI de 7 u 8 números"
        required
      />

      <label for="nombre">Nombre</label>
      <input
        id="nombre"
        v-model="form.nombre"
        type="text"
        maxlength="30"
        required
      />

      <label for="apellido">Apellido</label>
      <input
        id="apellido"
        v-model="form.apellido"
        type="text"
        maxlength="30"
        required
      />

      <label for="telefono">Teléfono</label>
      <input
        id="telefono"
        v-model="form.telefono"
        type="tel"
        maxlength="20"
        required
      />

      <label for="email">Email (opcional)</label>
      <input
        id="email"
        v-model="form.email"
        type="email"
        maxlength="50"
      />

      <button type="submit" :disabled="cargando">
        {{ cargando ? "Guardando..." : "Registrar dueño" }}
      </button>

      <p v-if="mensaje">{{ mensaje }}</p>
    </form>
  </section>
</template>

<script setup>
import { reactive, ref } from "vue";
import { useDuenoStore } from "../stores/dueno.js";

const duenoStore = useDuenoStore();
const cargando = ref(false);
const mensaje = ref("");

const form = reactive({
  dni: "",
  nombre: "",
  apellido: "",
  telefono: "",
  email: "",
});

async function guardar() {
  cargando.value = true;
  mensaje.value = "";

  await duenoStore.create({
    dni: form.dni,
    nombre: form.nombre.trim(),
    apellido: form.apellido.trim(),
    telefono: form.telefono.trim(),
    email: form.email.trim() || null,
  });

  if (duenoStore.errors.length === 0) {
    mensaje.value = "Dueño registrado.";
    form.dni = "";
    form.nombre = "";
    form.apellido = "";
    form.telefono = "";
    form.email = "";
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

input {
  padding: 9px;
  margin-bottom: 8px;
}

button {
  padding: 10px;
  cursor: pointer;
}
</style>