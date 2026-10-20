<template>
  <section>
    <h3>Registrar veterinario/a</h3>

    <form @submit.prevent="crear">
      <div class="campo">
        <label for="nombre">Nombre:</label>
        <input id="nombre" v-model.trim="form.nombre" required maxlength="30" />
      </div>

      <div class="campo">
        <label for="apellido">Apellido:</label>
        <input id="apellido" v-model.trim="form.apellido" required maxlength="30" />
      </div>

      <div class="campo">
        <label for="telefono">Teléfono:</label>
        <input id="telefono" v-model.trim="form.telefono" required maxlength="20" />
      </div>

      <div class="campo">
        <label for="email">Email:</label>
        <input id="email" type="email" v-model.trim="form.email" required maxlength="120" />
      </div>

      <div class="campo">
        <label for="matricula">Matrícula:</label>
        <input id="matricula" v-model.trim="form.matricula" required maxlength="20" />
      </div>

      <div class="campo">
        <label for="especialidad">Especialidad:</label>
        <input id="especialidad" v-model.trim="form.especialidad" required maxlength="120" />
      </div>

      <button class="btn-form" type="submit">Registrar veterinario</button>
    </form>
  </section>
</template>

<script setup>
import { reactive } from "vue";
import { useVeterinarioStore } from "../stores/veterinario.js";

const veterinarioStore = useVeterinarioStore();

const form = reactive({
  nombre: "",
  apellido: "",
  telefono: "",
  email: "",
  matricula: "",
  especialidad: "",
});

async function crear() {
  const creado = await veterinarioStore.create({ ...form });

  if (creado) {
    form.nombre = "";
    form.apellido = "";
    form.telefono = "";
    form.email = "";
    form.matricula = "";
    form.especialidad = "";
  }
}
</script>

<style scoped>
section {
  margin: 20px 0;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 8px;
}

.campo {
  display: flex;
  flex-direction: column;
  gap: 6px;
  margin-bottom: 16px;
  max-width: 400px;
}

input {
  padding: 9px;
  border: 1px solid #bbb;
  border-radius: 5px;
  width: 100%;
  box-sizing: border-box;
}

.btn-form {
  margin: 6px 8px 6px 0;
  padding: 9px 14px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}
</style>