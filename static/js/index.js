$(document).ready(() => {

  /* Dark mode */
  let darkModeSwitch = false;
  $('button.enable-dark-mode').click(() => {
    if (!darkModeSwitch) {
      document.documentElement.style.setProperty('--whitesmoke', getComputedStyle(document.documentElement).getPropertyValue('--black'));


      darkModeSwitch = true;
      $('.fa-moon').addClass('d-none');
      $('.fa-sun').removeClass('d-none');
    } else {
      document.documentElement.style.setProperty('--black', getComputedStyle(document.documentElement).getPropertyValue('--whitesmoke'));


      darkModeSwitch = false;
      $('.fa-moon').addClass('d-none');
      $('.fa-sun').removeClass('d-none');
    }

  });

  /* enabled tooltips using bootstrap & popper */
  var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
  var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
    return new bootstrap.Tooltip(tooltipTriggerEl);
  });

  /**
   * Handles the emoji'e's and makes visible to user to select a like option
   * written this way so emoji'e's are shown correctly and stay on screen.
   * The usual method will make them instantly disappear otherwise.
   */
  $('.like-btn').hover(function(){
    $(this).siblings().css('visibility', 'unset').animate({top: '-55px'});
  }, function(){
    $('.emojies').mouseleave(function () {
      $(this).css('visibility', 'hidden').css('top', '0px');
    });
  });
});

/* Alerts the user to any messages */
setTimeout(() => {
  let messages = document.getElementById("msg");
  let alert = new bootstrap.Alert(messages);

  if($('#msg').length > 0){
    alert.close();
  }
}, 3200);

const topBtn = $('#top-btn');
window.onscroll = () =>{showScrollerBtn();};

const showScrollerBtn = () => {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    topBtn.css('display', 'block');
  } else {
    topBtn.css('display', 'none');
  }
};

// configured for main browsers to scroll to top if clicked
let backToTop = () =>{
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
};
