<script lang="ts">
  import { getAuth, onAuthStateChanged } from 'firebase/auth';
  import { onMount } from 'svelte';
  import { IconBrandGithub, IconSchool } from '@tabler/icons-svelte';
  import { getFirestore, doc, getDoc, updateDoc } from 'firebase/firestore';
  import { writable } from 'svelte/store';
  import { AppBar, AppShell } from '@skeletonlabs/skeleton';

  let user = null;
  let countries = [];
  let imageFile = null;
  let imageError = null;
  const username = writable('');
  const description = writable('');
  const country = writable('');
  const availability = writable('');
  const contact = writable('');

  const auth = getAuth();
  const db = getFirestore();

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
        }
      } catch (error) {
        console.error('Error fetching user document:', error);
      }
    }
  }

  async function handleUpdate(event) {
    event.preventDefault();
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
        alert('Failed to update user details. Please try again.');
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

  <h1>User Details</h1>
  <p>Email: {user?.email || 'Not logged in'}</p>

  <form on:submit|preventDefault={handleUpdate}>
    <label for="username">Username:</label>
    <input class="input" id="username" type="text" bind:value={$username} placeholder="Username" required />

    <label for="description">Description:</label>
    <textarea class="textarea" id="description" bind:value={$description} placeholder="Description" required></textarea>

    <label for="contact">Contact:</label>
    <input class="input" id="contact" type="text" bind:value={$contact} placeholder="Contact" required />

    <label for="country">Country:</label>
    <select id="country" class="input" bind:value={$country} required>
      <option value="" disabled selected>Select your country</option>
      {#each countries as country}
        {#if country.name !== "Israel"}
          <option value={country.flag + " " + country.name}>{country.flag} {country.name}</option>
        {/if}
      {/each}
    </select>

    <label for="availability">Availability:</label>
    <input class="input" id="availability" type="input" bind:value={$availability} placeholder="Availability" required />

    <button class="variant-filled-secondary" type="submit">Update Details</button>
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
