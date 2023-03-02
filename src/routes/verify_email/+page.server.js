import { redirect, fail } from "@sveltejs/kit";
import { VerifyMail } from '../store.js';

export const actions = {
  default: async ({ cookies, request }) => {
    const data = Object.fromEntries(await request.formData());
    const code = parseInt(data.code, 10);
    const user_id = cookies.get('userId');

    if (!code)
      return fail(400, {missing: true});

    console.log({user_id, code});

    const res = await VerifyMail({code, user_id});
    if (res.status != 200 )
      return fail(400, {incorrect: true});
    redirect(301, '/login');
  }
}
