import os
from uuid import uuid4

from flask import current_app
from werkzeug.utils import secure_filename


def save_uploaded_file(file, folder):

    filename = secure_filename(file.filename)

    extension = os.path.splitext(filename)[1]

    new_filename = f"{uuid4().hex}{extension}"

    upload_folder = os.path.join(
        current_app.root_path,
        "static",
        "uploads",
        folder,
    )

    os.makedirs(upload_folder, exist_ok=True)

    file.save(
        os.path.join(upload_folder, new_filename)
    )

    return new_filename