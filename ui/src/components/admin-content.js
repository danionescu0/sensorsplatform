import React from 'react';
import {Container} from 'ahoy-reactstrap';

import NavigationContainer from '../containers/navigation-container';

const AdminContent = (props) => {
    return (
        <div>
            <NavigationContainer/>
            <div className="content-wrapper">
                <Container fluid>
                    {props.children}
                </Container>
            </div>
        </div>
    )
};

export default AdminContent;