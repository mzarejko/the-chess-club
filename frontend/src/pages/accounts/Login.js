import React, { Component } from 'react';
import {login} from '../../actions/auth';
import {urls} from '../../utils/urls'
import InfoDisplayer from '../../components/InfoDisplayer/InfoDisplayer';

class Login extends Component {
    
    constructor(props){
        super(props)
        this.state={
            mail: "",
            password: "",
        };
        this.infoDisplayerRef = React.createRef();
    }

    changeValue = (event) => {
        this.setState({
            [event.target.name]: event.target.value
        });
    }

    submit = () => {
        login(this.state.mail, this.state.password,
        this.infoDisplayerRef.current.updateInfo)
    }
   
    render(){    
        return (
            <div>
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
                    <button onClick={this.submit}>login</button> 
                    <a href={urls.FORGET_PASSWORD}>Don't you remember the password?</a>
                </div>
                <InfoDisplayer ref={this.infoDisplayerRef} />
            </div>
        );
    }
}

export default Login;
