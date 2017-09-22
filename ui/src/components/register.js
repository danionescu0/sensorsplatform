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
    Alert
} from 'ahoy-reactstrap';

const Register = ({handleInputChange, handleSubmit, errorMessage}) => {
    return (
        <Card className="card-register mx-auto mt-5">
            <CardHeader>Register an Account</CardHeader>
            <CardBody>
                <form onSubmit={handleSubmit}>
                    <FormGroup>
                        <Label>First name</Label>
                        <Input type="text" name="first_name" required placeholder="Enter firstname"
                               onChange={handleInputChange}/>
                    </FormGroup>
                    <FormGroup>
                        <Label>Last name</Label>
                        <Input type="text" name="last_name" required placeholder="Enter lastname"
                               onChange={handleInputChange}/>
                    </FormGroup>
                    <FormGroup>
                        <Label>Email address</Label>
                        <Input type="email" name="email" required placeholder="Enter email"
                               onChange={handleInputChange}/>
                    </FormGroup>
                    <FormGroup>
                        <Label>Phone</Label>
                        <Input type="phone" name="phone" required placeholder="Enter phone"
                               onChange={handleInputChange}/>
                    </FormGroup>
                    <FormGroup>
                        <Label>Password</Label>
                        <Input type="password" name="password" required placeholder="Password"
                               onChange={handleInputChange}/>
                    </FormGroup>
                    <FormGroup>
                        <Label>Confirm Password</Label>
                        <Input type="password" name="confirmed_password" required placeholder="Confirm password"
                               onChange={handleInputChange}/>
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