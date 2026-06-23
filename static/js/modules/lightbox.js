export function initLightbox() {
  const items = document.querySelectorAll("[data-lightbox]");
  if (!items.length) return;

  // Створюємо lightbox елемент
  const lb = document.createElement("div");
  lb.id = "lightbox";
  lb.setAttribute("role", "dialog");
  lb.setAttribute("aria-modal", "true");
  lb.setAttribute("aria-label", "Перегляд зображення");
  lb.innerHTML = `
    <div class="lightbox__backdrop"></div>
    <button class="lightbox__close" aria-label="Закрити">
      <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true">
        <line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/>
      </svg>
    </button>
    <img class="lightbox__img" src="" alt="">
  `;
  document.body.appendChild(lb);

  // Стилі через CSS клас — не inline
  lb.classList.add("lightbox");

  const img = lb.querySelector(".lightbox__img");

  function open(src, alt) {
    img.src = src;
    img.alt = alt || "";
    lb.classList.add("is-open");
    document.body.style.overflow = "hidden";
    lb.querySelector(".lightbox__close").focus();
  }

  function close() {
    lb.classList.remove("is-open");
    document.body.style.overflow = "";
    img.src = "";
  }

  items.forEach((el) => {
    el.addEventListener("click", () => open(el.dataset.lightbox, el.dataset.lightboxAlt));
    el.style.cursor = "pointer";
  });

  lb.querySelector(".lightbox__backdrop").addEventListener("click", close);
  lb.querySelector(".lightbox__close").addEventListener("click", close);

  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape" && lb.classList.contains("is-open")) close();
  });
}
