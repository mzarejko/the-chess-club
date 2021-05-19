import './Board.css'
import React, { Component } from 'react';

class Board extends Component {

    render() {
        return (
            <div className = 'container'>
                <div className = 'grid'>
                    {this.props.positions.map((item, id) => {
                        return (
                            <div className="field" key={id}>
                                {item}
                            </div>
                        )
                    })}
                </div>
            </div>    
        )
    }
}

export default Board;
