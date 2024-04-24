import React, { useEffect, useState } from "react";
import { Switch, Route } from "react-router-dom";
import NavBar from "./navigation/NavBar";
import Home from "./Home";

function App() {
  return (
    <div>
      <NavBar />
      <Home />
    </div>
  );
}

export default App;
