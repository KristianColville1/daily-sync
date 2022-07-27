$(document).ready(()=> {

  /* Switches icons for the menu when button clicked open and close*/
  $('#menu-toggle').on('click', () => {
      let toggle_on = 'i.fa-bars';
      let toggle_off = 'i.fa-x';

      if ($(toggle_off).hasClass('d-none')){
          $(toggle_off).removeClass('d-none');
          $(toggle_on).addClass('d-none').fadeIn(1300);

      }  else if ($(toggle_on).hasClass('d-none')){
          $(toggle_on).removeClass('d-none');
          $(toggle_off).addClass('d-none').fadeIn(1300);
      } 
  });
});