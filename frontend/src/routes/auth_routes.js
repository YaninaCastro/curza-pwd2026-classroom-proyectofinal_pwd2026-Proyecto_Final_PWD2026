const auth_routes = [
    {
        path: '/login',
        name: 'Login', 
        component: () => import('../views/LoginView.vue')  //component: () => import(...): carga la vista cuando se necesita, en lugar de cargar todas las páginas de entrada.
    },
];

export default auth_routes;