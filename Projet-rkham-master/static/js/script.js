document.addEventListener('DOMContentLoaded', () => {
    const track = document.querySelector('.carousel-track');
    const slides = Array.from(track.children);
    const prevButton = document.querySelector('.carousel-btn.prev');
    const nextButton = document.querySelector('.carousel-btn.next');

    let currentIndex = 0;

    const updateSlidePosition = () => {
        console.log(`Current Index: ${currentIndex}`);

        // Update the transform property to shift the track to the correct position
        track.style.transform = `translateX(-${currentIndex * 70}%)`; // Adjust width for each slide
        console.log(`Track transform: translateX(-${currentIndex * 70}%)`);

        // Reset classes for all slides
        slides.forEach((slide, index) => {
            slide.classList.remove('active', 'prev', 'next');
            
            // Add 'active' class to the current slide
            if (index === currentIndex) {
                slide.classList.add('active');
            } 
            // Add 'prev' class to the previous slide
            else if (index === (currentIndex - 1 + slides.length) % slides.length) {
                slide.classList.add('prev');
            } 
            // Add 'next' class to the next slide
            else if (index === (currentIndex + 1) % slides.length) {
                slide.classList.add('next');
            }
        });
    };

    prevButton.addEventListener('click', () => {
        console.log("Prev button clicked");
        // Move to the previous slide
        currentIndex = (currentIndex - 1 + slides.length) % slides.length;
        console.log(`New Current Index after Prev: ${currentIndex}`);
        updateSlidePosition();
    });

    nextButton.addEventListener('click', () => {
        console.log("Next button clicked");
        // Move to the next slide
        currentIndex = (currentIndex + 1) % slides.length;
        console.log(`New Current Index after Next: ${currentIndex}`);
        updateSlidePosition();
    });

    // Initialize the carousel on load
    console.log("Initializing carousel");
    updateSlidePosition();
});

// Select the toggle button
const darkModeToggle = document.getElementById('theme-toggle');

// Add event listener to the button
darkModeToggle.addEventListener('click', () => {
    document.body.classList.toggle('dark-mode');
    document.querySelectorAll('.header, .nav ul li a, .hero, .hero-overlay, .catalog, .footer, .contact form, .testimonials, section, article, aside, button, input[type="submit"], .card, img')
        .forEach(element => element.classList.toggle('dark-mode'));
    
    if (document.body.classList.contains('dark-mode')) {
        localStorage.setItem('darkMode', 'enabled');
    } else {
        localStorage.setItem('darkMode', 'disabled');
    }
});

if (localStorage.getItem('darkMode') === 'enabled') {
    document.body.classList.add('dark-mode');
    document.querySelectorAll('.header, .nav ul li a, .hero, .hero-overlay, .catalog, .footer, .contact form, .testimonials, section, article, aside, button, input[type="submit"], .card, img')
        .forEach(element => element.classList.add('dark-mode'));
}

document.addEventListener('DOMContentLoaded', () => {
    const body = document.body;
    const toggleCheckbox = document.getElementById('theme-toggle');
    const darkModeClass = 'dark-mode';
    const storedTheme = localStorage.getItem('theme');

    // Apply the saved theme on page load
    if (storedTheme === 'dark') {
        body.classList.add(darkModeClass);
        toggleCheckbox.checked = true; // Set the toggle to "on" for dark mode
    } else {
        body.classList.remove(darkModeClass);
        toggleCheckbox.checked = false; // Set the toggle to "off" for light mode
    }

    // Listen for toggle changes
    toggleCheckbox.addEventListener('change', () => {
        if (toggleCheckbox.checked) {
            body.classList.add(darkModeClass);
            localStorage.setItem('theme', 'dark');
        } else {
            body.classList.remove(darkModeClass);
            localStorage.setItem('theme', 'light');
        }
    });
});
