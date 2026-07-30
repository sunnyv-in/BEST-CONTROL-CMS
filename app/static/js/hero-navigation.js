let currentProduct = 0;

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