<script>
  import Balance from '../components/Balance.svelte';
  import AccountInfo from '../components/AccountInfo.svelte';
  import Activity from '../components/Activity.svelte';
  import { token } from './store.js';
  export let data;
  console.log($token);
  let accProps = {
    first_name: data.user.first_name,
    last_name: data.user.last_name,
    account_number: data.account.account_number
  }
</script>

<AccountInfo {...accProps} />
<div>
<Balance balance={data.account.balance} />
<Activity />
<h1>Token {$token} </h1>
</div>

<style lang="postcss">
</style>
