import { createContext, useState, useEffect } from "react";

export const CartContext = createContext();

export const CartProvider = ({ children }) => {
    const [cartItems, setCartItems] = useState([]);
    const [stripeLoaded, setStripeLoaded] = useState(false);

    useEffect(() => {
        const script = document.createElement("script");
        script.src = "https://js.stripe.com/v3/pricing-table.js";
        script.async = true;
        script.onload = () => {
            setStripeLoaded(true);
        };
        document.body.appendChild(script);

        return () => {
            document.body.removeChild(script);
        };
    }, []);

    // const handleViewCart = () => {
    //     if (!stripeLoaded) {
    //         loadStripeScript();
    //     }
    // };

    // const handleAddToCart = () => {
    //     if (!stripeLoaded) {
    //         loadStripeScript();
    //     }
    // };

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
