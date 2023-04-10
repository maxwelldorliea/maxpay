<script>
  export let data;
  const user = data.user.user;
  const account = data.user.account;
</script>

<div class="bg-slate-200 flex items-center flex-col h-screen p-8">
  <h1 class="text-4xl text-center mt-8 font-bold tracking-4">Account Infomation</h1>
  <div class="text-3xl mt-8">
    <h3><span class="font-semibold">Name</span>: {user.first_name} {user.last_name}</h3>
    <h3><span class="font-semibold">Account Number</span>: {account.account_number}</h3>
    <h3><span class="font-semibold">Email</span>: {user.email}</h3>
    <h3><span class="font-semibold">Balance</span>: {account.balance}</h3>
  </div>
</div>
<style lang="postcss">
</style>
