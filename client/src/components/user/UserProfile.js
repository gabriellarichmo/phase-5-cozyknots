import { Route, Routes } from "react-router-dom";
import UserCard from "./UserCard";
import EditProfile from "./EditProfile";

const UserProfile = () => {
  return (
    <Routes>
      <Route path="/" element={<UserCard />} />
      <Route path="/edit" element={<EditProfile />} />
    </Routes>
  );
};

export default UserProfile;
