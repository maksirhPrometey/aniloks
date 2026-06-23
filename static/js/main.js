import { initReveal }      from "./modules/animate.js";
import { initMobileNav }   from "./modules/mobile-nav.js";
import { initHeader }      from "./modules/header.js";
import { initLightbox }    from "./modules/lightbox.js";
import { initGalleryTabs } from "./modules/gallery-tabs.js";
import { initModal }       from "./modules/modal.js";

document.addEventListener("DOMContentLoaded", () => {
  initReveal();
  initMobileNav();
  initHeader();
  initLightbox();
  initGalleryTabs();
  initModal();
});
