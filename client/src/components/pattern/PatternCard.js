import { Link } from "react-router-dom"

const PatternCard = () => {
    return (
        <div className="pattern-card">
            <button>
            <Link to={`/patterns/${id}`} >
                <h3>{title}</h3>
                {/* {imageLoaded && imageUrl && <img src={imageUrl} alt={name} />} */}
            </Link>
        </button>
        </div>
    );
};

export default PatternCard;
