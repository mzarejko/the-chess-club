import React, { Component } from 'react';
import gameSocket from "../../utils/Sockets/gameSocket";
import {getGameEndpoint} from '../../utils/paths/API';
import Board from './Board/Board';
import Piece from './Board/Piece';
import NormalSquare from './Board/NormalSquare';
import ReachableSquare from './Board/ReachableSquare';

class Game extends Component {

  constructor(props){
    super(props)
    this.state = {
      numPos: 64,
      board: []
    }
  }

  componentDidMount(){
    //connect to socket
    const path = getGameEndpoint(this.props.gameId, localStorage.getItem('access_token'))
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
  
  findReachableSquare = (pos, piece) => {
    gameSocket.getReachableSquare(this.props.gameId, pos, piece)
  }
  
  updateReachable = (reachable) => {
    const new_board = [...this.state.board]
    reachable.forEach((square, id) => {
      new_board[square] = <ReachableSquare />
    })
  }
  
  updatePos = (white, black) => {
    let whitePieces = Object.keys(white)
    let blackPieces = Object.keys(black)
    let new_board = Array(this.state.numPos).fill(<NormalSquare />)

    //set white piece
    whitePieces.forEach((piece, id) => {
      const ref = white[piece]
      ref.position.forEach((pos, id)=>{
        new_board[pos] = <Piece findReachableSquare={this.findReachableSquare}
                          image={white[piece].image}
                          alt={piece} />
      });
    });

    // set black piece
    blackPieces.forEach((piece, id) => {
      const ref = black[piece]
      ref.position.forEach((pos, id)=>{
        new_board[pos] = <Piece findReachableSquare={this.findReachableSquare}
                          image={black[piece].image}
                          alt={piece}
                          pos={pos}/>
      });
    });


    this.setState({
      board: new_board
    },()=> console.log(this.state.board))
  }


  componentWillUnmount(){
    gameSocket.disconnect()
  }



  render() {
    return (
      <Board positions={this.state.board} />
    )
  }
}

export default Game;
