import React, { Component } from 'react';
import Chat from '../components/Chat/Chat';
import Game from '../components/Game/Game';
import {withRouter} from 'react-router-dom';

class GameRoom extends Component {
    
    
    render(){    
        return (
             <div>
                 <Chat chatId={this.props.match.params.Id} />
                 <Game gameId={this.props.match.params.Id} />
             </div>
        );
    }
}

export default withRouter(GameRoom);
