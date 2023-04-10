import { redirect } from '@sveltejs/kit';

export const load = async ( { cookies } ) => {
  cookies.set('token', '', {
      httpOnly: true,
      secure: true,
      sameSite: 'strict',
      maxAge: 0
  }); 
  throw redirect(302, '/');
}
