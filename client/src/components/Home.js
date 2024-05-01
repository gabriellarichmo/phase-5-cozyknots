import "./Home.css";
import PatternCard from "./pattern/PatternCard";
import { useState, useEffect } from "react";
// import toast from "react-hot-toast";
// import { useOutletContext } from "react-router-dom";

function Home({patterns}) {
    const [categories, setCategories] = useState([]);
    const [selectedCategory, setSelectedCategory] = useState("all");
    const [selectedType, setSelectedType] = useState("all");
    const [selectedDifficulty, setSelectedDifficulty] = useState("all");
    const [sortOrder, setSortOrder] = useState("asc");
//   const { updateCurrentUser } = useOutletContext();

    // useEffect(() => {
    //     fetch("/categories")
    //         .then((response) => {
    //             if (!response.ok) {
    //                 throw new Error("Network response was not ok");
    //             }
    //         return response.json();
    //         })
    //         .then((categories) => {
    //             setCategories(categories);
    //         })
    //         .catch((error) => {
    //             console.error("Error fetching categories:", error);
    //         });
    // }, []);


    const getCategoryName = (categoryId) => {
        const category = categories.find((cat) => cat.id === categoryId);
        return category ? category.name : "Unknown";
    };


    const filterPatterns = () => {
        return patterns.filter((pattern) => {
        const categoryName = getCategoryName(pattern.category_id);
        if (
            (selectedCategory === "all" ||
            categoryName === selectedCategory) &&
            (selectedType === "all" || pattern.type === selectedType) &&
            (selectedDifficulty === "all" ||
            pattern.difficulty === selectedDifficulty)
        ) {
            return true;
        }
        return false;
        });
    };


    const sortPatterns = (patterns) => {
        return patterns.sort((a, b) => {
        const patternA = a.title.toLowerCase();
        const patternB = b.title.toLowerCase();
        if (sortOrder === "asc") {
            return patternA.localeCompare(patternB);
        } else {
            return patternB.localeCompare(patternA);
        }
        });
    };

    const handleCategoryChange = (category) => {
        setSelectedCategory(category);
    };

    const handleTypeChange = (type) => {
        setSelectedType(type);
    };

    const handleDifficultyChange = (difficulty) => {
        setSelectedDifficulty(difficulty);
    };

    const handleSortChange = () => {
        setSortOrder(sortOrder === "asc" ? "desc" : "asc");
    };

    const filteredPatterns = filterPatterns();
    const sortedPatterns = sortPatterns(filteredPatterns);

    return (
        <div>
            <h1 className="title">Cozy Knots Co.</h1>
            {/* Type filter */}
            <select onChange={(e) => handleTypeChange(e.target.value)}>
                <option value="all">All Types</option>
                <option value="knit">Knit</option>
                <option value="crochet">Crochet</option>
            </select>

            {/* Category filter */}
            <select onChange={(e) => handleCategoryChange(e.target.value)}>
                <option value="all">All Categories</option>
                <option value="scarf">Scarves</option>
                <option value="sweater">Sweaters</option>
                <option value="hat">Hats</option>
                <option value="mittens">Mittens</option>
                <option value="socks">Socks</option>
                <option value="amigurumi">Amigurumi</option>
            </select>

            {/* Difficulty filter */}
            <select onChange={(e) => handleDifficultyChange(e.target.value)}>
                <option value="all">All Difficulties</option>
                <option value="Beginner">Beginner</option>
                <option value="Intermediate">Intermediate</option>
                <option value="Advanced">Advanced</option>
            </select>

            {/* Sort order */}
            <button onClick={handleSortChange}>
                {sortOrder === "asc" ? "Sort A-Z" : "Sort Z-A"}
            </button>

            {/* Display patterns */}
            <ul>
            {sortedPatterns.map((pattern) => (
                <PatternCard key={pattern.id} {...pattern} />
            ))}
            </ul>
        </div>
    );
}

export default Home;
