import React, { useEffect, useState } from "react";
import { Switch, Route, Outlet, useNavigate } from "react-router-dom";
import toast, { Toaster } from "react-hot-toast";
import NavBar from "./navigation/NavBar";
import Home from "./Home";
import UserCard from "./user/UserCard";
import "./App.css"

function App() {
  const [currentUser, setCurrentUser] = useState(null);
  const navigate = useNavigate();
  const [users, setUsers] = useState([]);

  useEffect(() => {
    fetch('/users')
      .then(resp => resp.json())
      .then(data => setUsers(data.users))
      .catch(err => console.error('Error fetching users:', err));
  }, []);

  const updateCurrentUser = (user) => setCurrentUser(user);

  return (
    <div className="background">
      <NavBar currentUser={currentUser} updateCurrentUser={updateCurrentUser} />
      <div>
        <Toaster />
      </div>
      <Outlet context={{ users, currentUser, setCurrentUser, updateCurrentUser }} />
    </div>
  );
}

export default App;
