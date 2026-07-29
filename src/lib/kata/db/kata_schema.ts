import { integer, sqliteTable, text } from 'drizzle-orm/sqlite-core';

export const project = sqliteTable('project', {
	id: text('id')
		.primaryKey()
		.$defaultFn(() => crypto.randomUUID()),
	number: text('number'),
	title: text('title').notNull(),
	status: integer('status').notNull().default(1),
	category: integer('category'),
	description: text('description'),
	started: text('started'),
	finished: text('finished')
});