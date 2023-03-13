<script>
  let login = false;
  const src = 'images/maxpay_logo.png';
</script>

<header class="w-full bg-blue-500 p-6 text-white flex justify-between">
 <a href='/' class="flex">
   <img class="w-16" {src} alt="MaxPay Logo" />
   <h3 class="mx-6 mt-4 font-bold text-2xl">MAXPAY</h3>
 </a>
 {#if !login}
   <a href='/login'><button>Sign In</button></a>
 {:else}
   <a href="/login"><button>Sign Out</button></a>
 {/if}
</header>

<style lang="postcss">
</style>
