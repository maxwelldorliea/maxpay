import { redirect, fail } from "@sveltejs/kit";
import { postData } from '$lib/request_utils.js';

export const actions = {
  default: async ({ request, cookies }) => {
    const data = Object.fromEntries(await request.formData());
    const code = parseInt(data.code, 10);
    const user_id = cookies.get('user_id');

    if (!code)
      return fail(400, {missing: true});

    const res = await postData({"user_id": user_id, "code": code}, 'verify_email');
    if (res.status === 400 )
      return fail(400, {incorrect: true});
    throw redirect(301, '/login');
  }
}
