import { Link } from "react-router-dom"
import { CartContext } from "../purchase/CartContext"; 
import { useContext, useEffect, useState } from "react";
import toast from "react-hot-toast";
import "./PatternCard.css"

const PatternCard = ({ id, title, author, description, difficulty, price, category, image }) => {
    const { addToCart, removeFromCart, cartItems } = useContext(CartContext);
    const [imageUrl, setImageUrl] = useState(null);
    const [imageLoaded, setImageLoaded] = useState(false);
    const [inCart, setInCart] = useState(false);
    const [favorited, setFavorited] = useState(false);

    useEffect(() => {
        if (!imageUrl) {
            fetch(`/images/${image}`)
            .then((data) => {
                return data.blob();
            })
            .then((blob) => {
                const url = URL.createObjectURL(blob);
                setImageUrl(url);
                setImageLoaded(true);
            })
            .catch((error) => console.error("Error:", error));
        }
        // Check if item is in cart
        if (cartItems.some((item) => item.id === id)) {
            setInCart(true);
        } else {
            setInCart(false);
        }

        return () => {
            if (imageUrl) {
            URL.revokeObjectURL(imageUrl);
            }
        };
    }, [cartItems, id, image, imageUrl]);
    
    const handleAddToCart = () => {
        addToCart({ id, title, author, description, difficulty, price, category, image });
        toast.success(`${title} added to cart!`)
    }

    const handleRemoveFromCart = () => {
        removeFromCart(id);
        toast.error(`${title} removed from cart!`);
    };

    const handleFavorite = () => {
        setFavorited(!favorited);
        //send a request to backend
    }

    return (
        <div className="pattern-container">
            <div className="pattern-card">
            {/* <Link to={`/patterns/${id}`} > */}
            <h3>{title}</h3>
            {imageLoaded && imageUrl && <img src={imageUrl} alt={title} />}
            <p>Author: {author}</p>
            <p>{description}</p>
            <p>{category.name}</p>
            <p>Difficulty: {difficulty}</p>
            <p>${price}</p>
            {favorited ? (
                <button onClick={handleFavorite}>Unfavorite ❤️</button>
            ) : (
                <button onClick={handleFavorite}>Favorite 🤍</button>
            )}
            {inCart ? (
                <button onClick={handleRemoveFromCart}>Remove from Cart 🛒</button>
            ) : (
                <button onClick={handleAddToCart}>Add to Cart🛒</button>
            )}
            </div>
        </div>
    );
};

export default PatternCard;
