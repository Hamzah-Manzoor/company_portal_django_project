document.getElementById('profile-icon').addEventListener('click', function() {
    var menu = document.getElementById('profile-menu');
    if (menu.style.display === 'block') {
        menu.style.display = 'none';
    } else {
        menu.style.display = 'block';
    }
});

let currentIndex = 0;
const slides = document.querySelectorAll('.slide');
const totalSlides = slides.length;

function showSlide(index) {
    slides.forEach((slide, i) => {
        slide.classList.remove('active', 'left', 'right');
        if (i === index) {
            slide.classList.add('active');
        } else if (i === (index - 1 + totalSlides) % totalSlides) {
            slide.classList.add('left');
        } else if (i === (index + 1) % totalSlides) {
            slide.classList.add('right');
        }
    });
}

function showNextSlide() {
    currentIndex = (currentIndex + 1) % totalSlides;
    showSlide(currentIndex);
}

function showPrevSlide() {
    currentIndex = (currentIndex - 1 + totalSlides) % totalSlides;
    showSlide(currentIndex);
}

document.getElementById('next').addEventListener('click', showNextSlide);
document.getElementById('prev').addEventListener('click', showPrevSlide);

setInterval(showNextSlide, 3500);

showSlide(currentIndex);

function incrementCount(type) {
    var countElement = document.getElementById(type + '-count');
    var count = parseInt(countElement.innerText);
    countElement.innerText = count + 1;
}


