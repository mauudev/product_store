export const actionTypes = {
  FETCH_PRODUCTS: "FETCH_PRODUCTS",
  SET_PRODUCTS: "SET_PRODUCTS",
  BUY_PRODUCT: "BUY_PRODUCT",
  UPDATE_PRODUCT_STOCK: "UPDATE_PRODUCT_STOCK",
};

export const fetchProducts = (payload) => ({ type: actionTypes.FETCH_PRODUCTS, payload });
export const buyProduct = (payload) => ({ type: actionTypes.BUY_PRODUCT, payload });
export const updateStock = (payload) => ({ type: actionTypes.UPDATE_PRODUCT_STOCK, payload });
