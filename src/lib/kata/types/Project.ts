import type { InferSelectModel } from 'drizzle-orm';
import { project as projectTable } from '$lib/server/db/schema';

export type Project = InferSelectModel<typeof projectTable>;

export enum ProjectStatus {
	Active = 1,
	Completed = 2,
	Stopped = 3,
	OnHold = 4
}

export function getProjectStatusLabel(status: number): string {
	switch (status) {
		case ProjectStatus.Active:
			return 'in arbeit';
		case ProjectStatus.Completed:
			return 'abgeschlossen';
		case ProjectStatus.Stopped:
			return 'abgebrochen';
		case ProjectStatus.OnHold:
			return 'pausiert';
		default:
			return 'unsicher';
	}
}
