<script>
  import Balance from '../components/Balance.svelte';
  import AccountInfo from '../components/AccountInfo.svelte';
  import Activity from '../components/Activity.svelte';
  
  export let data;
  let accProps = {
    first_name: data.obj.user.first_name,
    last_name: data.obj.user.last_name,
    account_number: data.obj.account.account_number
  }
</script>

<AccountInfo {...accProps} />
<div>
<Balance balance={data.obj.account.balance} />
<Activity />
</div>

<style lang="postcss">
</style>
