import React, { Component } from 'react';
import Square from './Square'
import './App.css';

class Board extends Component {
    
    renderBoard = () => {
        let fields = [];
        for (let i = 1; i<=64; i++)
        {
            if(i >= 9 && i <= 16)
            {   
                fields.push(<Square id = {i}/>)
            }    

            else if(i == 1 || i == 8)
            {
                fields.push(<Square id = {i}/>)   
            }
            else if(i == 2 || i == 7)
            {
                fields.push(<Square id = {i}/>)   
            }
            else if(i == 3 || i == 6)
            {
                fields.push(<Square id = {i}/>)   
            }
            else if(i == 4)
            {
                fields.push(<Square id = {i}/>)   
            }
            else if(i == 5)
            {
                fields.push(<Square id = {i}/>)   
            }

            else if(i >= 49 && i <= 56)
            {
                fields.push(<Square id = {i}/>)  
            }

            else if(i == 57 || i == 64)
            {
                fields.push(<Square id = {i}/>)  
            }

            else if(i == 58 || i == 63)
            {
                fields.push(<Square id = {i}/>)  
            }

            else if(i == 59 || i == 62)
            {
                fields.push(<Square id = {i}/>)  
            }
            
            else if(i == 60)
            {
                fields.push(<Square id = {i}/>)  
            }
  
            else if(i == 61)
            {
                fields.push(<Square id = {i}/>)  
            }

            else{
                fields.push(<Square id = {i}/>)  
            }
        }

        return fields
    }

    render() {
        return (
            <div className = 'container'>
                <div className = 'grid'>
                    {this.renderBoard()}
                </div>
            </div>    
        )
    }
}

export default Board
