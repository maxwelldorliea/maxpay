<script>
  export let login;
  const src = 'images/maxpay_logo.png';
</script>

<header class="w-full bg-blue-500 p-6 text-white flex justify-between">
 <a href='/' class="flex">
   <img class="w-16" {src} alt="MaxPay Logo" />
   <h3 class="mx-6 mt-4 font-bold text-2xl">MAXPAY</h3>
 </a>
 {#if !login}
   <div class="mt-4 text-xl">
     <a href='/login'><button>Login</button></a>
     <a href='/signup'><button>Signup</button></a>
   </div>
 {:else}
   <div class="mt-4 text-xl">
     <a href='/dashboard'><button>Dashboard</button></a>
     <a href='/logout'><button>Logout</button></a>
   </div>
 {/if}
</header>

<style lang="postcss">
</style>
