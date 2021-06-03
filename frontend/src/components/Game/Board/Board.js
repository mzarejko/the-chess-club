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
                <div className={this.props.isCheck ? 'vischeck' : 'hidde-check'}>
                    <p>CHECK</p>
                </div>
                <div className={this.props.isEnd ? 'visEnd' : 'hidde-end'}>
                    <p>CHECK MATE</p>
                </div>
            </div>    
        )
    }
}

export default Board;
