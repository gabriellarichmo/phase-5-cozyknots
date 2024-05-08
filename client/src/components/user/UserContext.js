import { createContext, useState, useEffect, useContext } from "react";
import { useNavigate } from "react-router-dom";
import toast from "react-hot-toast"

export const UserContext = createContext();

export const UserProvider = ({ children }) => {
  const [currentUser, setCurrentUser] = useState(null);
  const navigate = useNavigate();

  useEffect(() => {
    const fetchCurrentUser = async () => {
      try {
        const response = await fetch("/current_user");
        if (response.ok) {
          const user = await response.json();
          setCurrentUser(user);
          console.log(currentUser)
        } else {
          throw new Error("Unable to fetch current user.");
        }
      } catch (error) {
        console.error("Error fetching current user:", error);
        toast.error("Please log in");
        if (!currentUser) {
          navigate("/registration");
        }
      }
    };

    fetchCurrentUser();
  }, [navigate]);

  const handleLogout = async () => {
    try {
      await fetch("/logout", { method: "DELETE" });
      setCurrentUser(null);
      toast("Come back soon!", { icon: "👋" });
      navigate("/");
    } catch (error) {
      console.error("Error logging out:", error);
      toast.error("Failed to log out");
    }
  };

  const handleDeleteUser = async () => {
    try {
      await fetch(`/users/${currentUser.id}`, { method: "DELETE" });
      handleLogout();
    } catch (error) {
      console.error("Error deleting user:", error);
      toast.error("Failed to delete user");
    }
  };

  return (
      <UserContext.Provider value={{ currentUser, setCurrentUser, handleLogout, handleDeleteUser }}>
          {children}
      </UserContext.Provider>
  );
};

export const useUserContext = () => useContext(UserContext);