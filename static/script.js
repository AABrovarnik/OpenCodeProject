// Плавное появление карточек при скролле
const cards = document.querySelectorAll('.card');

const observer = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
      entry.target.style.opacity = '1';
      entry.target.style.transform = 'translateY(0)';
    }
  });
}, { threshold: 0.1 });

cards.forEach((card) => {
  card.style.opacity = '0';
  card.style.transform = 'translateY(30px)';
  card.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
  observer.observe(card);
});

// Анимированные частицы на фоне
const container = document.getElementById('particles');
const count = 40;

for (let i = 0; i < count; i++) {
  const dot = document.createElement('div');
  dot.className = 'particle';
  dot.style.left = Math.random() * 100 + '%';
  dot.style.width = dot.style.height = (2 + Math.random() * 4) + 'px';
  dot.style.animationDuration = (12 + Math.random() * 20) + 's';
  dot.style.animationDelay = (Math.random() * 15) + 's';
  dot.style.opacity = 0.1 + Math.random() * 0.3;
  container.appendChild(dot);
}
