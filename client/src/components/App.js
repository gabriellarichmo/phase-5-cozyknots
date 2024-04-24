import React, { useEffect, useState } from "react";
import { Switch, Route, Outlet, useNavigate } from "react-router-dom";
import toast, { Toaster } from "react-hot-toast";
import NavBar from "./navigation/NavBar";
import Home from "./Home";
import "./App.css"

function App() {
  const [currentUser, setCurrentUser] = useState(null);
  const navigate = useNavigate();
  

  const updateCurrentUser = (user) => setCurrentUser(user);

  return (
    <div className="background">
      <NavBar currentUser={currentUser} updateCurrentUser={updateCurrentUser} />
      <div>
        <Toaster />
      </div>
      <Outlet context={{ currentUser, setCurrentUser, updateCurrentUser }} />
    </div>
  );
}

export default App;
