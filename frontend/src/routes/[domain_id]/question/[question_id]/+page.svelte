<script lang="ts">
  import { Accordion, AccordionItem, AppBar, AppRail, AppRailAnchor, AppRailTile, AppShell, ProgressBar, TreeView, TreeViewItem } from '@skeletonlabs/skeleton';
    import { IconChecks } from '@tabler/icons-svelte';
  
  import { onMount, onDestroy } from 'svelte';
  
  let question_data: any;
  let currentTile: number = 0;
   // Get project id from params
   export let data 
     const {question_id} = data
     const {domain} = data


  let question_db_input: string = "sat_question_test"; // Set a specific type (string)
  let isFetchingData: boolean = false; // Flag for loading state
  
  async function fetchData(pageNumber: number) {
    try {
      isFetchingData = true; // Set loading state to true before fetching
      const response = await fetch(`https://getpantry.cloud/apiv1/pantry/018074c8-1891-4995-9fd6-2d8b5cf4eb17/basket/${domain}`);
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
      
    </svelte:fragment>
      {#if isFetchingData}
      <ProgressBar />
      {:else if question_data}
      <div class="card grid-cols-2 md:grid-cols-3 gap-4" style="height: auto; width: 800px; position: absolute; top: 40%; left: 45%; transform: translate(-40%, -40%);">
        <div class="card-content p-4">  <h class="h3"><b>Question #{question_data[question_id].id}</b></h>
          <br>
          <br>
          <hr class="!border-dashed" />
          <br>
          <p>{question_data[question_id].question.paragraph}</p>
          <br>
          <b><p>{question_data[question_id].question.question}</p></b>
          <br>
          <p>A. {question_data[question_id].question.choices.A}</p>
          <br>
          <p>B. {question_data[question_id].question.choices.B}</p>
          <br>
          <p>C. {question_data[question_id].question.choices.C}</p>
          <br>
          <p>D. {question_data[question_id].question.choices.D}</p>
          <br>
          <hr class="!border-dashed" />
          <Accordion>
            <AccordionItem>
              <svelte:fragment slot="lead"><IconChecks stroke={2} /></svelte:fragment>
              <svelte:fragment slot="summary"> Click to reveal the correct answer</svelte:fragment>
              <svelte:fragment slot="content"><b>Option {question_data[question_id].question.correct_answer} is the correct answer.</b>
              <br>
              {question_data[question_id].question.explanation}
            </svelte:fragment>
            </AccordionItem>
            <!-- ... -->
          </Accordion>
        </div>
      </div>
      
      {:else}
        <p>No data available yet.</p>
      {/if}

  
    <slot />
  </AppShell>
  