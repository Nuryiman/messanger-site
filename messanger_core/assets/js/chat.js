function sendMessage() {
    const input = document.getElementById('message-input');
    const message = input.value.trim();
    if (message !== "") {
        const chatBox = document.getElementById('chat-box');
        const newMessage = document.createElement('div');
        newMessage.className = 'message sent';

        // Добавить текст сообщения и текущее время
        const messageText = document.createElement('span');
        messageText.className = 'message-text';
        messageText.innerText = message;

        const messageTime = document.createElement('span');
        messageTime.className = 'message-time';
        const now = new Date();
        messageTime.innerText = now.getHours() + ':' + (now.getMinutes() < 10 ? '0' : '') + now.getMinutes();

        newMessage.appendChild(messageText);
        newMessage.appendChild(messageTime);
        chatBox.appendChild(newMessage);

        input.value = "";
        chatBox.scrollTop = chatBox.scrollHeight;
    }
}

function openChat(friendName) {
    const chatTitle = document.getElementById('chat-title');
    chatTitle.innerText = "Chat with " + friendName;
    const chatBox = document.getElementById('chat-box');
    chatBox.innerHTML = ''; // Очистить чат при переключении друга

    // Добавить приветственное сообщение
    const welcomeMessage = document.createElement('div');
    welcomeMessage.className = 'message received';

    const messageText = document.createElement('span');
    messageText.className = 'message-text';
    messageText.innerText = `You are now chatting with ${friendName}`;

    const messageTime = document.createElement('span');
    messageTime.className = 'message-time';
    messageTime.innerText = '10:00 AM';

    welcomeMessage.appendChild(messageText);
    welcomeMessage.appendChild(messageTime);
    chatBox.appendChild(welcomeMessage);

    // Обновить активного друга
    const friends = document.getElementById('friends').children;
    for (let friend of friends) {
        friend.classList.remove('active');
    }
    event.currentTarget.classList.add('active');
}
