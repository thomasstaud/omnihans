<script lang="ts">
	import { onMount } from 'svelte';
	let { selectedDate = $bindable(), onUpdate = () => {} } = $props();

	const uid = crypto.randomUUID();   // modern browsers
	const popoverId = `cally-popover-${uid}`;
	const anchorName = `--cally-${uid}`;

	let popover: HTMLDivElement;
	let button: HTMLButtonElement;

	onMount(async () => {
		await import('cally');
	});

	function onDateChange(event: Event) {
		const target = event.target as HTMLInputElement;
		selectedDate = target.value;
		popover?.hidePopover();
		button?.blur();
		onUpdate();
	}
</script>

<button
	bind:this={button}
	popovertarget={popoverId}
	class="input input-ghost blind-button w-min "
	type="button"
	style={`anchor-name: ${anchorName}`}
>
	{selectedDate || "+"}
</button>

<div
	bind:this={popover}
	popover
	id={popoverId}
	class="dropdown bg-base-100 rounded-box shadow-lg"
	style={`position-anchor: ${anchorName}`}
>
	<!-- can't use 'onchange' here since this is not a regular html element or something like that -->
	<!-- svelte-ignore event_directive_deprecated -->
	<calendar-date class="cally" on:change={onDateChange}>
		<!-- this nonsense is the only way i've found to block a pesky warning -->
		<svg {...{} as any} slot="previous" class="fill-base-content size-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
			<path d="M15.75 19.5 8.25 12l7.5-7.5" />
		</svg>

		<svg {...{} as any} slot="next" class="fill-base-content size-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
			<path d="m8.25 4.5 7.5 7.5-7.5 7.5" />
		</svg>

		<calendar-month></calendar-month>
	</calendar-date>
</div>
