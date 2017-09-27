import React from 'react';
import {
    Input,
    Label,
    FormGroup,
    Button,
    Alert
} from 'ahoy-reactstrap';

import ContentBox from '../content-box';

const RULES_TRIGGERS = ['email', 'sms'];

const RulesForm = ({handleInputChange, handleSubmit, error}) => {
    const footer = <Button color="primary" type="submit" onClick={handleSubmit}>Save</Button>;

    return (
        <ContentBox title="Add Rule" footer={footer} icon="fa fa-plus" headerClass="bg-success text-white">
            <form onSubmit={handleSubmit} className="mb-5">
                <FormGroup>
                    <Label>Name </Label>
                    <Input required type="text" name="name" placeholder="Write rule name" onChange={handleInputChange}/>
                </FormGroup>
                <FormGroup>
                    <Label>Select Trigger Type</Label>
                    <Input required type="select" name="trigger" multiple onChange={handleInputChange}>
                        {renderOptions()}
                    </Input>
                </FormGroup>
            </form>
            {error && <Alert className="mt-5" color="danger">{error}</Alert>}
        </ContentBox>
    )
};

const renderOptions = () => {
    return RULES_TRIGGERS.map((trigger, index) => <option key={trigger} value={trigger}>{trigger}</option>)
};

export default RulesForm;