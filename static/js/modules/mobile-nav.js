export function initMobileNav() {
  const burger = document.getElementById("burger-btn");
  const nav = document.getElementById("mobile-nav");

  if (!burger || !nav) return;

  function openNav() {
    nav.classList.add("is-open");
    burger.classList.add("is-open");
    burger.setAttribute("aria-expanded", "true");
    document.body.style.overflow = "hidden";
  }

  function closeNav() {
    nav.classList.remove("is-open");
    burger.classList.remove("is-open");
    burger.setAttribute("aria-expanded", "false");
    document.body.style.overflow = "";
  }

  burger.addEventListener("click", () => {
    const isOpen = nav.classList.contains("is-open");
    isOpen ? closeNav() : openNav();
  });

  // Закрити при кліку на backdrop (поза панеллю)
  nav.addEventListener("click", (e) => {
    if (e.target === nav) closeNav();
  });

  // Закрити при кліку на посилання
  nav.querySelectorAll(".mobile-nav__link, .mobile-nav__cta").forEach((link) => {
    link.addEventListener("click", closeNav);
  });

  // Закрити при Escape
  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape" && nav.classList.contains("is-open")) closeNav();
  });
}
