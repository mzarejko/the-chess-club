import React, { Component } from 'react'
import './Buttons.css' 
import {Link} from 'react-router-dom';

const BUTTONS = Object.freeze({
    STYLE: ['primary', 'outline'],
    SIZE: ['medium', 'large']
});


class Button extends Component {
    
    constructor(props){
        super(props)

        this.state = {
            onClick: this.props.onClick,
            type: this.props.type,
            children: this.props.children,
            buttonStyle: this.props.buttonStyle,
            buttonSize: this.props.buttonSize
        }
    }
    
        
    
    checkButtonStyle = () => {
      const style = BUTTONS.STYLE.includes(this.state.buttonStyle) ? 
            this.state.buttonStyle : BUTTONS.STYLE[0];
        return style;
    }
    
    checkButtonSize = () => {
      const size = BUTTONS.SIZE.includes(this.state.buttonSize) ? 
            this.state.buttonSize : BUTTONS.SIZE[0];
        return size;
    }

    render() {
        return (
            <Link to='#' className='btn-mobile'>
                <button className={`btn ${this.checkButtonStyle()} ${this.checkButtonSize()}`}
                    onClick={this.state.onClick} type={this.state.type}>
                    {this.state.children}
                </button>
            </Link>
        )   
    }
}


export default Button; 
