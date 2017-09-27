import React, { Component } from 'react';

import {getJson} from "../utils/fetch";
import Auth from "../utils/auth";
import AdminContent from '../components/admin-content';
import RulesList from '../components/rules/rules-list';

class RulesPage extends Component {
    constructor(props) {
        super(props);
        this.state = {
            rules: []
        };
    }

    componentDidMount() {
        this.loadRules();
    }

    loadRules() {
        getJson(`/users/${Auth.getUserId()}/rules`).then(rules => {
            this.setState({rules: rules});
        });
    }

    render() {
        return (
            <AdminContent>
                <RulesList rules={this.state.rules}/>
            </AdminContent>
        )
    }
}

export default RulesPage;