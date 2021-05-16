import React from 'react'
import Square from './Square'
import './App.css';

function SquarePiece(props) {

    return(
        <div className = 'field' style={{'backgroundColor': 'red'}}>{props.piece}</div> 
    )

}

export default SquarePiece
