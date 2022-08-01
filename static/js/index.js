$(document).ready(() => {

  /* Alerts the user to any messages */
  setTimeout(() => {
    let messages = document.getElementById("msg");
    let alert = new bootstrap.Alert(messages);
    alert.close();
  }, 3200);

});