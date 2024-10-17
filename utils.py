import os
from werkzeug.utils import secure_filename

def allowed_file(filename, allowed_extensions):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in allowed_extensions

def save_image(file, filename, category, upload_folder):
    category_path = os.path.join(upload_folder, category)
    if not os.path.exists(category_path):
        os.makedirs(category_path)
    file.save(os.path.join(category_path, filename))
