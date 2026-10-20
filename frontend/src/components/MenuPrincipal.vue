
<template>
  <main class="menu-principal">
    <h1>Clínica Veterinaria</h1>

    <p>Bienvenido/a, {{ authStore.auth_user }}</p>
    <p>Rol: {{ authStore.rol_user }}</p>

    <h2>Menú principal</h2>

    <nav>
      <RouterLink
        v-for="opcion in opciones"
        :key="opcion.path"
        :to="opcion.path"
        class="menu-boton"
      >
        {{ opcion.name }}
      </RouterLink>
    </nav>
  </main>
</template>

<script setup>
import { computed } from "vue";
import { RouterLink } from "vue-router";
import { useAuthStore } from "../stores/auth";
import { navegacion } from "../routes/navegacion";

const authStore = useAuthStore();

const opciones = computed(() =>
  navegacion.filter((opcion) =>
    opcion.rol_access.includes(authStore.rol_user)
  )
);
</script>

<style scoped>
.menu-principal {
  max-width: 900px;
  margin: 40px auto;
  padding: 24px;
}

nav {
  display: flex;
  flex-wrap: wrap;
  gap: 16px;
  margin-top: 24px;
}

.menu-boton {
  padding: 16px 24px;
  border-radius: 8px;
  background: #438ee4;
  color: white;
  text-decoration: none;
}

.menu-boton:hover {
  background: #357abd;
}
</style>
