<script lang="ts">
  import { onMount } from 'svelte';
import Desktop from "../layouts/desktop/desktop_explore.svelte"
import Mobile from "../layouts/mobile/mobile_explore.svelte"


let isMobile: any;

onMount(() => {
 isMobile = window.innerWidth < 768;
});
 
</script>

{#if isMobile}
 <Mobile />
{:else}
 <Desktop />
{/if}