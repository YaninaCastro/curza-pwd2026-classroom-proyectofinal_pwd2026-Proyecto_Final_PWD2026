import ApiService from "./ApiService.js";

class MascotaService extends ApiService {
  constructor() {
    super("/mascotas/");
  }
}

export default MascotaService;