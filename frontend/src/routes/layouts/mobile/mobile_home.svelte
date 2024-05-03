<script lang="ts">
    import { AppBar, AppRail, AppRailAnchor, AppRailTile, AppShell, ProgressBar, TreeView, TreeViewItem } from '@skeletonlabs/skeleton';
    import { IconAdjustmentsSearch, IconBalloon, IconFileDatabase, IconBrandGithub, IconCheck, IconFilter, IconFilterFilled, IconFlagCheck, IconListSearch, IconNotebook, IconSchool } from '@tabler/icons-svelte';
      
  
    
    </script>
    
    
     
      
    <AppShell slotSidebarLeft="h-auto">
      <svelte:fragment slot="header">
        <AppBar background="variant-soft-surface">
        <svelte:fragment slot="lead"><IconSchool stroke={1.5} size="42" style="color: #FF7777"/><h class="h4" style="position:relative; left:3.5%; color: #FF7777;"><b>OpenSAT</b></h></svelte:fragment>
       
        <svelte:fragment slot="trail"><a href="/" class="btn btn-sm variant-filled-primary" data-sveltekit-preload-data="hover">Home</a><a href="https://github.com/Anas099X/OpenSAT" class="btn btn-sm variant-filled-secondary" data-sveltekit-preload-data="hover"><IconBrandGithub /> Github</a></svelte:fragment>
        </AppBar>
        </svelte:fragment>
       
        <div class="flex flex-col justify-center items-center">
          <IconSchool stroke={1.5} size="175" style="color:#FF7777" />
          <h2 class="h2" style="position:relative;  margin-left13%;">
            Question Bank with <span style="color:#FF7777"><u>Endless</u></span><center>Possibilities</center>
          </h2>
          <br>
          <p class="text-center h4">
            OpenSAT, a free and open-source SAT question bank.<br>
            Dive into a massive pool of SAT practice problems,<br>
            constantly growing thanks to a dedicated community of contributors.
          </p>
          <br>
          <div class="flex justify-center space-x-11">   
            <a type="button" class="btn variant-filled-primary" href="/explore">
            <span><IconListSearch stroke={2} /></span>
            <span> Explore</span>
          </a>
      
          <a type="button" class="btn variant-filled-secondary" href="https://github.com/Anas099X/OpenSAT">
            <span><IconBrandGithub /></span>
            <span>Contribute</span>
          </a>
  
        </div>
        <br/>
        <a type="button" class="btn variant-filled-secondary" style="position:relative; left:-0.5%" href="https://api.jsonsilo.com/public/942c3c3b-3a0c-4be3-81c2-12029def19f5">
          <span><IconFileDatabase /></span>
          <span>JSON Database</span>
        </a>
        </div>
        
       
   
    
      <slot />
  
    </AppShell>
    
  
   
  
  
    
  
  <style>.text-glow {
    animation: glow 1.5s ease-in-out infinite alternate;
    -webkit-animation: glow 1.5s ease-in-out infinite alternate;
  }
  
  @keyframes glow {
    from {
      text-shadow: 0 0 0 rgba(255, 255, 255, 0.0);
    }
    to {
      text-shadow: 0 0 10px rgba(255, 255, 255, 0.7);
    }
  }
  </style>