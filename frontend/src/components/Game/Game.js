import React, { Component } from 'react';
import gameSocket from "../../utils/Sockets/gameSocket";
import {getGameEndpoint} from '../../utils/paths/API';
import './Game.css';
import Board from './Board';
import {pawns} from './board_settings';
import {color_chess} from './board_settings';

class Game extends Component {

  constructor(props){
    super(props)
    const height = 8
    const width = 8

    this.state={
      whiteChess: null,
      blackChess: null,
      positions: Array(height).fill().map(() => Array(width))
    }
  }

  componentDidMount(){
    //connect to socket
    const path = getGameEndpoint(this.props.gameId, localStorage.getItem('access_token'))
    console.log(path)
    gameSocket.connect(path)
    // get all old messages and set callbacks for websocket
    this.prepareConection(()=> {
      gameSocket.addCallbacks(this.updatePos)
      gameSocket.fetchPositions(this.props.gameId)
    });
  }

  prepareConection(callback){
    const component = this
    setTimeout(function() {
      if (gameSocket.status() === 1) {
        console.log("Connection game is made");
        return callback();
      } else {
        console.log("game wait for connection...");
        component.prepareConection(callback);
      }
    }, 100);
  }
  
  updatePos = (white, black) => {
    console.log(white)
  }


  componentWillUnmount(){
    gameSocket.disconnect()
  }



  render() {
    return (
      <Board whiteChess={this.state.whiteChess} 
             blackChess={this.state.blackChess}/>
    )
  }
}

export default Game;
