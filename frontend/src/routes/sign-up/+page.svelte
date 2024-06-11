<script>
 import { initializeApp } from 'firebase/app';
 import { getAuth, sendEmailVerification, createUserWithEmailAndPassword } from 'firebase/auth';
 import { getFirestore, doc, setDoc } from 'firebase/firestore';

 let email = '';
 let password = '';
 let username = '';
 let description = '';
 let banner = '';
 let country = '';
 let availability = '';
 let contact = '';


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

   // Create a new document in the "users" collection with user data, using uid as the document ID
   const userDocRef = doc(db, "users", userCredential.user.uid);
   await setDoc(userDocRef, {
    username,
    email, // Existing email variable
    description,
    availability,
    country,
    contact,
    banner
   });

   console.log('User created, verification email sent, and data stored:', userDocRef);

   // Display success message to the user
   alert('A verification email has been sent to your address. Please verify your email before signing in.');

  } catch (error) {
   console.error('Sign Up Error:', error);
 // Display error message to the user
 }
 }
</script>

<form on:submit|preventDefault={handleSignUp}>
<input type="text" bind:value={username} placeholder="Username" />
<input type="email" bind:value={email} placeholder="Email" />
<input type="text" bind:value={description} placeholder="Description" /> <!-- Changed to type="text" for description -->
<input type="password" bind:value={password} placeholder="Password" />
<input type="banner" bind:value={banner} placeholder="Banner" />
<input type="text" bind:value={contact} placeholder="Contact" />
<input type="text" bind:value={country} placeholder="Country" />
<input type="text" bind:value={availability} placeholder="Availability" />
<button type="submit">Sign Up</button>
</form>