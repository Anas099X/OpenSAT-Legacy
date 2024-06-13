<script lang="ts">
  import { initializeApp } from 'firebase/app';
  import { getAuth, sendEmailVerification, createUserWithEmailAndPassword } from 'firebase/auth';
  import { getFirestore, doc, setDoc } from 'firebase/firestore';

  let email = '';
  let password = '';
  let username = '';
  let description = '';
  let banner = ''; // Initially empty to store image URL
  let country = '';
  let availability = '';
  let contact = '';
  let imageFile: File | null = null; // Store the selected image file

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

  // Replace with your bbimg API details
  const bbimgApiKey = '24192b2e63280714909800d28158a458';
  const bbimgApiUrl = 'https://api.imgbb.com/1/upload';

  async function handleUploadImage(image: File) {
    const formData = new FormData();
    formData.append('image', image);
    formData.append('key', bbimgApiKey);

    try {
      const response = await fetch(bbimgApiUrl, {
        method: 'POST',
        body: formData,
      });

      const data = await response.json();
      if (data.success) {
        banner = data.data.url;
        console.log('Image uploaded successfully:', banner);
      } else {
        console.error('Image upload failed:', data.error.message);
        // Handle upload error (e.g., display error message to user)
      }
    } catch (error) {
      console.error('Error uploading image:', error);
      // Handle network or other errors
    }
  }

  async function handleSignUp(event: Event) {
    event.preventDefault(); // Prevent form from submitting the default way
    try {
      if (imageFile) {
        await handleUploadImage(imageFile);
      }

      const userCredential = await createUserWithEmailAndPassword(auth, email, password);

      // Send email verification after successful user creation
      await sendEmailVerification(userCredential.user);
      console.log('User created and verification email sent:', userCredential.user);

      // Create a new document in the "users" collection with user data, using uid as the document ID
      const userDocRef = doc(db, "users", userCredential.user.uid);
      await setDoc(userDocRef, {
        username,
        email,
        description,
        availability,
        country,
        contact,
        banner,
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
  <input type="text" bind:value={username} placeholder="Username" required />
  <input type="email" bind:value={email} placeholder="Email" required />
  <input type="text" bind:value={description} placeholder="Description" required />
  <input type="password" bind:value={password} placeholder="Password" required />
  <input type="file" accept="image/*" on:change={(e) => imageFile = e.target.files?.[0] || null} />
  <input type="text" bind:value={contact} placeholder="Contact" required />
  <input type="text" bind:value={country} placeholder="Country" required />
  <input type="text" bind:value={availability} placeholder="Availability" required />
  <button type="submit">Sign Up</button>
</form>

<style>
  form {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    max-width: 400px;
    margin: auto;
  }
  input, button {
    padding: 0.5rem;
    font-size: 1rem;
  }
</style>
