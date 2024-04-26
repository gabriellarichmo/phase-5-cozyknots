import { createContext, useState } from "react";

export const CartContext = createContext();

export const CartProvider = ({ children }) => {
    const [cartItems, setCartItems] = useState([]);

    const addToCart = (pattern) => {
        setCartItems([...cartItems, pattern]);
    };

    const removeFromCart = (patternId) => {
        setCartItems(cartItems.filter((item) => item.id !== patternId));
    };

    return (
        <CartContext.Provider value={{ cartItems, addToCart, removeFromCart }}>
        {children}
        </CartContext.Provider>
    );
};
