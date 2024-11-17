let selectedMessages = new Set(); // Хранение ID выбранных сообщений
let firstSelected = false; // Флаг для первого выбора
const editButton = document.getElementById('edit-button');
const deleteForm = document.getElementById('delete-form');
const messageIdsInput = document.getElementById('message-ids');
const editMessageContainer = document.getElementById('edit-message-container');
const editMessageInput = document.getElementById('edit-message-input');
const editMessageIdInput = document.getElementById('edit-message-id');

// Функция для обработки первого выбора (правый клик)
function rightClickFirstSelect(event, element) {
    event.preventDefault(); // Отменяем стандартное контекстное меню
    if (!firstSelected) {
        firstSelected = true;
        selectMessage(element); // Выбираем сообщение
    }
}

// Функция для обработки выбора последующих сообщений (левый клик)
function leftClickSelect(element) {
    if (!firstSelected) return; // Игнорируем выбор до первого выделения
    selectMessage(element); // Выбираем или снимаем выбор
}

// Общая функция для выделения/снятия выделения сообщения
function selectMessage(element) {
    const messageId = element.dataset.id;
    const senderId = element.dataset.sender;
    const isUserMessage = element.classList.contains('sent');

    // Снимаем выделение, если оно уже есть
    if (selectedMessages.has(messageId)) {
        selectedMessages.delete(messageId);
        element.classList.remove('selected');
    } else {
        // Добавляем сообщение в выделенные
        selectedMessages.add(messageId);
        element.classList.add('selected');
    }

    // Обновляем видимость кнопки редактирования и удаления
    if (isUserMessage) {
        editButton.style.display = selectedMessages.size === 1 ? 'inline-block' : 'none';
    }

    // Обновляем видимость кнопки удаления
    deleteForm.style.display = selectedMessages.size > 0 ? 'block' : 'none';

    // Обновляем значение в скрытом поле формы для удаления
    messageIdsInput.value = Array.from(selectedMessages).join(',');
}

// Редактирование выбранного сообщения
function editSelectedMessage() {
    const selectedMessageId = Array.from(selectedMessages)[0]; // Получаем ID выбранного сообщения
    const messageElement = document.querySelector(`.message[data-id="${selectedMessageId}"]`);
    const messageText = messageElement.querySelector('.message-text').innerText;

    // Получаем ID отправителя сообщения
    const senderId = messageElement.dataset.sender;

    // Проверяем, что сообщение принадлежит пользователю
    if (senderId === '{{ user.id }}') {  // Если сообщение от текущего пользователя
        // Показываем форму редактирования с текстом выбранного сообщения
        alert('Вы не можете редактировать сообщение собеседника.');
    } else {
        editMessageInput.value = messageText;
        editMessageIdInput.value = selectedMessageId;
        editMessageContainer.style.display = 'block';
    }
}
