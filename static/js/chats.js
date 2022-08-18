/**
 * Code from the django documentation for creating chats
 * I've simplified most of it for readability using jquery syntax as
 * its just easier to digest and parse through when fixing things.
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
const roomName = JSON.parse($('room-name').text());

/**
 * I'm using wss here because it works over http and https
 * and ws won't work over https.
 */
const chatSocket = new WebSocket(
    'wss://' +
    window.location.host +
    '/ws/chat/' +
    roomName +
    '/'
);

chatSocket.onmessage = (e) => {
    const data = JSON.parse(e.data);
    $('#chat-log').val() += (data.message + '\n');
};

chatSocket.onclose = (e) => {
    console.error('Chat socket closed unexpectedly');
};

$('#chat-message-input').focus();
$('#chat-message-input').on('keyup', (e) => {
    if (e.keyCode === 13) { // enter, return
        $('#chat-message-submit').click();
    }
});

$('#chat-message-submit').on('click', (e) => {
    const messageInputDom = $('#chat-message-input');
    const message = messageInputDom.value;
    chatSocket.send(JSON.stringify({
        'message': message
    }));
    messageInputDom.value = '';
});