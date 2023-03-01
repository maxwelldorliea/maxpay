import { redirect , fail} from '@sveltejs/kit';
import { log, token } from '../store.js';
import { browser } from '$app/environment';



export const actions = {
  default: async ({request, cookies}) => {
    const data = Object.fromEntries(await request.formData());
    if (!data.email || !data.password) {
        return fail(400, {
        error: 'Missing email or password'
        });
    }

    const user = new FormData();
    user.append('username', data.email);
    user.append('password', data.password);
    
    const info = await log(user);
    const { access_token } = info;

    token.update((val) => val += access_token);
    if (browser)
        localStorage.setItem('token', access_token);
    cookies.set('token', access_token, {httpOnly: false, secure: false});
    console.log('Cookies', cookies.get('token'));
    throw redirect(301, '/');
  }
}
