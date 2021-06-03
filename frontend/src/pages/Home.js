import React, { Component } from 'react';
import Navbar from '../components/Navbar/Navbar';
import {logout} from '../actions/auth';
import GameList from '../components/GameList/GameList';
import './Home.css';


class Home extends Component {
    


    render(){    
        return (
             <div className="home">
                 <GameList />
             </div>
        );
    }
}

export default Navbar(Home, logout);
