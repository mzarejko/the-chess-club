import React, { Component } from 'react';
import gameSocket from "../../utils/Sockets/gameSocket";
import {getGameEndpoint} from '../../utils/paths/API';
import Board from './Board/Board';
import Piece from './Board/Piece';
import NormalSquare from './Board/NormalSquare';
import ReachableSquare from './Board/ReachableSquare';
import AttackSquare from './Board/AttackSquare';

class Game extends Component {

  constructor(props){
    super(props)
    this.state = {
      numPos: 64,
      board: [],
      cleanBoard: [],
      isCheck: false,
      isEnd: false
    }
  }

  componentDidMount(){
    //connect to socket
    const path = getGameEndpoint(this.props.gameId, localStorage.getItem('access_token'))
    gameSocket.connect(path)
    // get all old messages and set callbacks for websocket
    this.prepareConection(()=> {
      gameSocket.addCallbacks(this.updatePos, this.updateReachable, this.chack, this.endGame, this.unchack)
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
 

  findReachableSquare = (pos, name, color) => {
    gameSocket.fetchReachableSquare(this.props.gameId, pos, name, color)
  }
  
  updateReachable = (reachable_squares, attack_squares, oldPos, color, name) => {
    // before each update of reachable squares board have to be clean, without previous reachable squares
    let refPos = [...this.state.cleanBoard]
    reachable_squares.forEach((pos) => {
      refPos[pos] = <ReachableSquare setPiece={this.setPiece}
                                     pos={pos}
                                     oldPos={oldPos}
                                     color={color}
                                     name={name} />
    })

    attack_squares.forEach((pos) => {
      const piece = refPos[pos]
      refPos[pos] = <AttackSquare takePiece={this.takePiece}
                                  piece={piece}
                                  pos={pos}
                                  oldPos={oldPos}
                                  color={color}
                                  name={name} />
    })

    this.setState({
      board: refPos
    }, console.log(refPos))
  }
  
  takePiece = (pos, old_pos, color, name) => {
    gameSocket.removePiece(this.props.gameId, pos, old_pos, color, name)
  }
  setPiece = (pos, old_pos, color, name) => {
    gameSocket.movePiece(this.props.gameId, pos, old_pos, color, name)
  }

  updatePos = (white, black) => {
    let whiteNames = Object.keys(white)
    let blackNames = Object.keys(black)
    let new_board = Array(this.state.numPos).fill(<NormalSquare />)

    //set white piece
    whiteNames.forEach((name) => {
      const piece = white[name]
      piece.position.forEach((pos)=>{
        new_board[pos] = <Piece findReachableSquare={this.findReachableSquare}
                          image={piece.image}
                          name={name}
                          pos={pos}
                          color={piece.color} />
      });
    });

    // set black piece
    blackNames.forEach((name) => {
      const piece = black[name]
      piece.position.forEach((pos)=>{
        new_board[pos] = <Piece findReachableSquare={this.findReachableSquare}
                          image={piece.image}
                          name={name}
                          pos={pos}
                          color={piece.color} />
      });
    });

  

    this.setState({
      cleanBoard: new_board,
      board: new_board
    },()=> console.log(this.state.board))
  }

  chack = () => {
    this.setState({
      isCheck: true
    }, console.log('check'))
    
  }

  unchack = () => {
    this.setState({
      isCheck: false
    }, console.log('uncheck'))
  }

  endGame = () => {
    this.setState({
      isEnd: true
    })
  }

  componentWillUnmount(){
    gameSocket.disconnect()
  }



  render() {
    return (
      <div>
        <Board positions={this.state.board} isCheck={this.state.isCheck}
                                            isEnd={this.state.isEnd}/>
      </div>
    )
  }
}

export default Game;
