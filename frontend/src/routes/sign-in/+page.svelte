<script>
  import { signInWithEmailAndPassword } from 'firebase/auth';
  import { initializeApp } from 'firebase/app';
  import { getAuth } from 'firebase/auth';

  let email = ''
  let password = ''

  const firebaseConfig = {
  apiKey: "AIzaSyDnbLx28r3PbTTWBUb1RwwfVe3xKFS6crY",
  authDomain: "crucial-study-390519.firebaseapp.com",
  projectId: "crucial-study-390519",
  storageBucket: "crucial-study-390519.appspot.com",
  messagingSenderId: "1048701385145",
  appId: "1:1048701385145:web:531265aff5615610901e68"
};

const app = initializeApp(firebaseConfig);
const auth = getAuth(app);

  async function handleLogin() {
    try {
      const userCredential = await signInWithEmailAndPassword(auth, email, password);
      console.log('User logged in:', userCredential.user);
      // Redirect or handle successful login here
    } catch (error) {
      console.error('Login Error:', error);
      // Display error message to the user
    }
  }
</script>

<form on:submit={() => {
  handleLogin();
}}>
  <input type="email" bind:value={email} placeholder="Email" />
  <input type="password" bind:value={password} placeholder="Password" />
  <a type="submit" href="/settings">Login</a>
</form>
