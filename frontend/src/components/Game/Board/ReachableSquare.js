import React from 'react'

function ReachableSquare(props){
    
    return (
        <div  onClick={this.props.setPiece} 
             style={{'backgroundColor': 'yellow'}} />
    )

}

export default ReachableSquare;
