<script lang="ts">
  import { AppBar, AppRail, AppRailAnchor, AppRailTile, AppShell, ProgressBar, TreeView, TreeViewItem } from '@skeletonlabs/skeleton';
    import { IconAdjustmentsSearch, IconCheck, IconFilter, IconFlagCheck } from '@tabler/icons-svelte';
  
  import { onMount, onDestroy } from 'svelte';
  
  let question_data: any;
  let currentTile: number = 0;

  export let data 
     const {domain_id} = data

  
  let question_db_input: string = "sat_question_test"; // Set a specific type (string)
  let isFetchingData: boolean = false; // Flag for loading state
  
  async function fetchData(pageNumber: number) {
    try {
      isFetchingData = true; // Set loading state to true before fetching
      const response = await fetch(`https://getpantry.cloud/apiv1/pantry/018074c8-1891-4995-9fd6-2d8b5cf4eb17/basket/${domain_id}?page=${pageNumber}`);
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
  
  let sat_section = 'English';

  
let flavors: Record<string, boolean> = {
	vanilla: true,
	chocolate: false,
	strawberry: false
};


function toggle(flavor: string): void {
	flavors[flavor] = !flavors[flavor];
}

  
  </script>
  
  
   
    
  <AppShell slotSidebarLeft="h-auto">
    <svelte:fragment slot="sidebarLeft">
      <div class="card p-4" style="width: 300px; height:100vh;">
        <h2 class="h2 d-flex justify-content-space-between align-items-center">
          <IconFilter stroke={1.5} size="30" />
          <span>Filters</span>
        </h2>
        
    <br> 
    <br> 
  <h class="h3">Sections</h>
  <br>
       
{#each ['English', 'Math'] as c}
<button
  class="chip {sat_section === c ? 'variant-filled' : 'variant-soft'} mr-2"
  on:click={() => sat_section = c}
  on:keypress
>
  {#if sat_section === c}<IconFlagCheck stroke={1.5} size="14" />{/if}
  <span>{c}</span>
</button>
{/each}
<br>
<br>
<h class="h3">Domains</h>
<br>
{#each Object.keys(flavors) as f}
	<button
		class="chip {flavors[f] ? 'variant-filled' : 'variant-soft'} mr-2"
		on:click={() => { toggle(f); }}
		on:keypress
	>
	
		<span class="capitalize">{f}</span>
	</button>
{/each}


      </div>
    </svelte:fragment>



      tttt
      {#if isFetchingData}
      <ProgressBar />
        {:else if question_data}
        <hr class="!border-t-2" />
        <div class="grid grid-cols-2 md:grid-cols-3 gap-5" style="position:relative; left:3%; top:8%; width:95%;">  
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
 
  
    <slot />
  </AppShell>
  