import React from "react";
import ProductList from "./components/ProductList";
import { ProductProvider } from './context/ProductContext';

const App = () => {
  return (
    <ProductProvider>
    <div>
      <h1>Tienda de Productos</h1>
      <ProductList />
    </div>
    </ProductProvider>
  );
};

export default App;
