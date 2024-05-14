import { useState, useContext, useEffect } from "react";
import "./Registration.css";
import { object, string } from "yup";
import { useFormik } from "formik";
import toast from "react-hot-toast";
import { useNavigate } from "react-router-dom";
import { UserContext } from "../user/UserContext";

const signupSchema = object({
  username: string()
    .max(20, "Username must be max of 20 characters")
    .required("Username is required"),
  email: string().email().required("Email is required"),
  password: string()
    .min(5, "Password must be at least 5 characters long")
    .matches(
      /[a-zA-Z0-9]/,
      "Passwords can only contain latin numbers and letters"
    )
    .required("Password is required"),
});

const signinSchema = object({
  username: string()
    .max(20, "Username must be max of 20 characters")
    .required("Username is required"),
  password: string()
    .min(5, "Password must be at least 5 characters long")
    .matches(
      /[a-zA-Z0-9]/,
      "Passwords can only contain latin numbers and letters"
    )
    .required("Password is required"),
});

const initialValues = {
  username: "",
  email: "",
  password: "",
};

const Registration = () => {
  const [login, setLogin] = useState(false);
  const requestedUrl = login ? "/login" : "/signup";
  const navigate = useNavigate();
  const { setCurrentUser } = useContext(UserContext);

  useEffect(() => {
    const checkAuthentication = async () => {
      try {
        const response = await fetch("/current_user");
        if (response.ok) {
          const user = await response.json();
          setCurrentUser(user);
          navigate("/");
        }
      } catch (error) {
        console.error("Error checking authentication:", error);
      }
    };

    checkAuthentication();
  }, []);

  const formik = useFormik({
    initialValues,
    validationSchema: login ? signinSchema : signupSchema,
    onSubmit: async (formData) => {
      try {
        const response = await fetch(requestedUrl, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(formData),
        });

        const data = await response.json();
        if (response.ok) {
          setCurrentUser(data);
          navigate("/");
          toast("Welcome to Cozy Knots Co.", {
            icon: "🧶",
          });
        } else {
          if (data.errors) {
            for (const [key, value] of Object.entries(data.errors)) {
              toast.error(`${key}: ${value}`);
            }
          } else {
            toast.error(data.message || "An error occurred");
          }
        }
      } catch (error) {
        console.error("Error logging in:", error);
        toast.error("Error logging in. Please try again later.");
      }
    },
  });


  //   initialValues,
  //   validationSchema: login ? signinSchema : signupSchema,
  //   onSubmit: async (formData) => {

  //     fetch(requestedUrl, {
  //       method: "POST",
  //       headers: {
  //         "Content-Type": "application/json",
  //       },
  //       body: JSON.stringify({
  //         username: formData.username,
  //         email: formData.email,
  //         password_hash: formData.password,
  //       }),
  //     }).then((resp) => {
  //       console.log("Login response:", resp);
  //       if (resp.ok) {
  //         resp
  //           .json()
  //           .then((user) => {
  //             setCurrentUser(user);
  //             navigate("/");
  //             toast("Cozy Knots Co.", {
  //               icon: "🧶",
  //             });
  //           });
  //       } else {
  //         return resp.json().then((errorObj) => toast.error(errorObj.message || errorObj.error));
  //       }
  //     })
  //     .catch((error) => {
  //       console.error("Error logging in:", error);
  //       toast.error("Error logging in. Please try again later.");
  //     });
  //   },
  // });

  return (
    <div className="registration-page">
      <div className="reg-form-body">
        <div className="reg-form-containter">
          <h2 className="reg-banner">Log in or Sign up for Cozy Knots Co.!</h2>
          <form id="regForm" onSubmit={formik.handleSubmit}>
            {!login && (
              <>
                <label>Email: </label>
                <input
                  type="text"
                  name="email"
                  onChange={formik.handleChange}
                  onBlur={formik.handleBlur}
                  value={formik.values.email}
                  className="reg-input"
                />
                {formik.errors.email && formik.touched.email && (
                  <div className="email-error">{formik.errors.email}</div>
                )}
              </>
            )}
            <label>Username: </label>
            <input
              type="text"
              name="username"
              onChange={formik.handleChange}
              onBlur={formik.handleBlur}
              value={formik.values.username}
              className="reg-input"
            />
            {formik.errors.username && formik.touched.username && (
              <div className="username-error">{formik.errors.username}</div>
            )}
            <label>Password: </label>
            <input
              type="password"
              name="password"
              onChange={formik.handleChange}
              onBlur={formik.handleBlur}
              value={formik.values.password}
              className="reg-input"
            />
            {formik.errors.password && formik.touched.password && (
              <div className="password-error">{formik.errors.password}</div>
            )}
            <input
              type="submit"
              className="button-55-1"
              value={login ? "Login!" : "Signup!"}
            />
          </form>
          <div className="swap">
            <h3>{login ? "Not a member?" : "Already a member?"}</h3>
            <button
              className="button-55"
              onClick={() => setLogin((currentState) => !currentState)}
            >
              {login ? "Join our community" : "Login"}
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Registration;
