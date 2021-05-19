import React from 'react'

function AttackSquare(props){
    
    return (
        <div onClick={this.props.removePiece} 
             style={{'backgroundColor': 'red'}} />
    )

}

export default AttackSquare;
