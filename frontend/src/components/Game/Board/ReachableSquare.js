import React from 'react'

function ReachableSquare(props){
    
    return (
        <div className='field reach'  onClick={() => props.setPiece(props.pos,
                                                                    props.oldPos,
                                                                    props.color,
                                                                    props.name)} /> 
    )

}

export default ReachableSquare;
