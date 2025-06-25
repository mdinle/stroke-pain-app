// src/services/AuthService.js
import axios from '@/axios-auth';

class AuthService {
  async login(username, password) {
    const response = await axios.post('/auth/login', { username, password });
    return response.data;
  }

  async register(username, password) {
    const response = await axios.post('/auth/register', { username, password });
    return response.data;
  }
}

export default new AuthService();
