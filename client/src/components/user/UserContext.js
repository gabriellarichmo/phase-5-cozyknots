import React, { createContext, useState, useEffect } from "react";

export const UserContext = createContext();

export const UserProvider = ({ children }) => {
    const [currentUser, setCurrentUser] = useState(null);

    useEffect(() => {
        fetch(`/users`)
            .then((resp) => resp.json())
            .then((data) => setCurrentUser(data.currentUser))
            .catch((err) => console.error("Error fetching current users:", err));
    }, []);

    
    return (
        <UserContext.Provider value={{ currentUser, setCurrentUser }}>
            {children}
        </UserContext.Provider>
    );
};
