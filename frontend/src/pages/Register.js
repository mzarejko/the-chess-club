import React, {Component} from 'react';
import {register} from '../actions/auth';

class Register extends Component {
    
    constructor(props){
        super(props)
        this.state = ({
            username: "",
            email: "",
            password1: "",
            password2: "",
        })
    }

    changeValue = (event) => {
        this.setState({
            ...this.state,
            [event.target.name]: event.target.value
        });
    }
    
    handleSubmit = () => {
        register(
            this.state.username,
            this.state.email,
            this.state.password1,
            this.state.password2
        )
    }
   
    render(){
        return (
            <div>
                <input
                    type="text"
                    name="username"
                    value={this.state.username}
                    onChange={this.changeValue}
                    placeholder="username" 
                />
                <input
                    type="text"
                    name="email"
                    value={this.state.mail}
                    onChange={this.changeValue}
                    placeholder="mail" 
                />
                <input
                    type="text"
                    name="password1"
                    value={this.state.password1}
                    onChange={this.changeValue}
                    placeholder="password" 
                />
                <input
                    type="text"
                    name="password2"
                    value={this.state.password2}
                    onChange={this.changeValue}
                    placeholder="password" 
                />
                <button onClick={this.handleSubmit} >Submit</button>
            </div>
        );
    }
}

export default Register;
