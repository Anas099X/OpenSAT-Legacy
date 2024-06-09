<script>
  import { initializeApp } from 'firebase/app';
  import { getAuth, sendEmailVerification, createUserWithEmailAndPassword } from 'firebase/auth';
  import { getFirestore, collection, addDoc } from 'firebase/firestore';

  let email = '';
  let password = '';
  let username = '';
  let desc = '';

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
  const db = getFirestore(app);

  async function handleSignUp() {
    try {
      const userCredential = await createUserWithEmailAndPassword(auth, email, password);

      // Send email verification after successful user creation
      await sendEmailVerification(userCredential.user);
      console.log('User created and verification email sent:', userCredential.user);

      // Create a new document in the "users" collection with user data
      const userDocRef = await addDoc(collection(db, "users"), {
        uid: userCredential.user.uid, // Firebase assigned user ID
        username,
        email, // Existing email variable
        desc
      });

      console.log('User created, verification email sent, and data stored:', userDocRef);

      // Display success message to the user
      alert('A verification email has been sent to your address. Please verify your email before signing in.');

      // Clear form fields (optional)
      email = '';
      password = '';
      username = '';
    } catch (error) {
      console.error('Sign Up Error:', error);
      // Display error message to the user
    }
  }
</script>

<form on:submit={() => {
  handleSignUp();
}}>
  <input type="text" bind:value={username} placeholder="Username" />
  <input type="email" bind:value={email} placeholder="Email" />
  <input type="description" bind:value={desc} placeholder="Description" />
  <input type="password" bind:value={password} placeholder="Password" />
  <button type="submit">Sign Up</button>
</form>
