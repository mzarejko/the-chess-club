import React from 'react'

function AttackSquare(props){
    
    return (
        <div className='piece' style={{'backgroundColor': 'red'}} onClick={() => {props.takePiece(
                                                                                props.pos,
                                                                                props.oldPos,
                                                                                props.color,
                                                                                props.name)}}>
            {props.piece}
        </div>
    )

}

export default AttackSquare;
