import { fail, redirect } from '@sveltejs/kit';
import { getDataWithToken, postDataWithToken } from '$lib/request_utils.js';


let account_number;
let amount;
let username;

export const actions = {
  initialize: async ( { request, locals, cookies } ) => {
    const data = Object.fromEntries(await request.formData());
    const account = locals.user.account;
    const user = locals.user.user;
    account_number = data.account_number;
    amount = data.amount;

    if (!account_number)
        return fail(400, {account: { missing:true }});

    if (!amount)
        return fail(400, {account_number, amount: { missing:true }});
    if (amount % 5 != 0)
        return fail(400, {account_number, notDivible: true});
    if (amount <= 0)
        return fail(400, {account_number, notValid: true});
    if (account_number === account.account_number)
        return fail(400, {account_number, amount, sameAcc: true});
    if (amount > account.balance)
        return fail(400, {account_number, amount, insufficient: true});

    const route = `users/acc/${account_number}`;
    const token = cookies.get('token');
    const acc = await getDataWithToken(token, route);
    if (acc.status === 404 || acc.status >= 400)
        return fail(400, {account_number, amount, notExist: true});
    const accInfo = await acc.json();
    username = `${accInfo.first_name} ${accInfo.last_name}`;
    return {isAvailable: true, amount, username, account_number};
  },

  complete: async ( { request, cookies } ) => {
    const data = Object.fromEntries(await request.formData());
    const pin = data.pin;
      const obj = {
          "account_number": account_number,
          "amount": amount,
          "pin": pin
    };
    if (!pin)
      return fail(400, {isAvailable: true, missing: true});
    const token = await cookies.get('token');
    const res = await postDataWithToken(token, obj, "transfer");
    if (res.status === 403)
      return fail(400, {isAvailable: true, username, amount, account_number, invalid: true});
    if (res.status === 400)
      return fail(400, {account_number, amount, isAvailable: false, insufficient: true});

    throw redirect(301, '/');
  }
}
