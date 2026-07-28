<script lang="ts">
	import Katacard from '$lib/kata/components/katacard.svelte';
	let { data } = $props();

	const today = new Date().toISOString().slice(0, 10);
	let nextNumber = $derived.by(() => {
		// TODO: to be safer, find the last project that has a number
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

<div class="relative min-h-screen" spellcheck="false">
    <!--eslint-disable-next-line svelte/no-navigation-without-resolve-->
    <a href="/">omni</a>

	<!-- Background text, kinda not working anymore -->
    <!--
	<div class="fixed inset-0 flex flex-col items-center justify-center">
		{#each Array(8) as i (i)}
			<p class="title -my-40">kata</p>
		{/each}
	</div>
    -->

	<!-- Projects grid -->
	<div class="flex flex-wrap justify-center">
		{#each data.projects as project (project.id)}
			<Katacard {project} />
		{/each}

		<Katacard project={defaultProject} isNew />
	</div>
</div>
