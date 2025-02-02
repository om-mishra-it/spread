import React from "react";
import ReactDOM from "react-dom/client";
import { RecoilRoot } from "recoil";
import AppRoutes from "./routes";
import "./styles.css";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
    <RecoilRoot>
        <AppRoutes />
    </RecoilRoot>
);
