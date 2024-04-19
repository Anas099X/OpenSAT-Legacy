<script lang="ts">
  import { AppBar, AppShell, TreeView, TreeViewItem } from '@skeletonlabs/skeleton';
  
  import { onMount, onDestroy } from 'svelte';
  
  let question_data: any;

  
  let question_db_input: string = "sat_question_test"; // Set a specific type (string)
  let isFetchingData: boolean = false; // Flag for loading state
  
  async function fetchData() {
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
  
  onMount(fetchData); // Fetch data on component mount with initial page
  
  
  
  </script>
  
  
  <AppShell slotSidebarLeft="w-50">
    {#if isFetchingData}
      <p>Loading data...</p>
    {:else if question_data}
      {#each question_data as x}
      
       
<TreeView>
	<TreeViewItem>
		<svelte:fragment slot="lead">(icon)</svelte:fragment>
		{x.id}
	</TreeViewItem>
</TreeView>
					
      {/each}
    {:else}
      <p>No data available yet.</p>
    {/if}
  
    </AppShell>
  