import React, { Component } from 'react';
import gameSocket from "../../utils/Sockets/gameSocket";
import {getGameEndpoint} from '../../utils/paths/endpoints';
import './Game.css';
import Board from './Board';

class Game extends Component {

  constructor(props){
    super(props)
    this.state={
      whiteChess: {},
      blackChess: {}
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
    this.setState({
      whiteChess: white,
      blackChess: black
    });
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
