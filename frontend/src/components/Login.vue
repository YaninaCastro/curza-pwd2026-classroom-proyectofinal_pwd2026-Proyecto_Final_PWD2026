<template>
  <main class="login-container">
    <section class="login-card">
      <h1>Clínica Veterinaria</h1>
      <p class="login-subtitle">Ingresá a tu cuenta</p>

      <form @submit.prevent="iniciarSesion">
        <label for="usuario">Usuario</label>
        <input
          id="usuario"
          v-model="user.usuario"
          type="text"
          placeholder="Ingresá tu usuario"
          autocomplete="username"
          required
        />

        <label for="password">Contraseña</label>
        <input
          id="password"
          v-model="user.password"
          type="password"
          placeholder="Ingresá tu contraseña"
          autocomplete="current-password"
          required
        />

        <p v-if="error" class="error-message">{{ error }}</p>
        <p v-if="mensaje" class="success-message">{{ mensaje }}</p>

        <button type="submit" :disabled="cargando">
          {{ cargando ? 'Ingresando...' : 'Iniciar sesión' }}
        </button>
      </form>
    </section>
  </main>
</template>


<script setup>
import { reactive, ref } from 'vue'
import { useAuthStore } from '../stores/auth'
import { storeToRefs } from 'pinia'
import { useRouter } from "vue-router";

const authStore = useAuthStore()
const { is_authenticated } = storeToRefs(authStore)
const router = useRouter();

const user = reactive({
  usuario: '',
  password: '',
})

const error = ref('')
const mensaje = ref('')
const cargando = ref(false)

async function iniciarSesion() {
  error.value = ''
  mensaje.value = ''
  cargando.value = true

  try {
    const success = await authStore.login(user)

    if (success && is_authenticated.value) {
      await router.push({ name: "Home" });
    } else {
      error.value =
        authStore.errors[0]?.message ||
        "Usuario o contraseña incorrectos.";
    }
  } finally {
    cargando.value = false
  }
}
</script>

<style scoped>
.login-container {
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 24px;
}

.login-card {
  width: 100%;
  max-width: 400px;
  padding: 32px;
  background: white;
  border-radius: 12px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
}

h1 {
  margin: 0;
  text-align: center;
  font-size: 26px;
}

.login-subtitle {
  margin-bottom: 28px;
  color: #64748b;
  text-align: center;
}

form {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

input {
  width: 100%;
  padding: 12px;
  margin-bottom: 10px;
  border: 1px solid #cbd5e1;
  border-radius: 6px;
}

button {
  padding: 12px;
  border: none;
  border-radius: 6px;
  background: #438ee4;
  color: white;
  cursor: pointer;
}

button:hover {
  background: #357abd;
}

button:disabled {
  opacity: 0.7;
  cursor: not-allowed;
}

.error-message {
  color: #b91c1c;
  font-size: 14px;
}

.success-message {
  color: #287a62;
  font-size: 14px;
}
</style>
