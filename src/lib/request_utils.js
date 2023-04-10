const BASE_URL = 'https://api.maxpay.maxwelldorliea.tech';

export const getData = async (id, url) => {
    const res = await fetch(`${BASE_URL}/${url}/${id}`);
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

export const getDataWithToken = async (token, route) => {
    const header = new Headers();
    header.append('Authorization', `Bearer ${token}`);
    header.append('Content-Type', 'application/json');
    const res = await fetch(`${BASE_URL}/${route}`, {
        headers: header,
        method: "GET"
    });

    return res;
}

export const postDataWithToken = async (token, data, route) => {
    const header = new Headers();
    header.append('Authorization', `Bearer ${token}`);
    header.append('Content-Type', 'application/json');
    const res = await fetch(`${BASE_URL}/${route}`, {
        method: "POST",
        headers: header,
        body: JSON.stringify(data)
    });

    return res;
}

export const postData = async (data, route) => {
    const res = await fetch(`${BASE_URL}/${route}`, {
        method: "POST",
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    });

    return res;
}
