import React from 'react';
import {Router, Switch, Route} from 'react-router-dom';
import Login from './pages/Login';
import Register from './pages/Register';
import Menu from './pages/Menu';
import Home from './pages/Home';
import {urls} from './utils/urls';
import './App.css';
import {history} from './utils/history';
import PrivateRoute from './components/Routes/PrivateRoute';

function App() {
  return (
    <Router history = {history}>
      <Switch>
        <Route path={urls.LOGIN} component={Login} />
        <Route path={urls.REGISTER} component={Register} />
        <Route exact path={urls.MENU} component={Menu} />
        <PrivateRoute path={urls.HOME} component={Home} />
      </Switch>
    </Router>
  );
}

export default App;


