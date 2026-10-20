const dueno_routes = [
        {
    path: '/duenos',
    name: 'Duenos',
    component: () => import('../views/DuenoView.vue'),
    meta: { requiresAuth: true},
    },
];

export default dueno_routes