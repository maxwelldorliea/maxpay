<script>
  export let form;
</script>

<form method="POST" class="flex flex-col h-screen justify-center p-8 bg-slate-200">
  <label>
    <span class="block text-center text-4xl mb-5">Verification Code</span>
    <input type="number" name="code" placeholder="Enter Your Verification Code" class="md:w-3/5 block rounded-xl p-4 container mx-auto">
    {#if form?.missing}<p class="text-red-700 text-center">Verification Code is required</p>{/if}
    {#if form?.incorrect}<p class="text-red-700 text-center">Incorrect Verification Code</p>{/if}
  </label>
  <button class="block text-3xl md:w-1/5 bg-blue-700 p-4 md:p-5 rounded-xl container mx-auto mt-5 text-white">Verify</button>
</form>

<style lang="postcss">
</style>
