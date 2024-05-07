import { createContext, useState, useEffect } from "react";
import toast from "react-hot-toast";

export const CartContext = createContext();

export const CartProvider = ({ children }) => {
    const [cartItems, setCartItems] = useState([]);
    const [stripeLoaded, setStripeLoaded] = useState(false);

    const addToCart = (pattern) => {
        setCartItems([...cartItems, pattern]);
    };

    const removeFromCart = (patternId) => {
        setCartItems(cartItems.filter((item) => item.id !== patternId));
    };

    
    return (
        <CartContext.Provider value={{ cartItems, addToCart, removeFromCart, stripeLoaded }}>
        {children}
        </CartContext.Provider>
    );
};
