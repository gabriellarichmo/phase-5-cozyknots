import { Link } from "react-router-dom"
import { CartContext } from "../purchase/CartContext"; 
import { useContext } from "react";
import "./PatternCard.css"

const PatternCard = ({ id, title, author, description, difficulty, price }) => {
    const { addToCart } = useContext(CartContext);

    const handleAddToCart = () => {
        addToCart({ id, title, author, description, difficulty, price })
    }

    return (
        <div className="pattern-card">
            {/* <Link to={`/patterns/${id}`} > */}
            <h3>{title}</h3>
            <p>Author: {author}</p>
            <p>{description}</p>
            <p>Difficulty: {difficulty}</p>
            <p>${price}</p>

                {/* {imageLoaded && imageUrl && <img src={imageUrl} alt={name} />} */}
            {/* </Link> */}
            <button onClick={handleAddToCart}>Add to Cart</button>
        </div>
    );
};

export default PatternCard;
