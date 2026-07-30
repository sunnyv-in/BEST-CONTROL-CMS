document.addEventListener("DOMContentLoaded", () => {

    renderHero(currentProduct);

    document
        .getElementById("hero-next")
        .addEventListener("click", nextProduct);

    document
        .getElementById("hero-prev")
        .addEventListener("click", previousProduct);

});