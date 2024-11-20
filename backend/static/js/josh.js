gsap.registerPlugin(ScrollTrigger);
let s1 = document.querySelectorAll('.s1');
s1.forEach(s1 =>{
  let image = s1.querySelectorAll('img');
  let tl = gsap.timeline({
    scrollTrigger: {
      trigger: s1,
      toggleActions: "play none none none"
    }
  });
  tl.set(s1, {autoAlpha: 1});
  tl.from(s1, 1.5, {
    xPercent: -100,
    ease: Power2.out
  });
  tl.from(image, 1.5, {
    xPercent: 100,
    scale: 1.3,
    delay: -1.5,
    ease: Power2.out
  });
} )