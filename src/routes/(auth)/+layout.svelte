<script>
import Header from '$lib/components/HeaderAuth.svelte';
export let data;
</script>
<Header login={data.login}/>

<slot />
