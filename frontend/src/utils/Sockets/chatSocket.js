import {frontendToBackendCommands, backendToFrontendCommands} from './SocketCommands';
import {logout, refreshToken} from '../../actions/auth';


class ChatWebSocket {

  constructor(){
    this.callbacks = {}
    this.socket = null
  }
  
  connect(path){
    try{
      this.socket = new WebSocket(path)
    }catch{
      return console.log('error chat connection')
    }

    this.socket.onopen = () => {
      console.log("chat websocket open")
    };

    this.socket.onmessage = (event) => {
      this.updateIncomingMessages(event.data) 
    }

    this.socket.onerror = (event)=> {
      refreshToken(()=>{this.socket = new WebSocket(path)}, logout)
      console.log(event.message)
    }

    this.socket.onclose = (event) => {
      console.log('chat websocket closed')
      this.connect();
    }
  }
  
  disconnect() {
    this.socket.close();
  }
  
  updateIncomingMessages(data){
    data = JSON.parse(data)
    const command = data.command;

    if (command === backendToFrontendCommands.UPDATE_MESSAGES){
      this.callbacks[command](data.messages)
    }

    if (command === backendToFrontendCommands.UPDATE_NEW_MESSAGE){
      this.callbacks[command](data.message)
    }

  }
  
  fetchMessages(chatId){
    const data = {
      command: frontendToBackendCommands.FETCH_MESSAGES,
      chatId: chatId,
    };
    this.sendMessage(data)
  }

  sendChatMessage(message){
    const data = {
      command: frontendToBackendCommands.SEND_NEW_MESSAGE,
      message: message.content,
      chatId: message.chatId
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

  addCallbacks(fetchMessagesCallback, newMessageCallback) {
    this.callbacks[backendToFrontendCommands.UPDATE_MESSAGES] = fetchMessagesCallback;
    this.callbacks[backendToFrontendCommands.UPDATE_NEW_MESSAGE] = newMessageCallback;
  }


  // tell if socket is ready
  status(){
    return this.socket.readyState
  }

}

const chatSocket = new ChatWebSocket()
export default chatSocket;
