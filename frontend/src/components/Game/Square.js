import React from 'react'
import Piece from './Piece'
import './App.css';

function Square(props) {

    // Funkcja do upuszczania pionków
    const drop = e => {
        e.preventDefault();
        const piece_id = e.dataTransfer.getData('piece_id');

        const piece = document.getElementById(piece_id);
        piece.style.display = 'block';
        
        e.target.appendChild(piece);
    }
    // Funkcja przy przesuwaniu pionka nad projektami (chyba???)
    const dragOver = e => {
        e.preventDefault();
    }
    // Wywoływane w Board.js, kiedy board tworzy plansze wywołuje z podanym id pola, na podstawie tego dobierany jest kolor pola, oraz wywoływane utworzenie pionka w Piece.js (podawane jest id Pionka - takie samo jak Id pola, ale z przedrostkiem 'P', oraz rodzaj pionka)
    if(props.id == 1){
        return(
            <div id = {props.id} className = 'field' style={{'backgroundColor': 'white'}} onDrop = {drop} onDragOver = {dragOver}><Piece id = {'P' + props.id} piece = {'♜'}/></div> 
        )
    }
    else if(props.id == 2){
        return(
            <div id = {props.id} className = 'field' style={{'backgroundColor': 'brown'}} onDrop = {drop} onDragOver = {dragOver}><Piece id = {'P' + props.id} piece = {'♞'}/></div> 
        )
    }
    else if(props.id == 3){
        return(
            <div id = {props.id} className = 'field' style={{'backgroundColor': 'white'}} onDrop = {drop} onDragOver = {dragOver}><Piece id = {'P' + props.id} piece = {'♝'}/></div> 
        )
    }
    else if(props.id == 4){
        return(
            <div id = {props.id} className = 'field' style={{'backgroundColor': 'brown'}} onDrop = {drop} onDragOver = {dragOver}><Piece id = {'P' + props.id} piece = {'♛'}/></div> 
        )
    }
    else if(props.id == 5){
        return(
            <div id = {props.id} className = 'field' style={{'backgroundColor': 'white'}} onDrop = {drop} onDragOver = {dragOver}><Piece id = {'P' + props.id} piece = {'♚'}/></div> 
        )
    }
    else if(props.id == 6){
        return(
            <div id = {props.id} className = 'field' style={{'backgroundColor': 'brown'}} onDrop = {drop} onDragOver = {dragOver}><Piece id = {'P' + props.id} piece = {'♝'}/></div> 
        )
    }
    else if(props.id == 7){
        return(
            <div id = {props.id} className = 'field' style={{'backgroundColor': 'white'}} onDrop = {drop} onDragOver = {dragOver}><Piece id = {'P' + props.id} piece = {'♞'}/></div> 
        )
    }
    else if(props.id == 8){
        return(
            <div id = {props.id} className = 'field' style={{'backgroundColor': 'brown'}} onDrop = {drop} onDragOver = {dragOver}><Piece id = {'P' + props.id} piece = {'♜'}/></div> 
        )
    }
    else if(props.id % 2 == 1 && props.id > 8 && props.id < 17){
        return(
            <div id = {props.id} className = 'field' style={{'backgroundColor': 'brown'}} onDrop = {drop} onDragOver = {dragOver}><Piece id = {'P' + props.id} piece = {'♟'}/></div> 
        )
    }
    else if(props.id % 2 == 0 && props.id > 8 && props.id < 17){
        return(
            <div id = {props.id} className = 'field' style={{'backgroundColor': 'white'}} onDrop = {drop} onDragOver = {dragOver}><Piece id = {'P' + props.id} piece = {'♟'}/></div> 
        )
    }
    else if(props.id % 2 == 0 && props.id > 16 && props.id < 25){        
        return(
            <div id = {props.id} className = 'field' style={{'backgroundColor': 'brown'}} onDrop = {drop} onDragOver = {dragOver}></div> 
        )
    }
    else if(props.id % 2 == 1 && props.id > 16 && props.id < 25){        
        return(
            <div id = {props.id} className = 'field' style={{'backgroundColor': 'white'}} onDrop = {drop} onDragOver = {dragOver}></div> 
        )
    }
    else if(props.id % 2 == 0 && props.id > 24 && props.id < 33){        
        return(
            <div id = {props.id} className = 'field' style={{'backgroundColor': 'white'}} onDrop = {drop} onDragOver = {dragOver}></div> 
        )
    }
    else if(props.id % 2 == 1 && props.id > 24 && props.id < 33){        
        return(
            <div id = {props.id} className = 'field' style={{'backgroundColor': 'brown'}} onDrop = {drop} onDragOver = {dragOver}></div> 
        )
    }
    else if(props.id % 2 == 0 && props.id > 32 && props.id < 41){        
        return(
            <div id = {props.id} className = 'field' style={{'backgroundColor': 'brown'}} onDrop = {drop} onDragOver = {dragOver}></div> 
        )
    }
    else if(props.id % 2 == 1 && props.id > 32 && props.id < 41){        
        return(
            <div id = {props.id} className = 'field' style={{'backgroundColor': 'white'}} onDrop = {drop} onDragOver = {dragOver}></div> 
        )
    }
    else if(props.id % 2 == 0 && props.id > 40 && props.id < 49){        
        return(
            <div id = {props.id} className = 'field' style={{'backgroundColor': 'white'}} onDrop = {drop} onDragOver = {dragOver}></div> 
        )
    }
    else if(props.id % 2 == 1 && props.id > 40 && props.id < 49){        
        return(
            <div id = {props.id} className = 'field' style={{'backgroundColor': 'brown'}} onDrop = {drop} onDragOver = {dragOver}></div> 
        )
    }
    else if(props.id % 2 == 0 && props.id > 48 && props.id < 57){
        return(
            <div id = {props.id} className = 'field' style={{'backgroundColor': 'brown'}} onDrop = {drop} onDragOver = {dragOver}><Piece id = {'P' + props.id} piece = {'♙'}/></div> 
        )
    }
    else if(props.id % 2 == 1 && props.id > 48 && props.id < 57){
        return(
            <div id = {props.id} className = 'field' style={{'backgroundColor': 'white'}} onDrop = {drop} onDragOver = {dragOver}><Piece id = {'P' + props.id} piece = {'♙'}/></div> 
        )
    }
    else if(props.id == 57){
        return(
            <div id = {props.id} className = 'field' style={{'backgroundColor': 'brown'}} onDrop = {drop} onDragOver = {dragOver}><Piece id = {'P' + props.id} piece = {'♖'}/></div> 
        )
    }
    else if(props.id == 58){
        return(
            <div id = {props.id} className = 'field' style={{'backgroundColor': 'white'}} onDrop = {drop} onDragOver = {dragOver}><Piece id = {'P' + props.id} piece = {'♘'}/></div> 
        )
    }
    else if(props.id == 59){
        return(
            <div id = {props.id} className = 'field' style={{'backgroundColor': 'brown'}} onDrop = {drop} onDragOver = {dragOver}><Piece id = {'P' + props.id} piece = {'♗'}/></div> 
        )
    }
    else if(props.id == 60){
        return(
            <div id = {props.id} className = 'field' style={{'backgroundColor': 'white'}} onDrop = {drop} onDragOver = {dragOver}><Piece id = {'P' + props.id} piece = {'♕'}/></div> 
        )
    }
    else if(props.id == 61){
        return(
            <div id = {props.id} className = 'field' style={{'backgroundColor': 'brown'}} onDrop = {drop} onDragOver = {dragOver}><Piece id = {'P' + props.id} piece = {'♔'}/></div> 
        )
    }
    else if(props.id == 62){
        return(
            <div id = {props.id} className = 'field' style={{'backgroundColor': 'white'}} onDrop = {drop} onDragOver = {dragOver}><Piece id = {'P' + props.id} piece = {'♗'}/></div> 
        )
    }
    else if(props.id == 63){
        return(
            <div id = {props.id} className = 'field' style={{'backgroundColor': 'brown'}} onDrop = {drop} onDragOver = {dragOver}><Piece id = {'P' + props.id} piece = {'♘'}/></div> 
        )
    }
    else if(props.id == 64){
        return(
            <div id = {props.id} className = 'field' style={{'backgroundColor': 'white'}} onDrop = {drop} onDragOver = {dragOver}><Piece id = {'P' + props.id} piece = {'♖'}/></div> 
        )
    }
}

export default Square;
