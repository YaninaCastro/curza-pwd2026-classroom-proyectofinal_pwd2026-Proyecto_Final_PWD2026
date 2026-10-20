
import { apiAxios as axios } from "../plugins/axios";

class AuthServices {
  auth_user = null;
  errors = [];

  async login(user) {
    this.errors = [];
    this.auth_user = null;

    try {
      const response = await axios.post("/auth/login", user);
      const data = response.data;

      this.auth_user = {
        id: data.id,
        nombre: data.nombre,
        apellido: data.apellido,
        authenticated: true,
        jwt: data.access_token,
        refresh_token: data.refresh_token,
        rol: data.rol,
      };

      return true;
    } catch (error) {
      this.errors.push(
        error.response?.data || {
          message: "No se pudo conectar con el servidor",
        }
      );

      return false;
    }
  }
}

export default AuthServices;
