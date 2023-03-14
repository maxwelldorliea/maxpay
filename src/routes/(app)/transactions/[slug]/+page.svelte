<script>
  import DateTime from '$lib/components/DateTime.svelte';
  export let data;
</script>

<div class="bg-slate-200 flex flex-col h-screen justify-center p-8 text-center text-xl">
  <h1 class="text-3xl font-bold mb-6">Transaction Details</h1>
  <p><span class="font-bold text-xl">Transaction Type</span>:  {data.obj.action}</p>
  <p><span class="font-bold text-xl">{(data.obj.action === "Transfer") ? "Receiver" : "Sender" }</span>: {data.obj.receiver_sender_acc_id}</p>
  <p><span class="font-bold text-xl">Amount</span>:  {data.obj.amount}</p>
  <p><span class="font-bold text-xl">Balance Before Transaction</span>:  {data.obj.balance_before_transaction}</p>
  <p><span class="font-bold text-xl">Balance After Transaction</span>:  {data.obj.balance_after_transaction}</p>
  <p><span class="font-bold text-xl">Date Of Transaction</span>:  <DateTime date={data.obj.created_at} /></p>
</div>

<style lang="postcss">
</style>
