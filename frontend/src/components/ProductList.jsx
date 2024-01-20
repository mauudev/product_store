import React, { useEffect, useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import { fetchProducts } from "../actions/productActions";

const ProductList = () => {
  const [page, setPage] = useState(1);
  const [size, setSize] = useState(3);
  const [searchTerm, setSearchTerm] = useState("");
  const currentData = useSelector((state) => state.productsData);
  const dispatch = useDispatch();

  useEffect(() => {
    dispatch(fetchProducts({ page, size }));
  }, [page]);

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
      {currentData.pageProducts.map((product) => (
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
