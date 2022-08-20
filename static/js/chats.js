/**
 * Some code pieces from the django documentation.
 * 
 * Link to original source https: //channels.readthedocs.io/en/latest/tutorial/part_2.html
 */
/**
 * Creating chat room 
 */
$('#room-name-input').focus();
$('#room-name-input').on('keyup', (e) => {
    if (e.KeyCode === 13) {
        $('#room-name-submit').click();
    }
});

$('#room-name-submit').on('click', (e) => {
    var roomName = $('#room-name-input').val();
    window.location.pathname = '/chats/' + roomName + '/';
});

/**
 * Using chat room
 */
const user_username = JSON.parse(document.getElementById('user_username').textContent);
document.querySelector('#submit-chat').onclick = function (e) {
    const messageInputDom = document.querySelector('#chat-message');
    const message = messageInputDom.value;
    chatSocket.send(JSON.stringify({
        'message': message,
        'username': user_username,
    }));
    messageInputDom.value = '';
};

const roomName = JSON.parse(document.getElementById('room-name').textContent);
const protocol = window.location.protocol === 'https:' ? 'wss:' : 'ws:';
const chatSocket = new WebSocket(
    protocol +
    window.location.host +
    '/ws/chat/' +
    roomName +
    '/'
);

chatSocket.onmessage = function (e) {
    const data = JSON.parse(e.data);
    console.log(data);
    document.querySelector('#chat-text').value += (data.username + ': ' + data.message + '\n');
};
