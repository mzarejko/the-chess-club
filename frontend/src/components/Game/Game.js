import React, { Component } from 'react';
import Socket from "../../utils/gameSocket";
import {getGameUrl} from '../../utils/endpoints';
import './game.css';
import Board from './Board';

class Game extends Component {

  constructor(props){
    super(props)
    this.state={
      whiteChess: {},
      blackChess: {}
    }
  }

  prepareConection(callback){
    const component = this
    setTimeout(function() {
      if (Socket.status() === 1) {
        console.log("Connection game is made");
        return callback();
      } else {
        console.log("wait for connection...");
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

  componentDidMount(){
    //connect to socket
    const path = getGameUrl(this.props.gameId)
    Socket.connect(path)
    // get all old messages and set callbacks for websocket
    this.prepareConection(()=> {
      Socket.addCallbacks(this.updatePos)
      Socket.fetchPositions(this.props.gameId)
    });
  }


  componentWillUnmount(){
    Socket.disconnect()
  }



  render() {
    return (
      <Board />
    )
  }
}

export default Game;
