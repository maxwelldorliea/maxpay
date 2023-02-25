const BASE_URL = 'http://localhost:8000/api/v1'

export const getUser = async () => {
    const data = await fetch(`${BASE_URL}/users`);
    const users = await data.json();
    return users[0];
}

export const getUserAccount = async (userId) => {
    const data = await fetch(`${BASE_URL}/${userId}/accounts`);
    const account = await data.json();
    return account;
}
