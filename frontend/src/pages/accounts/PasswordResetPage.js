import React, {Component} from 'react';
import {changePassword} from '../../actions/auth';
import queryString from 'query-string';

class PasswordResetPage extends Component {
    
    constructor(props){
        super(props)
        this.state = ({
            password1: "",
            password2: "",
            uidb64: '',
            token: ''
        })
    }

    changeValue = (event) => {
        this.setState({
            ...this.state,
            [event.target.name]: event.target.value
        });
    }
    
    handleSubmit = () => {
        changePassword(
            this.state.password1,
            this.state.password2,
            this.state.uidb64,
            this.state.token
        )
    }

    componentDidMount() {
        // retrive values from url after ? sign
        const values = queryString.parse(this.props.location.search)
        console.log(values.uidb64)
        console.log(values.token)
        try{
            this.setState({
                uidb64: values.uidb64,
            })
            this.setState({
                token: values.token,
            })
        }catch{
            console.log('missing uidb64 and token')
        }
    }
   
    render(){
        return (
            <div>
                <input
                    type="password"
                    name="password1"
                    value={this.state.password1}
                    onChange={this.changeValue}
                    placeholder="new password" 
                />
                <input
                    type="password"
                    name="password2"
                    value={this.state.password2}
                    onChange={this.changeValue}
                    placeholder="new password" 
                />
                <button onClick={this.handleSubmit} >Submit</button>
            </div>
        );
    }
}

export default PasswordResetPage;
