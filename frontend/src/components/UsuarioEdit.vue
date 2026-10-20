<template>
  <section>
    <h2>Editar usuario</h2>

    <p v-if="cargando">Cargando...</p>
    <p v-if="error">{{ error }}</p>

    <form v-if="!cargando && !error" @submit.prevent="guardar">
      <label for="usuario">Nombre de usuario</label>
      <input
        id="usuario"
        v-model="form.usuario"
        type="text"
        maxlength="50"
        required
      />

      <label for="password">Nueva contraseña (opcional)</label>
      <input
        id="password"
        v-model="form.password"
        type="password"
        minlength="8"
        autocomplete="new-password"
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

      <label for="email">Email</label>
      <input
        id="email"
        v-model="form.email"
        type="email"
        maxlength="200"
        required
      />

      <label for="rol">Rol</label>
      <select id="rol" v-model="form.rol_id" required>
        <option value="" disabled>Seleccioná un rol</option>
        <option
          v-for="rol in rolStore.roles"
          :key="rol.id"
          :value="rol.id"
        >
          {{ rol.nombre }}
        </option>
      </select>

      <button type="submit" :disabled="cargando">
        Guardar cambios
      </button>

      <button type="button" @click="emit('cancelar')">
        Cancelar
      </button>
    </form>
  </section>
</template>

<script setup>
import { reactive, ref, watch, onMounted } from "vue";
import { useUsuarioStore } from "../stores/usuario.js";
import { useRolStore } from "../stores/rol.js";

const props = defineProps({
  id: {
    type: [Number, String],
    required: true,
  },
});

const emit = defineEmits(["actualizado", "cancelar"]);

const usuarioStore = useUsuarioStore();
const rolStore = useRolStore();

const cargando = ref(false);
const error = ref("");
const mensaje = ref("");

const form = reactive({
  usuario: "",
  password: "",
  nombre: "",
  apellido: "",
  email: "",
  rol_id: "",
});

onMounted(async () => {
  await rolStore.getAll();
});

watch(
  () => props.id,
  async (id) => {
    cargando.value = true;
    error.value = "";
    mensaje.value = "";

    const encontrado = await usuarioStore.findOne(id);

    if (encontrado && usuarioStore.usuario) {
      const datos = usuarioStore.usuario;

      Object.assign(form, {
        usuario: datos.usuario ?? "",
        password: "",
        nombre: datos.nombre ?? "",
        apellido: datos.apellido ?? "",
        email: datos.email ?? "",
        rol_id: datos.rol?.id_rol ?? datos.rol_id ?? "",
      });
    } else {
      error.value = "No se pudieron cargar los datos del usuario.";
    }

    cargando.value = false;
  },
  { immediate: true }
);

async function guardar() {
  cargando.value = true;
  error.value = "";
  mensaje.value = "";

  const datos = {
    usuario: form.usuario.trim(),
    nombre: form.nombre.trim(),
    apellido: form.apellido.trim(),
    email: form.email.trim(),
    rol_id: Number(form.rol_id),
  };

  if (form.password.trim()) {
    datos.password = form.password;
  }

  const correcto = await usuarioStore.update(props.id, datos);

  if (correcto) {
    mensaje.value = "Datos actualizados correctamente.";
    emit("actualizado");
  } else {
    error.value =
      usuarioStore.errors[0]?.message ||
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