import ApiService from "./ApiService.js";

class VeterinarioService extends ApiService {
  constructor() {
    super("/veterinarios/");
  }
}

export default VeterinarioService;
