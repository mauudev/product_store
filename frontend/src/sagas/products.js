import { call, put, takeEvery } from "redux-saga/effects";
import { actionTypes } from "../actions/productActions";
import { api } from "../shared/api";

// Main -> dispatch(actions) -> sagas -> external calls -> put(actions) -> reducers -> redux store
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
    const { productId, quantity } = action.payload;
    yield call(api.buyProduct, { productId, quantity });
  } catch (error) {
    console.error("Error when buying product", error);
  }
}

function* productSaga() {
  yield takeEvery(actionTypes.FETCH_PRODUCTS, fetchProducts);
  yield takeEvery(actionTypes.BUY_PRODUCT, buyProduct);
}

export default productSaga;
