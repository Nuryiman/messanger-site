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
