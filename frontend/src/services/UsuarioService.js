import ApiService from "./ApiService.js";

class UsuarioService extends ApiService {
  constructor() {
    super("/usuarios/");
  }
}

export default UsuarioService;