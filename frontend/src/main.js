
import { createApp } from 'vue'
import './style.css' //import './style.css': carga los estilos globales
import App from './App.vue'
import { createPinia } from 'pinia'
import piniaPluginPersistedstate from "pinia-plugin-persistedstate";
import router from './routes'

const pinia = createPinia();
pinia.use(piniaPluginPersistedstate); 
const app = createApp(App) //crea la aplicación Vue usando App.vue como componente principal.


  app.use(pinia) //habilita Pinia para compartir estado entre componentes, por ejemplo, los datos del usuario que inició sesión
  app.use(router) //conecta Vue Router para navegar entre páginas sin recargar todo el sitio.
  app.mount('#app') // 

