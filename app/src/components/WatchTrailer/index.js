import React from 'react';
import Button from "react-bootstrap/Button";

const WatchTrailer = () => {

    const redirectTrailer = () => {
        console.log('Hi')
    }
    
    return (        
        <Button className="main-buttons" variant="info" onClick={redirectTrailer}>Watch Trailer</Button>
    );
    
}

export default WatchTrailer;