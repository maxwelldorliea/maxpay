import { redirect, fail } from '@sveltejs/kit';
import { postData } from '$lib/request_utils.js';

export const load = ( {cookies} ) => {
  if (cookies.get('token'))
      throw redirect(301, '/dashboard');
}


export const actions = {
  default: async ({ request, cookies}) => {
    const data = Object.fromEntries(await request.formData());
    const firstName = data.first_name;
    const lastName = data.last_name;
    const email = data.email;
    const password = data.password;
    if (!firstName)
      return fail(400, {fName: {missing: true}});
    if (!lastName)
      return fail(400, {firstName, lName: {missing: true}});
    if (!email)
      return fail(400, {firstName, lastName, mail: {missing: true}});
    if (!password)
      return fail(400, {firstName, lastName, email, password: {missing: true}});
    const res = await postData(data, 'users');
    if (res.status === 400)
      return fail(404, {firstName, lastName, email, mailTaken: true});
    const user = await res.json();
      cookies.set('user_id', user.user.id, {
          httpOnly: true,
          secure: true,
          path: '/verify_email',
          sameSite: 'strict',
          maxAge: 60*60*24
      });
    throw redirect(301, '/verify_email');
  }
}
