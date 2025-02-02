import { Link } from "react-router-dom";

function Navbar() {
  return (
    <nav style={{ padding: "1rem", background: "#333", color: "white" }}>
      <h2>Spread</h2>
      <div>
        <Link to="/" style={{ color: "white", marginRight: "10px" }}>Home</Link>
        <Link to="/login" style={{ color: "white", marginRight: "10px" }}>Login</Link>
        <Link to="/reading" style={{ color: "white" }}>Start Reading</Link>
      </div>
    </nav>
  );
}

export default Navbar;
