<script lang="ts">
  import { AppBar, AppRail, AppRailAnchor, AppRailTile, AppShell, ProgressBar, TreeView, TreeViewItem } from '@skeletonlabs/skeleton';
    import { IconAdjustmentsSearch, IconBalloon, IconBrandGithub, IconCheck, IconFilter, IconFilterFilled, IconFlagCheck, IconNotebook, IconSchool } from '@tabler/icons-svelte';
  
  import { onMount, onDestroy } from 'svelte';
  
  let english_question_data: any;
  let currentTile: number = 0;

  let sat_section = 'English'
  

  
  let isFetchingData: boolean = false; // Flag for loading state
  
  async function fetchData(pageNumber: number) {
    try {
      isFetchingData = true; // Set loading state to true before fetching
      const response = await fetch(`https://getpantry.cloud/apiv1/pantry/018074c8-1891-4995-9fd6-2d8b5cf4eb17/basket/sat_database`);
      if (!response.ok) {
        throw new Error(`Error fetching data: ${response.status}`);
      }
      const data = await response.json();
      english_question_data = data.english; // Adjust index based on page numbering
    } catch (error) {
      console.error('Error fetching data:', error);
      // Handle the error gracefully (e.g., display an error message)
    } finally {
      isFetchingData = false; // Set loading state to false after fetching
    }
  }

  function open_question(domain_id:any,question_id:any){
    window.location.href = `${domain_id}/question/${question_id}`
   

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
	"Problem_Solving_and_Data_Analysis": true,
  "Geometry_and_Trigonometry": true
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
      <AppBar background="variant-soft-surface">
        <svelte:fragment slot="lead"><IconSchool stroke={1.5} size="38"/></svelte:fragment>
        <h class="h3">OpenSAT</h>
        <svelte:fragment slot="trail"><a class="anchor h5" style="position:relative; left:-20px;" href="/">Home</a> <a class="anchor h5" style="position:relative; left:-20px;" href="/explore">Explore</a><a class="anchor h5" style="position:relative; left:-10px;" href="https://github.com/Anas099X/Omnibook"><IconBrandGithub /></a></svelte:fragment>
      </AppBar>
      </svelte:fragment>
     
      <div class="flex flex-col justify-center items-center">
        <IconSchool stroke={1.5} size="200" />
        <h2 class="h2"> Library with Endless Possibilities</h2>
      </div>
      

 
  
    <slot />

  </AppShell>
  