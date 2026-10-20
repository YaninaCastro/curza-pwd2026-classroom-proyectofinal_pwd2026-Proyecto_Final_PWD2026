<template>
  <section>
    <h3>Editar veterinario/a</h3>

    <p v-if="cargando">Cargando veterinario...</p>
    <p v-else-if="errorCarga">No se pudo cargar el veterinario.</p>

    <form v-else @submit.prevent="guardar">
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

      <button class="btn-form" type="submit">Guardar cambios</button>
      <button class="btn-form" type="button" @click="$emit('cancelar')">
        Cancelar
      </button>
    </form>
  </section>
</template>

<script setup>
import { onMounted, reactive, ref } from "vue";
import { useVeterinarioStore } from "../stores/veterinario.js";

const props = defineProps({
  id: {
    type: [Number, String],
    required: true,
  },
});

const emit = defineEmits(["actualizado", "cancelar"]);
const veterinarioStore = useVeterinarioStore();

const cargando = ref(true);
const errorCarga = ref(false);

const form = reactive({
  nombre: "",
  apellido: "",
  telefono: "",
  email: "",
  matricula: "",
  especialidad: "",
});

onMounted(async () => {
  const encontrado = await veterinarioStore.findOne(props.id);

  if (encontrado && veterinarioStore.veterinario) {
    Object.assign(form, veterinarioStore.veterinario);
  } else {
    errorCarga.value = true;
  }

  cargando.value = false;
});

async function guardar() {
  const actualizado = await veterinarioStore.update(props.id, { ...form });

  if (actualizado) {
    emit("actualizado");
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
