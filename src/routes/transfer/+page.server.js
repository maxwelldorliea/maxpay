import { fail, redirect } from '@sveltejs/kit';


export const actions = {
  initialize: async ( { request } ) => {
    const data = Object.fromEntries(await request.formData());
    const account_number = data.account_number;
    const amount = data.amount;

    if (!account_number)
        return fail(400, {account: { missing:true }});

    if (!amount)
        return fail(400, {account_number, amount: { missing:true }});

    return {isAvailable: true};
  },

  complete: async ( { request } ) => {
    const data = Object.fromEntries(await request.formData());
    const pin = data.pin;

    if (!pin)
      return fail(400, {missing: true});

    throw redirect(301, '/');
  }
}
