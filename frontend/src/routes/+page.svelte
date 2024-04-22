<script lang="ts">
  import { AppBar, AppRail, AppRailAnchor, AppRailTile, AppShell, ProgressBar, TreeView, TreeViewItem } from '@skeletonlabs/skeleton';
  
  import { onMount, onDestroy } from 'svelte';
  
  let question_data: any;
  let currentTile: number = 0;

  
  let question_db_input: string = "sat_question_test"; // Set a specific type (string)
  let isFetchingData: boolean = false; // Flag for loading state
  
  async function fetchData(pageNumber: number) {
    try {
      isFetchingData = true; // Set loading state to true before fetching
      const response = await fetch(`https://getpantry.cloud/apiv1/pantry/018074c8-1891-4995-9fd6-2d8b5cf4eb17/basket/${question_db_input}?page=${pageNumber}`);
      if (!response.ok) {
        throw new Error(`Error fetching data: ${response.status}`);
      }
      const data = await response.json();
      question_data = data.questions; // Adjust index based on page numbering
    } catch (error) {
      console.error('Error fetching data:', error);
      // Handle the error gracefully (e.g., display an error message)
    } finally {
      isFetchingData = false; // Set loading state to false after fetching
    }
  }

  function open_question(question_id:any){
    window.location.href = '/question/' + question_id
   

  }
  
  onMount(() => fetchData(0)); // Fetch data on component mount with initial page
  
  
  
  </script>
  
  

    
  <AppShell slotSidebarLeft="h-auto">
    <svelte:fragment slot="sidebarLeft">
      <AppRail height='h-full' gap='gap-1'>
        <svelte:fragment slot="lead">
		<AppRailAnchor href="/" >placeholder</AppRailAnchor>
	</svelte:fragment>
	<!-- --- -->
	<AppRailTile bind:group={currentTile} name="tile-1" value={0} title="tile-1">
		<svelte:fragment slot="lead">(icon)</svelte:fragment>
		<span>Tile 1</span>
	</AppRailTile>
	<AppRailTile bind:group={currentTile} name="tile-2" value={1} title="tile-2">
		<svelte:fragment slot="lead">(icon)</svelte:fragment>
		<span>Tile 2</span>
	</AppRailTile>
	<AppRailTile bind:group={currentTile} name="tile-3" value={2} title="tile-3">
		<svelte:fragment slot="lead">(icon)</svelte:fragment>
		<span>Tile 3</span>
	</AppRailTile>
	<!-- --- -->
	<svelte:fragment slot="trail">
		<AppRailAnchor href="/" target="_blank" title="Account">(icon)</AppRailAnchor>
	</svelte:fragment>
        </AppRail>
    </svelte:fragment>
    <div class="card-container p-4 overflow-y-auto !bg-transparent" style="height: 500px; width: 1200px; position: absolute; top: 45%; left: 35%; transform: translate(-30%, -30%);">
      {#if isFetchingData}
      <ProgressBar />
        {:else if question_data}
        <div class="grid grid-cols-2 md:grid-cols-3 gap-4">  
          {#each question_data as data, index}
            <div class="card p-4" style="height:20vh">
              <section class="p-2">
                <h class="h4">Question #{data.id}</h>
              </section>
              <!-- svelte-ignore a11y-no-static-element-interactions -->
              <!-- svelte-ignore a11y-click-events-have-key-events -->
              <footer class="p-4 flex justify-start items-center space-x-4"><small>{data.domain}</small><span class="chip variant-ghost-tertiary" on:click={() => open_question(index + 1)}>open</span></footer>
            </div>
            
          {/each}
        </div>
      {:else}
        <p>No data available yet.</p>
      {/if}
    </div>
  
    <slot />
  </AppShell>
  