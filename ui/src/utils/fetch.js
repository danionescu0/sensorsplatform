export const get = (path) => {
    return doFetch(path, {
        method: 'GET'
    })
    .then(response => response.json)
    .catch(error => console.log('request failed', error));
};

export const doFetch = (path, request) => {
    return fetch(API_ENDPOINT + path, request);
};

const API_ENDPOINT = 'http://localhost:8080';