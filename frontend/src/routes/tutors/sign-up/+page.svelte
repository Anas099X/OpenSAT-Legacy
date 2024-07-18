<script lang="ts">
  import { AppBar, AppShell } from '@skeletonlabs/skeleton';
  import { IconBrandGithub, IconSchool } from '@tabler/icons-svelte';
  import { getAuth, sendEmailVerification, createUserWithEmailAndPassword } from 'firebase/auth';
  import { getFirestore, doc, setDoc } from 'firebase/firestore';
  import { auth, db, app } from '$lib/firebase';
  import { onMount } from 'svelte';

  let email = '';
  let verified_tutor = false;
  let password = '';
  let username = '';
  let description = '';
  let banner = '';
  let country = '';
  let availability = '';
  let contact = '';
  let imageFile: File | '' = '';
  let imageError: string | '' = '';
  let countries = '';
  let gender = '';
  let errorMessage = '';




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
        errorMessage = 'Image upload failed. Please try again.';
      }
    } catch (error) {
      console.error('Error uploading image:', error);
      errorMessage = 'Error uploading image. Please try again.';
    }
  }

  async function handleSignUp(event: Event) {
    event.preventDefault();
    errorMessage = '';
    try {
      if (imageFile) {
        await handleUploadImage(imageFile);
      }

      const userCredential = await createUserWithEmailAndPassword(auth, email, password);
      await sendEmailVerification(userCredential.user);

      const userDocRef = doc(db, "users", userCredential.user.uid);
      await setDoc(userDocRef, {
        username,
        verified_tutor,
        gender,
        email,
        description,
        availability,
        country,
        contact,
        banner,
      });
      
      alert('A verification email has been sent to your address. Please verify your email before signing in.');
    } catch (error) {
      if (error.code === "auth/email-already-in-use"){

        errorMessage = 'Email is already in use!';
      } else {
        console.error('Sign Up Error:', error.code);
      errorMessage = 'An error occurred during sign-up. Please try again.';
      }
      
    }
    window.location.replace('/tutors/sign-in')
  }

  function handleFileChange(event: Event) {
    const target = event.target as HTMLInputElement;
    const file = target.files?.[0] || '';

    if (file) {
      const fileType = file.type.split('/')[0];
      if (fileType !== 'image') {
        imageError = 'Please select a valid image file.';
        imageFile = '';
      } else {
        imageError = '';
        imageFile = file;
      }
    }
  }

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

  <div class="min-h-screen flex flex-col justify-center py-12 sm:px-6 lg:px-8">
    <div class="sm:mx-auto sm:w-full sm:max-w-md">
      <h2 class="mt-6 text-center text-3xl font-extrabold text-gray-900">
        Create your account
      </h2>
    </div>

    <div class="mt-8 sm:mx-auto sm:w-full sm:max-w-md">
      <div class="py-8 px-4 shadow sm:rounded-lg sm:px-10" style="background-color:#f6f7f7">
        <form on:submit={handleSignUp} class="space-y-6">
          <div>
            <label for="username" class="block text-sm font-medium text-gray-700">Username</label>
            <input id="username" type="text" bind:value={username} required
              class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none">
          </div>
          
          <div>
            <label for="email" class="block text-sm font-medium text-gray-700">Email address</label>
            <input id="email" type="email" bind:value={email} required
              class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none">
          </div>
          
          <div>
            <label for="password" class="block text-sm font-medium text-gray-700">Password</label>
            <input id="password" type="password" bind:value={password} required
              class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none">
          </div>
          
          <div>
            <label for="description" class="block text-sm font-medium text-gray-700">Description</label>
            <textarea id="description" bind:value={description} required
              class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none"></textarea>
          </div>
          
          <div>
            <label for="image" class="block text-sm font-medium text-gray-700">Profile Image</label>
            <input id="image" type="file" accept="image/*" on:change={handleFileChange}
              class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none">
            {#if imageError}
              <p class="mt-2 text-sm text-red-600">{imageError}</p>
            {/if}
          </div>
          
          <div>
            <label for="contact" class="block text-sm font-medium text-gray-700">Contact</label>
            <input id="contact" placeholder="www.example.com" type="text" bind:value={contact} required
              class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none">
          </div>
          
          <div>
            <label for="country" class="block text-sm font-medium text-gray-700">Country</label>
            <select id="country" bind:value={country} required
              class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none">
              <option value="" disabled selected>Select your country</option>
              {#each countries as country}
                {#if country.name !== "Israel"}
                  <option value={country.flag+" "+country.name}>{country.flag} {country.name}</option>
                {/if}
              {/each}
            </select>
          </div>

          <div>
            <label for="gender" class="block text-sm font-medium text-gray-700">Gender</label>
            <select id="gender" bind:value={gender} required
              class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none">
              <option value="" disabled selected>Gender</option>
              <option value="Online">♂️ Male</option>
              <option value="Local">♀️ Female</option>
            </select>
          </div>
          
          <div>
            <label for="availability" class="block text-sm font-medium text-gray-700">Availability</label>
            <select id="availability" bind:value={availability} required
              class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none">
              <option value="" disabled selected>Select Availability</option>
              <option value="Online">Online</option>
              <option value="Local">Local</option>
              <option value="Online & Local">Online & Local</option>
            </select>
          </div>
          
          <div>
            <!-- svelte-ignore a11y-missing-attribute -->
            <button type="submit"
              class="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white variant-filled-primary">
              Sign Up
          </button>
          </div>
        </form>

        {#if errorMessage}
          <div class="mt-4 p-3 rounded-md bg-red-100 border border-red-400">
            <p class="text-sm text-red-700">{errorMessage}</p>
          </div>
        {/if}
      </div>
    </div>
  </div>
</AppShell>

<style>
  :global(body) {
    background-color: #f6f7f7;
  }
</style>