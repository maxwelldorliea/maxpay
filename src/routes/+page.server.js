import { getMe } from './store.js';
import { redirect } from '@sveltejs/kit';

export async function load ({ cookies }) {
  const token = cookies.get('token');
  const res = await getMe(token);
  if (res.status === 401) {
      cookies.set('token', '', {
          maxAge: 0
      })
      throw redirect(301, '/login');
  }
  const obj = await res.json();
  return {
        obj
  }
}
