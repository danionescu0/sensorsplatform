import React, { Component } from 'react';
import {
    BrowserRouter as Router,
    Route,
    Switch,
} from 'react-router-dom'

import AdminPage from  './admin-page'
import LoginPage from './login-page';
import RegisterPage from './register-page';
import ForgotPassword from '../components/forgot-password';
import SensorsListPage from './sensors-list-page';
import SensorPage from './sensor-page';
import SensorsFormContainer from './sensors-form-container';
import RulesFormContainer from './rules-form-container';
import RulesPage from './rules-page';
import secure from '../hoc/secure';


class App extends Component {
  render() {
    return (
        <Router>
          <Switch>
            <Route exact path="/admin" component={secure(AdminPage)}/>
            <Route exact path="/" component={secure(AdminPage)}/>
            <Route exact path="/rules" component={secure(RulesPage)}/>
            <Route exact path="/rules/add" component={secure(RulesFormContainer)}/>
            <Route exact path="/sensors" component={secure(SensorsListPage)}/>
            <Route exact path="/sensors/add" component={secure(SensorsFormContainer)}/>
            <Route path="/sensors/:id" component={secure(SensorPage)}/>
            <Route exact path="/login" component={LoginPage}/>
            <Route exact path="/register" component={RegisterPage}/>
            <Route exact path="/forgot-password" component={ForgotPassword}/>
          </Switch>
        </Router>
    );
  }
}

export default App;