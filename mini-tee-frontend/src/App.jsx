import React from 'react';
import { Container, Grid, css } from '@mui/material';
import './App.css';
import { ChatWindow } from './components/ChatWindow';
import { InfoBoard } from './components/InfoBoard';


const style = {
  display: "flex",
  flexDirection: "row",
justifyContent: "spaceBetween"
}

function App() {
  return (
    <div className="App">
      <h1>MiniTee Chatbot</h1>
      <main style={style}>

        <InfoBoard />
        <ChatWindow />
      </main>
    </div>
  );
}

export default App;
