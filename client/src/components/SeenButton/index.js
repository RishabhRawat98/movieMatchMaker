import React from 'react';
import Button from "react-bootstrap/Button";

const SeenButton = () => {

    const addToSeen = e => {
        e.preventDefault()
    }
    
    return (        
        <Button className="main-buttons" variant="info" onClick={addToSeen}>Mark as seen</Button>
    );
    
}

export default SeenButton;