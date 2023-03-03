const BASE_URL = 'http://localhost:8000/api/v1'

export const getUser = async (user_id) => {
    const res = await fetch(`${BASE_URL}/users/${user_id}`);
    return res;
}

export const login = async (data) => {
    const res = await fetch(`${BASE_URL}/sign_in`, {
        method: "POST",
        body: data,
        redirect: "follow"
    });
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

    return res;
}

export const registerUser = async (data) => {
    const res = await fetch(`${BASE_URL}/users`, {
        method: "POST",
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    });

    return res;
}

export const VerifyMail = async (data) => {
    const res = await fetch(`${BASE_URL}/verify_email`, {
        method: "POST",
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    });

    return res;
}
