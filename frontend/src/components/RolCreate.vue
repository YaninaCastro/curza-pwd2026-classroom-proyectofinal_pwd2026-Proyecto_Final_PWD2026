<template>
  <section>
    <h3>Crear rol</h3>

    <form @submit.prevent="crear">
      <div class="campo">
        <label for="nombre">Nombre:</label>
        <select id="nombre" v-model="form.nombre" required>
          <option value="" disabled>Seleccioná un rol</option>
          <option value="Administrador/a">Administrador/a</option>
          <option value="recepcionista">Recepcionista</option>
          <option value="veterinario/a">Veterinario/a</option>
        </select>
      </div>

      <div class="campo">
        <label for="activo">Estado:</label>
        <select id="activo" v-model="form.activo" required>
          <option value="S">Activo</option>
          <option value="N">Inactivo</option>
        </select>
      </div>

      <button class="btn-form" type="submit">Crear rol</button>
    </form>
  </section>
</template>

<script setup>
import { reactive } from "vue";
import { useRolStore } from "../stores/rol.js";

const rolStore = useRolStore();

const form = reactive({
  nombre: "",
  activo: "S",
});

async function crear() {
  const creado = await rolStore.create({ ...form });

  if (creado) {
    form.nombre = "";
    form.activo = "S";
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

select {
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