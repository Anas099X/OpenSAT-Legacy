<script>
    import { AppBar, AppShell, Avatar } from '@skeletonlabs/skeleton';
    import { IconBrandGithub, IconSchool } from '@tabler/icons-svelte';
  import { initializeApp } from 'firebase/app';
  import { getFirestore, collection, getDocs } from 'firebase/firestore';
  import { onMount } from 'svelte';

  // Firebase configuration object
  const firebaseConfig = {
    apiKey: "AIzaSyDnbLx28r3PbTTWBUb1RwwfVe3xKFS6crY",
    authDomain: "crucial-study-390519.firebaseapp.com",
    projectId: "crucial-study-390519",
    storageBucket: "crucial-study-390519.appspot.com",
    messagingSenderId: "1048701385145",
    appId: "1:1048701385145:web:531265aff5615610901e68"
  };

  // Initialize Firebase
  const app = initializeApp(firebaseConfig);
  const db = getFirestore(app);

  let users = [];

  async function fetchUsers() {
    try {
      const usersCollection = collection(db, 'users');
      const snapshot = await getDocs(usersCollection);
      users = snapshot.docs.map(doc => doc.data());
      console.log(users); // Log the fetched user data
    } catch (error) {
      console.error('Error fetching users:', error);
    }
  }

  onMount(() => {
    fetchUsers();
  });
</script>



<AppShell>
	<svelte:fragment slot="header">
    <AppBar background="!bg-transparent">
      <svelte:fragment slot="lead"><IconSchool stroke={1.5} size="42" style="color: #FF7777"/><h class="h4" style="position:relative; left:3.5%; color: #FF7777;"><b>OpenSAT</b></h></svelte:fragment>
     
      <svelte:fragment slot="trail"><a href="/" class="btn btn-sm variant-filled-primary" data-sveltekit-preload-data="hover">Home</a><a href="https://github.com/Anas099X/OpenSAT" class="btn btn-sm variant-filled-secondary" data-sveltekit-preload-data="hover"><IconBrandGithub /> Github</a></svelte:fragment>
    </AppBar>
  </svelte:fragment>
	<svelte:fragment slot="sidebarLeft">Sidebar Left</svelte:fragment>
	<!-- (sidebarRight) -->
	<!-- (pageHeader) -->

  
    {#if users.length === 0}
      <p>Loading users...</p>
    {/if}
  
    {#if users.length > 0}
    
      <ul>
        <div class="grid grid-cols-3 md:grid-cols-3 gap-3" style="position:relative; left:3%; height:auto; width:95%; margin-top:2.5%">  
        {#each users as user}
  
        <a class="card card-hover overflow-hidden" href="/elements/cards">
          <header>
            <div class="p-4 flex justify-start items-center space-x-4"> 
              <Avatar src={user.banner} width="w-12" /> <h3 class="h3" data-toc-ignore>{user.username}</h3>
            </div>
           
          </header>
          <div class="p-4 space-y-4">
            <article>
              <p>
                {user.description}
              </p>
            </article>
          </div>
          <hr class="opacity-50" />
          <footer class="p-4 flex justify-start items-center space-x-4">
            
            <div class="flex-auto flex justify-between items-center">
              <h6 class="font-bold" data-toc-ignore>{user.availability}</h6>
              {user.country}
            </div>
          </footer>
        </a>
  
        {/each}
        </div>
      </ul>
    {/if}

	<slot />
	<!-- ---- / ---- -->
	<!-- (pageFooter) -->
	<!-- (footer) -->
</AppShell>

