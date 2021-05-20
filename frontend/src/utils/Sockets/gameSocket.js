import {SocketCommands} from './SocketCommands';
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

    if (command === SocketCommands.NEW_POSITIONS){
      this.callbacks[command](data.white_pos, data.black_pos)
    }
    if (command === SocketCommands.REACHABLE_SQUARE){
      this.callbacks[command](data.squares, data.oldPos, data.color, data.name)
    }
  }
  
  
  fetchPositions(gameId){
    const data = {
      command: "fetch_positions",
      gameId: gameId,
    };
    this.sendMessage(data)
  }
  
  getReachableSquare(gameId, pos, name, color){
    const data = {
      command: "get_reachable_squares",
      gameId: gameId,
      position: pos,
      name: name,
      color: color
    }  
    this.sendMessage(data)
  }

  movePawn(gameId, pos, old_pos, color, name){
    const data = {
      command: "move_piece",
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

  addCallbacks(PositionsCallback, SquareCallback) {
    this.callbacks["positions"] = PositionsCallback;
    this.callbacks["squares"] = SquareCallback;
  }

  // tell if socket is ready
  status(){
    return this.socket.readyState
  }

}

const gameSocket = new GameWebSocket()
export default gameSocket;
