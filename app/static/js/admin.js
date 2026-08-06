document.addEventListener("DOMContentLoaded", () => {
  initializeImagePreview();

  initializeSlugGenerator();

  initializeSpecifications();
});

/* ==========================================================
   Image Preview
========================================================== */

function initializeImagePreview() {
  const imageInput = document.getElementById("primary_image");

  const previewImage = document.getElementById("preview-image");

  const placeholder = document.getElementById("preview-placeholder");

  if (!imageInput || !previewImage || !placeholder) return;

  imageInput.addEventListener("change", function () {
    const file = this.files[0];

    if (!file) return;

    previewImage.src = URL.createObjectURL(file);

    previewImage.classList.remove("d-none");

    placeholder.classList.add("d-none");
  });
}

/* ==========================================================
   Auto Slug
========================================================== */

function initializeSlugGenerator() {
  const productName = document.getElementById("product_name");

  const slug = document.getElementById("slug");

  if (!productName || !slug) return;

  productName.addEventListener("input", function () {
    slug.value = this.value
      .toLowerCase()
      .trim()
      .replace(/[^a-z0-9]+/g, "-")
      .replace(/^-+|-+$/g, "");
  });
}

/* ==========================================================
   Specifications
========================================================== */

function initializeSpecifications() {
  const libraryButton = document.getElementById("add-library-specification");

  const customButton = document.getElementById("add-custom-specification");

  const tbody = document.getElementById("specifications-body");

  const libraryTemplate = document.getElementById(
    "library-specification-template",
  );

  const customTemplate = document.getElementById(
    "custom-specification-template",
  );

  if (!tbody) return;

  function removeEmptyRow() {
    const empty = document.getElementById("empty-row");

    if (empty) empty.remove();
  }

  function restoreEmptyRow() {
    if (tbody.children.length === 0) {
      tbody.innerHTML = `

<tr id="empty-row">

<td colspan="3" class="text-center py-5 text-muted">

<i class="bi bi-list-ul fs-1 d-block mb-3"></i>

<h5>No Specifications Added</h5>

<p>

Click one of the buttons above to begin.

</p>

</td>

</tr>

`;
    }
  }

  if (libraryButton) {
    libraryButton.addEventListener("click", function () {
      removeEmptyRow();

      tbody.appendChild(libraryTemplate.content.cloneNode(true));
    });
  }

  if (customButton) {
    customButton.addEventListener("click", function () {
      removeEmptyRow();

      tbody.appendChild(customTemplate.content.cloneNode(true));
    });
  }

  tbody.addEventListener("click", function (event) {
    const removeButton = event.target.closest(".remove-specification");

    if (!removeButton) return;

    removeButton.closest("tr").remove();

    restoreEmptyRow();
  });
}
