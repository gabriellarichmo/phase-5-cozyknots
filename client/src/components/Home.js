import "./Home.css";
import PatternCard from "./pattern/PatternCard";
// import { useEffect } from "react";
// import toast from "react-hot-toast";
// import { useOutletContext } from "react-router-dom";

function Home({patterns}) {
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
                {patterns.map((pattern) => {
                    return <PatternCard key={pattern.id} {...pattern} />;
                })}
            </>
        </div>
    );
}

export default Home;
