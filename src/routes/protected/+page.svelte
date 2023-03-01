<script>
import { getMe, token } from '../store.js';
import { onMount } from 'svelte';

onMount(async ()=> {
  console.log(await cookieStore.get('token')); 
  const me = await getMe($token)
  console.log(me);
  console.log($token);
});
</script>

<h1> Hello Protected </h1>
