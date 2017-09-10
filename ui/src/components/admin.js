import React from 'react';
import {Container} from 'ahoy-reactstrap';

import NavigationContainer from '../containers/navigation-container';

const Admin = () => {
    return (
        <div>
            <NavigationContainer/>
            <div className="content-wrapper">
                <Container fluid>
                    <div>Dashboard content</div>
                </Container>
            </div>
        </div>
    )
};

export default Admin;