import { writable } from 'svelte/store';
import { browser } from '$app/environment';


export const token = writable('');

const BASE_URL = 'http://localhost:8000/api/v1'

export const getUser = async () => {
    const data = await fetch(`${BASE_URL}/users/d33d2926-69f3-4783-8427-76475d2fb1b9`);
    const users = await data.json();
    return users;
}

export const log = async (data) => {
    const info = await fetch(`${BASE_URL}/sign_in`, {
        method: "POST",
        body: data,
        redirect: "follow"
    });
    const res = await info.json();
    return res;
}

export const getMe = async (token) => {
    const header = new Headers();
    header.append('Authorization', `Bearer ${token}`);
    header.append('Content-Type', 'application/json');
    const res = await fetch(`${BASE_URL}/me`, {
        headers: header,
        method: "GET"
    });

    const me = await res.json();

    return me;
}

//export const getUserAccount = async (userId) => {
    //const data = await fetch(`${BASE_URL}/${userId}/accounts`);
    //const account = await data.json();
    //return account;
//}
