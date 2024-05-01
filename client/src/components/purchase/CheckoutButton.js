import { useState, useContext } from "react";
import { CartContext } from "./CartContext";

const CheckoutButton = ({ pattern }) => {
  const { stripeLoaded, addToCart } = useContext(CartContext);
  const [error, setError] = useState(null);

  const handleCheckout = async () => {
    if (!stripeLoaded) {
      setError("Stripe script not loaded.");
      return;
    }

    try {
      const response = await fetch("/checkout", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          pattern_id: pattern.id,
          price: pattern.price,
          payment_method: "stripe", // Assuming payment method is Stripe
        }),
      });
      const data = await response.json();
      // Handle response data, e.g., redirect to payment page or show success message
    } catch (error) {
      setError("Failed to initiate checkout.");
      console.error("Checkout Error:", error);
    }
  };

  return <button onClick={handleCheckout}>Checkout</button>;
};

export default CheckoutButton;
