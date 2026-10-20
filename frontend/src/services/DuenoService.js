import ApiService from "./ApiService.js";   //import ApiService: importa la clase que ya tiene
// las operaciones generales de la API (getAll, findOne, create, update y destroy).

class DuenoService extends ApiService { //class DuenoService extends ApiService: crea un servicio específico para Dueños que hereda los métodos de ApiService.
  constructor() {          //constructor(): se ejecuta cuando se crea un objeto de DuenoService.
    super("/duenos/");     //super("/duenos/"): llama al constructor de ApiService y le indica qué ruta del backend debe usar para este módulo.
  }
}
export default DuenoService;

/*recordar más adelante:
const service = new DuenoService();
const duenos = await service.getAll();


getAll() hará una petición al endpoint GET /duenos/, usando la dirección base que se configuro en Axios: http://localhost:5001.

Así, para otros módulos se puede reutilizar ApiService cambiando solamente la ruta: /mascotas/, /turnos/, etc. */

