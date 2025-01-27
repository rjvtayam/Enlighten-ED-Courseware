import os
from werkzeug.utils import secure_filename
from PIL import Image
from datetime import datetime

def save_file(file, directory):
    filename = secure_filename(file.filename)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    unique_filename = f"{timestamp}_{filename}"
    file_path = os.path.join(directory, unique_filename)
    file.save(file_path)
    return unique_filename

def process_image(image_path, size=(200, 200)):
    with Image.open(image_path) as img:
        img.thumbnail(size)
        img.save(image_path)

def format_datetime(dt):
    return dt.strftime('%B %d, %Y %I:%M %p')

def calculate_progress(completed, total):
    return int((completed / total * 100) if total > 0 else 0)
