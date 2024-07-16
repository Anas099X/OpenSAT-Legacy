<script>
  import { signInWithEmailAndPassword, sendEmailVerification } from 'firebase/auth';
  import { initializeApp } from 'firebase/app';
  import { getAuth } from 'firebase/auth';
    import { AppBar, AppShell } from '@skeletonlabs/skeleton';
    import { IconBrandGithub, IconSchool } from '@tabler/icons-svelte';
    import { FIREBASE_KEY } from '../keys/api_keys';

  let email = '';
  let password = '';
  let errorMessage = '';

  const firebaseConfig = {
    apiKey: FIREBASE_KEY,
    authDomain: "crucial-study-390519.firebaseapp.com",
    projectId: "crucial-study-390519",
    storageBucket: "crucial-study-390519.appspot.com",
    messagingSenderId: "1048701385145",
    appId: "1:1048701385145:web:531265aff5615610901e68"
  };

  const app = initializeApp(firebaseConfig);
  const auth = getAuth(app);

  async function handleLogin() {
    errorMessage = ''; // Clear any previous error messages
    try {
      const userCredential = await signInWithEmailAndPassword(auth, email, password);
      const user = userCredential.user;

      if (!user.emailVerified) {
        try {
          await sendEmailVerification(user);
          errorMessage = 'Email not verified. A new verification email has been sent.';
        } catch (verificationError) {
          if (verificationError.code === 'auth/too-many-requests') {
            errorMessage = 'Too many requests. Please try again later.';
          } else {
            errorMessage = `Verification email failed to send: ${verificationError.message}`;
          }
        }
        throw new Error(errorMessage);
      }

      console.log('User logged in:', user);
      window.location.replace('/settings')
      // Redirect or handle successful login here
    } catch (error) {
      console.error('Login Error:', error);
      if (error.code === 'auth/user-not-found' || error.code === 'auth/wrong-password') {
        errorMessage = 'Invalid email or password. Please try again.';
      } else if (error.code === 'auth/too-many-requests') {
        errorMessage = 'Too many failed login attempts. Please try again later.';
      } else if (error.code === 'auth/too-many-requests') {
        errorMessage = 'An error occurred during sign-in. Please try again.';
      } else {
        errorMessage = error;
      }
    }
  }
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
<div class=" flex flex-col justify-center py-12 sm:px-6 lg:px-8">
  <div class="sm:mx-auto sm:w-full sm:max-w-md">
    <h2 class="mt-6 text-center text-3xl font-extrabold text-gray-900">
      Sign in to your account
    </h2>
  </div>

  <div class="mt-8 sm:mx-auto sm:w-full sm:max-w-md">
    <div class="py-8 px-4 shadow sm:rounded-lg sm:px-10" style="background-color:#f6f7f7">
      <form on:submit|preventDefault={handleLogin} class="space-y-6">
        <div>
          <label for="email" class="block text-sm font-medium text-gray-700">
            Email address
          </label>
          <div class="mt-1">
            <input id="email" name="email" type="email" autocomplete="email" required
              class="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none"
              bind:value={email} placeholder="Enter your email">
          </div>
        </div>

        <div>
          <label for="password" class="block text-sm font-medium text-gray-700">
            Password
          </label>
          <div class="mt-1">
            <input id="password" name="password" type="password" autocomplete="current-password" required
              class="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none"
              bind:value={password} placeholder="Enter your password">
          </div>
        </div>

        <div>
          <button type="submit"
            class="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white variant-filled-primary">
            Sign in
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