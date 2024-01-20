import { experimentalStyled as styled } from "@mui/material/styles";
import Box from "@mui/material/Box";
import Paper from "@mui/material/Paper";
import Grid from "@mui/material/Grid";
import Typography from "@mui/material/Typography";
import Button from "@mui/material/Button";
import React, { useEffect, useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import { fetchProducts } from "../actions/productActions";
import { v4 as uuidv4 } from "uuid";

const Item = styled(Paper)(({ theme }) => ({
  backgroundColor: theme.palette.mode === "dark" ? "#1A2027" : "#fff",
  ...theme.typography.body2,
  padding: theme.spacing(2),
  textAlign: "center",
  color: theme.palette.text.secondary,
}));

const Main = () => {
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
    <React.Fragment>
      <Box sx={{ flexGrow: 1, margin: 5 }}>
        <Typography variant="h5" component="div" sx={{ flexGrow: 1 }}>
          Products available
        </Typography>
        <Grid container spacing={{ xs: 2, md: 3 }} columns={{ xs: 4, sm: 8, md: 12 }}>
          {currentData.pageProducts.map((product) => (
            <Grid item xs={2} sm={4} md={4} key={uuidv4()}>
              <Item>
                <img src={product.product_image} alt={product.product_name} />
                <h3>{product.product_name}</h3>
                <p>Stock: {product.stock}</p>
              </Item>
            </Grid>
          ))}
        </Grid>
        <Button variant="outlined" size="small" onClick={handleLoadMore}>
          Cargar mas
        </Button>
      </Box>
    </React.Fragment>
  );
};

export default Main;
