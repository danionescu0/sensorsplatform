import React, { Component } from 'react';
import {
    BrowserRouter as Router,
    Route,
    Switch,
} from 'react-router-dom'

import Admin from '../components/admin';
import LoginPage from './login-page';
import Register from '../components/register';
import ForgotPassword from '../components/forgot-password';
import secure from '../hoc/secure';


class App extends Component {
  render() {
    return (
        <Router>
          <Switch>
            <Route exact path="/admin" component={secure(Admin)}/>
            <Route exact path="/" component={secure(Admin)}/>
            <Route exact path="/login" component={LoginPage}/>
            <Route exact path="/register" component={Register}/>
            <Route exact path="/forgot-password" component={ForgotPassword}/>
          </Switch>
        </Router>
    );
  }
}

export default App;