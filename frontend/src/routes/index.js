
import { createRouter, createWebHistory} from 'vue-router'
//createRouter: crea el sistema de navegación. createWebHistory(): permite usar URLs normales, como /login.
import { useAuthStore } from '../stores/auth';
import auth_routes from "./auth_routes";
import dueno_routes from "./dueno_routes";
import mascota_routes from "./mascota_routes";
import usuario_routes from "./usuario_routes";
import rol_routes from "./rol_routes";
import veterinario_routes from './veterinario_routes';
import turno_routes from './turno_routes';
import HomeView from "../views/HomeView.vue";

const routes= [
    {
        path: '/',
        redirect: 'login',  //redirect: '/login': si alguien entra a la página inicial /, lo redirige al inicio de sesión.
    },

    {
        path: "/home",
        name: "Home",
        component: HomeView,
        meta: { requiresAuth: true },
    },

    ...auth_routes,
    ...dueno_routes,
    ...mascota_routes,
    ...usuario_routes,
    ...rol_routes,
    ...veterinario_routes,
    ...turno_routes,
];

const router = createRouter({
  history: createWebHistory(),
  routes,
})

router.beforeEach((to) => {
  const authStore = useAuthStore();

  if (to.meta.requiresAuth && !authStore.is_authenticated) {
    return { name: "Login" };
  }

  return true;
});

export default router

//routes: contiene las rutas disponibles y qué componente muestra cada una.



