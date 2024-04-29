import { Link } from "react-router-dom"
import "./PatternCard.css"

const PatternCard = ({ id, title, author, description, difficulty, price }) => {
    return (
        <div className="pattern-card">
            <button>
            <Link to={`/patterns/${id}`} >
                <h3>{title}</h3>
                <p>{author}</p>
                <p>{description}</p>
                <p>{difficulty}</p>
                <p>{price}</p>

                {/* {imageLoaded && imageUrl && <img src={imageUrl} alt={name} />} */}
            </Link>
        </button>
        </div>
    );
};

export default PatternCard;
