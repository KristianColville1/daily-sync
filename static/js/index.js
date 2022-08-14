$(document).ready(() => {

  /* Alerts the user to any messages */
  setTimeout(() => {
    let messages = document.getElementById("msg");
    let alert = new bootstrap.Alert(messages);
    alert.close();
  }, 3200);

  /* Darkmode */
  let darkModeSwitch = false;
  $('button.enable-dark-mode').click(() => {
    if (!darkModeSwitch) {
      document.documentElement.style.setProperty('--whitesmoke', getComputedStyle(document.documentElement).getPropertyValue('--black'));


      darkModeSwitch = true;
      $('.fa-moon').addClass('d-none')
      $('.fa-sun').removeClass('d-none')
    } else {
      document.documentElement.style.setProperty('--black', getComputedStyle(document.documentElement).getPropertyValue('--whitesmoke'));


      darkModeSwitch = false;
      $('.fa-moon').addClass('d-none')
      $('.fa-sun').removeClass('d-none')
    }

  })

  /* enabled tooltips*/
  $('.tooltip').tooltip();
  $('.nav-link').attr('title').css('background-color', 'var(--carolina-blue)')
});