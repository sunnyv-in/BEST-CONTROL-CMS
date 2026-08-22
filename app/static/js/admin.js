document.addEventListener("DOMContentLoaded", function () {
  initializeImagePreview();
  initializeIndustryImagePreview();
  initializeIndustrySEOPreview();
  initializeSlugGenerator();
  initializeSpecifications();
  initializeProductGallery();
  initializeProductImages();
  initializeDocuments();
  initializeSEOPreview();
});


/* ==========================================================
   Primary Image Preview
========================================================== */

function initializeImagePreview() {
  const imageInput = document.getElementById("primary_image");
  const previewImage = document.getElementById("preview-image");
  const placeholder = document.getElementById("preview-placeholder");

  if (!imageInput || !previewImage) {
    return;
  }

  imageInput.addEventListener("change", function () {
    const file = this.files && this.files[0];

    if (!file) {
      return;
    }

    if (!file.type.startsWith("image/")) {
      this.value = "";
      return;
    }

    /*
     * Release previous preview URL.
     */
    if (previewImage.dataset.objectUrl) {
      URL.revokeObjectURL(previewImage.dataset.objectUrl);
    }

    const objectUrl = URL.createObjectURL(file);

    previewImage.src = objectUrl;
    previewImage.dataset.objectUrl = objectUrl;

    previewImage.classList.remove("d-none");

    if (placeholder) {
      placeholder.classList.add("d-none");
    }
  });
}

/* ==========================================================
   Industry Image Preview
========================================================== */

function initializeIndustryImagePreview() {

  const imageInput = document.getElementById("industry_image");

  const previewContainer = document.getElementById(
    "industry-image-preview-container"
  );

  const previewImage = document.getElementById(
    "industry-image-preview"
  );

  const currentImage = document.getElementById(
    "current-industry-image"
  );


  /*
   * This page does not contain
   * the industry image fields.
   */
  if (!imageInput || !previewContainer || !previewImage) {
    return;
  }


  imageInput.addEventListener("change", function () {

    const file = this.files && this.files[0];


    /*
     * No file selected.
     */
    if (!file) {

      previewContainer.classList.add("d-none");

      if (currentImage) {
        currentImage.style.display = "";
      }

      return;
    }


    /*
     * Make sure the selected file
     * is actually an image.
     */
    if (!file.type.startsWith("image/")) {

      this.value = "";

      previewContainer.classList.add("d-none");

      if (currentImage) {
        currentImage.style.display = "";
      }

      return;
    }


    /*
     * Hide current saved image.
     */
    if (currentImage) {
      currentImage.style.display = "none";
    }


    /*
     * Release previous temporary
     * browser preview URL.
     */
    if (previewImage.dataset.objectUrl) {

      URL.revokeObjectURL(
        previewImage.dataset.objectUrl
      );

    }


    /*
     * Create temporary browser URL.
     */
    const objectUrl = URL.createObjectURL(file);


    /*
     * Show selected image.
     */
    previewImage.src = objectUrl;

    previewImage.dataset.objectUrl = objectUrl;


    /*
     * Show new image preview.
     */
    previewContainer.classList.remove("d-none");

  });

}

/* ==========================================================
   Industry SEO Preview
========================================================== */

