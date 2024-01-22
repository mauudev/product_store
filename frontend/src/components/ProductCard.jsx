import * as React from "react";
import Card from "@mui/material/Card";
import CardActions from "@mui/material/CardActions";
import CardContent from "@mui/material/CardContent";
import CardMedia from "@mui/material/CardMedia";
import Button from "@mui/material/Button";
import Typography from "@mui/material/Typography";

const ProductCard = ({ product, handlePurchase }) => {
  return (
    <Card sx={{ maxWidth: 345 }}>
      <CardMedia sx={{ height: 140 }} image={product.product_image} title={product.product_name} />
      <CardContent>
        <Typography gutterBottom variant="h5" component="div">
          {product.product_name}
        </Typography>
        <div>
          <Typography variant="body2" color="text.secondary">
            ID: {product.id}
          </Typography>
          <Typography variant="body2" color="text.secondary">
            Stock: {product.stock}
          </Typography>
        </div>
      </CardContent>
      <CardActions>
        <Button size="small" variant="outlined" onClick={() => handlePurchase(product.id)}>
          Comprar
        </Button>
      </CardActions>
    </Card>
  );
};

export default ProductCard;
