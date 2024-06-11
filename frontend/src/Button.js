import "./Button.css";
import React, { useState, useEffect } from "react";

function Buttons() {
    const [data, setData] = useState(null);

    useEffect(() => {
        fetch("http://192.168.178.47:8080/rest/config")
            .then((response) => response.json())
            .then((json) => setData(json))
            .catch((error) => console.error(error));
    }, []);

    return (
        <div className="Button-Container">
            {data &&
                data.buttons.map((button, i) => (
                    <button
                        className="Button"
                        id={i}
                        key={i}
                        onClick={() => {
                            fetch(
                                "http://192.168.178.47:8080/shortcut/".concat(
                                    { button }["button"]
                                )
                            );
                            console.log({ button }["button"]);
                        }}
                    >
                        {button}
                    </button>
                ))}
        </div>
    );
}

export default Buttons;
