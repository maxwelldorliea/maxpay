<script>
    import { fly, scale } from 'svelte/transition';
    import { quadOut } from 'svelte/easing';

    export let open;
    export let menu;
</script>

{#if open}
    <div>
        {#each menu as link, i}
            <a href="/{link}" transition:fly={{ y: -15, delay: 50 * i }}>
                {link}
            </a>
        {/each}
    </div>

    <hr transition:scale={{ duration: 750, easing: quadOut, opacity: 1 }} />
{/if}

<style>
    div {
        width: 100%;
        height: 100vh;
        background-color: #1d1d2f;
        text-align: center;
        font-size: 1.5em;
        letter-spacing: 0.15em;
        padding: 1em;
        padding-top: 0;
        color: #eef;
    }
    a {
        display: block;
        cursor: pointer;
        width: max-content;
        margin: 1rem auto;
    }
    a:hover {
        text-decoration: underline;
    }
</style>
