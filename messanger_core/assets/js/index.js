// Функция поиска друзей
function searchFriends() {
    const searchInput = document.getElementById('search-input').value.toLowerCase();
    const friendsList = document.querySelectorAll('.friend');

    friendsList.forEach(friend => {
        const friendName = friend.querySelector('span').textContent.toLowerCase();
        if (friendName.includes(searchInput)) {
            friend.style.display = '';
        } else {
            friend.style.display = 'none';
        }
    });
}

// Обработчик для клика по другу, чтобы сделать его активным
document.querySelectorAll('.friend').forEach(friend => {
    friend.addEventListener('click', function () {
        document.querySelectorAll('.friend').forEach(f => f.classList.remove('active'));
        this.classList.add('active');
    });
});

// Открытие и закрытие попапа для добавления друга
const addFriendBtn = document.getElementById('add-friend-btn');
const addFriendPopup = document.getElementById('add-friend-popup');
const cancelAddBtn = document.getElementById('cancel-add');
const saveFriendBtn = document.getElementById('save-friend');

addFriendBtn.addEventListener('click', function () {
    addFriendPopup.style.display = 'flex';
});

cancelAddBtn.addEventListener('click', function () {
    addFriendPopup.style.display = 'none';
});

saveFriendBtn.addEventListener('click', function () {
    const friendName = document.getElementById('new-friend-name').value;
    if (friendName) {
        alert(`Friend ${friendName} added!`);
        addFriendPopup.style.display = 'none';
    } else {
        alert('Please enter a name.');
    }
});

// Переключение между темной и светлой темой
const themeToggleBtn = document.createElement('button');
themeToggleBtn.textContent = 'Switch Theme';
themeToggleBtn.style.position = 'absolute';
themeToggleBtn.style.top = '20px';
themeToggleBtn.style.right = '20px';
themeToggleBtn.style.padding = '10px';
themeToggleBtn.style.backgroundColor = '#0984e3';
themeToggleBtn.style.color = 'white';
themeToggleBtn.style.border = 'none';
themeToggleBtn.style.borderRadius = '6px';
themeToggleBtn.style.cursor = 'pointer';
themeToggleBtn.addEventListener('click', () => {
    document.body.classList.toggle('dark-mode');
});

document.body.appendChild(themeToggleBtn);
