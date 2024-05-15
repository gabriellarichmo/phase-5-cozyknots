import { createContext, useState, useEffect, useContext } from "react";
import { useNavigate } from "react-router-dom";
import toast from "react-hot-toast"

export const UserContext = createContext();

export const UserProvider = ({ children }) => {
  const [currentUser, setCurrentUser] = useState(null);
  const [loading, setLoading] = useState(true);
  const navigate = useNavigate();

  useEffect(() => {
    const fetchCurrentUser = async () => {
      try {
        const response = await fetch(
          "/current_user", {
            method: "GET",
            headers: {
              "Content-Type": "application/json"
            },
          });
          if (!response.ok) {
            throw new Error(
              `Error: ${response.status} ${response.statusText}`
            );
          }          
          const user = await response.json();
          setCurrentUser(user);
        } catch (error) {
          console.error("Unable to fetch current user.", error);
        } finally {
          setLoading(false);
        }
      };
    fetchCurrentUser();
  }, []);

  const handleLogout = async () => {
    try {
      await fetch("/logout", {
        method: "DELETE",
      });
      setCurrentUser(null);
      toast("Come back soon!", { icon: "👋" });
      navigate("/");
    } catch (error) {
      console.error("Error logging out:", error);
      toast.error("Failed to log out");
    }
  };

//fix
  const handleDeleteUser = () => {
    fetch(`/users/${currentUser.id}`, {
      method: "DELETE",
    }).then(handleLogout);
  };
  // const handleDeleteUser = () => {
  //   fetch(`/users/${currentUser.id}`, { method: "DELETE" });
  // } catch (error) {
  //     console.error("Error deleting user:", error);
  //     toast.error("Failed to delete user");
  //   }
  // };

  return (
      <UserContext.Provider value={{ loading, currentUser, setCurrentUser, handleLogout, handleDeleteUser }}>
          {children}
      </UserContext.Provider>
  );
};

export const useUserContext = () => useContext(UserContext);