export const actionTypes = {
  FETCH_PRODUCTS: "FETCH_PRODUCTS",
  SET_PRODUCTS: "SET_PRODUCTS",
  BUY_PRODUCT: "BUY_PRODUCT",
  UPDATE_STOCK: "UPDATE_STOCK",
};

export const fetchProducts = (pagination) => ({ type: actionTypes.FETCH_PRODUCTS, payload: pagination });
export const buyProduct = (productId) => ({ type: actionTypes.BUY_PRODUCT, payload: { productId } });
export const updateStock = (productId, newStock) => ({
  type: actionTypes.UPDATE_STOCK,
  payload: { productId, newStock },
});
