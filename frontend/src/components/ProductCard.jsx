import { useState } from "react";
import Card from "@mui/material/Card";
import CardActions from "@mui/material/CardActions";
import CardContent from "@mui/material/CardContent";
import CardMedia from "@mui/material/CardMedia";
import Button from "@mui/material/Button";
import Typography from "@mui/material/Typography";
import TextField from "@mui/material/TextField";

const ProductCard = ({ product, handlePurchase }) => {
  const [quantity, setQuantity] = useState(1);

  const handleQuantityChange = (event) => {
    const value = parseInt(event.target.value, 10);
    setQuantity(value >= 0 ? value : 0);
  };

  const handleBuyClick = () => {
    handlePurchase(product.id, quantity);
  };

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
        <TextField
          id="outlined-number"
          label="Cantidad"
          type="number"
          step="1"
          min="0"
          max={product.stock}
          value={quantity}
          onChange={handleQuantityChange}
          InputLabelProps={{
            shrink: true,
          }}
          size="small"
        />
        <Button size="small" variant="outlined" onClick={handleBuyClick}>
          Comprar
        </Button>
      </CardActions>
    </Card>
  );
};

export default ProductCard;
