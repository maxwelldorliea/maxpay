<script>
import '../../app.css';
 import Header from '$lib/components/HeaderLanding.svelte';
 import Footer from '$lib/components/Footer.svelte';
 export let data;
</script>
<Header login={data.login} />
<slot />
<Footer />
