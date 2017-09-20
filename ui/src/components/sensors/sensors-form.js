import React from 'react';
import {
    Input,
    Label,
    FormGroup,
    Button,
    Modal,
    ModalBody,
    ModalHeader,
    ModalFooter,
    Alert
} from 'ahoy-reactstrap';

export const SENSOR_TYPES = {
    temperature: 'Temperature',
    humidity: 'Humidity',
    light: 'Light',
    air_pressure: 'Air pressure',
    gis: 'Gis',
};


const SensorsForm = ({handleInputChange, handleSubmit, isModalOpen, toogleModal, error}) => {
    return (
        <Modal isOpen={isModalOpen} toggle={toogleModal}>
            <ModalHeader toggle={this.toggle}>Add sensor</ModalHeader>
            <ModalBody>
                <form onSubmit={handleSubmit}>
                    <FormGroup>
                        <Label for="exampleSelect">Select</Label>
                        <Input required type="select" name="type" onChange={handleInputChange}>
                            <option/>
                            {renderOptions()}
                        </Input>
                    </FormGroup>
                </form>
                {error && <Alert color="danger">{error}</Alert>}
            </ModalBody>
            <ModalFooter>
                <Button color="primary" type="submit" onClick={handleSubmit}>Save</Button>{' '}
                <Button color="secondary" onClick={toogleModal}>Cancel</Button>
            </ModalFooter>
        </Modal>
    )
};

const renderOptions = () => {
    return Object.keys(SENSOR_TYPES).map(key => <option key={key} value={key}>{SENSOR_TYPES[key]}</option>)
};

export default SensorsForm;