$(document).ready(function () {
    let url = `ws://${window.location.host}/ws/socket-server/`;

    const chatSocket = new WebSocket(url)

    chatSocket.onmessage = (e) => {
        let data = JSON.parse(e.data)
        console.log('Data:', data)
    }
});