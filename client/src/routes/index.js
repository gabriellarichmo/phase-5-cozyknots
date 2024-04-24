import { createBrowserRouter } from "react-router-dom";
import App from "../components/App";
import Home from "../components/Home";
import Registration from "../components/authentication/Registration";
import Error from "../components/errors/Error";
import UserCard from "../components/user/UserCard";
import Community from "../components/user/Community";

export const router = createBrowserRouter([
  {
    path: "/",
    element: <App />,
    errorElement: <Error />,
    children: [
      {
        path: "/",
        index: true,
        element: <Home />
      },
      {
        path: "/registration",
        element: <Registration />
      },
      {
        path: "users/:userId",
        element: <UserCard />
      },
      {
        path: "/community",
        element: <Community />
      },
    ],
  },
]);
