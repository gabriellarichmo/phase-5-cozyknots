import { useContext } from "react";
import { CartContext } from "./CartContext";

const MyCart = () => {
    const { cartItems, removeFromCart } = useContext(CartContext);

    const handleRemoveFromCart = (patternId) => {
        removeFromCart(patternId);
    };

    return (
        <div>
        <h2>My Cart</h2>
        {cartItems.map((item) => (
            <div key={item.id}>
            <p>{item.name}</p>
            <button onClick={() => handleRemoveFromCart(item.id)}>Remove</button>
            </div>
        ))}
        {/* checkout button? */}
        </div>
    );
};

export default MyCart;