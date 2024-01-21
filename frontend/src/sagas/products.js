import { call, put, takeEvery } from "redux-saga/effects";
import { actionTypes } from "../actions/productActions";
import { api } from "../shared/api";

function* fetchProducts(action) {
  try {
    const { page, size, name } = action.payload;
    const productList = yield call(api.getAllProducts, page, size, name);
    yield put({
      type: actionTypes.SET_PRODUCTS,
      payload: { products: productList.items, size: productList.size, rawData: productList },
    });
  } catch (error) {
    console.error("Error al cargar la lista de productos", error);
  }
}

function* buyProduct(action) {
  try {
    const response = yield call(api.buyProduct, action.payload.productId);
    yield put(updateStock(action.payload.productId, response.data.newStock));
  } catch (error) {
    console.error("Error al comprar el producto", error);
  }
}

function* productSaga() {
  yield takeEvery(actionTypes.FETCH_PRODUCTS, fetchProducts);
  yield takeEvery(actionTypes.BUY_PRODUCT, buyProduct);
}

export default productSaga;
