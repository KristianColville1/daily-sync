/** 
 * comment form
 function collects the post id and manipulates
 the appropriate container with the element to select */

var commentForm = (postID) => {
    let selector = `.comment-form-${postID}`;
    if ($(selector).hasClass('opened')){
        $(selector).removeClass('opened').slideUp();
    } else {
        $(selector).removeClass('d-none').addClass('opened').slideDown();
    }
};

/**
 * Adds the required html code blocks depending on which modal.
 * Generates a create post & share post modal
 */
/* collects csrf_token */
let csrf_token = $("input[name=csrfmiddlewaretoken]").val();

/**
 * Modal logic
 */
/* create post */
$('.create-post-btn').hover(() => {
    $('.modal-title').html('Create a Post');
    let postForm = `
    <form method="post" action="/posts/create_post/">
        <input type="hidden" name="csrfmiddlewaretoken" value="${csrf_token}">
        <textarea name="post_body" rows="6" maxlength="500" required="" id="post_body" class="w-100 rounded" placeholder="Write here..."></textarea>
        <button type="Submit" class="btn general-btn w-100 my-2 text-uppercase" aria-label="Click here to submit post">Post</button>
    </form>
        `;
    $('.modal-body').html(`${postForm}`);
});

/* share post */
$('.share-post-btn').hover(function () {
    $('.modal-title').html('Share Post');
    let post_id = $(this).next().text();
    let to_share = $(this).parentsUntil('div.post').parent().html();
    
    
    let shareForm = `
    <form method="post" action="/posts/share_post/${post_id}/">
        <input type="hidden" name="csrfmiddlewaretoken" value="${csrf_token}">
        <textarea name="post_body" rows="6" maxlength="500" required="" id="post_body" class="w-100 rounded" placeholder="Write here..."></textarea>
        <h3 class="w-100 text-center">sharing:</h3>
        <div class="w-100 dark-boxes border shadow-sm post-to-share mt-3 p-2"></div>
        <button type="Submit" class="btn general-btn w-100 my-2 text-uppercase" aria-label="Click here to submit post">Share post</button>
    </form>
    
    `;
    $('.modal-body').html(`${shareForm}`);
    let post_sharing = $('.post-to-share').html(to_share);
    /* removes the button options at the end of the post the user is sharing*/
    $('.post-to-share').find('.post-options').html('');
    $('.post-to-share').find('.user-post-options').html('');
    $('.post-to-share').find('.user-post-options').next().html('');
});

/* modal container */
$('.modal-container').html(`
    <div class="modal fade" id="general-modal" tabindex="-1" aria-labelledby="general-modal" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content boxes">
          <div class="modal-header">
            <h1 class="modal-title text-center w-100"></h1>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
          </div>
          <div class="modal-extra-content"></div>
        </div>
      </div>
    </div>`);
