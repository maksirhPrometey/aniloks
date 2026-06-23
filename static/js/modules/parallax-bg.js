/** Паралакс фону сайту (iOS Safari — transform, не background-attachment) */

export function initParallaxBg() {
  const layer = document.getElementById("site-parallax-layer");
  if (!layer) return;

  const reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  if (reduced) return;

  const factor = 0.38;
  let ticking = false;

  const update = () => {
    layer.style.transform = `translate3d(0, ${window.scrollY * factor}px, 0)`;
    ticking = false;
  };

  window.addEventListener(
    "scroll",
    () => {
      if (!ticking) {
        requestAnimationFrame(update);
        ticking = true;
      }
    },
    { passive: true }
  );

  update();
}
