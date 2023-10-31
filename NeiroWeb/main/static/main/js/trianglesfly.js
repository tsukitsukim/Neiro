// Script made with ChatGPT by OpenAI
document.addEventListener("DOMContentLoaded", function() {
    // Get the triangles container element by ID
    const trianglesContainer = document.getElementById('triangles');
    // Calculate the center of the screen
    const centerX = window.innerWidth / 2;
    const centerY = window.innerHeight / 2;

    // Function to animate the triangles
    function animateTriangles() {
        for (let i = 0; i < 30; i++) {
            const triangle = document.createElement('div');
            triangle.classList.add('triangle');

            let startX, startY;
            // Determine the color of the triangle
            const color = i % 2 === 0 ? '#830fd2' : 'white';

            if (Math.random() < 0.25) {
                // Small triangles start from the left
                startX = -60;
                startY = Math.random() * window.innerHeight;
                triangle.style.left = `${startX}px`;
                triangle.style.top = `${startY}px`;
                triangle.style.borderLeft = '10px solid transparent'; // Smaller size
                triangle.style.borderRight = '10px solid transparent'; // Smaller size
                triangle.style.borderBottom = `17.5px solid ${color}`; // Smaller size
            } else if (Math.random() >= 0.25 && Math.random() < 0.5) {
                // Small triangles start from the right
                startX = window.innerWidth + 60;
                startY = Math.random() * window.innerHeight;
                triangle.style.left = `${startX}px`;
                triangle.style.top = `${startY}px`;
                triangle.style.borderLeft = '10px solid transparent'; // Smaller size
                triangle.style.borderRight = '10px solid transparent'; // Smaller size
                triangle.style.borderBottom = `17.5px solid ${color}`; // Smaller size
            } else if (Math.random() >= 0.5 && Math.random() < 0.75) {
                // Triangles start from the left
                startX = -60;
                startY = Math.random() * window.innerHeight;
                triangle.style.left = `${startX}px`;
                triangle.style.top = `${startY}px`;
                triangle.style.borderLeft = '20px solid transparent'; // Original size
                triangle.style.borderRight = '20px solid transparent'; // Original size
                triangle.style.borderBottom = `35px solid ${color}`; // Original size
            } else {
                // Triangles start from the right
                startX = window.innerWidth + 60;
                startY = Math.random() * window.innerHeight;
                triangle.style.left = `${startX}px`;
                triangle.style.top = `${startY}px`;
                triangle.style.borderLeft = '20px solid transparent'; // Original size
                triangle.style.borderRight = '20px solid transparent'; // Original size
                triangle.style.borderBottom = `35px solid ${color}`; // Original size
            }

            // Append the triangle to the container
            trianglesContainer.appendChild(triangle);

            // Calculate the duration of the animation
            const duration = 6 + Math.random() * 7;
            // Set transition properties
            triangle.style.transition = `all ${duration}s linear, transform ${duration}s ease-in-out, opacity ${duration}s linear`;

            // Generate a random angle for the triangle's motion
            const angle = Math.random() * 360;
            // Calculate the ending coordinates
            const endX = centerX + Math.cos(angle) * 1000;
            const endY = centerY + Math.sin(angle) * 1000;

            // Add a delay before the triangle appears
            setTimeout(() => {
                triangle.style.left = `${endX}px`;
                triangle.style.top = `${endY}px`;
                triangle.style.opacity = '1'; // Smooth appearance
                triangle.style.transform = `rotate(${Math.random() * 360}deg)`;
            }, 100);

            // Remove the triangle when the animation is complete
            triangle.addEventListener('transitionend', function() {
                trianglesContainer.removeChild(triangle);
            });
        }
    }

    // Call the animation function to start
    animateTriangles();

    // Set up a timer to repeat the animation every 4 seconds
    setInterval(animateTriangles, 4000);
});
