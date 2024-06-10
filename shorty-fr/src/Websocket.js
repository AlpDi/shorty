import React, { useState, useCallback, useEffect } from "react";
import useWebSocket, { ReadyState } from "react-use-websocket";
import RangeSlider from "react-range-slider-input";
import "react-range-slider-input/dist/style.css";
import "./Websocket.css";

export const WebSocket = () => {
    //Public API that will echo messages sent to it back to the client
    const [socketUrl, setSocketUrl] = useState("ws://localhost:8765");
    const [messageHistory, setMessageHistory] = useState([]);
    const [value, setValue] = useState([0, 12]);
    const [app, setApp] = useState("1");

    const { sendMessage, lastMessage, readyState } = useWebSocket(socketUrl);

    const handleDragSlider = (v) => {
        console.log(app + "," + v[1]);
        sendMessage(app + "," + v[1]);
    };

    const connectionStatus = {
        [ReadyState.CONNECTING]: "...",
        [ReadyState.OPEN]: "O",
        [ReadyState.CLOSING]: "Closing",
        [ReadyState.CLOSED]: "X",
        [ReadyState.UNINSTANTIATED]: "Uninstantiated",
    }[readyState];

    return (
        <div className="vc-container">
            <span className="connection">{connectionStatus}</span>
            <div className="Slider-container">
                <RangeSlider
                    className="single-thumb"
                    defaultValue={[0, 12]}
                    thumbsDisabled={[true, false]}
                    rangeSlideDisabled={true}
                    onInput={handleDragSlider}
                    max={99}
                    orientation="vertical"
                />
            </div>
            <div className="select-container">
                <select
                    name="Selected App"
                    value={app}
                    onChange={(e) => setApp(e.target.value)}
                >
                    <option value="1">Spotify</option>
                    <option value="2">Discord</option>
                    <option value="3">CS2</option>
                    <option value="4">Destiny 2</option>
                    <option value="5">Minecraft</option>
                    <option value="6">Firefox</option>
                </select>
            </div>
        </div>
    );
};
