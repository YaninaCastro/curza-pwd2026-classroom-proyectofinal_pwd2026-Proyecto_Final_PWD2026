
const rol_routes = [
  {
    path: "/roles",
    name: "Roles",
    component: () => import("../views/RolView.vue"),
    meta: { requiresAuth: true },
  },
];

export default rol_routes;