import { getMe } from '../store.js';

async function load ({ cookies }) {
  const token = cookies.get('token');
    console.log('token', token);
  const me = await getMe(token);
  console.log(me);
    return {
        me
    }
}
