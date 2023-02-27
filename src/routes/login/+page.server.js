import { redirect , fail} from '@sveltejs/kit';
import { log } from '../store.js';

export const actions = {
  default: async (event) => {
    const data = Object.fromEntries(await event.request.formData());
    if (!data.email || !data.password) {
        return fail(400, {
        error: 'Missing email or password'
        });
    }

    const user = new FormData();
    user.append('username', data.email);
    user.append('password', data.password);
    
    const info = await log(user);

    console.log(info);

    throw redirect(301, '/');
  }
}
