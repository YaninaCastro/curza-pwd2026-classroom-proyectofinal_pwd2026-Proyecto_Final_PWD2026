<template>
  <section>
    <h3>Editar rol</h3>

    <p v-if="cargando">Cargando rol...</p>

    <form v-else @submit.prevent="guardar">
      <div class="campo">
        <label for="nombre">Nombre:</label>
        <select id="nombre" v-model="form.nombre" required>
          <option value="Administrador/a">Administrador/a</option>
          <option value="recepcionista">Recepcionista</option>
          <option value="veterinario/a">Veterinario/a</option>
        </select>
      </div>

      <div class="campo">
        <label for="activo">Estado:</label>
        <select id="activo" v-model="form.activo" required>
          <option value="S">Activo</option>
          <option value="N">Inactivo</option>
        </select>
      </div>

      <button class="btn-form" type="submit">Guardar cambios</button>
      <button class="btn-form" type="button" @click="$emit('cancelar')">
        Cancelar
      </button>
    </form>
  </section>
</template>

<script setup>
import { onMounted, reactive, ref } from "vue";
import { useRolStore } from "../stores/rol.js";

const props = defineProps({
  id: {
    type: [Number, String],
    required: true,
  },
});

const emit = defineEmits(["actualizado", "cancelar"]);
const rolStore = useRolStore();
const cargando = ref(true);

const form = reactive({
  nombre: "",
  activo: "S",
});

onMounted(async () => {
  const encontrado = await rolStore.findOne(props.id);

  if (encontrado && rolStore.rol) {
    form.nombre = rolStore.rol.nombre;
    form.activo = rolStore.rol.activo;
  }

  cargando.value = false;
});

async function guardar() {
  const actualizado = await rolStore.update(props.id, { ...form });

  if (actualizado) {
    emit("actualizado");
  }
}
</script>

<style scoped>
section {
  margin: 20px 0;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 8px;
}

.campo {
  display: flex;
  flex-direction: column;
  gap: 6px;
  margin-bottom: 16px;
  max-width: 400px;
}

select {
  padding: 9px;
  border: 1px solid #bbb;
  border-radius: 5px;
  width: 100%;
  box-sizing: border-box;
}

.btn-form {
  margin: 6px 8px 6px 0;
  padding: 9px 14px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}
</style>