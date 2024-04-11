<script lang="ts">
import { AppBar, AppShell } from '@skeletonlabs/skeleton';

import { onMount } from 'svelte';

let question_data: any;

async function fetchData() {
  const response = await fetch('https://getpantry.cloud/apiv1/pantry/018074c8-1891-4995-9fd6-2d8b5cf4eb17/basket/sat_question_test');
  if (!response.ok) {
	throw new Error(`Error fetching data: ${response.status}`);
  }
  const data = await response.json();
  question_data = data.questions[0];
}
onMount(fetchData);

</script>

<!-- svelte-ignore missing-declaration -->
<AppShell slotSidebarLeft="w-50">
	<svelte:fragment slot="header"><AppBar><h1 class="h2">
		<span class="bg-gradient-to-br from-pink-500 to-violet-500 bg-clip-text text-transparent box-decoration-clone">SAT test project</span>
	</h1></AppBar></svelte:fragment>
	<svelte:fragment slot="sidebarLeft">
		<div class="card p-4" style=" position:relative; height:auto; width:550px;  background: transparent;  box-shadow: inset 0 0 0 1000px rgba(0, 0, 0, 0);">
		<h class=h5><p>
			{#if question_data}
              {question_data.question.paragraph}
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
        {#if question_data}
		<h class=h5>{question_data.question.question}</h>
	
        <a href="/elements/logo-clouds" class="logo-item" style="position:relative; border-radius: 10px; margin-bottom: 10px;">{question_data.question.choices.A}</a>
	    <a href="/elements/logo-clouds" class="logo-item">{question_data.question.choices.B}</a>
	    <a href="/elements/logo-clouds" class="logo-item">{question_data.question.choices.C}</a>
		<a href="/elements/logo-clouds" class="logo-item">{question_data.question.choices.D}</a>
        {/if}
	</div>

	<svelte:fragment slot="pageFooter"></svelte:fragment>
	<!-- (footer) -->
</AppShell>
