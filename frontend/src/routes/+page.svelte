<script lang="ts">
   import { onMount } from 'svelte';
 import Desktop from "./layouts/desktop/desktop_home.svelte"
 import Mobile from "./layouts/mobile/mobile_home.svelte"
 import Graph from './[domain_id]/question/[question_id]/math_syntax.svelte'


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