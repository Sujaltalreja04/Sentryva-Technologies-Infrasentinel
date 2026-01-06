"""
Analytics and Statistics
Handles confidence statistics and detection analytics
"""

import numpy as np


def calculate_confidence_stats(confidences):
    """
    Calculate statistical metrics for confidence scores
    
    Args:
        confidences (list): List of confidence scores
        
    Returns:
        dict: Statistical metrics
    """
    if not confidences:
        return {
            'mean': 0,
            'max': 0,
            'min': 0,
            'std': 0
        }
    
    return {
        'mean': np.mean(confidences),
        'max': np.max(confidences),
        'min': np.min(confidences),
        'std': np.std(confidences)
    }


def categorize_severity(confidence):
    """
    Categorize detection severity based on confidence
    
    Args:
        confidence (float): Confidence score
        
    Returns:
        str: Severity category (High, Medium, Low)
    """
    if confidence > 0.7:
        return 'High'
    elif confidence > 0.4:
        return 'Medium'
    else:
        return 'Low'


def get_severity_distribution(confidences):
    """
    Get distribution of severity levels
    
    Args:
        confidences (list): List of confidence scores
        
    Returns:
        dict: Count of each severity level
    """
    severities = [categorize_severity(c) for c in confidences]
    return {
        'High': severities.count('High'),
        'Medium': severities.count('Medium'),
        'Low': severities.count('Low')
    }


def calculate_detection_rate(total_scans, total_defects):
    """
    Calculate overall detection rate
    
    Args:
        total_scans (int): Total number of scans performed
        total_defects (int): Total defects found
        
    Returns:
        float: Detection rate as percentage
    """
    if total_scans == 0:
        return 0.0
    return (total_defects / total_scans) * 100


def get_historical_stats(detection_history):
    """
    Calculate statistics from detection history
    
    Args:
        detection_history (list): List of detection records
        
    Returns:
        dict: Historical statistics
    """
    if not detection_history:
        return {
            'total_detections': 0,
            'average_per_scan': 0,
            'scans_with_defects': 0,
            'total_scans': 0
        }
    
    detection_counts = [record['detections'] for record in detection_history]
    
    return {
        'total_detections': sum(detection_counts),
        'average_per_scan': sum(detection_counts) / len(detection_counts),
        'scans_with_defects': sum(1 for count in detection_counts if count > 0),
        'total_scans': len(detection_counts)
    }
