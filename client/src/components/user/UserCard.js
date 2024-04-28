import React, { useContext } from "react";
import { UserContext } from "./UserContext";

const UserCard = () => {
    const { currentUser } = useContext(UserContext);

    return (
        <div className="user-card">
            {currentUser ? (
                <>
                    <h2>{currentUser.username}</h2>
                    <img src={currentUser.avatar} alt="User Avatar" className="user-avatar" />
                    <div className="user-info">
                        <p>{currentUser.name}</p>
                        <p>{currentUser.email}</p>
                        <p>{currentUser.bio}</p>
                    </div>
                </>
            ) : (
                <h2>No user logged in</h2>
            )}
        </div>
    );
};

export default UserCard;
