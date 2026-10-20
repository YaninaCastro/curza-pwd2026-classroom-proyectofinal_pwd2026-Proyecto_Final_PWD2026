import ApiService from "./ApiService.js";

class TurnoService extends ApiService {
  constructor() {
    super("/turnos/");
  }
}

export default TurnoService;