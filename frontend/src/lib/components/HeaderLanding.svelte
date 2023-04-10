<script>
  import { Hamburger } from 'svelte-hamburgers';
  import Menu from './Menu.svelte';
  export let login;
  let loginMenu = ['dashboard', 'logout'];
  let menu = ['login', 'signup'];
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
    <div class="hidden md:block"style="background-color:#1d1d2f;">
      <Hamburger
        bind:open
        --color="white" />
      <Menu bind:open menu={loginMenu}/>
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
       <a href='/login' class='mx-3'>Login</a>
       <a href='/signup'>Signup</a>
     </div>
   {:else}
     <div class="hidden md:block mt-4 text-xl">
       <a href='/dashboard' class='mx-3'>Dashboard</a>
       <a href='/logout'>Logout</a>
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
