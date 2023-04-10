<script>
  export let form;
</script>
<form method="POST">
{#if !form?.isAvailable}
  <div class="bg-slate-200 flex flex-col h-screen justify-center p-4 text-center">
    <label>
      <span class="block text-2xl mb-2">Account Number</span>
      <input type="number" placeholder="Enter Account Number" name="account_number" value={form?.account_number} class="block container p-4 rounded-xl text-xl">
      {#if form?.account?.missing}<p class="text-center text-red-700">Receiver Account Number is Required</p>{/if}
      {#if form?.sameAcc}<p class="text-center text-red-700">Can't transfer to yourself</p>{/if}
      {#if form?.notExist}<p class="text-center text-red-700">This account doesn't exists</p>{/if}
    </label>
    <label class="mt-4">
      <span class="block text-2xl mb-2">Amount</span>
      <input type="number" placeholder="Enter Amount" name="amount" value={form?.amount} class="block container p-4 rounded-xl text-xl">
      {#if form?.amount?.missing}<p class="text-center text-red-700">Amount is Required</p>{/if}
      {#if form?.notDivible}<p class="text-center text-red-700">Amount must be divible by 5</p>{/if}
      {#if form?.notValid}<p class="text-center text-red-700">Amount can't be negative or zero</p>{/if}
      {#if form?.insufficient}<p class="text-center text-red-700">Not enough fund</p>{/if}
    </label>
    <button class="bg-blue-700 p-3 mt-4 rounded-xl text-white text-2xl" formaction="?/initialize">Next</button>
  </div>
{:else}
  <div class="bg-slate-200 flex flex-col h-screen justify-center p-4 text-center">
    <h4 class="text-2xl md:text-3xl mb-6">You are about to send ${form?.amount} to account number {form?.account_number}({form?.username})</h4>
    <label class="mt-4">
      <span class="block text-2xl mb-2">Transaction PIN</span>
      <input type="number" placeholder="Enter Your PIN" name="pin" class="block container p-4 rounded-xl text-xl">
      {#if form?.missing}<p class="text-center text-red-700">Pin is Required</p>{/if}
      {#if form?.invalid}<p class="text-center text-red-700">Invalid pin</p>{/if}
    </label>
    <button class="bg-blue-700 p-3 mt-4 rounded-xl text-white text-2xl" formaction="?/complete">Confirm Transfer</button>
  </div>
{/if}
</form>
<style lang="postcss">
</style>
