document.addEventListener("DOMContentLoaded", function () {
  // IMAGE PREVIEW

  const imageInput = document.getElementById("primary_image");
  const preview = document.getElementById("preview-image");
  const placeholder = document.getElementById("preview-placeholder");

  if (imageInput && preview && placeholder) {
    imageInput.addEventListener("change", function () {
      if (this.files.length) {
        preview.src = URL.createObjectURL(this.files[0]);

        preview.classList.remove("d-none");

        placeholder.classList.add("d-none");
      }
    });
  }

  // AUTO SLUG

  const productName = document.getElementById("product_name");
  const slug = document.getElementById("slug");

  if (productName && slug) {
    productName.addEventListener("input", function () {
      slug.value = this.value
        .toLowerCase()
        .trim()
        .replace(/[^a-z0-9]+/g, "-")
        .replace(/^-+|-+$/g, "");
    });
  }
});
