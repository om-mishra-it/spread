import axios from "axios";

const API_BASE = "http://localhost:8000/auth";

export const loginUser = async (email, password) => {
    const response = await axios.post(`${API_BASE}/login`, { email, password });
    return response.data;
};

export const registerUser = async (email, password) => {
    const response = await axios.post(`${API_BASE}/register`, { email, password });
    return response.data;
};
