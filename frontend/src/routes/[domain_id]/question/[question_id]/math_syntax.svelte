<script lang="ts">
  import { onMount } from 'svelte';
  import markdownIt from 'markdown-it';

  // Add MathJax type declarations
  declare global {
    interface Window {
      MathJax: {
        typesetPromise: (elements: Element[]) => Promise<void>;
        tex: {
          inlineMath: string[][];
          displayMath: string[][];
        };
        options: {
          skipHtmlTags: string[];
        };
      };
    }
  }

  export let markdownContent: string = '';
  let processedContent: string = '';
  let preview: HTMLDivElement;

  function processMarkdown(content: string): string {
    const md = markdownIt();
    return md.render(content);
  }

  function renderMath() {
    if (window.MathJax && window.MathJax.typesetPromise) {
      window.MathJax.typesetPromise([preview]).catch((err) => console.error('MathJax error:', err));
    }
  }

  onMount(() => {
    // Load MathJax
    const script = document.createElement('script');
    script.src = 'https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js';
    script.async = true;
    document.head.appendChild(script);

    script.onload = () => {
      window.MathJax = {
        tex: {
          inlineMath: [['$', '$'], ['\\(', '\\)']],
          displayMath: [['$$', '$$'], ['\\[', '\\]']],
        },
        options: {
          skipHtmlTags: ['script', 'noscript', 'style', 'textarea', 'pre']
        }
      };

      // Optional initial content
      // markdownContent = '$4\\sqrt{2}$';

      processedContent = processMarkdown(markdownContent);
      preview.innerHTML = processedContent;
      renderMath();
    };
  });

  $: {
    processedContent = processMarkdown(markdownContent);
    if (preview) {
      preview.innerHTML = processedContent;
      renderMath();
    }
  }
</script>

<div bind:this={preview}></div>