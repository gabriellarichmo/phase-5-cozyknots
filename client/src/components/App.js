import { useContext, useEffect } from "react";
import { Routes, Route, useNavigate } from "react-router-dom";
import toast, { Toaster } from "react-hot-toast";
import NavBar from "./navigation/NavBar";
import Home from "./Home";
import UserCard from "./user/UserCard";
import Registration from "./authentication/Registration";
import Community from "./user/Community";
import MyCart from "./purchase/MyCart";
import { UserProvider, useUserContext } from "./user/UserContext";
import { CartProvider } from "./purchase/CartContext"
import "./App.css";

function App() {
  const { currentUser } = useUserContext();
  const navigate = useNavigate();

  useEffect(() => {
    if (!currentUser) {
      navigate("/registration");
    }
  }, [currentUser, navigate]);

  return (
    <div>
      <Toaster />
      <NavBar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/registration" element={<Registration />} />
        <Route path="/community" element={<Community />} />
        <Route path="/cart" element={<MyCart />} />
        {currentUser && (
          <Route path={`/users/${currentUser.id}`} element={<UserCard />} />
        )}
      </Routes>
    </div>
  );
}

export default function AppWrapper() {
  return (
    <UserProvider>
      <CartProvider>
        <App />
      </CartProvider>
    </UserProvider>
  );
}
