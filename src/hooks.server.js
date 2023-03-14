import { getDataWithToken } from '$lib/request_utils.js';
import { redirect } from '@sveltejs/kit';

export const handle = async ( { event, resolve } ) => {
  const token = await event.cookies.get("token");
  const res = await getDataWithToken(token, 'me');
  const route = await event.url.pathname;
  if (res.status === 401 && !route.startsWith('/login') &&
      !route.startsWith('/signup') && !route.startsWith('/verify_email') &&
  route !== '/') {
      event.cookies.set("token", "", {
          httpOnly: true,
          secure: true,
          sameSite: 'strict',
          maxAge: 0
      });
    throw redirect(302, "/login");
  }
  if (res.status <= 400) {
    const user = await res.json();
    event.locals.user = user;
    event.locals.isLogin = true;
  }
  const response = await resolve(event);
  return response;
}
