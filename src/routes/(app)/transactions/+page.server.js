import { getDataWithToken } from '$lib/request_utils.js';

export const load = async ( { cookies } ) => {
  const token = cookies.get('token');
  const res = await getDataWithToken(token, 'transactions');
  const obj = await res.json();
    return {
        obj
    }
}
