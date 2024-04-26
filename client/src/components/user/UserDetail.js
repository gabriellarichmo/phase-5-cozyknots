import React, { useContext } from "react";
import { UserContext } from "./UserContext";

const UserDetail = () => {
    // const { currentUser } = useContext(UserContext);

    return (
        <div className="user-detail">
        {/* {currentUser ? (
            <p>User Detail for: {currentUser.username}</p>
        ) : (
            // user details here
            <p>No user logged in</p>
        )} */}
        </div>
    );
};

export default UserDetail;
