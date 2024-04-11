<script lang="ts">
import { AppBar, AppShell } from '@skeletonlabs/skeleton';

import { onMount } from 'svelte';

let downloadData: any;

async function fetchData() {
  const response = await fetch('https://getpantry.cloud/apiv1/pantry/018074c8-1891-4995-9fd6-2d8b5cf4eb17/basket/sat_question_test');
  if (!response.ok) {
	throw new Error(`Error fetching data: ${response.status}`);
  }
  const data = await response.json();
  downloadData = data.questions[0];
}
onMount(fetchData);

</script>

<!-- svelte-ignore missing-declaration -->
<AppShell slotSidebarLeft="w-50">
	<svelte:fragment slot="header"><AppBar>(title)</AppBar></svelte:fragment>
	<svelte:fragment slot="sidebarLeft">
		<div class="card p-4" style=" position:relative; height:auto; width:550px;  background: transparent;  box-shadow: inset 0 0 0 1000px rgba(0, 0, 0, 0);">
		<h class=h5><p>
			{#if downloadData}
              {downloadData.question.paragraph}
			{/if}
		</p>
	    </h>

	</div>
	</svelte:fragment>
	<!-- (sidebarRight) -->
	<!-- (pageHeader) -->
	<!-- Router Slot -->
	<slot />
	
	

	<div class="card p-4 shadowed-box" style=" position:relative; left:20%; top: 6%; height:500px; width:600px;">
        
		<h class=h5>What is the most logical and precise word or phrase to fill in the blank?</h>

        <a href="/elements/logo-clouds" class="logo-item" style="position:relative; border-radius: 10px; margin-bottom: 100px;">HR Solutions</a>
	    <a href="/elements/logo-clouds" class="logo-item">Acme Theaters</a>
	    <a href="/elements/logo-clouds" class="logo-item">Cruisin' Cuisine</a>
		<a href="/elements/logo-clouds" class="logo-item">Cruisin' Cuisine</a>

	</div>

	<svelte:fragment slot="pageFooter"></svelte:fragment>
	<!-- (footer) -->
</AppShell>
