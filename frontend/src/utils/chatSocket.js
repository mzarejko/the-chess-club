
class WebSocketInstance {

  constructor(){
    this.callbacks = {}
    this.socket = null
  }
  
  connect(path){
    try{
      this.socket = new WebSocket(path)
    }catch{
      return console.log('error connection')
    }

    this.socket.onopen = () => {
      console.log("websocket open")
    };

    this.socket.onmessage = (event) => {
      this.updateIncomingMessages(event.data) 
    }

    this.socket.onerror = (event)=> {
      console.log(event.message)
    }

    this.socket.onclose = (event) => {
      console.log('websocket closed')
      this.connect();
    }
  }
  
  disconnect() {
    this.socket.close();
  }
  
  updateIncomingMessages(data){
    data = JSON.parse(data)
    const command = data.command;

    if (command === "messages"){
      this.callbacks[command](data.messages)
    }

    if (command === "new_message"){
      this.callbacks[command](data.message)
    }

  }
  
  fetchMessages(chatId){
    const data = {
      command: "fetch_messages",
      chatId: chatId,
    };
    this.sendMessage(data)
  }

  sendChatMessage(message){
    const data = {
      command: "new_message",
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
    this.callbacks["messages"] = fetchMessagesCallback;
    this.callbacks["new_message"] = newMessageCallback;
  }

  // tell if socket is ready
  status(){
    return this.socket.readyState
  }

}

const Socket = new WebSocketInstance()
export default Socket;
