export function initGalleryTabs() {
  const tabs = document.querySelectorAll("[data-gallery-tab]");
  if (!tabs.length) return;

  tabs.forEach((tab) => {
    tab.addEventListener("click", () => {
      const target = tab.dataset.galleryTab;

      tabs.forEach((t) => {
        t.classList.remove("is-active");
        t.setAttribute("aria-selected", "false");
      });

      tab.classList.add("is-active");
      tab.setAttribute("aria-selected", "true");

      const panels = document.querySelectorAll("[id^='gallery-']");
      panels.forEach((panel) => {
        panel.hidden = panel.id !== `gallery-${target}`;
      });
    });
  });
}
