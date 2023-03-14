<script>
  import { Hamburger } from 'svelte-hamburgers';
  import Menu from './Menu.svelte';
  
  const menu = ['account', 'logout']
  const src = 'images/maxpay_logo.png';
  let open;
</script>
{#if !open}
  <header class="w-full bg-blue-600 p-6 text-white flex justify-between">
  <a href='/' class="flex">
     <img class="w-16" {src} alt="MaxPay Logo" />
     <h3 class="mx-6 mt-4 font-bold text-2xl">MAXPAY</h3>
  </a>
   <div class="mt-4 my-4 text-xl hidden md:block">
     <a href='/account' class="my-3">Account</a>
     <a href="/logout">Logout</a>
   </div>
   <div class="md:hidden">
     <Hamburger bind:open --color='white' />
   </div>
  </header>
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
<style lang="postcss">
</style>
