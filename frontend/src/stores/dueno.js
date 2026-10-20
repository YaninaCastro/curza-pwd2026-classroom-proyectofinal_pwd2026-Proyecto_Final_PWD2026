import DuenoService from "../services/DuenoService.js";
import { defineStore } from "pinia";
import { ref } from "vue";

export const useDuenoStore = defineStore(
  "dueno",
  () => {
    const duenos = ref([]); //duenos: guarda la lista de dueños
    const dueno = ref(null); //dueno: guarda un dueño individual.
    const service = new DuenoService(); //service: conecta el store con DuenoService, que se comunica con el backend.
    const errors = ref([]);
    const status_code = ref(null);

    async function getAll() {   //getAll(): obtiene todos los dueños.
      errors.value = [];
      const data = await service.getAll();

      if (data) {
        duenos.value = Array.isArray(data) ? data : [];
        return true;
      }

      errors.value = service.errors;
      return false;
    }

    async function findOne(id) {   //findOne(id): busca un dueño por su ID.
      errors.value = [];            //backend devuelve una lista cuando hay varios dueños, pero show(id) devuelve una lista con un solo dueño. Por eso findOne() contempla ambos casos.
      const data = await service.findOne(id);

      if (data) {
        dueno.value = Array.isArray(data) ? data[0] : data;
        return true;
      }

      errors.value = service.errors;
      return false;
    }

    async function create(data) {       //create(data): crea un dueño y vuelve a cargar la lista.
      errors.value = [];
      await service.create(data);

      if (service.errors.length === 0) {
        await getAll();
        return true;
      }

      errors.value = service.errors;
      return false;
    }

    async function update(id, data) { //update(id, data): actualiza un dueño y vuelve a cargar la lista
      errors.value = [];
      await service.update(id, data);

      if (service.errors.length === 0) {
        await getAll();
        return true;
      }

      errors.value = service.errors;
      return false;
    }

    async function destroy(id) { //destroy(id): elimina un dueño y vuelve a cargar la lista
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
      duenos,
      dueno,
      errors,
      status_code,
      getAll,
      findOne,
      create,
      update,
      destroy,
    };
  },
);