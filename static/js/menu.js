/* Nav dropdown */
let navDropdown = false;
$('#settings').on('click', () => {
    if (navDropdown == false) {
        $('#nav-dropdown-menu').slideDown();
        navDropdown = true;
    } else {
        $('#nav-dropdown-menu').slideUp();
        navDropdown = false;
    }
});

/* Nav dropdown */
let notifyDropdown = false;
$('#notifications-dropdown').on('click', () => {
    if (notifyDropdown == false) {
        $('#notifications-dropdown-menu').slideDown('fast');
        notifyDropdown = true;
    } else {
        $('#notifications-dropdown-menu').slideUp('fast');
        notifyDropdown = false;
    }
});

/* posts dropdown */
/* because there are multiple posts the history is stored and modified
    in order to slide the correct menu down.
    Could of used 'this' in regular function but wanted to practice different
    methods of accomplishing same goal and other use cases. */
let postDropdownHistory = [];
let postDropdown = (post_id) => {
    if (postDropdownHistory.includes(post_id)) {
        $(`.post-dropdown-${post_id}`).slideUp();
        let index = postDropdownHistory.indexOf(post_id);
        if (postDropdownHistory.length > 2) {
            postDropdownHistory = postDropdownHistory.splice(index, index + 1);
        } else if (postDropdownHistory.length == 2) {
            if (index > 0) {
                postDropdownHistory.pop();
            } else {
                postDropdownHistory = postDropdownHistory(1);
            }
        } else {
            postDropdownHistory = [];
        }
    } else {
        $(`.post-dropdown-${post_id}`).slideDown();
        postDropdownHistory.push(post_id);
    }
};

let commentDropdownHistory = [];
let commentDropdown = (comment_id) => {
    if (commentDropdownHistory.includes(comment_id)) {
        $(`.comment-dropdown-${comment_id}`).slideUp();
        let index = commentDropdownHistory.indexOf(comment_id);
        if (commentDropdownHistory.length > 2) {
            commentDropdownHistory = commentDropdownHistory.splice(index, index + 1);
        } else if (commentDropdownHistory.length == 2) {
            if (index > 0) {
                commentDropdownHistory.pop();
            } else {
                commentDropdownHistory = commentDropdownHistory(1);
            }
        } else {
            commentDropdownHistory = [];
        }
    } else {
        $(`.comment-dropdown-${comment_id}`).slideDown();
        commentDropdownHistory.push(comment_id);
    }
};