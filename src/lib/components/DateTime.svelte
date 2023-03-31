<script>
  export let date;
  const DAYS = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
  const MONTH = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
  date = new Date(date);
  const day = DAYS[date.getDay()];
  const dat = date.getDate();
  const month = MONTH[date.getMonth()];
  const year = date.getFullYear();
  const hour = date.getHours();
  const min = date.getMinutes();
  const sec = date.getSeconds();
</script>
<h1>{day}, {month} {dat}, {year}  {hour}:{(min <= 9) ? f'0{min}' : min}:{(sec === 0) ? '00' : sec}</h1>
