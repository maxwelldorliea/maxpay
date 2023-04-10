<script>
  import DateTime from '$lib/components/DateTime.svelte';
  export let data;
</script>

<div class="bg-slate-200 flex items-center flex-col h-screen p-8 text-xl">
  <h1 class="text-4xl text-center font-bold mt-8 tracking-tight">Transaction Details</h1>
  <div class="mt-10 text-3xl">
    <h3><span class="font-semibold">Transaction Type</span>:  {data.obj.action}</h3>
    <h3><span class="font-semibold">{(data.obj.action === "Transfer") ? "Receiver" : "Sender" }</span>: {data.obj.receiver_sender_acc_id}</h3>
    <h3><span class="font-semibold">Amount</span>:  {data.obj.amount}</h3>
    <h3><span class="font-semibold">Balance Before Transaction</span>:  {data.obj.balance_before_transaction}</h3>
    <h3><span class="font-semibold">Balance After Transaction</span>:  {data.obj.balance_after_transaction}</h3>
    <h3><span class="font-semibold">Date Of Transaction</span>:  <DateTime date={data.obj.created_at} /></h3>
  </div>
</div>

<style lang="postcss">
</style>
