console.log("BEST CONTROL CMS Loaded Successfully 🚀");

// ==========================
// NAVBAR
// ==========================

const navbar = document.querySelector(".navbar");
const navToggle = document.querySelector(".navbar-toggle");
const mobileMenu = document.querySelector(".mobile-menu");

// Mobile Menu Toggle

navToggle.addEventListener("click", () => {
  mobileMenu.classList.toggle("active");

  navToggle.classList.toggle("active");
});

// ==========================
// HIDE NAVBAR ON SCROLL
// ==========================

let lastScroll = 0;

window.addEventListener("scroll", () => {
  const currentScroll = window.scrollY;

  if (currentScroll > lastScroll && currentScroll > 100) {
    navbar.classList.add("navbar-hidden");
  } else {
    navbar.classList.remove("navbar-hidden");
  }

  lastScroll = currentScroll;
});
