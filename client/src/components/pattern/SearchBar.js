import "./SearchBar.css";

function SearchBar({ searchQuery, setSearchQuery }) {
  return (
    <div className="search-bar">
      <input
        type="text"
        id="search"
        value={searchQuery}
        placeholder="Search patterns ex. Scarves"
        onChange={(e) => setSearchQuery(e.target.value)}
      />
    </div>
  );
}

export default SearchBar;
