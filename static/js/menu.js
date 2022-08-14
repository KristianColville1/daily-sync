/* Switches icons for the menu when button clicked open and close*/
let navMenu = false;
$('#menu-toggle').on('click', () => {
    let toggle_on = 'i.fa-bars';
    let toggle_off = 'i.fa-x';

    let thisSwitch = () => {
        if ($(toggle_off).hasClass('d-none')) {
            $(toggle_off).removeClass('d-none');
            $(toggle_on).addClass('d-none').fadeIn(1300);

        } else if ($(toggle_on).hasClass('d-none')) {
            $(toggle_on).removeClass('d-none');
            $(toggle_off).addClass('d-none').fadeIn(1300);
        }
    }

    thisSwitch();
});

/* Nav dropdown */
let navDropdown = false
$('#dropdownMenuButton1').on('click', () => {
    if (navDropdown == false){
        $('#nav-dropdown-menu').slideDown()
        navDropdown = true
    } else {
        $('#nav-dropdown-menu').slideUp()
        navDropdown = false
    }
});

/* posts dropdown */
/* because there are mulitple posts the history is stored and modified
    in order to slide the correct menu down */
let postDropdownHistory = []
let postDropdown = (post_id) => {
    if (postDropdownHistory.includes(post_id)){
        $(`.post-dropdown-${post_id}`).slideUp()
        let index = postDropdownHistory.indexOf(post_id)
        if (postDropdownHistory.length > 2){
            postDropdownHistory = postDropdownHistory.splice(index, index+1)
        } else if (postDropdownHistory.length == 2) {
            if (index > 0){
                postDropdownHistory.pop()
            } else {
                postDropdownHistory = postDropdownHistory(1)
            }
        }
        else {
            postDropdownHistory = []
        }
    } else {
        $(`.post-dropdown-${post_id}`).slideDown()
        postDropdownHistory.push(post_id)
    }
}