export function initHeader() {
  const header = document.getElementById("site-header");
  if (!header) return;

  const SCROLL_THRESHOLD = 40;

  function update() {
    if (window.scrollY > SCROLL_THRESHOLD) {
      header.classList.add("is-scrolled");
    } else {
      header.classList.remove("is-scrolled");
    }
  }

  window.addEventListener("scroll", update, { passive: true });
  update();
}
