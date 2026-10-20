const mascota_routes = [
    {
  path: '/mascotas',
  name: 'Mascotas',
  component: () => import('../views/MascotaView.vue'),
  meta: { requiresAuth: true}, //Esto indica que el usuario debe tener una sesión iniciada para entrar
},
];

export default mascota_routes