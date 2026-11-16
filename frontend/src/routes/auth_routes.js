//Este archivo define la ruta correspondiente al inicio de sesión.
const auth_routes = [
    {
        path: '/login',
        name: 'Login', 
        component: () => import('../views/LoginView.vue')  //component: () => import(...): carga la vista cuando se necesita, en lugar de cargar todas las páginas de entrada.
    }, //Esto se denomina lazy loading o carga diferida.
//Significa que el componente se importa cuando se necesita, en lugar de cargarlo junto con todos 
//los demás componentes al iniciar la aplicación
];

export default auth_routes;
