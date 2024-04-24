import "./Home.css";
// import { useEffect } from "react";
// import toast from "react-hot-toast";
// import { useOutletContext } from "react-router-dom";

function Home() {
//   const { updateCurrentUser } = useOutletContext();

//   useEffect(() => {
//     fetch("/me").then((resp) => {
//       if (resp.ok) {
//         resp.json().then(updateCurrentUser);
//       } else {
//         toast.error("Please log in!");
//       }
//     });
//   }, []);

    return (
        <div className="home-page">
            <>
                <h1 className="title">
                Cozy Knots Co.
                </h1>
            </>
        </div>
    );
}

export default Home;
