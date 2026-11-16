const dueno_routes = [
        {
    path: '/duenos',
    name: 'Duenos',
    component: () => import('../views/DuenoView.vue'),
    meta: { requiresAuth: true},
    }, //Luego, en router/index.js, el beforeEach consulta esa propiedad para decidir si
        //permite la navegación o redirige al usuario al login.
];   //ambos archivos trabajan en conjunto:
//- dueno_routes.js indica que la ruta está protegida.
//- router/index.js comprueba si el usuario está autenticado.

export default dueno_routes
