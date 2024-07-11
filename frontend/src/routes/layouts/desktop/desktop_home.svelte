<script lang="ts">
  import { AppBar, AppShell } from '@skeletonlabs/skeleton';
  import { IconAdjustmentsSearch, IconBalloon, IconFileDatabase, IconBrandGithub, IconCheck, IconFilter, IconFilterFilled, IconFlagCheck, IconListSearch, IconNotebook, IconSchool } from '@tabler/icons-svelte';
</script>

<AppShell slotSidebarLeft="h-auto">
  <svelte:fragment slot="header">
    <AppBar background="!bg-transparent">
      <svelte:fragment slot="lead">
        <IconSchool stroke={1.5} size="42" class="text-primary-500"/>
        <h class="h4 ml-2 text-primary-500 font-bold text-glow">OpenSAT</h>
      </svelte:fragment>
      <svelte:fragment slot="trail">
        <a href="/" class="btn btn-sm variant-filled-primary hover:scale-105 transition-transform" data-sveltekit-preload-data="hover">Home</a>
        <a href="https://github.com/Anas099X/OpenSAT" class="btn btn-sm variant-filled-secondary hover:scale-105 transition-transform" data-sveltekit-preload-data="hover">
          <IconBrandGithub /> Github
        </a>
      </svelte:fragment>
    </AppBar>
  </svelte:fragment>
       
  <div class="flex flex-col justify-center items-center">
    <IconSchool class="text-primary-500 animate-bounce" style="position:relative; top:45px;" stroke={1.5} size="200" />
    <h2 class="h2 mt-8 text-4xl font-bold text-center">
      Question Bank with <span class="text-primary-500 underline decoration-wavy">Endless</span> Possibilities
    </h2>
    <p class="text-center h4 mt-4 max-w-2xl">
      OpenSAT, a free and open-source SAT question bank.
      Dive into a massive pool of SAT practice problems,
      constantly growing thanks to a dedicated community of contributors.
    </p>
    <div class="flex justify-center space-x-6 mt-8">   
      <a class="btn variant-filled-primary hover:scale-110 transition-transform" href="/explore">
        <span><IconListSearch stroke={2} /></span>
        <span>Explore</span>
      </a>
      <a class="btn variant-filled-secondary hover:scale-110 transition-transform" href="https://github.com/Anas099X/OpenSAT">
        <span><IconBrandGithub /></span>
        <span>Contribute</span>
      </a>
    </div>
    <a class="btn variant-filled-secondary hover:scale-110 transition-transform mt-4" href="https://api.jsonsilo.com/public/942c3c3b-3a0c-4be3-81c2-12029def19f5">
      <span><IconFileDatabase /></span>
      <span>JSON Database</span>
    </a>
  </div>

  <slot />
</AppShell>

<style>
  :global(body) {
    overflow: hidden;
  }

  

  .text-primary-500 {
    color: #FF7777;
  }



  .decoration-wavy {
    text-decoration-style: wavy;
  }
</style>