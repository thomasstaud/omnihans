import { env } from '$env/dynamic/private';
import type { Handle } from '@sveltejs/kit';

export const handle: Handle = async ({ event, resolve }) => {
    const authCookie = event.cookies.get("__admin_key");
    event.locals.authorized = authCookie == env.ADMIN_SECRET_COOKIE;

    return resolve(event);
}
