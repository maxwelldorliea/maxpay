<script>
import '../../app.css';
 import Header from '$lib/components/HeaderLanding.svelte';
 export let data;
</script>
<Header login={data.login} />

<slot />
