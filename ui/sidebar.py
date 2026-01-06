"""
Sidebar Components
Handles sidebar UI elements and controls
"""

import streamlit as st


def render_sidebar(confidence_threshold_default=0.25):
    """
    Render the sidebar with controls and statistics
    
    Args:
        confidence_threshold_default (float): Default confidence threshold
        
    Returns:
        float: Selected confidence threshold
    """
    with st.sidebar:
        st.markdown("### ⚙️ System Controls")
        st.markdown("---")
        
        confidence_threshold = st.slider(
            "Detection Confidence",
            min_value=0.01,
            max_value=1.0,
            value=confidence_threshold_default,
            step=0.01,
            help="Adjust sensitivity of defect detection"
        )
        
        st.markdown("---")
        st.markdown("### 📊 System Status")
        st.success("🟢 ONLINE")
        
        st.markdown("---")
        st.markdown("### 📈 Statistics")
        st.metric("Total Scans", st.session_state.total_scans)
        st.metric("Defects Found", st.session_state.total_defects)
        
        if st.session_state.total_scans > 0:
            detection_rate = (st.session_state.total_defects / st.session_state.total_scans) * 100
            st.metric("Detection Rate", f"{detection_rate:.1f}%")
    
    return confidence_threshold


def initialize_session_state():
    """
    Initialize Streamlit session state variables
    """
    if 'detection_history' not in st.session_state:
        st.session_state.detection_history = []
    if 'total_scans' not in st.session_state:
        st.session_state.total_scans = 0
    if 'total_defects' not in st.session_state:
        st.session_state.total_defects = 0
