import { useContext, useState } from "react";
import { CartContext } from "./CartContext";
// import { Link } from "react-router-dom"
import { loadStripe } from "@stripe/stripe-js";
import {
  PaymentElement,
  Elements,
  useStripe,
  useElements,
} from "@stripe/react-stripe-js";
import PatternCard from "../pattern/PatternCard";
import "./MyCart.css"

const MyCart = () => {
    const { cartItems, removeFromCart, stripeLoaded } = useContext(CartContext);


    return (
      <div>
        <h1>My Cart</h1>
        <div>
          {cartItems.length > 0 ? (
            cartItems.map((item) => (
              <div key={item.id}>
                <PatternCard {...item} />
                <form
                  action={`/create-checkout-session/${item.id}`}
                  method="POST"
                >
                  <button className="button-55" type="submit">
                    Proceed to Checkout
                  </button>
                </form>
              </div>
            ))
          ) : (
            <p>Your cart is empty.</p>
          )}
        </div>
      </div>
    );
};

export default MyCart;