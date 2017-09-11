import {doFetch} from "./fetch";
import Auth from "../utils/auth";

export const performLogin = (email, password) => {
    const params = new URLSearchParams();
    params.set("email", email);
    params.set("password", password);

    return new Promise((resolve, reject) => {
        doFetch('/auth', {
            body: params,
            method: 'POST'
        }).then(response => {
            if (!response.ok) {
                throw Error(response.statusText);
            }
            return response.text();
        })
        .then(token => {
            Auth.authenticateUser(token);
            resolve(token);
        }).catch(e => reject(e));
    });
};

