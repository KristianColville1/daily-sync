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

  /**
   * Handles the emojies and makes visible to user to select a like option
   * written this way so emojies are shown correctly and stay on screen.
   * The usual method will make them instantly disapear otherwise.
   */
  $('.like-btn').hover(function(){
    $(this).siblings().css('visibility', 'unset');
  }, function(){
    $('.emojies').mouseleave(function () {
      $(this).css('visibility', 'hidden');
    })
  });
});