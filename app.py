"""
InfraSentinel - AI-Powered Infrastructure Monitoring System
Main application entry point

This is a production-grade Streamlit application for infrastructure defect detection
using YOLOv8 deep learning models. The application features real-time detection,
analytics, and comprehensive reporting capabilities.

Author: InfraSentinel Team
Competition: Microsoft Imagine Cup / Azure Challenge
"""

import streamlit as st
from PIL import Image

# Core modules
from core.model import load_model
from core.detector import run_detection, extract_detection_data, create_detection_record
from core.analytics import calculate_confidence_stats, get_severity_distribution, get_historical_stats

# UI modules
from ui.styles import load_css
from ui.sidebar import render_sidebar, initialize_session_state
from ui.components import (
    render_header, render_upload_section, render_alert_box,
    render_detection_table, render_confidence_chart, render_severity_chart,
    render_type_distribution_chart, render_trend_chart,
    render_detection_history, render_footer
)

# Utility modules
from utils.file_utils import save_temp_file, cleanup_temp_file, load_image


# ============================================================================
# APPLICATION CONFIGURATION
# ============================================================================

st.set_page_config(
    page_title="InfraSentinel - Infrastructure Monitoring",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================================
# MAIN APPLICATION
# ============================================================================

def main():
    """Main application function"""
    
    # Load custom CSS
    st.markdown(load_css(), unsafe_allow_html=True)
    
    # Initialize session state
    initialize_session_state()
    
    # Render header
    render_header()
    
    # Render sidebar and get confidence threshold
    confidence_threshold = render_sidebar()
    
    # Render upload section
    uploaded_file = render_upload_section()
    
    # Load YOLO model
    try:
        model = load_model()
    except FileNotFoundError as e:
        st.error(f"❌ Error loading model: {e}")
        st.info("Please ensure the model file exists in the `models/` directory.")
        return
    
    # ========================================================================
    # DETECTION PROCESSING
    # ========================================================================
    
    if uploaded_file is not None:
        # Save uploaded file to temporary location
        image_path = save_temp_file(uploaded_file)
        
        # Display original and detection results
        st.markdown("---")
        st.markdown("### 🔍 Analysis Results")
        
        col_orig, col_detect = st.columns(2)
        
        with col_orig:
            st.markdown("#### Original Image")
            original_img = load_image(image_path)
            st.image(original_img, use_column_width=True)
        
        # Run detection
        with st.spinner('🔄 Analyzing infrastructure...'):
            results, result_img, num_detections = run_detection(
                model, 
                image_path, 
                confidence_threshold
            )
        
        with col_detect:
            st.markdown("#### Detection Result")
            st.image(result_img, use_column_width=True)
        
        # Update statistics
        st.session_state.total_scans += 1
        st.session_state.total_defects += num_detections
        
        # Create and store detection record
        detection_record = create_detection_record(num_detections, confidence_threshold)
        st.session_state.detection_history.insert(0, detection_record)
        if len(st.session_state.detection_history) > 10:
            st.session_state.detection_history.pop()
        
        # Render alert notification
        st.markdown("---")
        render_alert_box(num_detections, confidence_threshold)
        
        # ====================================================================
        # DETECTION DETAILS & ANALYTICS
        # ====================================================================
        
        if num_detections > 0:
            # Extract detection data
            detection_data = extract_detection_data(results, model)
            
            # Render detection table
            render_detection_table(detection_data)
            
            # Prepare analytics data
            confidences = [d['Confidence_Raw'] for d in detection_data]
            class_names = [d['Type'] for d in detection_data]
            
            # Interactive Analytics
            st.markdown("---")
            st.markdown("### 📊 Detection Analytics")
            
            graph_col1, graph_col2 = st.columns(2)
            
            with graph_col1:
                # Confidence distribution chart
                fig_conf = render_confidence_chart(confidences)
                st.plotly_chart(fig_conf, use_container_width=True)
            
            with graph_col2:
                # Severity distribution chart
                severity_counts = get_severity_distribution(confidences)
                fig_severity = render_severity_chart(severity_counts)
                st.plotly_chart(fig_severity, use_container_width=True)
            
            # Defect type distribution (if multiple types)
            if len(set(class_names)) > 1:
                st.markdown("#### 🏷️ Defect Type Distribution")
                type_counts = {}
                for name in class_names:
                    type_counts[name] = type_counts.get(name, 0) + 1
                
                fig_types = render_type_distribution_chart(type_counts)
                st.plotly_chart(fig_types, use_container_width=True)
            
            # Confidence statistics
            st.markdown("#### 📈 Confidence Statistics")
            stats = calculate_confidence_stats(confidences)
            
            stat_col1, stat_col2, stat_col3, stat_col4 = st.columns(4)
            with stat_col1:
                st.metric("Average Confidence", f"{stats['mean']:.1%}")
            with stat_col2:
                st.metric("Highest Confidence", f"{stats['max']:.1%}")
            with stat_col3:
                st.metric("Lowest Confidence", f"{stats['min']:.1%}")
            with stat_col4:
                st.metric("Std Deviation", f"{stats['std']:.1%}")
        
        # Cleanup temporary file
        cleanup_temp_file(image_path)
    
    # ========================================================================
    # DETECTION HISTORY & TRENDS
    # ========================================================================
    
    if st.session_state.detection_history:
        st.markdown("---")
        render_detection_history(st.session_state.detection_history)
        
        # Trend analysis (if enough data)
        if len(st.session_state.detection_history) >= 2:
            st.markdown("---")
            st.markdown("### 📈 Detection Trend Analysis")
            
            fig_trend = render_trend_chart(st.session_state.detection_history)
            st.plotly_chart(fig_trend, use_container_width=True)
            
            # Historical statistics
            hist_stats = get_historical_stats(st.session_state.detection_history)
            
            hist_col1, hist_col2, hist_col3 = st.columns(3)
            with hist_col1:
                st.metric("Total Historical Detections", hist_stats['total_detections'])
            with hist_col2:
                st.metric("Average per Scan", f"{hist_stats['average_per_scan']:.1f}")
            with hist_col3:
                st.metric("Scans with Defects", 
                         f"{hist_stats['scans_with_defects']}/{hist_stats['total_scans']}")
    
    # Render footer
    render_footer()


# ============================================================================
# APPLICATION ENTRY POINT
# ============================================================================

if __name__ == "__main__":
    main()
