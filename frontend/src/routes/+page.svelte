<script lang="ts">
  import { AppBar, AppShell, TreeView, TreeViewItem } from '@skeletonlabs/skeleton';
  
  import { onMount, onDestroy } from 'svelte';
  
  let question_data: any;

  
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
  
  

    
  <AppShell>
    <svelte:fragment slot="sidebarLeft">Sidebar Left</svelte:fragment>
  
    <div style="position: absolute; top: 20%; left: 50%; transform: translate(-50%, -20%); margin-bottom: 20%; width:50%">
      <div class="input-group input-group-divider grid-cols-[auto_1fr_auto]">
        <div class="input-group-shim">(icon)</div>
        <input type="search" placeholder="Search..." />
        <button class="variant-filled-secondary">Submit</button>
      </div>
    </div>
  
    <div class="card p-4 overflow-y-auto" style="height: 400px; width: 600px; position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);">  
      {#if isFetchingData}
        <p>Loading data...</p>
      {:else if question_data}
        {#each question_data as x}
          <ol class="list">
            <li>
              <span class="flex-auto">{x.question.paragraph}</span>
            </li>
          </ol>
        {/each}
      {:else}
        <p>No data available yet.</p>
      {/if}
    </div>
  
    <slot />
  </AppShell>
  