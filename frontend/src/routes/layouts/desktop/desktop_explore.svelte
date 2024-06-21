<script lang="ts">
  import { AppBar, AppRail, AppRailAnchor, AppRailTile, AppShell, ProgressBar, TreeView, TreeViewItem } from '@skeletonlabs/skeleton';
  import { IconAdjustmentsSearch, IconBalloon, IconBrandGithub, IconCheck, IconFilter, IconFilterFilled, IconFlagCheck, IconNotebook, IconSchool } from '@tabler/icons-svelte';
  import { onMount, onDestroy } from 'svelte';
  
  let english_question_data: any;
  let math_question_data: any;
  let currentTile: number = 0;

  let sat_section = 'English'
  

  
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
    } catch (error) {
      console.error('Error fetching data:', error);
      // Handle the error gracefully (e.g., display an error message)
    } finally {
      isFetchingData = false; // Set loading state to false after fetching
    }
  }

  function open_question(domain_id: any, question_id: any) {
  const url = `${domain_id}/question/${question_id}`;
  window.open(url, '_blank', 'noopener noreferrer');
}
  
  onMount(() => fetchData(0)); // Fetch data on component mount with initial page
  


  let sat_domains_english: Record<string, boolean> = {
  "Information and Ideas": true,
  "Craft and Structure": true,
  "Expression of Ideas": true,
  "Standard English Conventions": true
};


let sat_domains_math: Record<string, boolean> = {
	"Algebra": true,
	"Advanced Math": true,
	"Problem Solving and Data Analysis": true,
  "Geometry and Trigonometry": true
};

function toggle_english(domain: string): void {
	sat_domains_english[domain] = !sat_domains_english[domain];
 
  
}

function toggle_math(domain: string): void {
	sat_domains_math[domain] = !sat_domains_math[domain];
  
  
}

  
  </script>
  
  
   
    
  <AppShell slotSidebarLeft="h-auto">
    <svelte:fragment slot="header">
      <AppBar background="!bg-transparent">
        <svelte:fragment slot="lead"><IconSchool stroke={1.5} size="42" style="color: #FF7777"/><h class="h4" style="position:relative; left:3.5%; color: #FF7777;"><b>OpenSAT</b></h></svelte:fragment>
       
        <svelte:fragment slot="trail"><a href="/" class="btn btn-sm variant-filled-primary" data-sveltekit-preload-data="hover">Home</a><a href="https://github.com/Anas099X/OpenSAT" class="btn btn-sm variant-filled-secondary" data-sveltekit-preload-data="hover"><IconBrandGithub /> Github</a></svelte:fragment>
      </AppBar>
      </svelte:fragment>
    <svelte:fragment slot="sidebarLeft">
      <br>
      
      <div class="card p-4 bg-surface-200" style="width: 300px; height:80vh;">
        <h2 class="h2 d-flex justify-content-space-between align-items-center">
          <IconFilterFilled stroke={1.5} size="40" style="color: #FF7777" />  
          <span>Filters</span>
        </h2>
        
    <br> 
    <br> 
  <h class="h3">Sections</h>
  <br>

{#each ['English', 'Math'] as c}
<button
  class="chip {sat_section === c ? 'variant-filled-primary' : 'variant-soft-primary'} mr-2"
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

{#if sat_section == 'English'}
{#each Object.keys(sat_domains_english) as f}
	<button
		class="chip {sat_domains_english[f] ? 'variant-filled-secondary' : 'variant-soft-secondary'} mr-2"
		on:click={() => { toggle_english(f); }}
		on:keypress
    style="position:relative; margin-bottom:2%; "
	>
		{#if sat_domains_english[f]}<span><IconCheck stroke={1.5} size="14"/></span>{/if}
		<span class="capitalize">{f}</span>
	</button>
{/each}
{/if}

{#if sat_section == 'Math'}
{#each Object.keys(sat_domains_math) as f}
	<button
		class="chip {sat_domains_math[f] ? 'variant-filled-secondary' : 'variant-soft-secondary'} mr-2"
		on:click={() => { toggle_math(f); }}
		on:keypress
    style="position:relative; margin-bottom:2%; "
	>
		{#if sat_domains_math[f]}<span><IconCheck stroke={1.5} size="14"/></span>{/if}
		<span class="capitalize">{f}</span>
	</button>
{/each}
{/if}

      </div>
    </svelte:fragment>




      {#if isFetchingData}
      <ProgressBar meter="variant-filled-primary" track="!bg-transparent" />
      
        {:else if english_question_data}
        <div class="grid grid-cols-1 md:grid-cols-3 gap-3" style="position:relative; left:3%; width:95%; margin-top:2.5%">  
          {#if sat_section === "English"}
          {#each english_question_data as data, index}
           
            <!-- svelte-ignore a11y-no-static-element-interactions -->
            <!-- svelte-ignore a11y-click-events-have-key-events -->
            {#each Object.entries(sat_domains_english) as [domainName, isEnabled]}
                {#if isEnabled && data.domain === domainName}
                <div class="card card-hover bg-surface-200 p-4 " on:click={() => open_question("english",index + 1)} style="height:20vh">
                  <section class="p-1">
                    <IconNotebook stroke={2} size=36 style="color: #FF7777"/>
                  </section>
                  <h class="h4">Question #{data.id}</h>
                  <!-- svelte-ignore a11y-no-static-element-interactions -->
                  <!-- svelte-ignore a11y-click-events-have-key-events -->
                  <footer class="p-4 flex justify-end items-end space-x-5"><small style="position:relative; left:8%;"><b>{data.domain}</b></small></footer>
                </div>
                {/if}
                {/each}
          {/each}
          {/if}
          {#if sat_section === "Math"}
          {#each math_question_data as data, index}
           
            <!-- svelte-ignore a11y-no-static-element-interactions -->
            <!-- svelte-ignore a11y-click-events-have-key-events -->
            {#each Object.entries(sat_domains_math) as [domainName, isEnabled]}
                {#if isEnabled && data.domain === domainName}
                <div class="card card-hover bg-surface-200 p-4 " on:click={() => open_question("math",index + 1)} style="height:20vh">
                  <section class="p-1">
                    <IconNotebook stroke={2} size=36 style="color: #FF7777" />
                  </section>
                  <h class="h4">Question #{data.id}</h>
                  <!-- svelte-ignore a11y-no-static-element-interactions -->
                  <!-- svelte-ignore a11y-click-events-have-key-events -->
                  <footer class="p-4 flex justify-end items-end space-x-5"><small style="position:relative; left:8%"><b>{data.domain}</b></small></footer>
                </div>
                {/if}
                {/each}
          {/each}
          {/if}
        
        </div>
      {:else}
        <p>No data available yet.</p>
        {/if}
     
 
  
    <slot />

  </AppShell>
  