import React, {Component} from 'react';
import {sendMailToChangePassword} from '../../actions/auth';

class ForgetPasswordPage extends Component {
    
    constructor(props){
        super(props)
        this.state = ({
            email: ""
        })
    }

    changeValue = (event) => {
        this.setState({
            ...this.state,
            [event.target.name]: event.target.value
        });
    }
    
    handleSubmit = () => {
        sendMailToChangePassword(
            this.state.email,
        )
    }
   
    render(){
        return (
            <div>
                <input
                    type="mail"
                    name="email"
                    value={this.state.email}
                    onChange={this.changeValue}
                    placeholder="email" 
                />
                <button onClick={this.handleSubmit} >Submit</button>
            </div>
        );
    }
}

export default ForgetPasswordPage;
