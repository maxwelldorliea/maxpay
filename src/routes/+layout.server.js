import { getUser } from './store.js';

export async function load () {
    const data = await getUser();
    const user = data.user;
    const account = data.account;
    return {
        user,
        account
    };
}
