import React, { useContext } from "react";
import { UserContext } from "./UserContext";

const UserCard = ({ user }) => {
    const { currentUser } = useContext(UserContext);

    return (
        <div className="user-card">
            {/* <h2>{currentUser ? currentUser.username : "No user logged in"}</h2> */}
      {/* <img src={user.avatar} alt="User Avatar" className="user-avatar" /> */}
            {/* <div className="user-info">
                <h2>{user.username}</h2>
                <p>{user.name}</p>
                <p>{user.email}</p>
                <p>{user.bio}</p>
            </div> */}
        </div>
    );
};

export default UserCard;
