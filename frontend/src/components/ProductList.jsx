import React, { useEffect, useState } from "react";
import { useProduct } from "../context/ProductContext";
import { api } from "../utils/api";

const ProductList = () => {
  const { state, dispatch } = useProduct();
  const [page, setPage] = useState(1);
  const [size, setSize] = useState(100);
  const [searchTerm, setSearchTerm] = useState("");

  useEffect(() => {
    const fetchProducts = async () => {
      try {
        let productList;

        if (searchTerm) {
          productList = await api.searchProducts(searchTerm, page, size);
        } else {
          productList = await api.getAllProducts(page, size);
        }

        const updatedProducts = { ...state.products };

        productList.items.forEach((product) => {
          if (!updatedProducts[product.id]) {
            updatedProducts[product.id] = product;
          } else {
            updatedProducts[product.id] = { ...updatedProducts[product.id], ...product };
          }
        });

        dispatch({ type: "FETCH_PRODUCTS", payload: updatedProducts });
      } catch (error) {
        console.error("Error when getting products", error);
      }
    };

    fetchProducts();
  }, [page, size, searchTerm]);

  const handleLoadMore = async () => {
    setPage(page + 1);
  };

  const handleSearch = (event) => {
    setPage(1);
    setSearchTerm(event.target.value);
  };

  return (
    <div>
      <h1>Lista de Productos</h1>
      <input type="text" placeholder="Search product" value={searchTerm} onChange={handleSearch} />
      {Object.values(state.products).map((product) => (
        <div key={product.id}>
          <img src={product.product_image} alt={product.product_name} />
          <h3>{product.product_name}</h3>
          <p>Stock: {product.stock}</p>
        </div>
      ))}
      <button onClick={handleLoadMore}>Cargar mas</button>
    </div>
  );
};

export default ProductList;
