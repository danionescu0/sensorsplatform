import React from 'react';
import {
    Row,
    Col,
    Card,
    CardHeader,
    CardBody,
    CardFooter
} from 'ahoy-reactstrap';

const ContentBox = ({children, title, icon, headerClass, footer}) => {
    return (
        <Row>
            <Col lg="12">
                <Card className="mb-5">
                    <CardHeader className={headerClass}>
                        <i className={icon} aria-hidden="true"/> &nbsp; {title}
                    </CardHeader>
                    <CardBody>
                        {children}
                    </CardBody>
                    {footer && <CardFooter>{footer}</CardFooter>}
                </Card>
            </Col>
        </Row>
    )
};

export default ContentBox;