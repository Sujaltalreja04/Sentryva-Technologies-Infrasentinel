"""
CSS Styles for Streamlit App
Contains all custom styling for the Sentryx interface
"""


def load_css():
    """
    Returns the custom CSS styling for the application
    
    Returns:
        str: CSS styles as a string
    """
    return """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
        
        * { font-family: 'Inter', sans-serif; }
        
        .stApp {
            background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
        }
        
        .main-header {
            background: rgba(99, 102, 241, 0.1);
            border-radius: 15px;
            padding: 25px;
            margin-bottom: 25px;
            border: 1px solid rgba(99, 102, 241, 0.3);
        }
        
        .main-title {
            font-size: 2.5rem;
            font-weight: 700;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin: 0;
            text-align: center;
        }
        
        .subtitle {
            color: #a5b4fc;
            text-align: center;
            font-size: 1rem;
            margin-top: 8px;
        }
        
        .alert-box {
            background: rgba(239, 68, 68, 0.15);
            border-left: 4px solid #ef4444;
            border-radius: 12px;
            padding: 20px;
            margin: 20px 0;
        }
        
        .alert-success {
            background: rgba(34, 197, 94, 0.15);
            border-left: 4px solid #22c55e;
        }
        
        .alert-title {
            font-size: 1.3rem;
            font-weight: 700;
            color: #fca5a5;
            margin-bottom: 10px;
        }
        
        .alert-success .alert-title {
            color: #86efac;
        }
        
        .status-badge {
            display: inline-block;
            padding: 6px 14px;
            border-radius: 20px;
            font-weight: 600;
            font-size: 0.85rem;
            margin: 5px;
        }
        
        .status-critical {
            background: #ef4444;
            color: white;
        }
        
        .status-safe {
            background: #22c55e;
            color: white;
        }
        
        .detection-box {
            background: rgba(30, 27, 75, 0.5);
            border-radius: 12px;
            padding: 15px;
            border: 1px solid rgba(99, 102, 241, 0.3);
            margin: 8px 0;
        }
        
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
    </style>
    """
