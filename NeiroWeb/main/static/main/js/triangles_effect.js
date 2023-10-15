// Функция, создающая треугольник
function createTriangle() {
    // Создаем новый элемент div для треугольника
    var triangle = document.createElement(div);

    // Задаем случайные значения для высоты и начальной позиции треугольника
    var height = Math.random() * 200 + 100;
    var startPosX = Math.random() * window.innerWidth;
    var startPosY = Math.random() * window.innerHeight;

    // Задаем случайные значения для скорости и направления движения треугольника
    var speedX = Math.random() * 4 - 2; // от -2 до 2
    var speedY = Math.random() * 4 - 2; // от -2 до 2

    // Применяем стили к треугольнику
    triangle.style.left = startPosX + px;
    triangle.style.top = startPosY + px;
    triangle.style.transform = rotate( + Math.random() * 360 + deg);
    triangle.classList.add(triangle);
    if (Math.random() < 0.5) {
        triangle.classList.add(white);
    }

    // Добавляем треугольник на страницу
    document.body.appendChild(triangle);

     // Функция, обновляющая позицию треугольника с определенной периодичностью
    function updatePosition() {
        startPosX += speedX;
        startPosY += speedY;

        if (startPosX < 0 || startPosX > window.innerWidth) {
            speedX *= -1;
        }
        if (startPosY < 0 || startPosY > window.innerHeight) {
            speedY *= -1;
        }

        triangle.style.left = startPosX + px;
        triangle.style.top = startPosY + px;

        requestAnimationFrame(updatePosition);
    }
    requestAnimationFrame(updatePosition);
}

        // Функция, циклически создающая треугольники
        function createAnimatedTriangles() {
            // Очищаем текущие треугольники на странице
            var existingTriangles = document.querySelectorAll(.triangle);
            existingTriangles.forEach(function(triangle) {
                triangle.parentNode.removeChild(triangle);
            });

            // Создаем новые треугольники
            for (var i = 0; i < 10; i++) {
                createTriangle();
            }

            // Вызываем функцию снова после определенного времени
            setTimeout(createAnimatedTriangles, 5000);
        }

        // Запускаем создание треугольников
        createAnimatedTriangles();