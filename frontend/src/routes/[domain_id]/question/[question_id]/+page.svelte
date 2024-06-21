<script lang="ts">
  import { Accordion, AccordionItem, AppBar, AppRail, AppRailAnchor, AppRailTile, AppShell, ProgressBar, TreeView, TreeViewItem } from '@skeletonlabs/skeleton';
  import { IconAlertTriangle, IconArrowBack, IconChecks, IconListSearch, IconMessageReport } from '@tabler/icons-svelte';
  import Math_syntax from './math_syntax.svelte'
  import { onMount, onDestroy } from 'svelte';

  let isMobile: any;

 onMount(() => {
  isMobile = window.innerWidth < 768;
 });

  
  
  let english_question_data: any;
  let math_question_data: any;
  let currentTile: number = 0;
   // Get project id from params
   export let data 
     const {question_id} = data
     const {domain} = data
     


  //let question_db_input: string = "sat_question_test"; // Set a specific type (string)
  let isFetchingData: boolean = false; // Flag for loading state
  
  async function fetchData(pageNumber: number) {
    try {
      isFetchingData = true; // Set loading state to true before fetching
      const response = await fetch(`https://api.jsonsilo.com/public/942c3c3b-3a0c-4be3-81c2-12029def19f5`);
      if (!response.ok) {
        throw new Error(`Error fetching data: ${response.status}`);
      }
      const data = await response.json();
      english_question_data = data.english; // Adjust index based on page numbering
      math_question_data = data.math;
      //console.log(math_question_data)
    } catch (error) {
      console.error('Error fetching data:', error);
      // Handle the error gracefully (e.g., display an error message)
    } finally {
      isFetchingData = false; // Set loading state to false after fetching
    }
  }
  
  onMount(() => fetchData(0)); // Fetch data on component mount with initial page
  
  
  
  </script>
  
  
  {#if isMobile}
  
  <AppShell slotSidebarLeft="h-auto">
    <svelte:fragment slot="sidebarLeft">
      
    </svelte:fragment>
      {#if isFetchingData}
      <ProgressBar meter="variant-filled-primary" track="!bg-transparent" />
      {:else if english_question_data && domain == "english"}
      <div class="card grid-cols-2 md:grid-cols-3 gap-4 bg-surface-200 mx-auto" style="height: auto; width: auto; position:relative; top:4%;">
        <div class="card-content p-4">  
    
            
          <h class="h2" style="position:relative; margin-left:1%;">
            <a type="button" style="position:relative; margin-right:2.5%;" class="btn btn-sm variant-filled-secondary" href="/explore">
            <span><IconArrowBack stroke={2} size="20"/></span>  
          </a>
          <b>Question #{english_question_data[question_id].id}</b>
          <a type="button" style="position:relative; margin-left:2.5%;" href="https://github.com/Anas099X/Omnibook/issues" class="btn btn-sm variant-filled-primary">
            <span><IconMessageReport stroke={1.5} size="20"/></span>
            </a>
          </h>

        
         
        
          <br>
          <br>
          <hr class="!border-dashed" />
          <br>
          <p>{english_question_data[question_id].question.paragraph}</p> 
          <br>
          <b><p>{english_question_data[question_id].question.question}</p></b>
          <br>
          <p>A. {english_question_data[question_id].question.choices.A}</p>
          <br>
          <p>B. {english_question_data[question_id].question.choices.B}</p>
          <br>
          <p>C. {english_question_data[question_id].question.choices.C}</p>
          <br>
          <p>D. {english_question_data[question_id].question.choices.D}</p>
          <br>
          <hr class="!border-dashed" />
          <Accordion>
            <AccordionItem>
              <svelte:fragment slot="lead"><IconChecks stroke={2} /></svelte:fragment>
              <svelte:fragment slot="summary"> Click to reveal the correct answer</svelte:fragment>
              <svelte:fragment slot="content"><b>Option {english_question_data[question_id].question.correct_answer} is the correct answer.</b>
              <br>
              {english_question_data[question_id].question.explanation}
            </svelte:fragment>
            </AccordionItem>
            <!-- ... -->
          </Accordion>
        </div>
      </div>
      {:else if math_question_data && domain == "math"}
      <div class="card grid-cols-2 md:grid-cols-3 gap-4 bg-surface-200 mx-auto" style="height: auto; width: auto; position:relative; top:4%;">
        <div class="card-content p-4">  
    
            
          <h class="h2" style="position:relative; margin-left:1%;">
            <a type="button" style="position:relative; margin-right:2.5%;" class="btn btn-sm variant-filled-secondary" href="/explore">
            <span><IconArrowBack stroke={2} size="20"/></span>  
          </a>
          <b>Question #{math_question_data[question_id].id}</b>
          <a type="button" style="position:relative; margin-left:2.5%;" href="https://github.com/Anas099X/Omnibook/issues" class="btn btn-sm variant-filled-primary">
            <span><IconMessageReport stroke={1.5} size="20"/></span>
            </a>
          </h>

        
         
        
          <br>
          <br>
          <hr class="!border-dashed" />
          <br>
          <p><Math_syntax markdownContent={""} /></p> 
          <br>
          <b><p><Math_syntax markdownContent={math_question_data[question_id].question.question}/></p></b>
          <br>
          <p>A. <Math_syntax markdownContent={math_question_data[question_id].question.choices.A}/></p>
          <br>
          <p>B. <Math_syntax markdownContent={math_question_data[question_id].question.choices.B}/></p>
          <br>
          <p>C. <Math_syntax markdownContent={math_question_data[question_id].question.choices.C}/></p>
          <br>
          <p>D. <Math_syntax markdownContent={math_question_data[question_id].question.choices.D}/></p>
          <br>
          <hr class="!border-dashed" />
          <Accordion>
            <AccordionItem>
              <svelte:fragment slot="lead"><IconChecks stroke={2} /></svelte:fragment>
              <svelte:fragment slot="summary"> Click to reveal the correct answer</svelte:fragment>
              <svelte:fragment slot="content"><b>Option {math_question_data[question_id].question.correct_answer} is the correct answer.</b>
              <br>
              <Math_syntax markdownContent={math_question_data[question_id].question.explanation}/>
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


 {:else}
   
  <AppShell slotSidebarLeft="h-auto">
    <svelte:fragment slot="sidebarLeft">
      
    </svelte:fragment>
      {#if isFetchingData}
      <ProgressBar meter="variant-filled-primary" track="!bg-transparent" />
      {:else if english_question_data && domain == "english"}
      <div class="card grid-cols-2 md:grid-cols-3 gap-4 bg-surface-200 mx-auto" style="height: auto; width: 800px; position:relative; top:10%;">
        <div class="card-content p-4">  
          <h class="h3"><b>Question #{english_question_data[question_id].id}</b></h> 
          <a type="button" style="position:relative; left:57%;" class="btn btn-sm variant-filled-secondary" href="/explore">
            <span><IconArrowBack stroke={2} size="20"/></span>
            <span> Return</span>
          </a>
            <a type="button" style="position:relative; left:31%;" href="https://github.com/Anas099X/Omnibook/issues" class="btn btn-sm variant-filled-primary">
            <span><IconMessageReport stroke={1.5} size="20"/></span>
            <span>Report</span>
            </a>
         
        
          <br>
          <br>
          <hr class="!border-dashed" />
          <br>
          <p>{english_question_data[question_id].question.paragraph}</p> 
          <br>
          <b><p>{english_question_data[question_id].question.question}</p></b>
          <br>
          <p>A. {english_question_data[question_id].question.choices.A}</p>
          <br>
          <p>B. {english_question_data[question_id].question.choices.B}</p>
          <br>
          <p>C. {english_question_data[question_id].question.choices.C}</p>
          <br>
          <p>D. {english_question_data[question_id].question.choices.D}</p>
          <br>
          <hr class="!border-dashed" />
          <Accordion>
            <AccordionItem>
              <svelte:fragment slot="lead"><IconChecks stroke={2} /></svelte:fragment>
              <svelte:fragment slot="summary"> Click to reveal the correct answer</svelte:fragment>
              <svelte:fragment slot="content"><b>Option {english_question_data[question_id].question.correct_answer} is the correct answer.</b>
              <br>
              {english_question_data[question_id].question.explanation}
            </svelte:fragment>
            </AccordionItem>
            <!-- ... -->
          </Accordion>
        </div>
      </div>
      {:else if math_question_data && domain == "math"}
      <div class="card grid-cols-2 md:grid-cols-3 gap-4 bg-surface-200 mx-auto" style="height: auto; width: 800px; position:relative; top:10%;">
        <div class="card-content p-4">  
          <h class="h3"><b>Question #{math_question_data[question_id].id}</b></h> 
          <a type="button" style="position:relative; left:57%;" class="btn btn-sm variant-filled-secondary" href="/explore">
            <span><IconArrowBack stroke={2} size="20"/></span>
            <span> Return</span>
          </a>
            <a type="button" style="position:relative; left:31%;" href="https://github.com/Anas099X/Omnibook/issues" class="btn btn-sm variant-filled-primary">
            <span><IconMessageReport stroke={1.5} size="20"/></span>
            <span>Report</span>
            </a>
         
        
          <br>
          <br>
          <hr class="!border-dashed" />
          <br>
          <p><Math_syntax markdownContent={""} /></p> 
          <br>
          <b><p><Math_syntax markdownContent={math_question_data[question_id].question.question}/></p></b>
          <br>
          <p><Math_syntax markdownContent={"A. " +math_question_data[question_id].question.choices.A}/></p>
          <br>
          <p><Math_syntax markdownContent={"B. " +math_question_data[question_id].question.choices.B}/></p>
          <br>
          <p><Math_syntax markdownContent={"C. " +math_question_data[question_id].question.choices.C}/></p>
          <br>
          <p><Math_syntax markdownContent={"D. " +math_question_data[question_id].question.choices.D}/></p>
          <br>
          <hr class="!border-dashed" />
          <Accordion>
            <AccordionItem>
              <svelte:fragment slot="lead"><IconChecks stroke={2} /></svelte:fragment>
              <svelte:fragment slot="summary"> Click to reveal the correct answer</svelte:fragment>
              <svelte:fragment slot="content"><b>Option {math_question_data[question_id].question.correct_answer} is the correct answer.</b>
              <br>
              <Math_syntax markdownContent={math_question_data[question_id].question.explanation}/>
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
  {/if}