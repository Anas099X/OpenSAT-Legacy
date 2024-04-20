<script lang="ts">
  import { AppBar, AppRail, AppRailAnchor, AppRailTile, AppShell, TreeView, TreeViewItem } from '@skeletonlabs/skeleton';
  
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
  
  onMount(() => fetchData(0)); // Fetch data on component mount with initial page
  
  
  
  </script>
  
  

    
  <AppShell slotSidebarLeft="h-auto">
    <svelte:fragment slot="sidebarLeft">
      <AppRail height='h-full' gap='gap-1'>
        <svelte:fragment slot="lead">
		<AppRailAnchor href="/" >(icon)</AppRailAnchor>
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
    <input class="input" title="Input (text)" type="text" placeholder="input text" style="position: absolute; top: 20%; left: 18%; transform: translate(-20%, -18%); width:300px; margin-bottom: 2%;" />
    <div class="card-container p-4 overflow-y-auto !bg-transparent" style="height: 400px; width: 1100px; position: absolute; top: 45%; left: 35%; transform: translate(-30%, -30%);">
      {#if isFetchingData}
        <p>Loading data...</p>
      {:else if question_data}
        <div class="grid grid-cols-2 md:grid-cols-3 gap-4">  
          {#each question_data as x}
            <div class="card p-4" style="height:20vh">
              <section class="p-2">
                <h class="h4">English Section</h>
              </section>
              <footer class="p-4 flex justify-start items-center space-x-4"><small>Question #{x.id}</small></footer>
            </div>
            
          {/each}
        </div>
      {:else}
        <p>No data available yet.</p>
      {/if}
    </div>
  
    <slot />
  </AppShell>
  