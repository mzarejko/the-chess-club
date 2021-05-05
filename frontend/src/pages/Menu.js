import React, { Component } from 'react';
import Cards from '../components/Cards/Cards';
import Navbar from '../components/Navbar/Navbar';

class Menu extends Component {
    
    render() {
        return (
            <div>
                <Cards />
            </div>
        )
    }
}

export default Navbar(Menu, null);
