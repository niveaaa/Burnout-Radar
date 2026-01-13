function updateDateTime(){
  const d = new Date();

  document.getElementById("current-datetime").innerText =
    d.toDateString() + " · " +
    d.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });

  document.getElementById("current-day").innerText =
    "Have a Nice " + d.toLocaleDateString(undefined, { weekday: 'long' }) + "!";
}

updateDateTime();
setInterval(updateDateTime, 60000);
