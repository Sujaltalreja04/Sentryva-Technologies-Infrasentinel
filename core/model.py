"""
YOLO Model Loading and Management
Handles loading and caching of YOLO models for infrastructure detection
"""

import streamlit as st
from ultralytics import YOLO
import os


@st.cache_resource
def load_model(model_path="models/microsoft_infra.pt"):
    """
    Load YOLO model with caching for performance
    
    Args:
        model_path (str): Path to the YOLO model file
        
    Returns:
        YOLO: Loaded YOLO model instance
    """
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found: {model_path}")
    
    return YOLO(model_path)


def get_model_info(model):
    """
    Get information about the loaded model
    
    Args:
        model (YOLO): Loaded YOLO model
        
    Returns:
        dict: Model information including class names and count
    """
    return {
        'class_names': model.names,
        'num_classes': len(model.names),
        'model_type': 'YOLOv8'
    }
