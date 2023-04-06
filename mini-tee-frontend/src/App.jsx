import React from "react";
import { Container, Grid, css } from "@mui/material";
import "./App.css";
import { ChatWindow } from "./components/ChatWindow";

const style = {
  display: "flex",
  flexDirection: "row",
  justifyContent: "spaceBetween",
};

function App() {
  return (
    <div className="App">
      <main style={style}>
        <div style={{ width: "50%", height: "100vh" }}>
          <div>Left hand side</div>
        </div>
        <div style={{ width: "50%", height: "100vh" }}>
          <ChatWindow />
        </div>
      </main>
    </div>
  );
}

export default App;
