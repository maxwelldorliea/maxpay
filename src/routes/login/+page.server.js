import { redirect , fail} from '@sveltejs/kit';
import { login } from '$lib/request_utils.js';



export const load = ( { cookies } ) => {
    if (cookies.get('token')) {
        throw redirect(301, '/');
    }
}


export const actions = {
  default: async ({request, cookies}) => {
    const data = Object.fromEntries(await request.formData());
    const email = data.email;
    const password = data.password;
 
    if (!email)
        return fail(400, {mail: {missing: true}});
    if (!password)
        return fail(400, {email, password: { missing: true}});

    const user = new FormData();
    user.append('username', data.email);
    user.append('password', data.password);

    const res = await login(user);
    if (res.status === 401)
        return fail(401, {incorrect: true});

    const { access_token } = await res.json();
    cookies.set('token', access_token, {
          httpOnly: true,
          secure: true,
          sameSite: "strict",
          path: "/",
          maxAge: 60 * 5
      });
    throw redirect(301, '/');
  }
}
