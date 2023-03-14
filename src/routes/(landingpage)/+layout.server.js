export const load = async ( { locals } ) => {
    let login = false;
    console.log('Landing', locals.isLogin, locals.isLogin === undefined);
    if (locals.isLogin)
        login = true
    return {
        login
    }
}
