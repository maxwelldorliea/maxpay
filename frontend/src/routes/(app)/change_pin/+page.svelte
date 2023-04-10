<script>
  export let form;
</script>

<form method="POST" class="form bg-slate-200 flex flex-col h-screen justify-center p-8 rounded-xl">
  <h1 class="text-center text-4xl font-bold mb-6">Change Transaction Pin</h1>
  <label>
    <span class="block text-center text-4xl mb-4">Pin</span>
    <input name="pin" type="password" placeholder="Enter your current pin" class="md:w-3/5 block p-4 rounded-xl container mx-auto">
    {#if form?.pin?.missing}<p class="text-red-700 text-center">Pin field is required</p>{/if}
    {#if form?.incorrect}<p class="text-red-700 text-center">Incorrect pin</p>{/if}
  </label>
  <label>
    <span class="block text-center text-4xl mt-4 mb-4">New Pin</span>
    <input name="new_pin" type="password" value={form?.new_pin ?? ''} placeholder="Enter your new pin" class="md:w-3/5 block p-4 rounded-xl container mx-auto">
    {#if form?.new_pin?.missing}<p class="text-red-700 text-center">New Pin field is required</p>{/if}
    {#if form?.same}<p class="text-red-700 text-center">New and current pins can't be the same</p>{/if}
    {#if form?.charExist}<p class="text-red-700 text-center">New pin can't include character(a-z)</p>{/if}
    {#if form?.lenInvalid}<p class="text-red-700 text-center">Pin must be 4 digits</p>{/if}
  <label>
    <span class="block text-center text-4xl mt-4 mb-4">Confirm Pin</span>
    <input name="confirm_pin" type="password" value={form?.confirm_pin ?? ''} placeholder="Enter your new pin again" class="md:w-3/5 block p-4 rounded-xl container mx-auto">
    {#if form?.confirm_pin?.missing}<p class="text-red-700 text-center">Confirm Pin field is required</p>{/if}
    {#if form?.mismatch}<p class="text-red-700 text-center">Confirm pin and new must be the same</p>{/if}
  </label>
  <button class="block text-3xl md:w-1/5 bg-blue-700 p-4 md:p-5 rounded-xl container mx-auto mt-5 text-white">Change</button>
</form>
<style lang="postcss">
</style>
