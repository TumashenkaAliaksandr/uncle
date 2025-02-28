// Получаем кнопку и контент выпадающего списка
var dropdownBtn = document.getElementsByClassName("dropdown-btn");
var dropdownContent = document.getElementsByClassName("dropdown-content");

// Добавляем обработчик клика на кнопку
for (var i = 0; i < dropdownBtn.length; i++) {
    dropdownBtn[i].addEventListener("click", function() {
        // Получаем родительский элемент кнопки
        var parent = this.parentNode;

        // Находим выпадающий контент внутри родителя
        var content = parent.querySelector(".dropdown-content");

        // Показываем или скрываем выпадающий контент
        if (content.classList.contains('show')) {
            content.classList.remove('show');
        } else {
            content.classList.add('show');
        }
    });
}

// Закрываем выпадающий список при клике вне его
window.addEventListener("click", function(event) {
    if (!event.target.matches('.dropdown-btn')) {
        var dropdowns = document.getElementsByClassName("dropdown-content");
        var i;
        for (i = 0; i < dropdowns.length; i++) {
            var openDropdown = dropdowns[i];
            if (openDropdown.classList.contains('show')) {
                openDropdown.classList.remove('show');
            }
        }
    }
});

document.getElementById('song-list').addEventListener('click', function(event) {
    if (event.target.tagName === 'LI') {
        var songSrc = event.target.getAttribute('data-song-src');
        if (songSrc) {
            var link = document.createElement('a');
            link.href = songSrc;
            link.download = songSrc.split('/').pop(); // Установить имя файла для скачивания
            link.click();
        }
    }
});

