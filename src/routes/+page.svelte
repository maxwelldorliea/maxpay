<script>
  import Balance from '../components/Balance.svelte';
  import AccountInfo from '../components/AccountInfo.svelte';
  import Activity from '../components/Activity.svelte';
  export let data;

  let accProps = {
    first_name: data.user.first_name,
    last_name: data.user.last_name,
    account_number: data.account.account_number
  }
</script>

<div>
<AccountInfo {...accProps} />
<Balance balance={data.account.balance} />
<Activity />
</div>

<style lang="postcss">
</style>