function initializeIndustrySEOPreview() {

  const nameInput = document.getElementById("name");

  const slugInput = document.getElementById("slug");

  const metaTitleInput = document.getElementById("meta_title");

  const metaDescriptionInput = document.getElementById(
    "meta_description"
  );


  const previewTitle = document.getElementById(
    "industry-seo-preview-title"
  );

  const previewURL = document.getElementById(
    "industry-seo-preview-url"
  );

  const previewDescription = document.getElementById(
    "industry-seo-preview-description"
  );


  const generateButton = document.getElementById(
    "generate-industry-seo"
  );


  /*
   * This page does not contain
   * the Industry SEO elements.
   */
  if (
    !nameInput ||
    !metaTitleInput ||
    !metaDescriptionInput ||
    !previewTitle
  ) {
    return;
  }


  function generateSlug(name) {

    return name
      .toLowerCase()
      .trim()
      .replace(/[^a-z0-9]+/g, "-")
      .replace(/^-+|-+$/g, "");

  }


  function updatePreview() {

    const name =
      nameInput.value.trim() ||
      "Industry Title";


    const slug =
      slugInput?.value.trim() ||
      generateSlug(name) ||
      "industry-slug";


    const metaTitle =
      metaTitleInput.value.trim() ||
      `${name} | BEST CONTROL`;


    const metaDescription =
      metaDescriptionInput.value.trim() ||
      `BEST CONTROL transformer solutions for ${name}. Reliable step-down transformers designed for industrial applications.`;


    previewTitle.textContent = metaTitle;


    if (previewURL) {

      previewURL.textContent =
        `https://bestcontrol.in/industries/${slug}`;

    }


    if (previewDescription) {

      previewDescription.textContent =
        metaDescription;

    }

  }


  /*
   * Update preview while typing.
   */
  nameInput.addEventListener(
    "input",
    updatePreview
  );


  metaTitleInput.addEventListener(
    "input",
    updatePreview
  );


  metaDescriptionInput.addEventListener(
    "input",
    updatePreview
  );


  if (slugInput) {

    slugInput.addEventListener(
      "input",
      updatePreview
    );

  }


  /*
   * Generate SEO button.
   */
  if (generateButton) {

    generateButton.addEventListener(
      "click",
      function () {

        const name =
          nameInput.value.trim();


        if (!name) {

          alert(
            "Please enter the industry name first."
          );

          nameInput.focus();

          return;

        }


        const descriptionInput =
          document.querySelector(
            'textarea[name="description"]'
          );


        const description =
          descriptionInput?.value.trim() || "";


        /*
         * Generate Meta Title
         */
        metaTitleInput.value =
          `${name} | BEST CONTROL`;


        /*
         * Generate Meta Description
         */
        if (description) {

          metaDescriptionInput.value =
            `BEST CONTROL provides reliable transformer solutions for ${name}. ${description}`;

        } else {

          metaDescriptionInput.value =
            `BEST CONTROL provides reliable step-down transformer solutions for ${name}, designed for industrial applications and control systems.`;

        }


        updatePreview();

      }
    );

  }


  /*
   * Initial preview.
   */
  updatePreview();

}



/* ==========================================================
   Product Gallery - Older Gallery Rows
========================================================== */

function initializeProductGallery() {
  const addGalleryButton = document.getElementById("add-gallery-image");

  const galleryBody = document.getElementById("gallery-body");

  const galleryTemplate = document.getElementById("gallery-template");

  if (addGalleryButton && galleryBody && galleryTemplate) {
    addGalleryButton.addEventListener("click", function () {
      const empty = document.getElementById("empty-gallery-row");

      if (empty) {
        empty.remove();
      }

      galleryBody.appendChild(galleryTemplate.content.cloneNode(true));
    });
  }

  /*
   * Gallery image preview.
   */
  document.addEventListener("change", function (event) {
    const input = event.target;

    if (!input.classList.contains("gallery-input")) {
      return;
    }

    const file = input.files && input.files[0];

    if (!file) {
      return;
    }

    if (!file.type.startsWith("image/")) {
      input.value = "";
      return;
    }

    const row = input.closest("tr");

    if (!row) {
      return;
    }

    const preview = row.querySelector(".gallery-preview");

    if (!preview) {
      return;
    }

    /*
     * Release old preview URL.
     */
    if (preview.dataset.objectUrl) {
      URL.revokeObjectURL(preview.dataset.objectUrl);
    }

    const objectUrl = URL.createObjectURL(file);

    preview.src = objectUrl;

    preview.dataset.objectUrl = objectUrl;

    preview.classList.remove("d-none");

    /*
     * Hide any placeholder in this gallery row.
     */
    const placeholder = row.querySelector(
      ".gallery-preview-placeholder, " +
        ".preview-placeholder, " +
        ".image-preview-placeholder",
    );

    if (placeholder) {
      placeholder.classList.add("d-none");
    }
  });

  /*
   * Remove gallery row.
   */
  document.addEventListener("click", function (event) {
    const removeButton = event.target.closest(".remove-gallery");

    if (!removeButton) {
      return;
    }

    const row = removeButton.closest("tr");

    if (!row) {
      return;
    }

    row.remove();

    if (galleryBody && galleryBody.children.length === 0) {
      galleryBody.innerHTML = `
        <tr id="empty-gallery-row">
          <td colspan="4" class="text-center py-5 text-muted">
            <i class="bi bi-images fs-1 d-block mb-3"></i>
            <h5>No Gallery Images</h5>
            <p>Click Add Image to upload gallery photos.</p>
          </td>
        </tr>
      `;
    }
  });
}

