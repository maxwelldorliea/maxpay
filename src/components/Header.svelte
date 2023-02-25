<script>
  let login = false;
</script>

<header class="bg-blue-500 p-6 text-white flex justify-between">
 <h3 class="font-bold text-2xl">MAXPAY</h3>
 {#if !login}
   <button>Sign In</button>
 {:else}
   <a href="/login"><button>Sign Out</button></a>
 {/if}
</header>

<style lang="postcss">
</style>
