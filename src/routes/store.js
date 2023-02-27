const BASE_URL = 'http://localhost:8000/api/v1'

export const getUser = async () => {
    const data = await fetch(`${BASE_URL}/users/953a7b83-51da-4aa5-b8e6-fd432fe37d1b`);
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

//export const getUserAccount = async (userId) => {
    //const data = await fetch(`${BASE_URL}/${userId}/accounts`);
    //const account = await data.json();
    //return account;
//}
