import { getUser, getUserAccount } from './store.js';

export function load () {
    const user = getUser();
    const id = "fb1d363e-0b11-4495-a895-c5b11d756e81";
    const account = getUserAccount(id);
    return {
        user,
        account
    };
}
