import { postDataWithToken } from '$lib/request_utils.js';
import { fail, redirect } from '@sveltejs/kit';

export const actions = {
default: async ( { cookies, request } ) => {
  const data = Object.fromEntries(await request.formData());
  const pin = data.pin;
  const new_pin = data.new_pin;
  const confirm_pin = data.confirm_pin;
  const isnum = /^\d+$/.test(new_pin);
  
  if (!isnum)
    return fail(400, {charExist:true});
  if (new_pin.length !== 4)
    return fail(400, {lenInvalid: true});
  if (!pin)
    return fail(400, {pin: {missing: true}});
  if (!new_pin)
    return fail(400, {new_pin: {missing: true}});
  if (!confirm_pin)
    return fail(400, {new_pin, confirm_pin: {missing: true}});
  if (new_pin !== confirm_pin)
    return fail(400, {confirm_pin, new_pin, mismatch: true});
  if (pin === new_pin)
    return fail(400, {confirm_pin, new_pin, same: true});

  const token = cookies.get('token');
  const obj = {
    pin,
    new_pin
  }
  const res = await postDataWithToken(token, obj,'change_pin');
  if (res.status >= 400)
    return fail(400, {new_pin, confirm_pin, incorrect: true});

  throw redirect(302, '/');
  }
}
