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

    const row = removeButton.closest("tr");

const deleteFlag = row.querySelector(".delete-document-flag");

if (deleteFlag) {

    deleteFlag.value = "1";

    row.style.display = "none";

} else {

    row.remove();

}

    restoreEmptyRow();
  });
}
// ======================================
// Product Documents
// ======================================

const addLibraryDocumentBtn = document.getElementById("add-library-document");

const addCustomDocumentBtn = document.getElementById("add-custom-document");

const documentsBody = document.getElementById("documents-body");

const libraryDocumentTemplate = document.getElementById(
  "library-document-template",
);

const customDocumentTemplate = document.getElementById(
  "custom-document-template",
);

// -------------------------
// Add Library Document
// -------------------------

if (addLibraryDocumentBtn && documentsBody && libraryDocumentTemplate) {
  addLibraryDocumentBtn.addEventListener("click", function () {
    const emptyRow = document.getElementById("empty-document-row");

    if (emptyRow) {
      emptyRow.remove();
    }

    const clone = libraryDocumentTemplate.content.cloneNode(true);

    documentsBody.appendChild(clone);
  });
}

// -------------------------
// Add Custom Document
// -------------------------

if (addCustomDocumentBtn && documentsBody && customDocumentTemplate) {
  addCustomDocumentBtn.addEventListener("click", function () {
    const emptyRow = document.getElementById("empty-document-row");

    if (emptyRow) {
      emptyRow.remove();
    }

    const clone = customDocumentTemplate.content.cloneNode(true);

    documentsBody.appendChild(clone);
  });
}

document.addEventListener("click", function (event) {

    const removeButton = event.target.closest(".remove-document");

    if (!removeButton) return;

    const row = removeButton.closest("tr");

    const deleteFlag = row.querySelector(".delete-document-flag");

    // Existing document
    if (deleteFlag) {

        deleteFlag.value = "1";

        row.style.display = "none";

    }

    // Newly added document
    else {

        row.remove();

    }

    if (
        [...documentsBody.querySelectorAll("tr")]
            .filter(r => r.style.display !== "none")
            .length === 0
    ) {

        documentsBody.innerHTML = `
        <tr id="empty-document-row">
            <td colspan="4" class="text-center py-5 text-muted">
                <i class="bi bi-file-earmark-pdf fs-1 d-block mb-3"></i>
                <h5>No Documents Added</h5>
                <p>Upload PDFs for this product.</p>
            </td>
        </tr>
        `;

    }

});
// ==========================================
// SEO Preview
// ==========================================

const productNameInput = document.getElementById("product_name");
const slugInput = document.getElementById("slug");

const metaTitleInput = document.getElementById("meta_title");
const metaDescriptionInput = document.getElementById("meta_description");
const keywordsInput = document.getElementById("keywords");

const previewTitle = document.getElementById("seo-preview-title");
const previewURL = document.getElementById("seo-preview-url");
const previewDescription = document.getElementById("seo-preview-description");

function updateSEOPreview() {
  if (!previewTitle) return;

  const productName = productNameInput?.value || "Product Title";

  const slug = slugInput?.value || "product-slug";

  const metaTitle = metaTitleInput?.value || productName + " | BEST CONTROL";

  const metaDescription =
    metaDescriptionInput?.value || "Your product description will appear here.";

  previewTitle.textContent = metaTitle;

  previewURL.textContent = "https://bestcontrol.in/products/" + slug;

  previewDescription.textContent = metaDescription;
}

[productNameInput, slugInput, metaTitleInput, metaDescriptionInput].forEach(
  (input) => {
    if (!input) return;

    input.addEventListener("input", updateSEOPreview);
  },
);

updateSEOPreview();

// ==========================================
// Auto Generate SEO
// ==========================================

const generateSEOButton = document.getElementById("generate-seo");

if (generateSEOButton) {
  generateSEOButton.addEventListener("click", function () {
    const productName = productNameInput?.value.trim() || "";

    const shortDescription =
      document
        .querySelector('textarea[name="short_description"]')
        ?.value.trim() || "";

    const modelNumber =
      document.querySelector('input[name="model_number"]')?.value.trim() || "";

    if (!metaTitleInput.value.trim()) {
      metaTitleInput.value = productName + " | BEST CONTROL";
    }

    if (!metaDescriptionInput.value.trim()) {
      metaDescriptionInput.value = `Buy ${productName} from BEST CONTROL. ${shortDescription}`;
    }

    if (!keywordsInput.value.trim()) {
      keywordsInput.value = [
        productName,
        "Transformer",
        modelNumber,
        "BEST CONTROL",
      ]
        .filter(Boolean)
        .join(", ");
    }

    updateSEOPreview();
  });
}
