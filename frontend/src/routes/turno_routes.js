import TurnoView from "../views/TurnoView.vue";

const turno_routes = [
  {
    path: "/turnos",
    name: "Turnos",
    component: TurnoView,
    meta: { requiresAuth: true },
  },
];

export default turno_routes;