<script>
  import { Hamburger } from 'svelte-hamburgers';
  import Menu from './Menu.svelte';
  export let login;
  let loginMenu = ['Dashboard', 'Logout'];
  let menu = ['Login', 'Signup'];
  let open;
  const src = 'images/maxpay_logo.png';
</script>

{#if open}
  {#if login}
    <div class="md:hidden" style="background-color:#1d1d2f;">
      <Hamburger
        bind:open
        --color="white" />
      <Menu bind:open menu={loginMenu}/>
    </div>
    <div style="background-color:#1d1d2f;">
      <Hamburger
        bind:open
        --color="white" />
      <Menu bind:open {loginMenu}/>
    </div>
  {:else}
    <div class="md:hidden" style="background-color:#1d1d2f;">
      <Hamburger
        bind:open
        --color="white" />
      <Menu bind:open {menu}/>
    </div>
    <div class="hidden md:block" style="background-color:#1d1d2f;">
      <Hamburger
        bind:open
        --color="white" />
      <Menu bind:open {menu}/>
    </div>
  {/if}
{/if}

{#if !open}
  <header class="w-full bg-blue-600 p-6 text-white flex justify-between">
   <a href='/' class="flex">
     <img class="w-16" {src} alt="MaxPay Logo" />
     <h3 class="mx-6 mt-4 font-bold text-2xl">MAXPAY</h3>
   </a>
   {#if !login}
     <div class="mt-4 text-xl hidden md:block">
       <a href='/login'><button>Login</button></a>
       <a href='/signup'><button>Signup</button></a>
     </div>
   {:else}
     <div class="mt-4 text-xl">
       <a href='/dashboard'><button>Dashboard</button></a>
       <a href='/logout'><button>Logout</button></a>
     </div>
   {/if}
   <div class="md:hidden">
     <Hamburger
        bind:open
        --color="white" />
    </div>
  </header>
{/if}

<style lang="postcss">
</style>
