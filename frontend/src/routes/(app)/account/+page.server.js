export const load = async ( { locals } ) => {
  const user = await locals.user;
  return {
        user
  }
}
