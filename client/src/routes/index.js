import { createBrowserRouter } from "react-router-dom";
import App from "../components/App";
import Home from "../components/Home";
import Registration from "../components/authentication/Registration";
import Error from "../components/errors/Error";
import UserCard from "../components/user/UserCard";
import Community from "../components/user/Community";
import PurchaseCard from "../components/purchase/PurchaseCard";
import NewPatternForm from "../components/pattern/NewPatternForm";
import MyCart from "../components/purchase/MyCart";
import EditProfile from "../components/user/EditProfile";

export const router = createBrowserRouter([
  {
    path: "/",
    element: <App />,
    errorElement: <Error />,
    children: [
      {
        path: "/",
        index: true,
        element: <Home />,
      },
      {
        path: "/registration",
        element: <Registration />,
      },
      {
        path: "/users/:userId",
        element: <UserCard />,
        children: [
          {
            path: "/edit",
            element: <EditProfile />,
          },
        ],
      },
      {
        path: "/community",
        element: <Community />,
      },
      {
        path: "/patterns/:patternId",
        element: <PatternCard />
      },
      {
        path: "/patterns",
        element: <NewPatternForm />,
      },
      // {
      //   path: "/purchases/:purchaseId",
      //   element: <PurchaseCard />,
      // },
      {
        path: "/cart",
        element: <MyCart />,
      },
      {
        path: "success/:purchaseId",
        element: <PurchaseCard />,
      },
    ],
  },
]);
