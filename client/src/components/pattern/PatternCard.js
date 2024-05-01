import { Link } from "react-router-dom"
import { CartContext } from "../purchase/CartContext"; 
import { useContext, useEffect, useState } from "react";
import toast from "react-hot-toast";
import "./PatternCard.css"

const PatternCard = ({ id, title, author, description, difficulty, price, category, image }) => {
    const { addToCart } = useContext(CartContext);
    const [imageUrl, setImageUrl] = useState(null);
    const [imageLoaded, setImageLoaded] = useState(false);

    useEffect(() => {
        if (!imageUrl)
        fetch(`/images/${image}`)
            .then((data) => {
            return data.blob();
            })
            .then((blob) => {
            // src.current = URL.createObjectURL(blob);
            const url = URL.createObjectURL(blob);
            setImageUrl(url);
            setImageLoaded(true);
            })
            .catch((error) => console.error("Error:", error));
        return () => {
        if (imageUrl) {
            URL.revokeObjectURL(imageUrl);
        }
        };
    }, []);
    
    const handleAddToCart = () => {
        addToCart({ id, title, author, description, difficulty, price, category, image });
        toast.success(`${title} added to cart!`)
    }

    return (
        <div className="pattern-card">
            {/* <Link to={`/patterns/${id}`} > */}
            <h3>{title}</h3>
            {imageLoaded && imageUrl && <img src={imageUrl} alt={title} />}
            <p>Author: {author}</p>
            <p>{description}</p>
            <p>{category.name}</p>
            <p>Difficulty: {difficulty}</p>
            <p>${price}</p>

            {/* {imageLoaded && imageUrl && <img src={imageUrl} alt={name} />} */}
            {/* </Link> */}
            <button onClick={handleAddToCart}>Add to Cart🛒</button>
        </div>
    );
};

export default PatternCard;
