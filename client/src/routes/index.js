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
    // path: "/",
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
        path: "/user/:userId",
        element: <UserCard />,
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

@app.route("/registration")
@app.route("/user/:<int:id>")
@app.route("/")
@app.route("/cart")
@app.route("/success/:<int:id>")
@app.route("/community")


def index(id=0):
    return render_template("index.html")