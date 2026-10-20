<template>
  <section>
    <h2>Registrar usuario</h2>

    <p v-if="error">{{ error }}</p>
    <p v-if="mensaje">{{ mensaje }}</p>

    <form @submit.prevent="guardar">
      <label for="usuario">Nombre de usuario</label>
      <input
        id="usuario"
        v-model="form.usuario"
        type="text"
        maxlength="50"
        required
      />

      <label for="password">Contraseña</label>
      <input
        id="password"
        v-model="form.password"
        type="password"
        minlength="8"
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

      <button type="submit" :disabled="cargando || rolStore.roles.length === 0">
        {{ cargando ? "Guardando..." : "Registrar usuario" }}
      </button>
    </form>
  </section>
</template>

<script setup>
import { reactive, ref, onMounted } from "vue";
import { useUsuarioStore } from "../stores/usuario.js";
import { useRolStore } from "../stores/rol.js";

const usuarioStore = useUsuarioStore();
const rolStore = useRolStore();

const cargando = ref(false);
const mensaje = ref("");
const error = ref("");

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

async function guardar() {
  cargando.value = true;
  mensaje.value = "";
  error.value = "";

  const correcto = await usuarioStore.create({
    usuario: form.usuario.trim(),
    password: form.password,
    nombre: form.nombre.trim(),
    apellido: form.apellido.trim(),
    email: form.email.trim(),
    rol_id: Number(form.rol_id),
  });

  if (correcto) {
    mensaje.value = "Usuario registrado.";
    Object.assign(form, {
      usuario: "",
      password: "",
      nombre: "",
      apellido: "",
      email: "",
      rol_id: "",
    });
  } else {
    error.value =
      usuarioStore.errors[0]?.message || "No se pudo registrar el usuario.";
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