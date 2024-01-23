import axios from "axios";

const BASE_URL = "http://localhost:8000/v1";

const api = {
  createProduct: async (data) => {
    try {
      const response = await axios.post(`${BASE_URL}/products/create`, data);
      return response.data;
    } catch (error) {
      console.error("Error when creating product ", error);
      throw error;
    }
  },

  getProduct: async (productId) => {
    try {
      const response = await axios.get(`${BASE_URL}/products/${productId}`);
      return response.data;
    } catch (error) {
      console.error("Error when getting product", error);
      throw error;
    }
  },

  getAllProducts: async (page, size, name) => {
    try {
      const response = await axios.get(`${BASE_URL}/products`, { params: { page, size, name } });
      return response.data;
    } catch (error) {
      console.error("Error when getting products", error);
      throw error;
    }
  },

  updateProduct: async (productId, data) => {
    try {
      const response = await axios.put(`${BASE_URL}/products/${productId}`, data);
      return response.data;
    } catch (error) {
      console.error("Error when updating product ", error);
      throw error;
    }
  },

  updateProductPartial: async (productId, data) => {
    try {
      await axios.patch(`${BASE_URL}/products/${productId}`, data);
    } catch (error) {
      console.error("Error when updating product ", error);
      throw error;
    }
  },

  buyProduct: async (data) => {
    try {
      const response = await axios.patch(`${BASE_URL}/products/${data.productId}/buy/${data.quantity}`, {"stock": data.quantity});
      return response.data;
    } catch (error) {
      console.error("Error when buying product ", error);
      throw error;
    }
  },
};

export { api };
