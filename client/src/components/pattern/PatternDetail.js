import React, { useContext, useEffect, useState } from "react";
import { CartContext } from "./CartContext";
//useParams to extract pattern id and useEffect to fetch pattern by id and set into state

const PatternDetail = ({ pattern }) => {
    const { addToCart } = useContext(CartContext);

    const handleAddToCart = () => {
        addToCart(pattern);
    };


    return (
        <div>
        <h2>{pattern.title}</h2>
        {/* pattern details will be added here! */}
        <button onClick={handleAddToCart}>Add to Cart</button>
        </div>
    );
};

export default PatternDetail;