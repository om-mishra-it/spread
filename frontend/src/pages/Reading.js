import React, { useState } from "react";

function Reading() {
    const [wpm, setWpm] = useState(200);
    const [readingMode, setReadingMode] = useState("rsvp");

    return (
        <div>
            <h2>Reading Mode</h2>
            <label>Words Per Minute (WPM): </label>
            <input type="number" value={wpm} onChange={(e) => setWpm(e.target.value)} />

            <div>
                <label>Mode: </label>
                <select value={readingMode} onChange={(e) => setReadingMode(e.target.value)}>
                    <option value="rsvp">Rapid Serial Visual Presentation</option>
                    <option value="highlight">Highlighted Text</option>
                </select>
            </div>

            <button>Start Reading</but
