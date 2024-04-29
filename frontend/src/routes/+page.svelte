<script lang="ts">
  import { AppBar, AppRail, AppRailAnchor, AppRailTile, AppShell, ProgressBar, TreeView, TreeViewItem } from '@skeletonlabs/skeleton';
  import { IconAdjustmentsSearch, IconBalloon, IconBrandGithub, IconCheck, IconFilter, IconFilterFilled, IconFlagCheck, IconListSearch, IconNotebook, IconSchool } from '@tabler/icons-svelte';
    

  
  </script>
  
  
   
    
  <AppShell slotSidebarLeft="h-auto">
    <svelte:fragment slot="header">
      <AppBar background="variant-soft-surface">
        <svelte:fragment slot="lead"><IconSchool stroke={1.5} size="38"/><h class="h3" style="position:relative; left:3.5%;">OpenSAT</h></svelte:fragment>
        
        <svelte:fragment slot="trail"><a class="anchor h5" style="position:relative; left:-20px;" href="/">Home</a> <a class="anchor h5" style="position:relative; left:-20px;" href="/explore">Explore</a><a class="anchor h5" style="position:relative; left:-10px;" href="https://github.com/Anas099X/OpenSAT"><IconBrandGithub /></a></svelte:fragment>
      </AppBar>
      </svelte:fragment>
     
      <div class="flex flex-col justify-center items-center">
        <IconSchool stroke={1.5} size="200" />
        <h2 class="h2">
          Question Bank with <span class="text-glow">Endless</span> Possibilities
        </h2>
        <br>
        <p class="text-center h4">
          OpenSAT, a free and open-source SAT question bank.
          Dive into a massive pool of SAT practice problems,<br>
          constantly growing thanks to a dedicated community of contributors.
        </p>
        <br>
        <div class="flex justify-center space-x-10">   
          <a type="button" class="btn variant-filled" href="/explore">
          <span><IconListSearch stroke={2} /></span>
          <span> Explore</span>
        </a>
    
        <a type="button" class="btn variant-filled" href="https://github.com/Anas099X/OpenSAT">
          <span><IconBrandGithub /></span>
          <span>Contribute</span>
        </a>
      </div>
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