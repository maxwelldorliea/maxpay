<script>
  export let form;
  console.log(form);
</script>

<form method="POST" class="form bg-slate-200 flex flex-col h-screen justify-center p-8 rounded-xl">
  <label>
    <span class="block text-center text-4xl mb-4">Email</span>
    <input name="email" type="email" value={form?.email ?? ''} class="md:w-3/5 block p-4 rounded-xl container mx-auto">
  {#if form?.mail?.missing}<p class="text-red-700 text-center">Email field is required</p>{/if}
  </label>
  <label>
    <span class="block text-center text-4xl mt-4 mb-4">Password</span>
    <input name="password" type="password" class="md:w-3/5 block p-4 rounded-xl container mx-auto">
  {#if form?.password?.missing}<p class="text-red-700 text-center">Password field is required</p>{/if}
  {#if form?.incorrect}<p class="text-red-700 text-center">Incorrect email or password</p>{/if}
  </label>
  <button class="block text-3xl md:w-1/5 bg-blue-700 p-4 md:p-5 rounded-xl container mx-auto mt-5 text-white">Log in</button>
  <p class="text-2xl">You Don't Have An Account <a href="/signup"><span class="text-blue-700">Sign Up</span></a></p>
</form>

<style lang="postcss">
</style>
