import React from 'react';
import {
    Row,
    Col,
    Card,
    CardHeader,
    CardBody,
    CardTitle,
} from 'ahoy-reactstrap';

const SensorBox = ({children, title, icon, headerClass}) => {
    return (
        <Row>
            <Col lg="12">
                <Card className="mb-5">
                    <CardHeader className={headerClass}>
                        <CardTitle>
                            <i className={icon} aria-hidden="true"/> &nbsp; {title}
                        </CardTitle>
                    </CardHeader>
                    <CardBody>
                        {children}
                    </CardBody>
                </Card>
            </Col>
        </Row>
    )
};

export default SensorBox;