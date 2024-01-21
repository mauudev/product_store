import { actionTypes } from "../actions/productActions";

const initialState = {
  products: [],
  size: 0,
  rawData: null,
};

const productsData = (state = initialState, action) => {
  switch (action.type) {
    case actionTypes.SET_PRODUCTS:
      return {
        ...state,
        products: [...state.products, ...action.payload.products],
        size: action.payload.size,
        rawData: action.payload.rawData,
      };
    default:
      return state;
  }
};

export default productsData;
