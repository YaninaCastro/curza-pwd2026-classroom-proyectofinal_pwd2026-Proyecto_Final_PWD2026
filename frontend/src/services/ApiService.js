import { apiAxios as axios } from "../plugins/axios";

class ApiService {
  url = "";
  errors = [];

  constructor(url) {
    this.url = url;
  }

  async getAll() {
    this.errors = [];

    const data = await axios
      .get(this.url)
      .then((response) => response.data)
      .catch((error) => {
        this.errors.push({
          ...(
            error.response?.data || {
              message: "Error de red",
            }
              ),
        status: error.response?.status,
      });
      return null;
    });

    if (this.errors.length === 0) {
      return data;
    }
      return null;
  }

  async findOne(id) {
    this.errors = [];
    const urlId = `${this.url.replace(/\/$/, "")}/${id}`;

    const data = await axios
      .get(urlId)
      .then((response) => response.data)
      .catch((error) => {
        this.errors.push(
          error.response?.data || { message: "Error de red" }
        );
        return null;
      });

    if (this.errors.length === 0) {
      return data;
    }

    return null;
  }

  async create(data) {
    this.errors = [];

    await axios
      .post(this.url, data)
      .then((response) => alert(response.data.message))
      .catch((error) => {
        this.errors.push(
          error.response?.data || { message: "Error de red" }
        );
        alert(this.errors[0].message || "Error al crear el registro");
      });
  }

  async update(id, data) {
    this.errors = [];
    const urlId = `${this.url.replace(/\/$/, "")}/${id}`;

    await axios
      .put(urlId, data)
      .then((response) => alert(response.data.message))
      .catch((error) => {
        this.errors.push(
          error.response?.data || { message: "Error de red" }
        );
        alert(this.errors[0].message || "Error al actualizar el registro");
      });
  }

  async destroy(id) {
    this.errors = [];
    const urlId = `${this.url.replace(/\/$/, "")}/${id}`;

    await axios
      .delete(urlId)
      .then((response) => alert(response.data.message))
      .catch((error) => {
        this.errors.push(
          error.response?.data || { message: "Error de red" }
        );
        alert(this.errors[0].message || "Error al eliminar el registro");
      });
  }
}

export default ApiService;