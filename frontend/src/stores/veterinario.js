import VeterinarioService from "../services/VeterinarioService.js";
import { defineStore } from "pinia";
import { ref } from "vue";

export const useVeterinarioStore = defineStore("veterinario", () => {
  const veterinarios = ref([]);
  const veterinario = ref(null);
  const errors = ref([]);
  const service = new VeterinarioService();

  async function getAll() {
    errors.value = [];
    const data = await service.getAll();

    if (data) {
      veterinarios.value = Array.isArray(data) ? data : [];
      return true;
    }

    errors.value = service.errors;
    return false;
  }

  async function findOne(id) {
    errors.value = [];
    const data = await service.findOne(id);

    if (data) {
      veterinario.value = Array.isArray(data) ? data[0] : data;
      return true;
    }

    errors.value = service.errors;
    return false;
  }

  async function create(data) {
    errors.value = [];
    await service.create(data);

    if (service.errors.length === 0) {
      await getAll();
      return true;
    }

    errors.value = service.errors;
    return false;
  }

  async function update(id, data) {
    errors.value = [];
    await service.update(id, data);

    if (service.errors.length === 0) {
      await getAll();
      return true;
    }

    errors.value = service.errors;
    return false;
  }

  async function destroy(id) {
    errors.value = [];
    await service.destroy(id);

    if (service.errors.length === 0) {
      await getAll();
      return true;
    }

    errors.value = service.errors;
    return false;
  }

  return {
    veterinarios,
    veterinario,
    errors,
    getAll,
    findOne,
    create,
    update,
    destroy,
  };
});
