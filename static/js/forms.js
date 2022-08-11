/** 
 * comment form
 function collects the post id and manipulates
 the appropriate container with the element to select */
var commentForm = (postID) => {
    let selector = `.comment-form-${postID}`
    $(selector).removeClass('d-none');
}

$(document).ready(() => {
    /**
     * Styles comment form
     */
    let commentContainer = $('#div_id_comment');
    let comment = $('#id_comment');
    $(comment).addClass('dark-boxes rounded-5 text-center');
    $(commentContainer).children().first().addClass('d-none')
})
