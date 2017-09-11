import React from 'react';
import {Link} from 'react-router-dom';
import {
    Card,
    CardBody,
    CardHeader,
    CardFooter,
    Input,
    Label,
    FormGroup,
    Button,
    Col,
    Alert
} from 'ahoy-reactstrap';

const Register = ({handleInputChange, handleSubmit, errorMessage}) => {
    return (
        <Card className="card-register mx-auto mt-5">
            <CardHeader>Register an Account</CardHeader>
            <CardBody>
                <form onSubmit={handleSubmit}>
                    <FormGroup>
                        <div className="form-row">
                            <Col md="6">
                                <Label>First name</Label>
                                <Input type="text" name="first_name" required placeholder="Enter first name" onChange={handleInputChange}/>
                            </Col>
                        </div>
                    </FormGroup>
                    <FormGroup>
                        <div className="form-row">
                            <Col md="6">
                                <Label>Last name</Label>
                                <Input type="text" name="last_name" required placeholder="Enter last name" onChange={handleInputChange}/>
                            </Col>
                        </div>
                    </FormGroup>
                    <FormGroup>
                        <div className="form-row">
                            <Col md="6">
                                <Label>Email address</Label>
                                <Input type="email" name="email" required placeholder="Enter email" onChange={handleInputChange}/>
                            </Col>
                        </div>
                    </FormGroup>
                    <FormGroup>
                        <div className="form-row">
                            <Col md="6">
                                <Label>Phone</Label>
                                <Input type="phone" name="phone" required placeholder="Enter phone" onChange={handleInputChange}/>
                            </Col>
                        </div>
                    </FormGroup>
                    <FormGroup>
                        <div className="form-row">
                            <Col md="6">
                                <Label>Password</Label>
                                <Input type="password" name="password" required placeholder="Password" onChange={handleInputChange}/>
                            </Col>
                        </div>
                    </FormGroup>
                    <FormGroup>
                        <div className="form-row">
                            <Col md="6">
                                <Label>Confirm Password</Label>
                                <Input type="password" name="confirmed_password" required placeholder="Confirm password" onChange={handleInputChange}/>
                            </Col>
                        </div>
                    </FormGroup>
                    <Button color="primary" type="submit" block>Register</Button>
                </form>
                <div className="text-center">
                    <Link className="d-block small mt-3" to="/login">Login</Link>
                    <Link className="d-block small" to="/forgot-password">Forgot Password?</Link>
                </div>
            </CardBody>
            {errorMessage && <CardFooter>
                    <Alert color="danger"> {errorMessage} </Alert>
                </CardFooter>
            }
        </Card>
    )
};

export default Register;