import React, { Component } from 'react';

class Board extends Component {

    constructor(props){
        super(props)

        const height = 8
        const width = 8

        this.state = {
            positions: Array(height).fill().map(() => Array(width))
        }
    }


    render() {
        return (
            <div className = 'container'>
            </div>    
        )
    }
}

export default Board
