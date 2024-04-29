import { Link } from "react-router-dom"

const PatternCard = ({ id, title, author, description, difficulty }) => {
    return (
        <div className="pattern-card">
            <button>
            <Link to={`/patterns/${id}`} >
                <h3>{title}</h3>
                <p>{author}</p>
                <p>{description}</p>
                <p>{difficulty}</p>

                {/* {imageLoaded && imageUrl && <img src={imageUrl} alt={name} />} */}
            </Link>
        </button>
        </div>
    );
};

export default PatternCard;
