import ApiService from "./ApiService.js";

class RolService extends ApiService {
  constructor() {
    super("/roles/");
  }
}

export default RolService;