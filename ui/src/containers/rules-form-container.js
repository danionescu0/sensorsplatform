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
        if (!form.rule_name || !form.triggers || !form.rule_text) {
            this.setState({
                errorMessage: "Please complete all fields"
            });
            return;
        }

        postJson(`/users/${Auth.getUserId()}/rules`, form).then(() => {
            this.setState({errorMessage: ""});
            this.props.history.push("/rules");
        }, e => {
            this.setState({errorMessage: "Request failed"});
        });
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