import React, {Component} from 'react';
import { Route, Redirect } from 'react-router-dom';

class PrivateRoute extends Component {
    
    render() {
        if (localStorage.getItem('access_token') != null) {
            return <Route {...this.props} />
        }
        return <Redirect to='/' />
    }
}

export default PrivateRoute;
