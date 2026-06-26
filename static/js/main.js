import { initReveal }      from "./modules/animate.js";
import { initMobileNav }   from "./modules/mobile-nav.js";
import { initHeader }      from "./modules/header.js";
import { initModal }       from "./modules/modal.js";

document.addEventListener("DOMContentLoaded", () => {
  initReveal();
  initMobileNav();
  initHeader();
  initModal();
});
