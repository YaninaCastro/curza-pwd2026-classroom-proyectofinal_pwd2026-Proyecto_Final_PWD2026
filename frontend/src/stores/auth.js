
import AuthServices from "../services/AuthService.js";
import { defineStore } from "pinia";
import { ref } from "vue";

export const useAuthStore = defineStore(
  "auth",
  () => {
    const auth_user = ref(null);
    const is_authenticated = ref(false);
    const jwt = ref("");
    const refresh_token = ref("");
    const rol_user = ref("");
    const service = new AuthServices();
    const errors = ref([]);
    const status_code = ref(null);

    async function login(user) {
      errors.value = [];
      const success = await service.login(user);

      if (!success) {
        errors.value = service.errors;
        is_authenticated.value = false;
        return false;
      }

      auth_user.value = service.auth_user.nombre;
      is_authenticated.value = service.auth_user.authenticated;
      jwt.value = service.auth_user.jwt;
      refresh_token.value = service.auth_user.refresh_token;
      rol_user.value = service.auth_user.rol;

      return true;
    }

    function logout() {
      auth_user.value = null;
      is_authenticated.value = false;
      jwt.value = "";
      refresh_token.value = "";
      rol_user.value = "";
      errors.value = [];
    }

    return {
      auth_user,
      is_authenticated,
      jwt,
      refresh_token,
      rol_user,
      errors,
      status_code,
      login,
      logout,
    };
  },
  { persist: true },
);
