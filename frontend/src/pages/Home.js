import React, { Component } from 'react';
import Cards from '../components/Cards/Cards';
import Navbar from '../components/Navbar/Navbar';

class Home extends Component {
    
    render(){    
        return (
            <div>
                <Navbar />
                <Cards />
            </div>
        );
    }
}

export default Home;
