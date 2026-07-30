<script lang="ts">
	import Katacard from '$lib/kata/components/katacard.svelte';
	import { page } from '$app/state';
	import './kata.css';

	let { data } = $props();

	const today = new Date().toISOString().slice(0, 10);
	let nextNumber = $derived.by(() => {
		// TODO: find the highest number over all projects
		let lastNumber = data.projects[data.projects.length - 1]?.number;
		let value = parseInt(lastNumber?.slice(1) || "0") + 1;
		return `#${value.toString().padStart(4, "0")}`;
	})

	let defaultProject = $derived({
		title: "",
		number: nextNumber,
		started: today
	});
</script>

<div class="kata relative min-h-screen" spellcheck="false">
	<!-- Background text -->
	<div class="fixed inset-0 flex flex-col items-center justify-center">
		{#each Array(8) as _, i}
			<p class="title bg-text -my-40">kata</p>
		{/each}
	</div>

	<!-- Projects grid -->
	<div class="flex flex-wrap justify-center">
		{#each data.projects as project (project.id)}
			<Katacard {project} />
		{/each}

		{#if page.data.authorized}
			<Katacard project={defaultProject} isNew />
		{/if}
	</div>
	
	<div class="fixed text-center w-screen bottom-10">
		<!--eslint-disable-next-line svelte/no-navigation-without-resolve-->
		<a class="exit-btn" href="/">omni</a>
	</div>
</div>
