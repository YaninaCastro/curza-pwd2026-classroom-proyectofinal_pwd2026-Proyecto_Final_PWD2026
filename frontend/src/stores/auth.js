
import AuthServices from "../services/AuthService.js";
import { defineStore } from "pinia";
import { ref } from "vue";

export const useAuthStore = defineStore( //defineStore() permite crear un Store de Pinia.
  "auth", //"auth" es el identificador del Store.
  () => { //La función define los estados y métodos que estarán disponibles.

    //Estados del Store: Cada variable representa un dato que puede ser compartido por los componentes de Vue.
    const auth_user = ref(null);
    const is_authenticated = ref(false);
    const jwt = ref("");
    const refresh_token = ref("");
    const rol_user = ref("");
    const service = new AuthServices();
    const errors = ref([]);
    const status_code = ref(null);


    //Este método recibe los datos ingresados por el usuario y llama al servicio de autenticación.
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

    //Se encarga de cerrar la sesión en el frontend, limpiando los datos almacenados en el Store.
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

//Esta configuración habilita la persistencia del Store mediante pinia-plugin-persistedstate.
//Esto significa que, al recargar la página, los datos del Store pueden recuperarse sin que el 
//usuario tenga que iniciar sesión nuevamente.
//En éste caso, es importante porque permite conservar el estado de autenticación y los tokens entre recargas.
//B. routes/auth_routes.js – Ruta de autenticación
