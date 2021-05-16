import React from 'react'
import './App.css';

function Piece(props) {

    //Funkcja do rozpoczęcia ruchu pionka
    const dragStart = e => {       
        const target = e.target;

        e.dataTransfer.setData('piece_id', target.id);

        setTimeout(() => {
            target.style.display = 'none';
        }, 0);
    }

    // Funkcja przy przesuwaniu pionka nad projektami (chyba???)
    const dragOver = e => {    
        e.stopPropagation();
    }

    return( 
        // Zwraca pionek z odpowiednim ID i rodzajem pionka zapisanym jako tekst (Wywoływane w Square.js)
       <div id = {props.id} className = 'piece' draggable = 'true'  onDragStart = {dragStart} onDragOver = {dragOver}>{props.piece}</div> 
    )

}

export default Piece;
