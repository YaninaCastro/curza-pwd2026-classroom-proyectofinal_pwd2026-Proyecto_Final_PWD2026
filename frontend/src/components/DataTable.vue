<template>
  <section>
    <table>
      <thead>
        <tr>
        <th v-for="head in headers" :key="head"  
          v-if="head !== 'CAMBIAR ESTADO' || estadoEditable">{{ head }}</th>
        </tr>
      </thead>

      <tbody>
        <tr v-for="row in items" :key="row.id">
          <td v-for="(cell, index) in row.cells" :key="index">
            {{ cell }}
          </td>
          <td v-if="estadoEditable">
            <select
              :value="row.estado"
              @change="$emit('cambiar-estado', row.id, $event.target.value)"
              >
              <option value="pendiente">Pendiente</option>
              <option value="atendido">Atendido</option>
              <option value="cancelado">Cancelado</option>
            </select>
          </td>
          <td v-if="acciones">
            <button class="btn btn-primary" @click="$emit('editar', row.id)">
              <mdicon name="pencil"></mdicon> Editar
            </button>
            <button class="btn btn-danger" @click="$emit('eliminar', row.id)">
              <mdicon name="trash-can"></mdicon> Eliminar
            </button>
          </td>
        </tr>
      </tbody>
    </table>
  </section>
</template>

<script setup>
import { computed } from "vue";

const props = defineProps({
  headers: {
    type: Array,
    required: true,
  },
  data: {
    type: Array,
    required: true,
  },
  acciones: {
    type: Boolean,
    default: true,
  },
  estadoEditable: {
    type: Boolean,
    default: false,
  },
});

defineEmits(["editar", "eliminar", "cambiar-estado"]);

const items = computed(() => {
  return props.data.map((item) => ({
    id: item.id,
    estado:item.estado,
    cells: props.headers
      .filter(
        (head) =>
          head.toUpperCase() !== "ACCIONES" &&
          head.toUpperCase() !== "CAMBIAR ESTADO"
      )
      .map((head) => {
        const key = Object.keys(item).find(
          (key) => key.toUpperCase() === head.toUpperCase()
        );
        return key ? item[key] : "";
      }),
  }));
});
</script>

 <style scoped>
section {
  width: 95%;
  margin: 24px auto;
  overflow-x: auto;
  border: 1px solid #e2e8f0;
  border-radius: 10px;
  background: #ffffff;
  box-shadow: 0 2px 8px rgba(15, 23, 42, 0.05);
}

table {
  width: 100%;
  border-collapse: collapse;
  font-size: 14px;
}

th {
  padding: 14px 12px;
  background: #f1f5f9;
  color: #334155;
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 0.5px;
  text-align: left;
  border-bottom: 1px solid #e2e8f0;
}

td {
  padding: 12px;
  color: #475569;
  text-align: left;
  border-bottom: 1px solid #f1f5f9;
}

tbody tr:hover {
  background: #f8fafc;
}

tbody tr:last-child td {
  border-bottom: none;
}

.btn {
  border: none;
  color: white;
  cursor: pointer;
  padding: 7px 10px;
  border-radius: 6px;
  margin: 3px;
  font-size: 12px;
  font-weight: 600;
  transition: background 0.2s;
}

.btn-primary {
  background: #0b7b8d;
}

.btn-primary:hover {
  background: #096575;
}

.btn-danger {
  background: #dc6464;
}

.btn-danger:hover {
  background: #c24141;
}

button:focus-visible {
  outline: 2px solid #0b7b8d;
  outline-offset: 2px;
}

@media (max-width: 700px) {
  table {
    min-width: 650px;
  }
}
</style>