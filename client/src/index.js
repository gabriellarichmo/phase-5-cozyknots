import React from "react";
import ReactDOM from "react-dom";
import { BrowserRouter as Router } from "react-router-dom"; // Import BrowserRouter
import { UserProvider } from "./components/user/UserContext";
import App from "./components/App";

ReactDOM.render(
    <Router>
      <UserProvider>
        <App />
      </UserProvider>
    </Router>,
  document.getElementById("root")
);
