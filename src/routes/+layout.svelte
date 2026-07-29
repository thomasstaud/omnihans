<script lang="ts">
	import './layout.css';
	import favicon from '$lib/shared/favicon.svg';

	let { children } = $props();
</script>

<title>omnihans</title>
<svelte:head><link rel="icon" href={favicon} /></svelte:head>
{@render children()}
