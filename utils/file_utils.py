"""
File Utilities
Helper functions for file handling and temporary file management
"""

import tempfile
import os
from PIL import Image


def save_temp_file(uploaded_file, suffix=".jpg"):
    """
    Save uploaded file to temporary location
    
    Args:
        uploaded_file: Streamlit UploadedFile object
        suffix (str): File extension suffix
        
    Returns:
        str: Path to temporary file
    """
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        tmp.write(uploaded_file.read())
        return tmp.name


def cleanup_temp_file(file_path):
    """
    Remove temporary file
    
    Args:
        file_path (str): Path to file to remove
    """
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
    except Exception as e:
        print(f"Error removing temporary file: {e}")


def load_image(image_path):
    """
    Load image from file path
    
    Args:
        image_path (str): Path to image file
        
    Returns:
        PIL.Image: Loaded image
    """
    return Image.open(image_path)


def validate_image_file(uploaded_file):
    """
    Validate uploaded image file
    
    Args:
        uploaded_file: Streamlit UploadedFile object
        
    Returns:
        tuple: (is_valid, error_message)
    """
    if uploaded_file is None:
        return False, "No file uploaded"
    
    # Check file extension
    valid_extensions = ['jpg', 'jpeg', 'png']
    file_extension = uploaded_file.name.split('.')[-1].lower()
    
    if file_extension not in valid_extensions:
        return False, f"Invalid file type. Supported: {', '.join(valid_extensions)}"
    
    # Check file size (max 10MB)
    max_size_mb = 10
    file_size_mb = uploaded_file.size / (1024 * 1024)
    
    if file_size_mb > max_size_mb:
        return False, f"File too large. Maximum size: {max_size_mb}MB"
    
    return True, ""
