import { Route, Routes, Router, useNavigate } from "react-router-dom";
import React, { useContext, useEffect } from "react";
import toast, { Toaster } from "react-hot-toast";
import NavBar from "./navigation/NavBar";
import Home from "./Home";
import UserCard from "./user/UserCard";
// import UserDetail from "./user/UserDetail";
import { UserProvider, UserContext } from "./user/UserContext";
import { CartProvider } from "./purchase/CartContext";
import Registration from "./authentication/Registration";
import Community from "./user/Community";
import MyCart from "./purchase/MyCart";
import "./App.css";

function App() {
  const { currentUser } = useContext(UserContext);
  const navigate = useNavigate();

  useEffect(() => {
    if (!currentUser) {
      navigate("/registration");
    }
  }, [currentUser, navigate]);

  return (
    <UserProvider>
      <CartProvider>
        <Toaster />
        <NavBar />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/registration" element={<Registration />} />
          <Route path="/community" element={<Community />} />
          <Route path="/cart" element={<MyCart />} />
          {currentUser && (
            <Route path={`/user/${currentUser.id}`} element={<UserCard />} />
          )}
        </Routes>
      </CartProvider>
    </UserProvider>
  );
}

export default App;
