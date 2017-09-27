import React from 'react';
import {Link} from 'react-router-dom';
import {
    Button,
    Table
} from 'ahoy-reactstrap';

import ContentBox from '../content-box';

const RulesList = ({rules}) => {
    return (
        <ContentBox title="Rules list" footer={getTableFooter()} icon="fa th-list" headerClass="bg-success text-white">
            <Table hover>
                <thead>
                <tr>
                    <th>Id</th>
                    <th>Name</th>
                    <th>Triggers</th>
                </tr>
                </thead>
                <tbody>
                {renderRows([])}
                </tbody>
            </Table>
        </ContentBox>
    )
};

const renderRows = rules => {
    return null;
};

const getTableFooter = () => {
    return (
        <Link to="/sensors/add" >
            <Button color="success">
                <i className="fa fa-plus" aria-hidden="true"/> &nbsp; Add Rule
            </Button>
        </Link>
    );
};

export default RulesList;