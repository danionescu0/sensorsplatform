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

const Login = ({handleInputChange, handleSubmit, failedLogin}) => {
    return (
        <Card className="card-login mx-auto mt-5">
            <CardHeader>Login</CardHeader>
            <CardBody>
                <form onSubmit={handleSubmit}>
                    <FormGroup>
                        <Label>Email address</Label>
                        <Input type="email" name="email" placeholder="Enter email" onChange={handleInputChange}/>
                    </FormGroup>
                    <FormGroup>
                        <Label>Password</Label>
                        <Input type="password" name="password" placeholder="Password" onChange={handleInputChange} required/>
                    </FormGroup>
                    <Button color="primary" block type="submit">Login</Button>
                </form>
                <div className="text-center">
                    <Link className="d-block small mt-3" to="/register">Register an Account</Link>
                    <Link className="d-block small" to="/forgot-password">Forgot Password?</Link>
                </div>
            </CardBody>
            {failedLogin && <CardFooter>
                    <Alert color="danger">Wrong email or password</Alert>
                </CardFooter>
            }

        </Card>
    )
};

export default Login;