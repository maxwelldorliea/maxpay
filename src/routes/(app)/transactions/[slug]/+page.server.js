import { getDataWithToken } from '$lib/request_utils.js';
import { error } from '@sveltejs/kit';

export const load = async ( { params, cookies } ) => {
    const token = cookies.get('token');
    const res = await getDataWithToken(token, 'transactions');
    const transactions = await res.json();
    for (let obj of transactions) {
        if (obj.id === params.slug)
            return {
                obj
            }
    }

    throw error(404, 'Not Found');
}
