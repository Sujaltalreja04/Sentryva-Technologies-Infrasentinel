"""
Detection Logic
Handles YOLO prediction and result processing
"""

import cv2
import numpy as np
from datetime import datetime


def run_detection(model, image_path, confidence_threshold=0.25, iou_threshold=0.45, img_size=1024):
    """
    Run YOLO detection on an image
    
    Args:
        model: YOLO model instance
        image_path (str): Path to the image file
        confidence_threshold (float): Minimum confidence for detections
        iou_threshold (float): IOU threshold for NMS
        img_size (int): Image size for inference
        
    Returns:
        tuple: (results, processed_image, detection_count)
    """
    results = model.predict(
        source=image_path,
        conf=confidence_threshold,
        iou=iou_threshold,
        imgsz=img_size,
        save=False
    )
    
    # Process results
    result_img = results[0].plot()
    result_img = cv2.cvtColor(result_img, cv2.COLOR_BGR2RGB)
    
    # Get detection count
    boxes = results[0].boxes
    num_detections = len(boxes)
    
    return results, result_img, num_detections


def extract_detection_data(results, model):
    """
    Extract detailed detection data from YOLO results
    
    Args:
        results: YOLO prediction results
        model: YOLO model instance
        
    Returns:
        list: List of detection dictionaries with details
    """
    boxes = results[0].boxes
    detection_data = []
    
    for idx, box in enumerate(boxes):
        conf = float(box.conf[0])
        cls = int(box.cls[0])
        class_name = model.names[cls]
        
        detection_data.append({
            'ID': idx + 1,
            'Type': class_name,
            'Confidence': f"{conf:.2%}",
            'Confidence_Raw': conf,
            'Severity': '🔴 High' if conf > 0.7 else '🟡 Medium' if conf > 0.4 else '🟢 Low'
        })
    
    return detection_data


def create_detection_record(num_detections, confidence_threshold):
    """
    Create a detection record for history tracking
    
    Args:
        num_detections (int): Number of detections found
        confidence_threshold (float): Confidence threshold used
        
    Returns:
        dict: Detection record with timestamp and metadata
    """
    return {
        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'detections': num_detections,
        'confidence': confidence_threshold,
        'status': 'Critical' if num_detections > 0 else 'Safe'
    }
