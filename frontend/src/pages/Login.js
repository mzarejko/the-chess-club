import React, { Component } from 'react';
import {login} from '../actions/auth';

class Login extends Component {
    
    constructor(props){
        super(props)
        this.state={
            mail: "",
            password: "",
        };
    }

    changeValue = (event) => {
        this.setState({
            [event.target.name]: event.target.value
        });
    }
   
    render(){    
        return (
            <div>
            <input
               name="mail"
               type="text"
               value={this.state.mail}
               onChange={this.changeValue}
               placeholder = "email"
            /> 
            <input
               name="password"
               type="password"
               value={this.state.password}
               onChange={this.changeValue}
               placeholder = "password"
            />
            <button onClick={()=> {login(this.state.mail, this.state.password)}}>login</button> 
            </div>
        );
    }
}

export default Login;
