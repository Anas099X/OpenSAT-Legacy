<script lang="ts">
  import { AppBar, AppShell } from '@skeletonlabs/skeleton';
  import { IconBrandGithub, IconSchool } from '@tabler/icons-svelte';
  import { initializeApp } from 'firebase/app';
  import { getAuth, sendEmailVerification, createUserWithEmailAndPassword } from 'firebase/auth';
  import { getFirestore, doc, setDoc } from 'firebase/firestore';
  import { onMount } from 'svelte';

  let email = '';
  let password = '';
  let username = '';
  let description = '';
  let banner = ''; // Initially empty to store image URL
  let country = '';
  let availability = '';
  let contact = '';
  let imageFile: File | null = null; // Store the selected image file
  let imageError: string | null = null; // Store error message for image upload
  let countries = [];

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

  function handleFileChange(event: Event) {
    const target = event.target as HTMLInputElement;
    const file = target.files?.[0] || null;

    if (file) {
      const fileType = file.type.split('/')[0];
      if (fileType !== 'image') {
        imageError = 'Please select a valid image file.';
        imageFile = null;
      } else {
        imageError = null;
        imageFile = file;
      }
    }
  }

  // Fetch countries from the API
  async function fetchCountries() {
    try {
      const response = await fetch('https://cdn.simplelocalize.io/public/v1/countries');
      if (response.ok) {
        countries = await response.json();
      } else {
        console.error('Failed to fetch countries');
      }
    } catch (error) {
      console.error('Error fetching countries:', error);
    }
  }

  onMount(() => {
    fetchCountries();
  });
</script>

<AppShell>
  <svelte:fragment slot="header">
    <AppBar background="!bg-transparent">
      <svelte:fragment slot="lead">
        <IconSchool stroke={1.5} size="42" style="color: #FF7777" />
        <h class="h4" style="position:relative; left:3.5%; color: #FF7777;"><b>OpenSAT</b></h>
      </svelte:fragment>
      <svelte:fragment slot="trail">
        <a href="/" class="btn btn-sm variant-filled-primary" data-sveltekit-preload-data="hover">Home</a>
        <a href="https://github.com/Anas099X/OpenSAT" class="btn btn-sm variant-filled-secondary" data-sveltekit-preload-data="hover"><IconBrandGithub /> Github</a>
      </svelte:fragment>
    </AppBar>
  </svelte:fragment>

  <form on:submit|preventDefault={handleSignUp}>
    <input class="input" type="text" bind:value={username} placeholder="Username" required />
    <input class="input" type="email" bind:value={email} placeholder="Email" required />
    <textarea class="textarea" bind:value={description} placeholder="Description" required />
    <input class="input" type="password" bind:value={password} placeholder="Password" required />
    <input class="input" type="file" accept="image/*" on:change={handleFileChange} />
    {#if imageError}
      <p style="color: red;">{imageError}</p>
    {/if}
    <input class="input" type="text" bind:value={contact} placeholder="Contact" required />
    <select class="input" bind:value={country} required>
      <option value="" disabled selected>Select your country</option>
      {#each countries as country}
      {#if country.name == "Israel"}
      <div></div>
      {:else}
      <option value={country.flag+" "+country.name}><small>{country.flag}</small> {country.name}</option>
      {/if}
      {/each}
    </select>
    <select class="select" bind:value={availability} required>
      <option value="" disabled selected>Select Availability</option>
      <option value="Online">Online</option>
      <option value="Local">Local</option>
      <option value="Online & Local">Online & Local</option>
      
    </select>
    <button class="btn variant-filled-secondary" type="submit">Sign Up</button>
  </form>
  <slot />
</AppShell>

<style>
  form {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    max-width: 400px;
    margin: auto;
  }
  input, select, textarea, button {
    padding: 0.5rem;
    font-size: 1rem;
  }
</style>
