<script lang="ts">
  import { Accordion, AccordionItem, AppShell, ProgressBar } from '@skeletonlabs/skeleton';
  import { IconAlertTriangle, IconArrowBack, IconChecks, IconMessageReport } from '@tabler/icons-svelte';
  import { onMount } from 'svelte';
    import Math_syntax from './math_syntax.svelte'

  interface QuestionData {
    id: number;
    question: {
      paragraph: string;
      question: string;
      choices: {
        A: string;
        B: string;
        C: string;
        D: string;
      };
      correct_answer: string;
      explanation: string;
    };
  }

  export let data: { question_id: number; domain: string };
  const { question_id, domain } = data;

  let questionData: QuestionData | null = null;
  let isFetchingData = false;

  async function fetchData() {
    try {
      isFetchingData = true;
      const response = await fetch('https://api.jsonsilo.com/public/942c3c3b-3a0c-4be3-81c2-12029def19f5');
      if (!response.ok) {
        throw new Error(`Error fetching data: ${response.status}`);
      }
      const fetchedData = await response.json();
      questionData = domain === "english" ? fetchedData.english[question_id] : fetchedData.math[question_id];
    } catch (error) {
      console.error('Error fetching data:', error);
      // Handle the error gracefully (e.g., display an error message)
    } finally {
      isFetchingData = false;
    }
  }

  onMount(fetchData);
</script>

<AppShell>
  {#if isFetchingData}
    <ProgressBar meter="variant-filled-primary" track="!bg-transparent" />
  {:else if questionData}
    <div class="flex justify-center relative top-[10%]">
      <div class="card bg-surface-200 max-w-[100vh]">
        <div class="card-content p-4">  
          <div class="flex justify-between flex-wrap">
            <h3 class="h3"><b>Question #{questionData.id}</b></h3> 
            <div>
              <a href="/explore" class="btn btn-sm variant-filled-secondary">
                <IconArrowBack stroke={2} size={20}/>
              </a>
              <a href="https://github.com/Anas099X/Omnibook/issues" class="btn btn-sm variant-filled-primary">
                <IconMessageReport stroke={1.5} size={20}/>
              </a>
            </div>
          </div>  
          
          <hr class="!border-dashed my-4" />
          
          {#if questionData.question.paragraph}
          <p><Math_syntax markdownContent={questionData.question.paragraph}/></p>
          {/if}

          <p class="font-bold my-4"><Math_syntax markdownContent={questionData.question.question}/></p>
          
          {#each ['A', 'B', 'C', 'D'] as choice}
          <div class="flex items-start my-2">
            <span class="mr-2 flex-shrink-0">{choice}.</span>
            <Math_syntax markdownContent={questionData.question.choices[choice]} />
          </div>
        {/each}
        <div hidden><Math_syntax markdownContent={''}/></div>
          <hr class="!border-dashed my-4" />
          
          <Accordion>
            <AccordionItem>
              <svelte:fragment slot="lead"><IconChecks stroke={2} /></svelte:fragment>
              <svelte:fragment slot="summary">Click to reveal the correct answer</svelte:fragment>
              <svelte:fragment slot="content">
                <p class="font-bold">Option {questionData.question.correct_answer} is the correct answer.</p>
                <p><Math_syntax markdownContent={questionData.question.explanation}/></p>
                <div hidden><Math_syntax markdownContent={''}/></div>
              </svelte:fragment>
            </AccordionItem>
          </Accordion>
        </div>
      </div>
    </div>
  {:else}
    <p>No data available.</p>
  {/if}
</AppShell>