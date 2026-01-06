"""
UI Components
Reusable UI components for the Streamlit app
"""

import streamlit as st
from datetime import datetime
import plotly.graph_objects as go
import numpy as np


def render_header():
    """Render the main application header"""
    st.markdown("""
    <div class="main-header">
        <h1 class="main-title">🛡️ INFRASENTINEL</h1>
        <p class="subtitle">AI-Powered Infrastructure Monitoring & Defect Detection System</p>
    </div>
    """, unsafe_allow_html=True)


def render_upload_section():
    """
    Render the file upload section
    
    Returns:
        UploadedFile: Uploaded file object or None
    """
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 📤 Upload Infrastructure Image")
        uploaded_file = st.file_uploader(
            "Choose an image file",
            type=["jpg", "jpeg", "png"],
            help="Upload an image of infrastructure for defect detection"
        )
    
    with col2:
        st.markdown("### ℹ️ Quick Info")
        st.info("""
        **Supported Formats:**
        - JPG, JPEG, PNG
        
        **Detection Types:**
        - Cracks
        - Structural damage
        - Surface defects
        - Anomalies
        """)
    
    return uploaded_file


def render_alert_box(num_detections, confidence_threshold):
    """
    Render alert box based on detection results
    
    Args:
        num_detections (int): Number of detections found
        confidence_threshold (float): Confidence threshold used
    """
    if num_detections > 0:
        st.markdown(f"""
        <div class="alert-box">
            <div class="alert-title">⚠️ ALERT: Defects Detected!</div>
            <p style="color: #fecaca; font-size: 1.1rem; margin: 10px 0;">
                <strong>{num_detections}</strong> potential infrastructure defect(s) identified
            </p>
            <p style="color: #fca5a5; margin: 5px 0;">
                📍 Timestamp: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
            </p>
            <p style="color: #fca5a5; margin: 5px 0;">
                🎯 Confidence Threshold: {confidence_threshold:.0%}
            </p>
            <span class="status-badge status-critical">REQUIRES ATTENTION</span>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="alert-box alert-success">
            <div class="alert-title">✅ All Clear!</div>
            <p style="color: #bbf7d0; font-size: 1.1rem; margin: 10px 0;">
                No defects detected in the infrastructure
            </p>
            <p style="color: #86efac; margin: 5px 0;">
                📍 Timestamp: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
            </p>
            <span class="status-badge status-safe">INFRASTRUCTURE SAFE</span>
        </div>
        """, unsafe_allow_html=True)


def render_detection_table(detection_data):
    """
    Render detection details table
    
    Args:
        detection_data (list): List of detection dictionaries
    """
    st.markdown("### 📋 Detection Details")
    st.dataframe(detection_data, use_container_width=True)


def render_confidence_chart(confidences):
    """
    Render confidence distribution bar chart
    
    Args:
        confidences (list): List of confidence scores
        
    Returns:
        plotly.graph_objects.Figure: Confidence chart
    """
    fig = go.Figure(data=[go.Bar(
        x=[f"Detection {i+1}" for i in range(len(confidences))],
        y=confidences,
        marker=dict(
            color=confidences,
            colorscale='RdYlGn',
            showscale=True,
            colorbar=dict(title="Confidence", x=1.15),
            line=dict(color='rgba(255,255,255,0.3)', width=1)
        ),
        text=[f"{c:.1%}" for c in confidences],
        textposition='outside',
        hovertemplate='<b>Detection %{x}</b><br>Confidence: %{y:.2%}<extra></extra>'
    )])
    
    fig.update_layout(
        title=dict(
            text="Confidence Levels by Detection",
            font=dict(size=16, color='#a5b4fc')
        ),
        xaxis_title="Detection ID",
        yaxis_title="Confidence Score",
        template="plotly_dark",
        height=400,
        plot_bgcolor='rgba(30, 27, 75, 0.5)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#a5b4fc'),
        yaxis=dict(range=[0, 1], tickformat='.0%'),
        margin=dict(t=50, b=50, l=50, r=100)
    )
    
    return fig


def render_severity_chart(severity_counts):
    """
    Render severity distribution pie chart
    
    Args:
        severity_counts (dict): Dictionary of severity counts
        
    Returns:
        plotly.graph_objects.Figure: Severity pie chart
    """
    severity_colors = {'High': '#ef4444', 'Medium': '#f59e0b', 'Low': '#22c55e'}
    
    fig = go.Figure(data=[go.Pie(
        labels=list(severity_counts.keys()),
        values=list(severity_counts.values()),
        marker=dict(
            colors=[severity_colors[s] for s in severity_counts.keys()],
            line=dict(color='rgba(255,255,255,0.3)', width=2)
        ),
        textinfo='label+percent+value',
        textfont=dict(size=14),
        hovertemplate='<b>%{label}</b><br>Count: %{value}<br>Percentage: %{percent}<extra></extra>',
        hole=0.4
    )])
    
    fig.update_layout(
        title=dict(
            text="Severity Distribution",
            font=dict(size=16, color='#a5b4fc')
        ),
        template="plotly_dark",
        height=400,
        plot_bgcolor='rgba(30, 27, 75, 0.5)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#a5b4fc'),
        showlegend=True,
        legend=dict(orientation="h", yanchor="bottom", y=-0.2, xanchor="center", x=0.5)
    )
    
    return fig


