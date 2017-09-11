import Auth from "../utils/auth";

export const postJson = (path, body) => {
    return doFetch(path, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `bearer ${Auth.getToken()}`
        },
        body: JSON.stringify(body)
    }).then(response => response.json);
};

export const doFetch = (path, request) => {
    return fetch(API_ENDPOINT + path, request);
};

const API_ENDPOINT = 'http://localhost:8080';