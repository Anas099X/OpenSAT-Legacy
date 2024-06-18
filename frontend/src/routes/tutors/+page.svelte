<script>
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

<main>
  <h1>Users</h1>

  {#if users.length === 0}
    <p>Loading users...</p>
  {/if}

  {#if users.length > 0}
    <ul>
      {#each users as user}
        <li>{user.username} ({user.desc})</li>
        <img src={user.banner}/>
      {/each}
    </ul>
  {/if}
</main>

<style>
  main {
    font-family: Arial, sans-serif;
    padding: 1rem;
  }
</style>
