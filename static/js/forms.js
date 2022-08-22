/** 
 * comment form
 function collects the post id and manipulates
 the appropriate container with the element to select */
var commentForm = (postID) => {
    let selector = `.comment-form-${postID}`;
    $(selector).removeClass('d-none');
};

$(document).ready(() => {
    /**
     * Styles comment form
     */
    let commentContainer = $('#div_id_comment');
    let comment = $('#id_comment');
    $(comment).addClass('dark-boxes rounded-5 text-center');
    $(commentContainer).children().first().addClass('d-none');
});
/**
 * Adds create post modal form to template
 */
let csrf_token = $("input[name=csrfmiddlewaretoken]").val();
let postForm = `
    <div class="modal-header">
        <h1 class="modal-title w-100 text-center" id="create-post">Create a post</h1>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
    </div>
    <div class="modal-body">
    <form method="post" action="/posts/create_post/">
        <input type="hidden" name="csrfmiddlewaretoken" value="${csrf_token}">
        <label for="title" class="w-100 text-center modal-label">Title</label>
        <textarea name="title" rows="1" maxlength="200" required="" id="title" class="w-100 rounded"></textarea>
        <label for="post_body" class="w-100 text-center modal-label">Content</label>
        <textarea name="post_body" rows="6" maxlength="500" required="" id="post_body" class="w-100 rounded"></textarea>
        <button type="Submit" class="btn general-btn w-100 my-2 text-uppercase" aria-label="Click here to submit post">Post</button>
    </form>
    </div>
    `;

let shareForm = `
    <div class="modal-header">
        <h1 class="modal-title w-100 text-center" id="create-post">Create a post</h1>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
    </div>
    <div class="modal-body">
    <form method="post" action="/posts/create_post/">
        <input type="hidden" name="csrfmiddlewaretoken" value="${csrf_token}">
        <label for="title" class="w-100 text-center modal-label">Title</label>
        <textarea name="title" rows="1" maxlength="200" required="" id="title" class="w-100 rounded"></textarea>
        <label for="post_body" class="w-100 text-center modal-label">Content</label>
        <textarea name="post_body" rows="6" maxlength="500" required="" id="post_body" class="w-100 rounded"></textarea>
        <button type="Submit" class="btn general-btn w-100 my-2 text-uppercase" aria-label="Click here to submit post">Post</button>
    </form>
    </div>
    `;

let modalContents = '';
let addModalContents = (modalType) => {
    let modalTypes = {
        'post': postForm,
        'sharePost': shareForm,
    };
    for (const [key, value] of Object.entries(modalTypes)) {
        if (key === modalType) {
            modalContents = value;
            break;
        }
    }
    $('.modal-container').html(`
    <div class="modal fade" id="feed-create-post" tabindex="-1" aria-labelledby="feedCreatePost" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                ${modalContents}
            </div>
        </div>
    </div>`);
};


