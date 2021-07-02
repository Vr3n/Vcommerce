import { useState } from "react";
import { useQuery } from "react-query";

import { Wrapper } from "./App.styles";
import Drawer from "@material-ui/core/Drawer";
import LinearProgress from "@material-ui/core/LinearProgress";
import Grid from "@material-ui/core/Grid";
// import AddShoppingCartIcon from "@material-ui/icons/AddShoppingCart";
// import Badge from "@material-ui/core/Badge";

import Item from "./item/item";
import Cart from "./Cart/Cart";
import Navbar from "./Navbar/Navbar";

// Types.
export type CartItemType = {
  id: number;
  category: string;
  description: string;
  image: string;
  price: number;
  title: string;
  amount: number;
};

// Fetchi functions.

const getProducts = async (): Promise<CartItemType[]> =>
  await (await fetch("https://fakestoreapi.com/products")).json();

const App = () => {
  const [cartOpen, setCartOpen] = useState(false);

  const [cartItems, setCartItems] = useState([] as CartItemType[]);

  const { data, isLoading, error } = useQuery<CartItemType[]>(
    "products",
    getProducts
  );

  const getTotalItems = (items: CartItemType[]) =>
    items.reduce((ack: number, item) => ack + item.amount, 0);

  const handleAddToCart = (clickedItem: CartItemType) => {
    setCartItems((prev) => {
      // 1. Is the item already in cart ?
      const isItemInCart = prev.find((item) => item.id === clickedItem.id);

      if (isItemInCart) {
        return prev.map((item) =>
          item.id === clickedItem.id
            ? { ...item, amount: item.amount + 1 }
            : item
        );
      }

      // item is added for first time.
      return [...prev, { ...clickedItem, amount: 1 }];
    });
  };

  const handleCartOpen = () => setCartOpen(true);

  const handleRemoveCart = (id: number) => {
    setCartItems((prev) =>
      prev.reduce((ack, item) => {
        if (item.id === id) {
          if (item.amount === 1) return ack;
          return [...ack, { ...item, amount: item.amount - 1 }];
        } else {
          return [...ack, item];
        }
      }, [] as CartItemType[])
    );
  };

  if (isLoading) return <LinearProgress />;

  if (error) return <div>Bruhh!!</div>;

  return (
    <>
      <Navbar getItems={getTotalItems(cartItems)} cartOpen={handleCartOpen}  />
      <Wrapper>
        <Drawer
          anchor="right"
          open={cartOpen}
          onClose={() => setCartOpen(false)}
        >
          <Cart
            cartItems={cartItems}
            addToCart={handleAddToCart}
            removeFromCart={handleRemoveCart}
          />
        </Drawer>
        {/* <StyledButton onClick={() => setCartOpen(true)}>
          <Badge badgeContent={getTotalItems(cartItems)} color="error">
            <AddShoppingCartIcon />
          </Badge>
        </StyledButton> */}
        <Grid container spacing={3}>
          {data?.map((item) => (
            <Grid item key={item.id} xs={12} md={6} lg={4} xl={3}>
              <Item item={item} handleAddToCart={handleAddToCart} />
            </Grid>
          ))}
        </Grid>
      </Wrapper>
    </>
  );
};

export default App;
