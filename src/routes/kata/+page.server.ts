import { db } from '$lib/server/db';
import { project } from '$lib/server/db/schema';
import { redirect } from '@sveltejs/kit';
import { eq } from 'drizzle-orm';

export const load = async () => {
	const allProjects = await db.select().from(project).orderBy(project.started);

	return {
		projects: allProjects
	};
};

export const actions = {
	save: async ({ request }) => {
		const formData = await request.formData();

		const id = formData.get('id') as string;

		const title = formData.get('title') as string;
		const number = formData.get('number') as string;
		const description = formData.get('description') as string;
		const started = formData.get('started') as string;
		const finished = formData.get('finished') as string;

		if (id) {
			// update existing project
			await db.update(project).set({
				title,
				number,
				description,
				started,
				finished,
			}).where(eq(project.id, id));

		} else {
			// create new project
			await db.insert(project).values({
				title,
				number,
				description,
				started,
				finished,
			});
		}

		throw redirect(303, '/');
	},
	delete: async ({ request }) => {
        const formData = await request.formData();
        const id = formData.get('id') as string;

        if (id) {
            await db.delete(project).where(eq(project.id, id));
        }

		throw redirect(303, '/');
    },
};
