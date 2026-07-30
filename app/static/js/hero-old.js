let currentProduct = 0;

document.addEventListener("DOMContentLoaded", () => {

    renderHero(currentProduct);

    document
        .getElementById("hero-next")
        .addEventListener("click", nextProduct);

    document
        .getElementById("hero-prev")
        .addEventListener("click", previousProduct);

});

function renderHero(index) {

    const product = heroProducts[index];

    // Hero Content
    document.getElementById("hero-badge").innerHTML =
        product.badge;

    document.getElementById("hero-title").innerHTML =
        product.title;

    document.getElementById("hero-description").innerHTML =
        product.description;

    // Buttons
    document.getElementById("hero-primary-btn").textContent =
        product.primaryButton.text;

    document.getElementById("hero-primary-btn").href =
        product.primaryButton.link;

    document.getElementById("hero-secondary-btn").textContent =
        product.secondaryButton.text;

    document.getElementById("hero-secondary-btn").href =
        product.secondaryButton.link;

    // Product Image
    document.getElementById("hero-product-image").src =
        product.image;

    // Product Details
    document.getElementById("product-model").textContent =
        "Model: " + product.model;

    document.getElementById("product-title").textContent =
        product.name;

    // Features
    const featureContainer =
        document.getElementById("hero-features");

    featureContainer.innerHTML = "";

    product.features.forEach(feature => {

        const div = document.createElement("div");

        div.className = "feature";

        div.textContent = feature;

        featureContainer.appendChild(div);

    });

    // Specifications
    const specGrid =
        document.getElementById("product-spec-grid");

    specGrid.innerHTML = "";

    product.specs.forEach(spec => {

        const item = document.createElement("div");

        item.className = "spec-item";

        item.innerHTML = `
            <span>${spec.label}</span>
            <strong>${spec.value}</strong>
        `;

        specGrid.appendChild(item);

    });

}

function nextProduct() {

    currentProduct++;

    if (currentProduct >= heroProducts.length) {
        currentProduct = 0;
    }

    renderHero(currentProduct);

}

function previousProduct() {

    currentProduct--;

    if (currentProduct < 0) {
        currentProduct = heroProducts.length - 1;
    }

    renderHero(currentProduct);

}