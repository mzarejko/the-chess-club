import React, { Component } from 'react';
import Chat from '../components/Chat/Chat';
import {withRouter} from 'react-router-dom';

class Game extends Component {
    
    
    render(){    
        return (
             <div>
                 <Chat chatId={this.props.match.params.gameId} />
             </div>
        );
    }
}

export default withRouter(Game);
