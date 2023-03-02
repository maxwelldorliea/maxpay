<script>
  export let form;
  console.log(form);
</script>

<form method="POST" class="form bg-slate-200 flex flex-col h-screen justify-center p-8 rounded-xl">
  <label>
    <span class="block text-center text-3xl mb-4">First Name<span class="text-red-700">*</span></span>
    <input name="first_name" type="text" value={form?.firstName ?? ''} class="md:w-3/5 block p-4 rounded-xl container mx-auto">
    {#if form?.fName?.missing}<p class="text-red-700 text-center">First Name is required</p>{/if}
  </label>
  <label>
    <span class="block text-center text-3xl mb-4">Middle Name</span>
    <input name="middle_name" type="text" value={form?.middleName ?? ''} class="md:w-3/5 block p-4 rounded-xl container mx-auto">
  </label>
  <label>
    <span class="block text-center text-3xl mb-4">Last Name<span class="text-red-700">*</span></span>
    <input name="last_name" type="text" value={form?.lastName ?? ''} class="md:w-3/5 block p-4 rounded-xl container mx-auto">
    {#if form?.lName?.missing}<p class="text-red-700 text-center">Last Name is required</p>{/if}
  </label>
  <label>
    <span class="block text-center text-3xl mb-4">Email<span class="text-red-700">*</span></span>
    <input name="email" type="email" value={form?.email ?? ''} class="md:w-3/5 block p-4 rounded-xl container mx-auto">
    {#if form?.mail?.missing}<p class="text-red-700 text-center">Email is required</p>{/if}
    {#if form?.mailTaken}<p class="text-red-700 text-center">Email is taken</p>{/if}
  </label>
  <label>
    <span class="block text-center text-3xl mt-4 mb-4">Password<span class="text-red-700">*</span></span>
    <input name="password" type="password" class="md:w-3/5 block p-4 rounded-xl container mx-auto">
    {#if form?.password?.missing}<p class="text-red-700 text-center">Password is required</p>{/if}
  </label>
  <button class="block text-3xl md:w-1/5 bg-blue-700 p-4 md:p-5 rounded-xl container mx-auto mt-5 text-white">Sign Up</button>
  <p class="text-2xl">Already Have An Account <a href="/login"><span class="text-blue-700">Sign In</span></a></p>
</form>

<style lang="postcss">
</style>
