/** 
 * comment form
 function collects the post id and manipulates
 the appropriate container with the element to select */
var commentForm = (postID) => {
    let selector = `.comment-form-${postID}`;
    $(selector).removeClass('d-none');
};

/**
 * Adds create post modal form to template
 */
let csrf_token = $("input[name=csrfmiddlewaretoken]").val();

/**
 * Styles comment form
 */
let commentContainer = $('#div_id_comment');
let comment = $('#id_comment');
$(comment).addClass('dark-boxes rounded-5 text-center');
$(commentContainer).children().first().addClass('d-none');

/**
 * Modal logic
 */
/* create post */
$('.create-post-btn').hover(() => {
    $('.modal-title').html('Create a Post');
    let postForm = `
    <form method="post" action="/posts/create_post/">
        <input type="hidden" name="csrfmiddlewaretoken" value="${csrf_token}">
        <textarea name="post_body" rows="6" maxlength="500" required="" id="post_body" class="w-100 rounded"></textarea>
        <button type="Submit" class="btn general-btn w-100 my-2 text-uppercase" aria-label="Click here to submit post">Post</button>
    </form>
        `;
    $('.modal-body').html(`${postForm}`);
});

/* share post */
$('.share-post-btn').hover(function () {
    $('.modal-title').html('Share Post');
    let post_id = $(this).next().text();
    let shareForm = `
    <form method="post" action="/posts/share_post/${post_id}">
        <input type="hidden" name="csrfmiddlewaretoken" value="${csrf_token}">
        <textarea name="post_body" rows="6" maxlength="500" required="" id="post_body" class="w-100 rounded"></textarea>
        <button type="Submit" class="btn general-btn w-100 my-2 text-uppercase" aria-label="Click here to submit post">Share post</button>
    </form>
    `;
    $('.modal-body').html(`${shareForm}`);
});

/* modal container */
$('.modal-container').html(`
    <div class="modal fade" id="general-modal" tabindex="-1" aria-labelledby="general-modal" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
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
