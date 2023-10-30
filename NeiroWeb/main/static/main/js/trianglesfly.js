document.addEventListener("DOMContentLoaded", function() {
    const trianglesContainer = document.getElementById('triangles');
    const centerX = window.innerWidth / 2;
    const centerY = window.innerHeight / 2;

    function animateTriangles() {
        // Очищаем контейнер от старых треугольников
        // trianglesContainer.innerHTML = '';

        for (let i = 0; i < 30; i++) {
            const triangle = document.createElement('div');
            triangle.classList.add('triangle');

            let endXPosition;

            if (Math.random() < 0.5) {
                triangle.style.left = `${window.innerWidth + 60}px`;
                triangle.style.top = `${Math.random() * window.innerHeight}px`;
                endXPosition = -60; // треугольник должен исчезнуть за левым краем
            }
            else {
                triangle.style.left = '-60px';
                triangle.style.top = `${Math.random() * window.innerHeight}px`;
                endXPosition = window.innerWidth + 60; // треугольник должен исчезнуть за правым краем
            }

            const endYPosition = parseFloat(triangle.style.top) + (Math.random() - 0.5) * 1000;

            const color = i % 2 === 0 ? '#830fd2' : 'white';
            triangle.style.borderLeft = '20px solid transparent';
            triangle.style.borderRight = '20px solid transparent';
            triangle.style.borderBottom = `35px solid ${color}`;

            trianglesContainer.appendChild(triangle);

            const duration = 5 + Math.random() * 7;
            triangle.style.transition = `all ${duration}s linear, transform ${duration}s ease-in-out, opacity ${duration}s linear`;

            setTimeout(() => {
                triangle.style.left = `${endXPosition}px`;
                triangle.style.top = `${endYPosition}px`; // используем endYPosition здесь
                triangle.style.opacity = '0';
                triangle.style.transform = `rotate(${Math.random() * 360}deg)`;
            }, 100);

            // Удаление треугольника, когда анимация завершена
            triangle.addEventListener('transitionend', function() {
                trianglesContainer.removeChild(triangle);
            });
        }
    }

    animateTriangles();  // Запускаем первый раз

    // Запускаем анимацию каждые 4 секунды
    setInterval(animateTriangles, 4000);
});
