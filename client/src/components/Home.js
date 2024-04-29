import "./Home.css";
import PatternCard from "./pattern/PatternCard";
import SearchBar from "./pattern/SearchBar"
import { useState } from "react";
// import toast from "react-hot-toast";
// import { useOutletContext } from "react-router-dom";

function Home({patterns}) {
    const [searchQuery, setSearchQuery] = useState("");
    // const [sortByAZ, setSortByAZ] = useState(false);
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
    const filteredPatterns = patterns
        .filter((pattern) =>
        pattern.name.toLowerCase().includes(searchQuery.toLowerCase())
        )



    // const handleSortByAZ = () => {
    //     setSortByAZ(!sortByAZ);
    // }; 



    return (
      <div className="home-page">
        <>
          <h1 className="title">Cozy Knots Co.</h1>
          <div className="sort-filter-container">
            <div className="search-container">
              <SearchBar setSearchQuery={setSearchQuery} />
            </div>
            {/* <button className="sort-button" onClick={handleSortByAZ}> */}
              {/*sort here */}
            {/* </button> */}
          </div>
          <div className="patterns-container">
            {patterns.map((pattern) => {
                return <PatternCard key={pattern.id} {...pattern} />;
            })}
          </div>
        </>
      </div>
    );
}

export default Home;
