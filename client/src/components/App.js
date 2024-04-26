import React, { useEffect, useState } from "react";
import { Switch, Route, Outlet, useNavigate } from "react-router-dom";
import toast, { Toaster } from "react-hot-toast";
import NavBar from "./navigation/NavBar";
import Home from "./Home";
import UserCard from "./user/UserCard";
import UserDetail from "./user/UserDetail";
import { UserProvider } from "./user/UserContext";
import "./App.css"
import { CartProvider } from "./purchase/CartContext";

// function App() {


//     return (
//       <UserProvider>
//         <CartProvider>
//           <div className="app">
            {/* anything in here will have access to the context */}
            {/* <NavBar />
            <UserCard />
            <UserDetail />
          </div>
        </CartProvider>
      </UserProvider>
    );
} */}

function App() {
  const [currentUser, setCurrentUser] = useState(null);
  const updateCurrentUser = (user) => setCurrentUser(user);
  
  return (
    <>
      <NavBar
        currentUser={currentUser}
        updateCurrentUser={updateCurrentUser}
      />
      <div>
        <Toaster />
      </div>
      <Outlet
        context={{
          currentUser,
          updateCurrentUser,
        }}
      />
    </>
  );
}
export default App;
