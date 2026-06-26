/** Lightbox для збільшення фото в модалці каталогу */

let lightboxRoot = null;

function ensureLightbox() {
  if (lightboxRoot) return lightboxRoot;

  const lb = document.createElement("div");
  lb.id = "lightbox";
  lb.className = "lightbox";
  lb.setAttribute("role", "dialog");
  lb.setAttribute("aria-modal", "true");
  lb.setAttribute("aria-label", "Перегляд зображення");
  lb.innerHTML = `
    <div class="lightbox__backdrop"></div>
    <button type="button" class="lightbox__close" aria-label="Закрити">
      <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true">
        <line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/>
      </svg>
    </button>
    <img class="lightbox__img" src="" alt="">
  `;
  document.body.appendChild(lb);

  const img = lb.querySelector(".lightbox__img");

  function close() {
    lb.classList.remove("is-open");
    if (!document.querySelector(".detail-modal")) {
      document.body.style.overflow = "";
    }
    img.src = "";
    img.alt = "";
  }

  lb.querySelector(".lightbox__backdrop").addEventListener("click", close);
  lb.querySelector(".lightbox__close").addEventListener("click", close);

  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape" && lb.classList.contains("is-open")) {
      event.stopPropagation();
      close();
    }
  });

  lightboxRoot = { lb, img, close };
  return lightboxRoot;
}

export function initLightbox(scope = document) {
  const { lb, img } = ensureLightbox();

  scope.querySelectorAll("[data-lightbox]").forEach((el) => {
    if (el.dataset.lightboxBound) return;
    el.dataset.lightboxBound = "1";
    el.addEventListener("click", (event) => {
      event.stopPropagation();
      img.src = el.dataset.lightbox;
      img.alt = el.dataset.lightboxAlt || "";
      lb.classList.add("is-open");
      document.body.style.overflow = "hidden";
      lb.querySelector(".lightbox__close").focus();
    });
  });
}
