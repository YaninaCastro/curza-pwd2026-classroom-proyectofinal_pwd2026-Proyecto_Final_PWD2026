
import axios from "axios";   //import axios from "axios": importa la herramienta que permite enviar solicitudes HTTP.
import { useAuthStore } from "../stores/auth.js";


export const apiAxios = axios.create({    //export const api: permite importar esta misma instancia desde otros archivos, 
  //sin repetir la configuración/axios.create(...): crea una instancia de Axios con una configuración común.
  baseURL: "http://localhost:5001",  //baseURL: establece la dirección base de tu backend Flask
  timeout: 10000,  //límite de espera de 10 segundos.
  headers: {
    "Content-Type": "application/json", //indica que enviaremos datos en formato JSON cuando corresponda.
  }, //Los headers son encabezados HTTP.
});

// Agrega el access token a las peticiones.
apiAxios.interceptors.request.use((config) => {   //Un interceptor es una función que permite intervenir en una solicitud o respuesta
  //antes de que Axios la procese normalmente.
  //request: indica que queremos interceptar las peticiones, interviene antes de enviar una solicitud.
  //use(): registra una función que Axios ejecutará antes de enviar cada petición.
  //¿Qué es config? Es un objeto que contiene información sobre la petición que Axios está por enviar.
  //config es un parámetro que Axios le entrega automáticamente a la función.
 //No hay que crearlo ni declararlo previamente.
  //ejemplo: apiAxios.get("/usuarios"), Axios prepara internamente un objeto similar a este:
  //{method: "get",
  //url: "/usuarios",
  //baseURL: "http://localhost:5001",
  //headers: {...},
  //timeout: 10000}
  //Se podría llamar de otra manera, ej: apiAxios.interceptors.request.use((solicitud) => {
  const jwt = localStorage.getItem("auth"); //Acá estás buscando en el almacenamiento local del navegador (LocalStorage) un elemento cuya clave sea "auth"
//LocalStorage guarda información en formato texto
//localStorage es una funcionalidad que ya viene incorporada en los navegadores web.
//No se necesitá instalarla, crearla ni importarla
  if (jwt) {
    try {
      const auth = JSON.parse(jwt);
      //JSON.parse() convierte ese texto JSON en un objeto, porque LocalStorage almacena los valores como texto.

      if (auth.jwt) {
        config.headers.Authorization = `Bearer ${auth.jwt}`;
      } //Authorization es un encabezado HTTP que utilizamos para enviar información de autenticación definido por el estándar HTTP
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
      const respuesta = await axios.post(  //¿Por qué axios.post y no apiAxios.post?
        //Porque estamos haciendo una solicitud independiente para renovar el token.
        //Podríamos utilizar apiAxios, pero hay que tener cuidado porque tiene interceptores que podrían volver a ejecutarse.
        //Usar axios.post directamente evita que esta solicitud pase por los interceptores de apiAxios.
        "http://localhost:5001/auth/refresh",
        {},
        {
          timeout: 10000,
          headers: {
            Authorization: `Bearer ${authStore.refresh_token}`,
          }, //esta vez enviamos el refresh token en lugar del access token.
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
Sin esa línea: Axios normalmente establece el encabezado adecuado cuando se envía un objeto JavaScript como JSON. Por eso, 
en muchos casos, la petición seguiría funcionando igual. */
