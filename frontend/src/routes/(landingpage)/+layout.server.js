export const load = async ( { cookies } ) => {
    let login = ( cookies.get('token') ) ? true : false;
    return {
        login
    }
}
