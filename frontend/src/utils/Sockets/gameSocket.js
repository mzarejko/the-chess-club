import {SocketCommands} from './SocketCommands';

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

    if (command === SocketCommands.positions){
      this.callbacks[command](data.white_pos, data.black_pos)
    }
    if (command === SocketCommands.squares){
      this.callbacks[command](data.squares)
    }
    

  }
  
  fetchPositions(gameId){
    const data = {
      command: "fetch_positions",
      gameId: gameId,
    };
    this.sendMessage(data)
  }
  
  getReachableSquare(gameId, pos, piece){
    const data = {
      command: "get_reachable_squares",
      gameId: gameId,
      position: pos,
      piece: piece
    }  
    this.sendMessage(data)
  }

  movePawn(pos, color, pawn, id){
    const data = {
      command: "move_pawn",
      color: color,
      pawn: pawn,
      id_pawn: id
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