/* ==========================================================
   Auto Slug
========================================================== */

function initializeSlugGenerator() {
  const productName = document.getElementById("product_name");

  const slug = document.getElementById("slug");

  if (!productName || !slug) {
    return;
  }

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

  if (!tbody) {
    return;
  }

  function removeEmptyRow() {
    const empty = document.getElementById("empty-row");

    if (empty) {
      empty.remove();
    }
  }

  function restoreEmptyRow() {
    if (tbody.children.length === 0) {
      tbody.innerHTML = `
        <tr id="empty-row">
          <td colspan="3" class="text-center py-5 text-muted">
            <i class="bi bi-list-ul fs-1 d-block mb-3"></i>
            <h5>No Specifications Added</h5>
            <p>Click one of the buttons above to begin.</p>
          </td>
        </tr>
      `;
    }
  }

  if (libraryButton && libraryTemplate) {
    libraryButton.addEventListener("click", function () {
      removeEmptyRow();

      tbody.appendChild(libraryTemplate.content.cloneNode(true));
    });
  }

  if (customButton && customTemplate) {
    customButton.addEventListener("click", function () {
      removeEmptyRow();

      tbody.appendChild(customTemplate.content.cloneNode(true));
    });
  }

  tbody.addEventListener("click", function (event) {
    const removeButton = event.target.closest(".remove-specification");

    if (!removeButton) {
      return;
    }

    const row = removeButton.closest("tr");

    if (!row) {
      return;
    }

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

/* ==========================================================
   Product Documents
========================================================== */

function initializeDocuments() {
  const addLibraryDocumentBtn = document.getElementById("add-library-document");

  const addCustomDocumentBtn = document.getElementById("add-custom-document");

  const documentsBody = document.getElementById("documents-body");

  const libraryDocumentTemplate = document.getElementById(
    "library-document-template",
  );

  const customDocumentTemplate = document.getElementById(
    "custom-document-template",
  );

  if (addLibraryDocumentBtn && documentsBody && libraryDocumentTemplate) {
    addLibraryDocumentBtn.addEventListener("click", function () {
      const emptyRow = document.getElementById("empty-document-row");

      if (emptyRow) {
        emptyRow.remove();
      }

      documentsBody.appendChild(
        libraryDocumentTemplate.content.cloneNode(true),
      );
    });
  }

  if (addCustomDocumentBtn && documentsBody && customDocumentTemplate) {
    addCustomDocumentBtn.addEventListener("click", function () {
      const emptyRow = document.getElementById("empty-document-row");

      if (emptyRow) {
        emptyRow.remove();
      }

      documentsBody.appendChild(customDocumentTemplate.content.cloneNode(true));
    });
  }

  document.addEventListener("click", function (event) {
    const removeButton = event.target.closest(".remove-document");

    if (!removeButton) {
      return;
    }

    const row = removeButton.closest("tr");

    if (!row) {
      return;
    }

    const deleteFlag = row.querySelector(".delete-document-flag");

    if (deleteFlag) {
      deleteFlag.value = "1";
      row.style.display = "none";
    } else {
      row.remove();
    }

    if (!documentsBody) {
      return;
    }

    const visibleRows = [...documentsBody.querySelectorAll("tr")].filter(
      (r) => r.style.display !== "none",
    );

    if (visibleRows.length === 0) {
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
}

/* ==========================================================
   SEO Preview
========================================================== */

function initializeSEOPreview() {
  const productNameInput = document.getElementById("product_name");

  const slugInput = document.getElementById("slug");

  const metaTitleInput = document.getElementById("meta_title");

  const metaDescriptionInput = document.getElementById("meta_description");

  const keywordsInput = document.getElementById("keywords");

  const previewTitle = document.getElementById("seo-preview-title");

  const previewURL = document.getElementById("seo-preview-url");

  const previewDescription = document.getElementById("seo-preview-description");

  function updateSEOPreview() {
    if (!previewTitle) {
      return;
    }

    const productName = productNameInput?.value || "Product Title";

    const slug = slugInput?.value || "product-slug";

    const metaTitle = metaTitleInput?.value || productName + " | BEST CONTROL";

    const metaDescription =
      metaDescriptionInput?.value ||
      "Your product description will appear here.";

    previewTitle.textContent = metaTitle;

    if (previewURL) {
      previewURL.textContent = "https://bestcontrol.in/products/" + slug;
    }

    if (previewDescription) {
      previewDescription.textContent = metaDescription;
    }
  }

  [productNameInput, slugInput, metaTitleInput, metaDescriptionInput].forEach(
    function (input) {
      if (!input) {
        return;
      }

      input.addEventListener("input", updateSEOPreview);
    },
  );

  updateSEOPreview();

  /*
   * Auto Generate SEO
   */
  const generateSEOButton = document.getElementById("generate-seo");

  if (generateSEOButton) {
    generateSEOButton.addEventListener("click", function () {
      const productName = productNameInput?.value.trim() || "";

      const shortDescription =
        document
          .querySelector('textarea[name="short_description"]')
          ?.value.trim() || "";

      const modelNumber =
        document.querySelector('input[name="model_number"]')?.value.trim() ||
        "";

      if (metaTitleInput && !metaTitleInput.value.trim()) {
        metaTitleInput.value = productName + " | BEST CONTROL";
      }

      if (metaDescriptionInput && !metaDescriptionInput.value.trim()) {
        metaDescriptionInput.value = `Buy ${productName} from BEST CONTROL. ${shortDescription}`;
      }

      if (keywordsInput && !keywordsInput.value.trim()) {
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
}

/* ==========================================================
   Product Images
========================================================== */

function initializeProductImages() {
  const addButton = document.getElementById("add-product-image");

  const container = document.getElementById("product-images-container");

  const template = document.getElementById("product-image-template");

  const emptyState = document.getElementById("empty-product-images");

  /*
   * Product image section does not exist
   * on this page.
   */
  if (!addButton || !container || !template) {
    return;
  }

  /* --------------------------------------------------------
     Empty State
  -------------------------------------------------------- */

  function updateEmptyState() {
    if (!emptyState) {
      return;
    }

    const visibleImages = container.querySelectorAll(
      ".product-image-item:not([style*='display: none'])",
    );

    emptyState.classList.toggle("d-none", visibleImages.length > 0);
  }

  /* --------------------------------------------------------
     Hide Preview Placeholder
  -------------------------------------------------------- */

  function hidePreviewPlaceholder(item) {
    if (!item) {
      return;
    }

    /*
     * These cover the possible placeholder
     * class names used by the product image card.
     */
    const placeholders =
  item.querySelectorAll(
    ".new-image-placeholder, " +
    ".image-preview-placeholder, " +
    ".preview-placeholder, " +
    ".product-image-placeholder, " +
    ".product-image-preview-placeholder, " +
    "[data-image-placeholder]"
  );

    placeholders.forEach(function (placeholder) {
      placeholder.classList.add("d-none");
      placeholder.style.display = "none";
    });
  }

  /* --------------------------------------------------------
     Show Preview Placeholder
  -------------------------------------------------------- */

  function showPreviewPlaceholder(item) {
    if (!item) {
      return;
    }

    const placeholders =
  item.querySelectorAll(
    ".new-image-placeholder, " +
    ".image-preview-placeholder, " +
    ".preview-placeholder, " +
    ".product-image-placeholder, " +
    ".product-image-preview-placeholder, " +
    "[data-image-placeholder]"
  );

    placeholders.forEach(function (placeholder) {
      placeholder.classList.remove("d-none");
      placeholder.style.display = "";
    });
  }

  /* --------------------------------------------------------
     Release Image URL
  -------------------------------------------------------- */

  function releasePreviewURL(preview) {
    if (preview && preview.dataset.objectUrl) {
      URL.revokeObjectURL(preview.dataset.objectUrl);

      delete preview.dataset.objectUrl;
    }
  }

  /* --------------------------------------------------------
     Update Product Image Preview
  -------------------------------------------------------- */

  function updateProductImagePreview(input) {
    if (!input) {
      return;
    }

    const item = input.closest(".product-image-item");

    if (!item) {
      return;
    }

    const file = input.files && input.files[0];

    /*
     * No file selected.
     */
    if (!file) {
      return;
    }

    /*
     * Only accept image files.
     */
    if (!file.type.startsWith("image/")) {
      input.value = "";

      return;
    }

    /*
     * Find the image element.
     */
    let preview = item.querySelector(".product-image-preview");

    /*
     * Find the preview area.
     */
    let previewArea = item.querySelector(
      ".product-image-preview-container, " +
        ".image-preview, " +
        ".preview-container, " +
        ".product-image-preview-area",
    );

    /*
     * If there is no image element but there
     * is a preview area, create the image.
     */
    if (!preview && previewArea) {
      preview = document.createElement("img");

      preview.className = "product-image-preview";

      preview.alt = "Product image preview";

      preview.draggable = false;

      previewArea.appendChild(preview);
    }

    /*
     * If we still cannot find the preview,
     * stop safely.
     */
    if (!preview) {
      return;
    }

    /*
     * Release previous temporary URL.
     */
    releasePreviewURL(preview);

    /*
     * Create new temporary URL.
     */
    const objectUrl = URL.createObjectURL(file);

    preview.src = objectUrl;

    preview.dataset.objectUrl = objectUrl;

    /*
     * Make image visible.
     */
    preview.classList.remove("d-none");

    preview.style.display = "";

    /*
     * IMPORTANT:
     * Hide the old "Image Preview"
     * placeholder.
     */
    hidePreviewPlaceholder(item);

    /*
     * Prevent dragging/copy-dragging
     * the preview image.
     */
    preview.addEventListener("dragstart", function (event) {
      event.preventDefault();
    });
  }

  /* --------------------------------------------------------
     Add Product Image
  -------------------------------------------------------- */

  addButton.addEventListener("click", function () {
    if (emptyState) {
      emptyState.classList.add("d-none");
    }

    const clone = template.content.cloneNode(true);

    container.appendChild(clone);

    const items = container.querySelectorAll(".product-image-item");

    const newItem = items[items.length - 1];

    if (!newItem) {
      return;
    }

    /*
     * Hide placeholder only when
     * an image actually exists.
     */
    const input = newItem.querySelector(".product-image-input");

    if (input) {
      input.addEventListener("change", function () {
        updateProductImagePreview(this);
      });
    }
  });

  /* --------------------------------------------------------
     Handle Existing / Dynamically Added Inputs
  -------------------------------------------------------- */

  container.addEventListener("change", function (event) {
    if (!event.target.classList.contains("product-image-input")) {
      return;
    }

    updateProductImagePreview(event.target);
  });

  /* --------------------------------------------------------
     Remove Product Image
  -------------------------------------------------------- */

  container.addEventListener("click", function (event) {
    const removeButton = event.target.closest(".remove-product-image");

    if (!removeButton) {
      return;
    }

    const item = removeButton.closest(".product-image-item");

    if (!item) {
      return;
    }

    /*
     * Existing image:
     * mark it for deletion.
     */
    const deleteFlag = item.querySelector(".delete-product-image-flag");

    if (deleteFlag) {
      deleteFlag.value = "1";

      /*
       * Release preview URL if present.
       */
      const preview = item.querySelector(".product-image-preview");

      releasePreviewURL(preview);

      item.style.display = "none";
    } else {

    /*
     * Newly added image:
     * completely remove it.
     */
      const preview = item.querySelector(".product-image-preview");

      releasePreviewURL(preview);

      item.remove();
    }

    updateEmptyState();
  });

  /* --------------------------------------------------------
     Set Primary Image
  -------------------------------------------------------- */

  container.addEventListener("click", function (event) {
    const primaryButton = event.target.closest(
      ".set-primary-image, " + ".set-primary",
    );

    if (!primaryButton) {
      return;
    }

    const item = primaryButton.closest(".product-image-item");

    if (!item) {
      return;
    }

    /*
     * Remove primary state from all
     * visible product image cards.
     */
    container
      .querySelectorAll(".product-image-item")
      .forEach(function (otherItem) {
        if (otherItem === item || otherItem.style.display === "none") {
          return;
        }

        otherItem.classList.remove("is-primary");

        const otherButtons = otherItem.querySelectorAll(
          ".set-primary-image, " + ".set-primary",
        );

        otherButtons.forEach(function (button) {
          button.classList.remove("active");
        });
      });

    /*
     * Add primary state.
     */
    item.classList.add("is-primary");

    primaryButton.classList.add("active");

    /*
     * If there is a radio/hidden input
     * for primary state, update it.
     */
    const primaryInput = item.querySelector(
      'input[name*="primary"], ' + 'input[name*="is_primary"]',
    );

    if (primaryInput) {
      primaryInput.checked = true;
      primaryInput.value = "1";
    }
  });

  /* --------------------------------------------------------
     Initial State
  -------------------------------------------------------- */

  updateEmptyState();
}
