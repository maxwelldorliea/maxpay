import { getDataWithToken } from '$lib/request_utils.js';
import { redirect } from '@sveltejs/kit';

export const handle = async ( { event, resolve } ) => {
  const route = await event.url.pathname;
  if (!route.startsWith('/login') &&
      !route.startsWith('/signup') && !route.startsWith('/verify_email') &&
  route !== '/') {
    const token = await event.cookies.get("token");
    const res = await getDataWithToken(token, 'me');
    if (res.status === 401) {
      event.cookies.set("token", "", {
          httpOnly: true,
          secure: true,
          sameSite: 'strict',
          maxAge: 0
      });
      throw redirect(302, "/login");     
    }
    const user = await res.json();
    event.locals.user = user;
    event.locals.isLogin = true;
  }
  const response = await resolve(event);
  return response;
}
