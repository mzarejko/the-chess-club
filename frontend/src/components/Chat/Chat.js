import React, { Component } from 'react';
import chatSocket from "../../utils/Sockets/chatSocket";
import {getChatEndpoint} from '../../utils/paths/API';
import './Chat.css';

class Chat extends Component {

  constructor(props){
    super(props)
    this.state={
      messages: [],
      typedMessage: ""
    }
    
  }
  
  componentDidMount(){
    //connect to socket
    const path = getChatEndpoint(this.props.chatId, localStorage.getItem('access_token'))
    chatSocket.connect(path)
    // get all old messages and set callbacks for websocket
    this.prepareConection(()=> {
      chatSocket.addCallbacks(this.setMessage, this.addMessage)
      chatSocket.fetchMessages(this.props.chatId)
    })

  }

  componentWillUnmount(){
    chatSocket.disconnect()
  }

  prepareConection(callback){
    const component = this
    setTimeout(function() {
      if (chatSocket.status() === 1) {
        console.log("Connection chat is made");
        return callback();
      } else {
        console.log("chat wait for connection...");
        component.prepareConection(callback);
      }
    }, 100);
  }


  updateMessageInput = (input) => {
    this.setState({
      typedMessage: input.target.value
    })
  }


  renderMessages = (messages) => {
    return messages.map((message) => (
      <li key={message.id} className="message"> 
        <p>{message.author}</p>
        <p>{message.content}</p>
        <small>{message.date}</small>
      </li>
    ))
  }


  
  sendMessage = (event) => {
    event.preventDefault();
    const object = {
      content: this.state.typedMessage,
      chatId: this.props.chatId
    };
    chatSocket.sendChatMessage(object)
    this.setState({typedMessage: ""})
  }

  setMessage = messages => {
    this.setState({
      messages: messages.reverse()
    });
  } 

  addMessage = message => {
    this.setState({
      messages: [...this.state.messages, message]
    });
  }

  render() {
    return (
      <div>
        <div>
          <ul className='chat'>
            {this.renderMessages(this.state.messages)}
          </ul>
        </div>
        <form onSubmit={this.sendMessage}>
          <input
            onChange={this.updateMessageInput}
            value={this.state.newMessage}
            type="text"
            placeholder="write your message..."
            />
        </form>
      </div>
    )
  }
}

export default Chat;
