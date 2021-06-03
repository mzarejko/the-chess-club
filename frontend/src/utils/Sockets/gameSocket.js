import {frontendToBackendCommands, backendToFrontendCommands} from './SocketCommands';
import {logout, refreshToken} from '../../actions/auth';

class GameWebSocket {

  constructor(){
    this.callbacks = {}
    this.socket = null
  }
  
  connect(path){
    try{
      this.socket = new WebSocket(path)
    }catch{
      return console.log('error game connection')
    }

    this.socket.onopen = () => {
      console.log("Game socket open")
    };

    this.socket.onmessage = (event) => {
      this.updateIncomingPositions(event.data) 
    }

    this.socket.onerror = (event)=> {
      refreshToken(()=>{this.socket = new WebSocket(path)}, logout)
      console.log(event.message)
    }

    this.socket.onclose = (event) => {
      console.log('game websocket closed')
      this.connect();
    }
  }
  
  disconnect() {
    this.socket.close();
  }
  
  updateIncomingPositions(data){
    data = JSON.parse(data)
    const command = data.command;

    if (command === backendToFrontendCommands.UPDATE_POSITIONS){
      this.callbacks[command](data.white_pos, data.black_pos)
    }
    else if (command === backendToFrontendCommands.UPDATE_REACHABLE_SQUARES){
      this.callbacks[command](data.reachable_squares, data.attack_squares, data.oldPos, data.color, data.name)
    }
    else if (command === backendToFrontendCommands.END_GAME){
      this.callbacks[command](data.winner)
    }
    else if (command === backendToFrontendCommands.CHECK){
      this.callbacks[command]()
    }
    else if (command === backendToFrontendCommands.UNCHECK){
      this.callbacks[command]()
    }
  }
  
  
  fetchPositions(gameId){
    const data = {
      command: frontendToBackendCommands.FETCH_POSITIONS,
      gameId: gameId,
    };
    this.sendMessage(data)
  }
  
  fetchReachableSquare(gameId, pos, name, color){
    const data = {
      command: frontendToBackendCommands.FETCH_REACHABLE_SQUARES,
      gameId: gameId,
      pos: pos,
      name: name,
      color: color
    }  
    this.sendMessage(data)
  }

  movePiece(gameId, pos, old_pos, color, name){
    const data = {
      command: frontendToBackendCommands.MOVE_PIECE,
      gameId: gameId,
      color: color,
      name: name,
      pos: pos,
      old_pos: old_pos

    }
    this.sendMessage(data)
  }

  removePiece(gameId, pos, old_pos, color, name){
    const data = {
      command: frontendToBackendCommands.REMOVE_PIECE,
      gameId: gameId,
      color: color,
      name: name,
      pos: pos,
      old_pos: old_pos
    }
    this.sendMessage(data)
  }

  sendMessage(data){
    try{
      this.socket.send(JSON.stringify({...data}));
    }catch(error){
      console.log(error.message)
    }
  }

  addCallbacks(PositionsCallback, SquareCallback, CheckCallback, EndCallback, unCheckCallback) {
    this.callbacks[backendToFrontendCommands.UPDATE_POSITIONS] = PositionsCallback;
    this.callbacks[backendToFrontendCommands.UPDATE_REACHABLE_SQUARES] = SquareCallback;
    this.callbacks[backendToFrontendCommands.END_GAME] = EndCallback;
    this.callbacks[backendToFrontendCommands.CHECK] = CheckCallback;
    this.callbacks[backendToFrontendCommands.UNCHECK] = unCheckCallback;
  }

  // tell if socket is ready
  status(){
    return this.socket.readyState
  }

}

const gameSocket = new GameWebSocket()
export default gameSocket;
