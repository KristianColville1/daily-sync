
/** 
 * comment form
 function collects the post id and manipulates
 the appropriate container with the element to select */  
var commentForm = (postID) => {
    let selector = `.comment-form-${postID}`
    $(selector).removeClass('d-none');
}