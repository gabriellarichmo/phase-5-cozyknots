import { createContext, useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import toast from "react-hot-toast"

export const UserContext = createContext();

export const UserProvider = ({ children }) => {
  const [currentUser, setCurrentUser] = useState(null);
  const navigate = useNavigate();


  useEffect(() => {
    if (!currentUser) {
      fetch("/current_user").then((resp) => {
        if (resp.ok) {
          return resp.json();
        } else {
          throw new Error("Unable to fetch current user.");
        }
      })
      .then((user) => {
        setCurrentUser(user);
        return user;
      })
      .then((user) => {
        fetch(`/users/${user.id}`)
        .then((resp) => {
          if (resp.ok) {
            return resp.json();
          } else {
            throw new Error("Unable to fetch current user ID.");
          }
        })
        .then((userId) => {
          if (user.id !== userId) {
            navigate(`/users/${user.id}`);
          }
        });
      })
      .catch((error) => {
        toast.error("Please log in");
        navigate("/registration");
      });
    }
  }, [currentUser, navigate]);
    
  return (
      <UserContext.Provider value={{ currentUser, setCurrentUser }}>
          {children}
      </UserContext.Provider>
  );
};
