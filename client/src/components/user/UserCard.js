import { useContext, useState, useEffect } from "react";
import { UserContext } from "./UserContext";
import "./UserCard.css";
import NewPatternForm from "../pattern/NewPatternForm";
import EditProfile from "./EditProfile";
import PurchaseCard from "../purchase/PurchaseCard";
import PatternCard from "../pattern/PatternCard";
import PurchaseCardTwo from "../purchase/PurchaseCardTwo";

const UserCard = () => {
  const { currentUser } = useContext(UserContext);
  const [favoritedPatterns, setFavoritedPatterns] = useState([]);

  useEffect(() => {
    if (currentUser) {
      fetch(`/favorites/${currentUser.id}`)
        .then((response) => {
          if (!response.ok) {
            throw new Error("Failed to fetch favorited patterns");
          }
          return response.json();
        })
        .then((data) => {
          if (data && data.favoritedPatterns) {
            console.log("Favorited patterns:", data.favoritedPatterns);
            setFavoritedPatterns(data.favoritedPatterns);
          } else {
            console.error("Favorited patterns data is missing or invalid:", data);
          }
        })
        .catch((error) => {
          console.error("Error fetching favorited patterns:", error);
        });
    }
  }, [currentUser]);


  return (
    <>
      <div className="user-profile">
        <div className="user-card">
          {currentUser ? (
            <>
              <h2>{currentUser.name}</h2>
              <img
                src={currentUser.avatar}
                alt="User Avatar"
                className="user-avatar"
              />
              <div className="user-info">
                <p>{currentUser.username}</p>
                <p>{currentUser.email}</p>
                <p>{currentUser.bio}</p>
              </div>
            </>
          ) : (
            <h2>No user logged in</h2>
          )}
        </div>
        <EditProfile {...currentUser} />
        <NewPatternForm />
        {currentUser?.purchases?.map(p => <PurchaseCardTwo {...p} key={p.id} />)}
        {favoritedPatterns.length > 0 && (
          <div className="favorited-patterns">
            <h3>Favorited Patterns:</h3>
            {favoritedPatterns?.map((pattern) => (
              <PatternCard key={pattern.id} {...pattern} />
            ))}
          </div>
        )}
      </div>
    </>
  );
};

export default UserCard;
