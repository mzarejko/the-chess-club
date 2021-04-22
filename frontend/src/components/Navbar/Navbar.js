import React, { Component } from 'react'
import './Navbar.css'
import {logout} from '../../actions/auth';
 
class Navbar extends Component {
    
    render() {
        return (
            <div>
                <div className="Navbar">
                    <h1 className="logo-navbar">The chess club</h1>
                </div>
                <div className="logout">
                    <button onClick={logout}>Logout</button>
                </div>
            </div>
        )   
    }
}



export default Navbar; 
