<script lang="ts">
	import '../app.postcss';
	
</script>

<div class="mainlayout">
	<slot />
  </div>
  
  <style>
	.mainlayout {
	  height: 100vh; /* Set height to 100 viewport height */
	  width: 100%;
	  display: flex;
	  flex-direction: column;
	  align-items: center;
	  position: relative;
	}
  </style>
  
