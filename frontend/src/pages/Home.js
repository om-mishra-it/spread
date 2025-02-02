import React from "react";
import { Link } from "react-router-dom";

function Home() {
    return (
        <div>
            <h1>Welcome to Spread</h1>
            <p>Your AI-powered reading assistant.</p>
            <Link to="/login">Login</Link> | <Link to="/register">Register</Link>
        </div>
    );
}

export default Home;
