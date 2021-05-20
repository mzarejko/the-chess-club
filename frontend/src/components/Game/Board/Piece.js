import React, { Component } from 'react';

class Piece extends Component {

    
    render() {
        return (
            <div className='piece' onClick={() => this.props.findReachableSquare(this.props.pos, 
                                                                                  this.props.name,
                                                                                  this.props.color)}>
                <img src={this.props.image} alt={this.props.name} />
            </div>
        )
    }

}

export default Piece;

