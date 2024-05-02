import { useContext, useState } from "react";
import { CartContext } from "./CartContext";
// import { Link } from "react-router-dom"
import StripePricingTable from "./StripePricingTable";
import PatternCard from "../pattern/PatternCard";
import "./MyCart.css"

const MyCart = () => {
    const { cartItems, removeFromCart, stripeLoaded } = useContext(CartContext);


    return (
        <div>
            <h1>My Cart</h1>
            {stripeLoaded && (
                <div>
                    <StripePricingTable />
                </div>
            )}
            <div>
                {cartItems.length > 0 ? (
                    cartItems.map((item) => (
                        <div key={item.id}>
                            <PatternCard {...item} />
                            <button onClick={() => removeFromCart(item.id)}>Remove from My Cart</button>
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