def render_type_distribution_chart(type_counts):
    """
    Render defect type distribution chart
    
    Args:
        type_counts (dict): Dictionary of defect type counts
        
    Returns:
        plotly.graph_objects.Figure: Type distribution chart
    """
    fig = go.Figure(data=[go.Bar(
        x=list(type_counts.keys()),
        y=list(type_counts.values()),
        marker=dict(
            color='#667eea',
            line=dict(color='rgba(255,255,255,0.3)', width=1)
        ),
        text=list(type_counts.values()),
        textposition='outside',
        hovertemplate='<b>%{x}</b><br>Count: %{y}<extra></extra>'
    )])
    
    fig.update_layout(
        title=dict(
            text="Defect Types Detected",
            font=dict(size=16, color='#a5b4fc')
        ),
        xaxis_title="Defect Type",
        yaxis_title="Count",
        template="plotly_dark",
        height=350,
        plot_bgcolor='rgba(30, 27, 75, 0.5)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#a5b4fc'),
        margin=dict(t=50, b=50, l=50, r=50)
    )
    
    return fig


def render_trend_chart(detection_history):
    """
    Render detection trend chart
    
    Args:
        detection_history (list): List of detection records
        
    Returns:
        plotly.graph_objects.Figure: Trend chart
    """
    history_reversed = list(reversed(detection_history))
    timestamps = [record['timestamp'] for record in history_reversed]
    detection_counts = [record['detections'] for record in history_reversed]
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=list(range(1, len(timestamps) + 1)),
        y=detection_counts,
        mode='lines+markers',
        name='Detections',
        line=dict(color='#667eea', width=3),
        marker=dict(
            size=10,
            color=detection_counts,
            colorscale='RdYlGn_r',
            showscale=True,
            colorbar=dict(title="Count", x=1.15),
            line=dict(color='white', width=2)
        ),
        text=[f"Scan {i+1}<br>{ts}<br>{count} defects" 
              for i, (ts, count) in enumerate(zip(timestamps, detection_counts))],
        hovertemplate='<b>%{text}</b><extra></extra>'
    ))
    
    fig.add_hline(
        y=0, 
        line_dash="dash", 
        line_color="rgba(34, 197, 94, 0.5)",
        annotation_text="Safe Threshold",
        annotation_position="right"
    )
    
    fig.update_layout(
        title=dict(
            text="Detection Count Over Time",
            font=dict(size=18, color='#a5b4fc')
        ),
        xaxis_title="Scan Number",
        yaxis_title="Number of Defects Detected",
        template="plotly_dark",
        height=400,
        plot_bgcolor='rgba(30, 27, 75, 0.5)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#a5b4fc'),
        hovermode='x unified',
        margin=dict(t=60, b=50, l=50, r=100)
    )
    
    return fig


def render_detection_history(detection_history):
    """
    Render recent detection history
    
    Args:
        detection_history (list): List of detection records
    """
    st.markdown("### 📜 Recent Detection History")
    
    for record in detection_history[:5]:
        status_class = "status-critical" if record['status'] == 'Critical' else "status-safe"
        st.markdown(f"""
        <div class="detection-box">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div>
                    <p style="color: #a5b4fc; margin: 0;">🕐 {record['timestamp']}</p>
                    <p style="color: white; font-size: 1.1rem; margin: 5px 0;">
                        Detections: <strong>{record['detections']}</strong>
                    </p>
                </div>
                <span class="status-badge {status_class}">{record['status']}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)


def render_footer():
    """Render application footer"""
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #a5b4fc; padding: 20px;">
        <p style="margin: 0;">Powered by InfraSentinel AI | Real-time Infrastructure Monitoring</p>
        <p style="margin: 5px 0; font-size: 0.9rem;">🛡️ Protecting Infrastructure with Advanced AI Detection</p>
        <p style="margin: 10px 0; font-size: 0.85rem; color: #8b92c7;">
            This project belongs to <strong style="color: #667eea;">Sentryva Technologies Team</strong>
        </p>
    </div>
    """, unsafe_allow_html=True)
