import React from "react";
import App from "./components/App";
import "./index.css";
import { createRoot } from "react-dom/client";
import { RouterProvider } from "react-router-dom";
import { router } from "./routes";

const container = document.getElementById("root");
const root = createRoot(container);
root.render(<App />);

root.render(<RouterProvider router={router} />);