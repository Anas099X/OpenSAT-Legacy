<script lang="ts">
	import '../app.postcss';
	import { dev } from '$app/environment';
    import { inject } from '@vercel/analytics';
	import 'katex/dist/katex.min.css';
	inject({ mode: dev ? 'development' : 'production' });
 	
	
</script>

<div class="mainlayout">
	<slot />
	<inject />
	
  </div>
  
  <style>
	.mainlayout {
	  height: 100vh; /* Set height to 100 viewport height */
	  width: 100%;
	  display: flex;
	  flex-direction: column;
	  align-items: center;
	  position: relative;
	  

  background-size: cover;
  background-position: center center;
 
  background-image: url("data:image/svg+xml;utf8,%3Csvg width=%222000%22 height=%221400%22 xmlns=%22http:%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Cdefs%3E%3ClinearGradient id=%22a%22 gradientTransform=%22rotate(90)%22%3E%3Cstop offset=%225%25%22 stop-color=%22%23fce3a2%22%2F%3E%3Cstop offset=%2295%25%22 stop-color=%22%23fceab9%22%2F%3E%3C%2FlinearGradient%3E%3ClinearGradient id=%22b%22 gradientTransform=%22rotate(90)%22%3E%3Cstop offset=%225%25%22 stop-color=%22%23ffb878%22%2F%3E%3Cstop offset=%2295%25%22 stop-color=%22%23ffc999%22%2F%3E%3C%2FlinearGradient%3E%3ClinearGradient id=%22c%22 gradientTransform=%22rotate(90)%22%3E%3Cstop offset=%225%25%22 stop-color=%22%23f77%22%2F%3E%3Cstop offset=%2295%25%22 stop-color=%22%23f99%22%2F%3E%3C%2FlinearGradient%3E%3C%2Fdefs%3E%3Cpath fill=%22%23f6f6f6%22 d=%22M0 0h2000v1400H0z%22%2F%3E%3Cpath d=%22M0 350c83.597 10.964 167.194 21.927 251 27 83.806 5.073 167.821 4.255 246-8 78.179-12.255 150.52-35.948 237-49 86.48-13.052 187.095-15.464 273-2s157.098 42.805 238 43c80.902.195 171.512-28.755 253-41 81.488-12.245 153.854-7.784 236 0 82.146 7.784 174.073 18.892 306 30l-40 1050H0Z%22 fill=%22url(%23a)%22%2F%3E%3Cpath d=%22M0 700c84.69-6.676 169.38-13.352 252-9s163.17 19.733 242 16c78.83-3.733 155.938-26.58 245-19 89.062 7.58 190.077 45.59 274 50 83.923 4.41 150.752-24.777 232-46 81.248-21.223 176.913-34.483 262-31 85.087 3.483 159.596 23.71 240 33s166.702 7.645 293 6l-40 700H0Z%22 fill=%22url(%23b)%22%2F%3E%3Cpath d=%22M0 1050c79.512-22.166 159.023-44.331 242-35 82.977 9.331 169.418 50.159 258 56 88.582 5.841 179.305-23.303 257-39s142.363-17.946 228-8c85.637 9.946 192.243 32.089 276 45 83.757 12.911 144.665 16.591 226 19 81.335 2.409 183.096 3.545 272-3s164.952-20.773 281-35l-40 350H0Z%22 fill=%22url(%23c)%22%2F%3E%3C%2Fsvg%3E");
}






	
  </style>
  
