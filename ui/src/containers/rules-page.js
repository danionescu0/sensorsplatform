import React, { Component } from 'react';

import AdminContent from '../components/admin-content';
import RulesList from '../components/rules/rules-list';

class RulesPage extends Component {
    render() {
        return (
            <AdminContent>
                <RulesList/>
            </AdminContent>
        )
    }
}

export default RulesPage;