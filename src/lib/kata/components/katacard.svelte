<script lang="ts">
	import Datepicker from '$lib/kata/components/datepicker.svelte';
	import { enhance } from '$app/forms';
	import { page } from '$app/state';
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

		<!-- top row: title & number -->
		<div class="flex">
			<input bind:value={project.title} name="title" placeholder="neues Projekt" type="text" class="ghost text-xl font-bold header w-60"
					onblur={projectEdited} disabled={!page.data.authorized} />
			<input bind:value={project.number} name="number" placeholder="#0000" type="text" class="ghost text-xl font-bold header w-24"
					onblur={projectEdited} disabled={!page.data.authorized} />
		</div>

		<!-- center: textarea -->
		<textarea bind:value={project.description} name="description" class="ghost w-full" onblur={projectEdited} disabled={!page.data.authorized}></textarea>

		<!-- bottom row: start/end date & actions -->
		<div class="flex items-end justify-between ml-3">
			<div class="flex items-end gap-5">
				<div class="max-w-30">
					<!-- this is only a button so that it looks the same as "Ende" -->
					<button type="button" class="text-xs mb-1" onclick={() => {}}>Start</button> <br>
					<input type="hidden" name="started" value={project.started} />
					<Datepicker bind:selectedDate={project.started} onUpdate={projectEdited} />
				</div>
				{#if project.finished}
					<div class="max-w-30">
						<button class={[ "text-xs mb-1", page.data.authorized && "blind-button finished-label" ]} onclick={() => project.finished = ""} disabled={!page.data.authorized}>
							Ende
						</button> <br>
						<input type="hidden" name="finished" value={project.finished} />
						<Datepicker bind:selectedDate={project.finished} onUpdate={projectEdited} />
					</div>
				{:else if page.data.authorized}
					<Datepicker bind:selectedDate={project.finished} onUpdate={projectEdited} />
				{/if}
			</div>

			<!-- if authorized, show the appropriate action button -->
			{#if page.data.authorized}
				{#if isNew || isEdited}
					<button type="submit" class="btn btn-sm">
						Speichern
					</button>
				{:else}
					<!-- this button is connected to the form below -->
					<button type="submit" class="btn btn-sm" form="delete-form-{project.id}">
						Löschen
					</button>
				{/if}
			{/if}
		</div>
	</form>

	<!-- this hidden form allows for easily discerning update and delete actions -->
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
