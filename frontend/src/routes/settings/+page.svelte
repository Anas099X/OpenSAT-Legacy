<script>
  import { getAuth, onAuthStateChanged } from 'firebase/auth';
  import { onMount } from 'svelte';
  import { getFirestore, doc, getDoc } from 'firebase/firestore';

  let user = null;
  let username = '';
  let description = '';

  const auth = getAuth();
  const db = getFirestore();

  async function fetchUsername(user) {
    if (user?.uid) {
      try {
        console.log('Fetching username for UID:', user.uid); // Debug log
        const userDocRef = doc(db, "users", user.uid);
        const userDocSnap = await getDoc(userDocRef);
        if (userDocSnap.exists()) {
          console.log('User document found:', userDocSnap.data()); // Debug log
          username = userDocSnap.data().username;
          description = userDocSnap.data().description;
        } else {
          console.error('User document not found!');
        }
      } catch (error) {
        console.error('Error fetching user document:', error);
      }
    }
  }

  onMount(() => {
    onAuthStateChanged(auth, async (currentUser) => {
      if (currentUser) {
        console.log('User is authenticated:', currentUser); // Debug log
        console.log('Current user UID:', currentUser.uid); // Debug log
        user = currentUser;
        await fetchUsername(user);
      } else {
        console.log('No authenticated user found.'); // Debug log
        user = null;
        username = '';
      }
    });
  });
</script>

<h1>User Details</h1>
<p>Email: {user?.email || 'Not logged in'}</p>
<p>Username: {username || 'Not available'}</p>
<p>Desc: {description || 'Not available'}</p>