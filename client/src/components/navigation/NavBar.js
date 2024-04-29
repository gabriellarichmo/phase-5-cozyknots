import toast, { Toaster } from "react-hot-toast";
import { Link, NavLink, useNavigate } from "react-router-dom";
import { useState } from "react";
import "./NavBar.css";
import { useContext } from "react";
import { UserContext } from "../user/UserContext";

const NavBar = () => {
    const { currentUser, handleLogout } = useContext(UserContext);

    return (
      <div>
        <Toaster />
        <div className="nav">
          <nav className="navbar">
            <NavLink to="/">Home</NavLink>
            <br></br>
            {!currentUser && (
              <>
                <NavLink to="/registration">Login</NavLink>
                <br></br>
              </>
            )}
            {currentUser && (
              <>
                <NavLink to={`/users/${currentUser.id}`}>My Profile</NavLink>
                <br></br>
                <NavLink to="/community">Community</NavLink>
                <br></br>
                <NavLink to="/cart">My Cart</NavLink>
                <br></br>
                <NavLink onClick={handleLogout}>Logout</NavLink>
              </>
            )}
          </nav>
        </div>
      </div>
    );
};

export default NavBar;

//   return (
//     <>
//       <Toaster />
//       <div className="navigation">
//         <nav className="navbar">
//           <NavLink to="/">Cozy Knots Co.</NavLink> <br></br>
//           <>
//             {currentUser ? (
//               <div className="container">
//                 <NavLink to={`/users/${currentUser.id}`}>Profile</NavLink>{" "}
//                 <br></br>
//                 <NavLink onClick={handleLogout}>Logout</NavLink>
//               </div>
//             ) : (
//               <Link to={"/registration"}>Login / Sign up</Link>
//             )}
//           </>
//         </nav>
//       </div>
//     </>
//   );