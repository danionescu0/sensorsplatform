import React from 'react';
import {
    Row,
    Col,
    Card,
    CardHeader,
    CardBody,
    CardTitle,
} from 'ahoy-reactstrap';

const SensorBox = ({children, title, icon}) => {
    return (
        <Row>
            <Col lg="12">
                <Card className="mb-5" outline color="primary">
                    <CardHeader color="danger">
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