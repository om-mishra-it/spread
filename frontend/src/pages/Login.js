import React, { useState } from "react";
import { loginUser } from "../api/auth";
import { useNavigate } from "react-router-dom";
import { useRecoilState } from "recoil";
import { authState } from "../state/authState";

function Login() {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [auth, setAuth] = useRecoilState(authState);
    const navigate = useNavigate();

    const handleLogin = async () => {
        try {
            const data = await loginUser(email, password);
            setAuth({ isAuthenticated: true, user: data.user, token: data.access_token });
            navigate("/reading");
        } catch (error) {
            console.error("Login failed", error);
        }
    };

    return (
        <div>
            <h2>Login</h2>
            <input type="email" placeholder="Email" value={email} onChange={(e) => setEmail(e.target.value)} />
            <input type="password" placeholder="Password" value={password} onChange={(e) => setPassword(e.target.value)} />
            <button onClick={handleLogin}>Login</button>
        </div>
    );
}

export default Login;
