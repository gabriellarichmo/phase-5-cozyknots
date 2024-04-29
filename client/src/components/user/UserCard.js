import React, { useContext, useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { object, string } from "yup";
import { useFormik, Formik } from "formik";
import { UserContext } from "./UserContext";
import "./UserCard.css";
import NewPatternForm from "../pattern/NewPatternForm";
import EditProfile from "./EditProfile";

const UserCard = ({ handleDeleteUser }) => {
  const { currentUser } = useContext(UserContext);
  // const [ editForm, setEditForm ] = useState(false);
  const navigate = useNavigate();

  const handleConfirmDelete = () => {
    if (window.confirm("Are you sure you want to delete your account?")) {
      handleDeleteUser();
    } else {
      navigate(`/users/${currentUser.id}`);
    }
  };

  const buttonStyle = {
    backgroundColor: "red",
  };

  return (
    <>
      <div className="user-profile">
        <EditProfile />
        <NewPatternForm />
        <div className="user-card">
          {currentUser ? (
            <>
              <h2>{currentUser.name}</h2>
              <img
                src={currentUser.avatar}
                alt="User Avatar"
                className="user-avatar"
              />
              <div className="user-info">
                <p>{currentUser.username}</p>
                <p>{currentUser.email}</p>
                <p>{currentUser.bio}</p>
              </div>
              {/* <div>
                <NewPatternForm />
              </div> */}
              {/* <Link to="/edit" className="edit-profile-link">
                Edit Profile
              </Link> */}
              {/* <NewPatternForm /> */}
              {/* <div className="delete-profile">
                <h3>Delete Profile</h3>
                <button style={buttonStyle} onClick={handleConfirmDelete}>
                  {" "}
                  Delete
                </button>
              </div> */}
            </>
          ) : (
            <h2>No user logged in</h2>
          )}
        </div>
      </div>
    </>
  );
};

export default UserCard;
