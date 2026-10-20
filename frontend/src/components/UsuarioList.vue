<template>
  <section>
    <h2>Usuarios registrados</h2>

    <p v-if="cargando">Cargando usuarios...</p>
    <p v-if="error">{{ error }}</p>

    <table v-if="!cargando && usuarioStore.usuarios.length">
      <thead>
        <tr>
          <th>Usuario</th>
          <th>Nombre</th>
          <th>Apellido</th>
          <th>Email</th>
          <th>Rol</th>
          <th v-if="puedeEditar">Acciones</th>
        </tr>
      </thead>

      <tbody>
        <tr v-for="usuario in usuarioStore.usuarios" :key="usuario.id_usuario">
          <td>{{ usuario.usuario }}</td>
          <td>{{ usuario.nombre }}</td>
          <td>{{ usuario.apellido }}</td>
          <td>{{ usuario.email }}</td>
          <td>{{ usuario.rol?.nombre_rol ?? "Sin rol" }}</td>
          <td v-if="puedeEditar">
            <button type="button" @click="emit('editar', usuario.id_usuario)">
              Editar
            </button>
            <button type="button" @click="eliminar(usuario.id_usuario)">
              Eliminar
            </button>
          </td>
        </tr>
      </tbody>
    </table>

    <p v-else-if="!cargando && !error && usuarioStore.usuarios.length === 0">
        No hay usuarios registrados.
    </p>
  </section>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useUsuarioStore } from "../stores/usuario.js";
import { useAuthStore } from "../stores/auth.js";

const emit = defineEmits(["editar"]);

const usuarioStore = useUsuarioStore();
const authStore = useAuthStore();

const cargando = ref(false);
const error = ref("");

const puedeEditar = authStore.rol_user === "Administrador/a";

async function cargar() {
  cargando.value = true;
  error.value = "";

  const correcto = await usuarioStore.getAll();

  if (!correcto) {
    const status = usuarioStore.errors[0]?.status;

    if (status === 401) {
      error.value = "Tu sesión no es válida. Iniciá sesión nuevamente.";
    } else if (status === 403) {
      error.value = "No tenés permisos para consultar los usuarios.";
    } else {
      error.value = "No se pudieron cargar los usuarios.";
    }
  }

  cargando.value = false;
}

async function eliminar(id) {
  if (!confirm("¿Seguro que querés eliminar este usuario?")) return;

  const correcto = await usuarioStore.destroy(id);

  if (!correcto) {
    error.value =
      usuarioStore.errors[0]?.message || "No se pudo eliminar el usuario.";
  }
}

onMounted(cargar);
</script>

<style scoped>
section {
  margin: 24px auto;
  max-width: 1000px;
  overflow-x: auto;
}

table {
  width: 100%;
  border-collapse: collapse;
}

th,
td {
  padding: 10px;
  border: 1px solid #ddd;
  text-align: left;
}

button {
  padding: 7px 10px;
  margin: 2px;
  cursor: pointer;
}
</style>