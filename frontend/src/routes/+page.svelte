<script lang="ts">
import { AppBar, AppShell } from '@skeletonlabs/skeleton';

import { onMount, onDestroy } from 'svelte';

let question_data: any;
let page_num: any = 1
let question_db_input: any
let question_list_input: any;

if (page_num === 1){

question_list_input = 2
question_db_input = "sat_question_test"

}


async function fetchData() {
  const response = await fetch('https://getpantry.cloud/apiv1/pantry/018074c8-1891-4995-9fd6-2d8b5cf4eb17/basket/' + question_db_input);
  if (!response.ok) {
	throw new Error(`Error fetching data: ${response.status}`);
  }
  const data = await response.json();
  question_data = data.questions[question_list_input];
}
onMount(fetchData);

let initialTime = 10; // Change this to your desired starting time in seconds
  let minutes = Math.floor(initialTime / 60);
  let seconds = initialTime % 60;
  let intervalId: string | number | NodeJS.Timeout | undefined;

  function startTimer() {
    intervalId = setInterval(() => {
      if (seconds > 0) {
        seconds--;
      } else if (minutes > 0) {
        minutes--;
        seconds = 59;
      } else {
        clearInterval(intervalId);
        //console.log('TEST')
      }
    }, 1000); // Update every second
  }

  function stopTimer() {
    clearInterval(intervalId);
  }

  onMount(startTimer);
  onDestroy(stopTimer); // Cleanup the interval on component unmount

</script>

{#if page_num == 1}
<!-- svelte-ignore missing-declaration -->
<AppShell slotSidebarLeft="w-50">
	<svelte:fragment slot="header">
		<AppBar gridColumns="grid-cols-3" slotDefault="place-self-center" slotTrail="place-content-end">
			<svelte:fragment slot="lead"><h1 class="h3"><span class="bg-gradient-to-br from-pink-500 to-violet-500 bg-clip-text text-transparent box-decoration-clone">SAT test project</span></h1></svelte:fragment>
			<div class="countdown" style="position:relative;">
				<h1 class="h3">{minutes}m {seconds.toString().padStart(2, '0')}s</h1>
			  </div>
			<svelte:fragment slot="trail">(actions)</svelte:fragment>
		</AppBar>

	</svelte:fragment>
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
		<h class=h5 >{question_data.question.question}</h>
	
        <a href="/elements/logo-clouds" class="logo-item variant-soft" style="position:relative; border-radius: 10px; margin-bottom: 10px;">{question_data.question.choices.A}</a>
	    <a href="/elements/logo-clouds" class="logo-item variant-soft" style="position:relative; border-radius: 10px; margin-bottom: 10px;">{question_data.question.choices.B}</a>
	    <a href="/elements/logo-clouds" class="logo-item variant-soft" style="position:relative; border-radius: 10px; margin-bottom: 10px;">{question_data.question.choices.C}</a>
		<a href="/elements/logo-clouds" class="logo-item variant-soft" style="position:relative; border-radius: 10px; margin-bottom: 10px;">{question_data.question.choices.D}</a>
        {/if}
	</div>

	<svelte:fragment slot="pageFooter"></svelte:fragment>
	<!-- (footer) -->
</AppShell>
{/if}