import { actionTypes } from "../actions/productActions";

const initialState = {
  pageProducts: [],
  products: [],
  size: 0,
  rawData: null,
};

const productsData = (state = initialState, action) => {
  switch (action.type) {
    case actionTypes.SET_PRODUCTS:
      return {
        ...state,
        products: action.payload.products,
        size: action.payload.size,
        rawData: action.payload.rawData,
        pageProducts: [...state.pageProducts, ...action.payload.products],
      };
    default:
      return state;
  }
};

export default productsData;
