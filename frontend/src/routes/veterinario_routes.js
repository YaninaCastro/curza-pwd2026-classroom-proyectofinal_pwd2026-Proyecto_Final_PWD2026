const veterinario_routes = [
  {
    path: "/veterinarios",
    name: "Veterinarios",
    component: () => import("../views/VeterinarioView.vue"),
    meta: { requiresAuth: true },
  },
];

export default veterinario_routes;
