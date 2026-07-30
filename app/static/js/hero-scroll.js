gsap.registerPlugin(ScrollTrigger);

window.addEventListener("load", () => {

    const image = document.getElementById("hero-image-wrapper");
    const card = document.getElementById("product-card");

    gsap.to(image, {

        x: -180,

        ease: "none",

        scrollTrigger: {

            trigger: "#hero-section",

            start: "top top",

            end: "bottom top",

            scrub: true,

            markers: true

        }

    });

    gsap.to(card, {

        x: 180,

        ease: "none",

        scrollTrigger: {

            trigger: "#hero-section",

            start: "top top",

            end: "bottom top",

            scrub: true,

            markers: true

        }

    });

});