export const load = async ( { locals } ) => {
    let login = false;
    if (locals.isLogin)
        login = true
    return {
        login
    }
}
