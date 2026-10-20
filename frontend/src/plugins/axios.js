
import axios from "axios";   //import axios from "axios": importa la herramienta que permite enviar solicitudes HTTP.
import { useAuthStore } from "../stores/auth.js";


export const apiAxios = axios.create({    //export const api: permite importar esta misma instancia desde otros archivos, sin repetir la configuración/axios.create(...): crea una instancia de Axios con una configuración común.
  baseURL: "http://localhost:5001",  //baseURL: establece la dirección base de tu backend Flask
  timeout: 10000,  //límite de espera de 10 segundos.
  headers: {
    "Content-Type": "application/json", //indica que enviaremos datos en formato JSON cuando corresponda.
  },
});

// Agrega el access token a las peticiones.
apiAxios.interceptors.request.use((config) => {
  const jwt = localStorage.getItem("auth");

  if (jwt) {
    try {
      const auth = JSON.parse(jwt);

      if (auth.jwt) {
        config.headers.Authorization = `Bearer ${auth.jwt}`;
      }
    } catch {
      // No se pudo leer la sesión guardada.
    }
  }

  return config;
});

// Renueva el access token si venció.
apiAxios.interceptors.response.use(
  (response) => response,
  async (error) => {
    const peticion = error.config;


    if (
      error.response?.status !== 401 ||
      !peticion ||
      peticion._retry ||
      peticion.url?.includes("/auth/login") ||
      peticion.url?.includes("/auth/refresh")
    ) {
      return Promise.reject(error);
    }

    peticion._retry = true;

    const authStore = useAuthStore();

    if (!authStore.refresh_token) {
      authStore.logout();
      return Promise.reject(error);
    }

    try {
      const respuesta = await axios.post(
        "http://localhost:5001/auth/refresh",
        {},
        {
          timeout: 10000,
          headers: {
            Authorization: `Bearer ${authStore.refresh_token}`,
          },
        }
      );

      const nuevoToken = respuesta.data.access_token;

      // Actualiza el token en Pinia.
      authStore.jwt = nuevoToken;

      // Actualiza el encabezado y repite la petición original.
      peticion.headers.Authorization = `Bearer ${nuevoToken}`;

      return apiAxios(peticion);
    } catch (errorRefresh) {
      authStore.logout();
      return Promise.reject(errorRefresh);
    }
  }
);


/*Con Content-Type: Flask puede interpretar correctamente el cuerpo JSON cuando la petición lo requiere.
Sin esa línea: Axios normalmente establece el encabezado adecuado cuando enviás un objeto JavaScript como JSON. Por eso, 
en muchos casos, la petición seguiría funcionando igual. */