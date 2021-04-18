import React, { Component } from 'react';
import {urls} from '../utils/urls';
import {history} from '../utils/history';

class Menu extends Component {
    
    render() {
        return (
             <div>
                <h2>MENU</h2>
                <ul>
                    <div>
                        <a href={urls.LOGIN}>login</a>
                    </div>
                    <div>
                        <a href={urls.REGISTER}>register</a>
                    </div>
                </ul>
            </div>
        )
    }
}

export default Menu;
