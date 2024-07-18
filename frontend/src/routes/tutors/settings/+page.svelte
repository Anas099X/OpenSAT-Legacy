<script lang="ts">
  import { getAuth, onAuthStateChanged } from 'firebase/auth';
  import { onMount } from 'svelte';
  import { IconBrandGithub, IconSchool } from '@tabler/icons-svelte';
  import { getFirestore, doc, getDoc, updateDoc } from 'firebase/firestore';
  import { writable } from 'svelte/store';
  import { AppBar, AppShell } from '@skeletonlabs/skeleton';
  import { auth, db, app } from '$lib/firebase';


  let user = null;
  let countries = [];
  let imageFile = null;
  let imageError = null;
  let errorMessage = '';
  const username = writable('');
  const description = writable('');
  const country = writable('');
  const availability = writable('');
  const contact = writable('');


  async function fetchUserData(user) {
    if (user?.uid) {
      try {
        const userDocRef = doc(db, "users", user.uid);
        const userDocSnap = await getDoc(userDocRef);
        if (userDocSnap.exists()) {
          const userData = userDocSnap.data();
          username.set(userData.username);
          description.set(userData.description);
          country.set(userData.country);
          availability.set(userData.availability);
          contact.set(userData.contact);
        } else {
          console.error('User document not found!');
          errorMessage = 'User data not found. Please try again later.';
        }
      } catch (error) {
        console.error('Error fetching user document:', error);
        errorMessage = 'Failed to load user data. Please try again.';
      }
    }
  }

  async function handleUpdate(event) {
    event.preventDefault();
    errorMessage = '';
    if (user?.uid) {
      try {
        const userDocRef = doc(db, "users", user.uid);
        await updateDoc(userDocRef, {
          username: $username,
          description: $description,
          country: $country,
          availability: $availability,
          contact: $contact
        });
        alert('User details updated successfully!');
      } catch (error) {
        console.error('Error updating user document:', error);
        errorMessage = 'Failed to update user details. Please try again.';
      }
    }
  }

  function handleFileChange(event) {
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
    onAuthStateChanged(auth, async (currentUser) => {
      if (currentUser) {
        user = currentUser;
        await fetchUserData(user);
      } else {
        user = null;
        username.set('');
        description.set('');
        country.set('');
        availability.set('');
        contact.set('');
      }
    });
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
        User Details
      </h2>
    </div>

    <div class="mt-8 sm:mx-auto sm:w-full sm:max-w-md">
      <div class="py-8 px-4 shadow sm:rounded-lg sm:px-10" style="background-color:#f6f7f7">
        <form on:submit={handleUpdate} class="space-y-6">
          <div>
            <label for="username" class="block text-sm font-medium text-gray-700">Username</label>
            <input id="username" type="text" bind:value={$username} required
              class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none">
          </div>

          <div>
            <label for="email" class="block text-sm font-medium text-gray-700">Email</label>
            <input id="email" type="text" value={user?.email} disabled
              class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm bg-gray-100">
          </div>

          <div>
            <label for="description" class="block text-sm font-medium text-gray-700">Description</label>
            <textarea id="description" bind:value={$description} required
              class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none"></textarea>
          </div>

          <div>
            <label for="contact" class="block text-sm font-medium text-gray-700">Contact</label>
            <input id="contact" type="text" bind:value={$contact} required
              class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none">
          </div>

          <div>
            <label for="country" class="block text-sm font-medium text-gray-700">Country</label>
            <select id="country" bind:value={$country} required
              class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none">
              <option value="" disabled selected>Select your country</option>
              {#each countries as country}
                {#if country.name !== "Israel"}
                  <option value={country.flag + " " + country.name}>{country.flag} {country.name}</option>
                {/if}
              {/each}
            </select>
          </div>

          <div>
            <label for="availability" class="block text-sm font-medium text-gray-700">Availability</label>
            <select id="availability" bind:value={$availability} required
              class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none">
              <option value="" disabled selected>Select Availability</option>
              <option value="Online">Online</option>
              <option value="Local">Local</option>
              <option value="Online & Local">Online & Local</option>
            </select>
          </div>

          <div>
            <button type="submit"
              class="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white variant-filled-primary">
              Update Details
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