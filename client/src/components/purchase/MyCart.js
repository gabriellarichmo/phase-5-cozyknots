import { useContext, useState } from "react";
import { CartContext } from "./CartContext";
import { Link } from "react-router-dom"

const MyCart = () => {
    const { cartItems, removeFromCart, stripeLoaded } = useContext(CartContext);


    return (
        <div>
            <h1>My Cart</h1>
            {stripeLoaded && (
                <stripe-pricing-table
                    pricing-table-id="prctbl_1PAwvT01oc5MNduHbiUlqy5Y"
                    publishable-key="pk_test_51P8nqZ01oc5MNduH9V0nlRddBjThEeQnoi03xdx8IgdJNBeZrOkN9qtQ9qih3wkz4FxbortvgqNkhlBnEaPwLTW600gDX8r3B0"
                ></stripe-pricing-table>
            )}
            <div>
                {cartItems.length > 0 ? (
                    cartItems.map((item) => (
                        <div key={item.id}>
                            <p>{item.title}</p>
                            <button onClick={() => removeFromCart(item.id)}>Remove from My Cart</button>
                        </div>
                    ))
                ) : (
                    <p>Your cart is empty.</p>
                )}
            </div>
            <Link to="/checkout">Proceed to Checkout</Link>
        </div>
    );
};

export default MyCart;