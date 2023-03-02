import { redirect, fail } from '@sveltejs/kit';
import { registerUser } from '../store.js';

export const actions = {
  default: async ({ request }) => {
    const data = Object.fromEntries(await request.formData());
    if (!data.middle_name)
        delete data['middle_name'];
    const firstName = data.first_name;
    const middleName = data.middle_name;
    const lastName = data.last_name;
    const email = data.email;
    const password = data.password;
    if (!firstName)
      return fail(400, {fName: {missing: true}});
    if (!lastName)
      return fail(400, {firstName, middleName, lName: {missing: true}});
    if (!email)
      return fail(400, {firstName, lastName, middleName, mail: {missing: true}});
    if (!password)
      return fail(400, {firstName, lastName, email, middleName, password: {missing: true}});
    const res = await registerUser(data);
    if (res.status === 400)
      return fail(404, {firstName, lastName, email, middleName, mailTaken: true});
    throw redirect(301, '/');
  }
}
