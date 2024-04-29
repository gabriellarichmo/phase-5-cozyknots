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
        } else {
          throw new Error("Unable to fetch current user.");
        }
      } catch (error) {
        console.error("Error fetching current user:", error);
        toast.error("Please log in");
        navigate("/registration");
      }
    };

    fetchCurrentUser();
  }, [navigate]);

  // useEffect(() => {
  //   if (!currentUser) {
  //     fetch("/current_user").then((resp) => {
  //       if (resp.ok) {
  //         return resp.json();
  //       } else {
  //         throw new Error("Unable to fetch current user.");
  //       }
  //     })
  //     .then((user) => {
  //       setCurrentUser(user);
  //       return user;
  //     })
  //     .then((user) => {
  //       fetch(`/users/${user.id}`)
  //       .then((resp) => {
  //         if (resp.ok) {
  //           return resp.json();
  //         } else {
  //           throw new Error("Unable to fetch current user ID.");
  //         }
  //       })
  //       .then((userId) => {
  //         if (user.id !== userId) {
  //           navigate(`/users/${user.id}`);
  //         }
  //       });
  //     })
  //     .catch((error) => {
  //       toast.error("Please log in");
  //       navigate("/registration");
  //     });
  //   }
  // }, [currentUser, navigate]);

  // const handleEditUser = (formData) => {
  //   try {
  //     fetch(`/users/${currentUser.id}`, {
  //       method: "PATCH",
  //       headers: {
  //         "Content-Type": "application/json",
  //       },
  //       body: JSON.stringify(formData),
  //     }).then((resp) => {
  //       if (resp.ok) {
  //         resp.json().then((user) => {
  //           setCurrentUser(user);
  //         });
  //       } else {
  //         return resp
  //           .json()
  //           .then((errorObj) => toast.error(errorObj.message));
  //       }
  //     });
  //   } catch (err) {
  //     throw err;
  //   }
  // };
  const handleEditUser = async (formData) => {
    try {
      const response = await fetch(`/users/${currentUser.id}`, {
        method: "PATCH",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(formData),
      });
      if (response.ok) {
        const updatedUser = await response.json();
        setCurrentUser(updatedUser);
        toast.success("Profile updated successfully");
      } else {
        const errorObj = await response.json();
        toast.error(errorObj.message);
      }
    } catch (error) {
      console.error("Error editing user:", error);
      toast.error("Failed to update profile");
    }
  };

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
  // const handleLogout = () => {
  //   fetch("/logout", { method: "DELETE" })
  //     .then(() => {
  //       setCurrentUser(null);
  //       toast("Come back soon!", {
  //         icon: "👋",
  //       });
  //       navigate("/");
  //     })
  //     .catch((err) => console.log(err));
  // };

  // const handleDeleteUser = () => {
  //   fetch(`/users/${currentUser.id}`, { method: "DELETE" })
  //     .then(handleLogout);
  // };
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
      <UserContext.Provider value={{ currentUser, setCurrentUser, handleLogout, handleEditUser, handleDeleteUser }}>
          {children}
      </UserContext.Provider>
  );
};

export const useUserContext = () => useContext(UserContext);