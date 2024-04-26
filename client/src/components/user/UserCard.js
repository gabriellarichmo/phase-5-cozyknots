

const UserCard = ({ user }) => {
    return (
        <div className="user-card">
            {/* <img src={user.avatar} alt="User Avatar" className="user-avatar" /> */}
            <div className="user-info">
                <h2>{user.username}</h2>
                <p>{user.name}</p>
                <p>{user.email}</p>
                <p>{user.bio}</p>
            </div>
        </div>
    );
};

export default UserCard