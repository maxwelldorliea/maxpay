export const load = async ( { url } ) => {
  let login = false;
  if (url.pathname.startsWith('/login'))
    login = true
  return {
        login
  }
}
