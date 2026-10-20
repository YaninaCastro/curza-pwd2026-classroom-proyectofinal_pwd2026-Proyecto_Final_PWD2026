import UsuarioService from "../services/UsuarioService.js";
import { defineStore } from "pinia";
import { ref } from "vue";

export const useUsuarioStore = defineStore("usuario", () => {
  const usuarios = ref([]);
  const usuario = ref(null);
  const service = new UsuarioService();
  const errors = ref([]);
  const status_code = ref(null);

  async function getAll() {
    errors.value = [];
    const data = await service.getAll();

    if (data) {
      usuarios.value = Array.isArray(data) ? data : [];
      return true;
    }

    errors.value = service.errors;
    return false;
  }

  async function findOne(id) {
    errors.value = [];
    const data = await service.findOne(id);

    if (data) {
      usuario.value = Array.isArray(data) ? data[0] : data;
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
    usuarios,
    usuario,
    errors,
    status_code,
    getAll,
    findOne,
    create,
    update,
    destroy,
  };
});