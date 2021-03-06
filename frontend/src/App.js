import React, {Component} from 'react';
import {Router, Switch, Route} from 'react-router-dom';
import Login from './pages/accounts/Login';
import Register from './pages/accounts/Register';
import Menu from './pages/Menu';
import Home from './pages/Home';
import GameRoom from './pages/GameRoom';
import AnonymousRoom from './pages/AnonymousRoom';
import {urls} from './utils/paths/urls';
import './App.css';
import {history} from './utils/history';
import PrivateRoute from './components/Routes/PrivateRoute';
import PasswordResetPage from './pages/accounts/PasswordResetPage';
import ForgetPasswordPage from './pages/accounts/ForgetPasswordPage';

class App extends Component {
  

  render(){
    return (
      <div>
        <Router history={history}>
          <Switch>
            <PrivateRoute path={urls.HOME} component={Home} />
            <PrivateRoute path={urls.GAME} component={GameRoom} />
            <Route path={urls.ANONYMOUS_GAME} component={AnonymousRoom} />
            

            <Route exact path={urls.LOGIN} component={Login} />
            <Route exact path={urls.REGISTER} component={Register} />
            <Route path={urls.RESET_PASSWORD} component={PasswordResetPage} />
            <Route exact path={urls.FORGET_PASSWORD} component={ForgetPasswordPage} />
            <Route exact path={urls.MENU} component={Menu} />
          </Switch>
        </Router>
      </div>
    );  
  }
}

export default App;


