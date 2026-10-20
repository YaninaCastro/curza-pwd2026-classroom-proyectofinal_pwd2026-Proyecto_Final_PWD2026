const usuario_routes = [
  {
    path: "/usuarios",
    name: "Usuarios",
    component: () => import("../views/UsuarioView.vue"),
    meta: { requiresAuth: true },
  },
];

export default usuario_routes;