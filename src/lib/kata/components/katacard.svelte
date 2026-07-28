<script lang="ts">
	import Datepicker from '$lib/kata/components/datepicker.svelte';
	import { enhance } from '$app/forms';
	import './katacard.css';

	let {
		project: initialProject,
		isNew = false,
	} = $props();

	// svelte-ignore state_referenced_locally
	let project = $state({ ...initialProject });
	let isEdited = $state(false);

	function projectEdited() {
		isEdited = true;
	}
</script>

<div class="katacard card bg-base-300/60 flex-1 min-w-85 max-w-100 backdrop-blur-sm" class:new-card={isNew}>
	<form class="card-body" method="POST" action="?/save" onsubmit={() => isEdited = false}>
		<input type="hidden" name="id" value={project.id} />
		<div class="flex">
			<input bind:value={project.title} name="title" placeholder="neues Projekt" type="text" class="input input-ghost text-xl font-bold header" onblur={projectEdited} />
			<input bind:value={project.number} name="number" placeholder="#0000" type="text" class="input input-ghost text-xl font-bold header w-24" onblur={projectEdited} />
		</div>
		<textarea bind:value={project.description} name="description" class="textarea textarea-ghost" onblur={projectEdited}></textarea>
		<div class="flex items-end justify-between">
			<div class="flex items-end gap-2">
				<div class="max-w-30">
					<button type="button" class="text-xs mb-1" onclick={() => {}}>Start</button>
					<input type="hidden" name="started" value={project.started} />
					<Datepicker bind:selectedDate={project.started} onUpdate={projectEdited} />
				</div>
				{#if project.finished}
					<div class="max-w-30">
						<button class="text-xs mb-1 blind-button finished-label" onclick={() => project.finished = ""}>Ende</button>
						<input type="hidden" name="finished" value={project.finished} />
						<Datepicker bind:selectedDate={project.finished} onUpdate={projectEdited} />
					</div>
				{:else}
					<Datepicker bind:selectedDate={project.finished} onUpdate={projectEdited} />
				{/if}
			</div>
			{#if isNew || isEdited}
				<button type="submit" class="btn btn-sm">
					Speichern
				</button>
			{:else}
				<button type="submit" class="btn btn-sm" form="delete-form-{project.id}">
					Löschen
				</button>
			{/if}
		</div>
	</form>
		<form 
			id="delete-form-{project.id}"
			method="POST" 
			action="?/delete" 
			use:enhance={({ cancel }) => {
				const proceed = confirm("Sie beabsichtigen Abschiednahme von " + project.title + "?");
				if (!proceed) {
					cancel();
				}
				
				return async ({ update }) => {
					await update();
				};
			}}
		>
			<input type="hidden" name="id" value={project.id} />
		</form>
</div>
