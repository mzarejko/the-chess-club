import React, { Component } from 'react';

class Piece extends Component {

    
    render() {
        return (
            <div className='piece' onClick={() => this.props.findReachableSquares(this.props.pos, this.props.alt)}>
                <img src={this.props.image} alt={this.props.alt} />
            </div>
        )
    }

}

export default Piece;

