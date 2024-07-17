<script lang="ts">
  import { onMount } from 'svelte';
  import markdownIt from 'markdown-it';
  import 'katex/dist/katex.min.css'; // Ensure KaTeX CSS is loaded
  import markdownItKatex from 'markdown-it-katex';

  export let markdownContent: string = '';
  let processedContent: string = '';
  let preview: HTMLDivElement;

  function processMarkdown(content: string): string {
    const md = markdownIt().use(markdownItKatex, {
      throwOnError: false,
      errorColor: " #cc0000"
    });
    return md.render(content);
  }

  onMount(() => {
    // Optional initial content
    // markdownContent = '$4\\sqrt{2}$'
   
    processedContent = processMarkdown(markdownContent);
    preview.innerHTML = processedContent;
  });

  $: {
    processedContent = processMarkdown(markdownContent);
    if (preview) {
      preview.innerHTML = processedContent;
    }
  }
</script>

<div bind:this={preview}></div>

