/** Модальні вікна деталей каталогу (HTMX + vanilla JS) */

export function initModal() {
  const root = document.getElementById("detail-modal-root");
  if (!root) return;

  const closeModal = () => {
    root.innerHTML = "";
    document.body.classList.remove("modal-open");
  };

  document.body.addEventListener("click", (event) => {
    if (event.target.closest("[data-modal-close]")) {
      closeModal();
    }
  });

  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape" && root.querySelector(".detail-modal")) {
      closeModal();
    }
  });

  document.body.addEventListener("htmx:afterSwap", (event) => {
    if (event.detail.target !== root) return;
    const modal = root.querySelector(".detail-modal");
    if (!modal) return;

    document.body.classList.add("modal-open");
    modal.querySelector(".detail-modal__close")?.focus();
  });
}
