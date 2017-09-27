import React, { Component } from 'react';
import {withRouter} from 'react-router-dom';

import RulesForm from '../components/rules/rules-form';
import withForm from '../hoc/form';
import {postJson} from "../utils/fetch";
import Auth from "../utils/auth";
import AdminContent from '../components/admin-content';

class RulesFormContainer extends Component {
    constructor(props) {
        super(props);
        this.state = {
            errorMessage: null,
        }
    }

    handleSubmit(e) {
        const {form} = this.props;
        e.preventDefault();
        if (!form.name || !form.trigger) {
            this.setState({
                errorMessage: "Please complete all fields"
            });
            return;
        }

        const rule = Object.assign({}, form, {
            userid: Auth.getUserId()
        });
        console.log(rule);
        // postJson(`/user-sensors/${Auth.getUserId()}`, sensor).then(() => {
        //     this.setState({errorMessage: ""});
        //     this.props.history.push("/sensors");
        // }).catch(e => {
        //     this.setState({errorMessage: "Request failed"});
        // });
    }

    render() {
        const {handleInputChange} = this.props;

        return (
            <AdminContent>
                <RulesForm error={this.state.errorMessage}
                             handleInputChange={handleInputChange}
                             handleSubmit={this.handleSubmit.bind(this)}
                />
            </AdminContent>
        )
    }
}

export default withForm(withRouter(RulesFormContainer));