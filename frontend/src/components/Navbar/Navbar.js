import React, { Component } from 'react'
import './Navbar.css'
import Button from '../Buttons/Buttons';


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
                        <Button buttonSize='medium'    
                            buttonStyle='outline' 
                            onClick={leftButtonFunc}>
                                logout
                        </Button>
                    </div>
                )
            }
        }

        render() {
            return (
                <div>
                     <div className="Navbar">
                         <h1 className="logo-navbar">The chess club</h1>
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
