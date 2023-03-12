import { fail, redirect } from '@sveltejs/kit';
import { getData, postDataWithToken } from '../store.js';


let account_number;
let amount;
let username;

export const actions = {
  initialize: async ( { request } ) => {
    const data = Object.fromEntries(await request.formData());
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

    const acc = await getData(account_number, 'users/acc');
    if (acc.status === 404)
        return fail(400, {account_number, amount, notExist: true});
    const accInfo = await acc.json();
    username = `${accInfo.first_name} ${accInfo.last_name}`
    return {isAvailable: true};
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
      return fail(400, {isAvailable: true, invalid: true});
    console.log(await res.json());

    throw redirect(301, '/');
  }
}
