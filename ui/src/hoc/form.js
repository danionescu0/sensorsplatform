import React, {Component} from 'react';

const withForm = WrapperComponent => class extends Component {
    constructor(props) {
        super(props);
        this.state = {
            form: {}
        }
    }

    handleInputChange(event) {
        const target = event.target;
        const value = target.type === 'checkbox' ? target.checked : target.value;
        const name = target.name;

        this.setState(function(prevState, props) {
            let form = prevState.form;
            form[name] = value;

            return {form: form};
        });
    }

    render() {
        return (
            <WrapperComponent form={this.state.form} handleInputChange={this.handleInputChange.bind(this)}/>
        )
    }
};


export default withForm;