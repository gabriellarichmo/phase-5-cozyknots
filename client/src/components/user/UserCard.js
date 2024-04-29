import { useContext } from "react";
import { UserContext } from "./UserContext";
import "./UserCard.css";
import NewPatternForm from "../pattern/NewPatternForm";
import EditProfile from "./EditProfile";

const UserCard = () => {
  const { currentUser } = useContext(UserContext);

  return (
    <>
      <div className="user-profile">
        <EditProfile />
        <NewPatternForm />
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
      </div>
    </>
  );
};

export default UserCard;
