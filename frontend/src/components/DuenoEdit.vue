<template>
  <section>
    <h2>Editar dueño</h2>

    <p v-if="cargando">Cargando...</p>
    <p v-if="error">{{ error }}</p>

    <form v-if="!cargando && !error" @submit.prevent="guardar">
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
import { reactive, ref, watch } from "vue";
import { useDuenoStore } from "../stores/dueno.js";

const props = defineProps({
  id: {       //Recibe el id del dueño que se quiere editar.
    type: [Number, String],
    required: true,
  },
});

const emit = defineEmits(["actualizado", "cancelar"]);

const duenoStore = useDuenoStore();
const cargando = ref(false);
const mensaje = ref("");
const error = ref("");

const form = reactive({
  dni: "",
  nombre: "",
  apellido: "",
  telefono: "",
  email: "",
});

watch(                           //watch() observa ese ID y llama a findOne() para cargar los datos
  () => props.id,
  async (id) => {
    mensaje.value = "";
    error.value = "";
    cargando.value = true;

    const encontrado = await duenoStore.findOne(id);

    if (encontrado && duenoStore.dueno) {
      Object.assign(form, {               //Object.assign() coloca los datos recibidos en el formulario
        dni: duenoStore.dueno.dni ?? "",  //Al guardar, llama a duenoStore.update(id, datos).
        nombre: duenoStore.dueno.nombre ?? "",
        apellido: duenoStore.dueno.apellido ?? "",
        telefono: duenoStore.dueno.telefono ?? "",
        email: duenoStore.dueno.email ?? "",
      });
    } else {
      error.value = "No se pudieron cargar los datos del dueño.";
    }

    cargando.value = false;
  },
  { immediate: true }
);

async function guardar() {
  cargando.value = true;
  mensaje.value = "";
  error.value = "";

  await duenoStore.update(props.id, {
    dni: form.dni,
    nombre: form.nombre.trim(),
    apellido: form.apellido.trim(),
    telefono: form.telefono.trim(),
    email: form.email.trim() || null,
  });

  if (duenoStore.errors.length === 0) {
    mensaje.value = "Datos actualizados correctamente.";
    emit("actualizado");     //Emite actualizado o cancelar para que el componente padre decida qué mostrar
  } else {
    error.value =
      duenoStore.errors[0]?.message || "No se pudieron actualizar los datos.";
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