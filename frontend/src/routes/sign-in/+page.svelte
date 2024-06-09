<script>
  import { signInWithEmailAndPassword, sendEmailVerification } from 'firebase/auth';
  import { initializeApp } from 'firebase/app';
  import { getAuth } from 'firebase/auth';

  let email = '';
  let password = '';
  let errorMessage = '';

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
      // Redirect or handle successful login here
    } catch (error) {
      console.error('Login Error:', error);
      errorMessage = error.message;
    }
  }
</script>

<form on:submit|preventDefault={handleLogin}>
  <input type="email" bind:value={email} placeholder="Email" required />
  <input type="password" bind:value={password} placeholder="Password" required />
  <a type="submit" href="/settings">Login</a>
</form>

{#if errorMessage}
  <p style="color: red;">{errorMessage}</p>
{/if}
