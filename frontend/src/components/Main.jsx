import React, { useEffect, useState, useRef } from "react";
import { useSelector, useDispatch } from "react-redux";
import Box from "@mui/material/Box";
import Grid from "@mui/material/Grid";
import Typography from "@mui/material/Typography";
import Button from "@mui/material/Button";
import SearchInput from "./SearchInput";
import ProductCard from "./ProductCard";
import { createWebSocketConnection } from "../shared/socket";
import { fetchProducts, buyProduct } from "../actions/productActions";
import { v4 as uuidv4 } from "uuid";

const Main = () => {
  const socketRef = useRef(null);
  const [page, setPage] = useState(1);
  const [size, setSize] = useState(10);
  const [searchTerm, setSearchTerm] = useState("");
  const currentData = useSelector((state) => state.productsData);
  const dispatch = useDispatch();

  useEffect(() => {
    dispatch(fetchProducts({ page, size, name: searchTerm }));

    const handleSocket = async () => {
      try {
        const socketInstance = await createWebSocketConnection();
        socketRef.current = socketInstance;

        socketRef.current.on("reply", (msg) => {
          dispatch({
            type: "UPDATE_PRODUCT_STOCK",
            payload: {
              productId: msg.productId,
              newStock: msg.newStock,
            },
          });
        });

        return () => {
          socketRef.current.disconnect();
        };
      } catch (error) {
        console.error("Error ocurred when connecting to the socket:", error);
      }
    };

    handleSocket();
  }, [page, searchTerm]);

  const handleLoadMore = async () => {
    setPage(page + 1);
  };

  const handleSearch = (search) => {
    setPage(1);
    setSearchTerm(search);
  };

  const handlePurchase = (productId, quantity) => {
    console.log(`Purchasing ${quantity} of product ${productId}`);
    dispatch(buyProduct({ productId, quantity }));
  };

  const filterRenderProducts = (products, searchTerm) => {
    return products
      .filter((product) => (searchTerm ? product.product_name.includes(searchTerm) : true))
      .map((product) => (
        <Grid item xs={2} sm={4} md={4} key={uuidv4()}>
          <ProductCard product={product} handlePurchase={handlePurchase} />
        </Grid>
      ));
  };

  return (
    <React.Fragment>
      <Box sx={{ flexGrow: 1, margin: 5 }}>
        <Typography variant="h5" component="div" sx={{ flexGrow: 1 }}>
          Products available
        </Typography>
        <SearchInput page={page} size={size} onChange={handleSearch} />
        <Grid container spacing={{ xs: 2, md: 3 }} columns={{ xs: 4, sm: 8, md: 12 }}>
          {filterRenderProducts(currentData.products, searchTerm)}
        </Grid>
        <Button variant="outlined" size="small" onClick={handleLoadMore}>
          Cargar mas
        </Button>
      </Box>
    </React.Fragment>
  );
};

export default Main;
