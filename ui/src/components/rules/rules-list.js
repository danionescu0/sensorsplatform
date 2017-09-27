import React from 'react';
import {Link} from 'react-router-dom';
import {
    Button,
    Table
} from 'ahoy-reactstrap';

import ContentBox from '../content-box';

const RulesList = ({rules}) => {
    return (
        <ContentBox title="Rules list" footer={getTableFooter()} icon="fa fa-th-list" headerClass="bg-success text-white">
            <Table hover>
                <thead>
                <tr>
                    <th>Id</th>
                    <th>Rule name</th>
                    <th>Rule</th>
                    <th>Triggers</th>
                </tr>
                </thead>
                <tbody>
                {renderRows(rules)}
                </tbody>
            </Table>
        </ContentBox>
    )
};

const renderRows = rules => rules.map(rule => (
    <tr key={rule.id}>
        <td>{rule.id}</td>
        <td>{rule.name}</td>
        <td>{rule.rule_text}</td>
        <td>{rule.triggers.join(" | ")}</td>
    </tr>
));

const getTableFooter = () => {
    return (
        <Link to="/rules/add" >
            <Button color="success">
                <i className="fa fa-plus" aria-hidden="true"/> &nbsp; Add Rule
            </Button>
        </Link>
    );
};

export default RulesList;