import React, { Component } from 'react'
import './Navbar.css'


/*
    this is HOC component, example of implementation in 
    MENU component
*/

const Navbar = (Child, leftButtonFunc) =>{
    class Bar extends Component {
        
        renderLeftButton = () => {
            if (leftButtonFunc){
                return (
                    <div className="logout">
                        <button onClick={leftButtonFunc}>Logout</button>
                    </div>
                )
            }
        }

        render() {
            return (
                <div>
                    <div>
                        <div className="Navbar">
                            <h1 className="logo-navbar">The chess club</h1>
                        </div>
                        {this.renderLeftButton()}
                    </div>
                    <Child />
                </div>
            )   
        }
    }
    return Bar;
}



export default Navbar; 
