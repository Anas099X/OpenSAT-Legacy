<script>
  // @ts-nocheck
  
      import { AppBar, AppShell, Avatar, ProgressRadial} from '@skeletonlabs/skeleton';
      import { IconBrandGithub, IconSchool, IconMail, IconMessage, IconCurrentLocation} from '@tabler/icons-svelte';
      import { initializeApp } from 'firebase/app';
      import { getFirestore, collection, getDocs } from 'firebase/firestore';
      import { onMount } from 'svelte';
      import { FIREBASE_KEY } from '../keys/api_keys';
  
      // Firebase configuration object
      const firebaseConfig = {
          apiKey: FIREBASE_KEY,
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
          <AppBar background="bg-surface-100-800-token">
              <svelte:fragment slot="lead">
                  <IconSchool stroke={1.5} size="42" class="text-primary-500"/>
                  <h class="h4" style="position:relative; left:3.5%; color: #FF7777;"><b>OpenSAT</b></h>
              </svelte:fragment>
              <svelte:fragment slot="trail">
                  <a href="/" class="btn btn-sm variant-filled-primary" data-sveltekit-preload-data="hover">Home</a>
                  <a href="https://github.com/Anas099X/OpenSAT" class="btn btn-sm variant-filled-secondary" data-sveltekit-preload-data="hover">
                      <IconBrandGithub /> Github
                  </a>
              </svelte:fragment>
          </AppBar>
      </svelte:fragment>
  
      <div class="container mx-auto p-4">
          {#if users.length === 0}
              <p style="display: flex; justify-content:center;">
                <ProgressRadial stroke={50} meter="stroke-primary-500" track="stroke-primary-500/30" strokeLinecap="round" value={undefined} />
              </p>
          {:else}
              <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">  
                  {#each users as user}
                      {#if user.verified_tutor == true}
                          <div class="card card-hover overflow-hidden variant-glass-primary">
                              <header class="card-header flex items-center space-x-4 p-4">
                                  <Avatar src={user.banner} width="w-16" border="border-4 border-primary-500" />
                                  <div>
                                      <h3 class="h3">{user.username}</h3>
                                      <h3 class="text-sm"><b><div variant="filled">{user.availability}</div></b></h3>
                                  </div>
                              </header>
                              <div class="p-4 space-y-4">
                                  <p class="text-lg">{user.description}</p>
                                  <div class="flex items-center space-x-2">
                                      <IconMail size={18} />
                                      <span class="text-sm">{user.email}</span>
                                  </div>
                                  <div class="flex items-center space-x-2">
                                      
                                      <span class="text-sm"><b>{user.gender || 'Not specified'}</b></span>
                                  </div>
                              </div>
                              <footer class="card-footer p-4 flex justify-between items-center">
                                  <span class="text-sm font-bold">{user.country}</span>
                                  <a class="btn btn-sm variant-filled-secondary" href={user.contact}><IconMessage stroke={2} size="19" />Contact</a>
                              </footer>
                          </div>
                      {/if}
                  {/each}
              </div>
          {/if}
      </div>
  
      <slot />
  </AppShell>