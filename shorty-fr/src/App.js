import "./App.css";
import Buttons from "./Button.js";
import { WebSocket } from "./Websocket.js";
import React, { useState, useEffect } from "react";

function App() {
    return (
        <div className="App">
            <Buttons />
            <WebSocket />
            <WebSocket />
        </div>
    );
}

export default App;
