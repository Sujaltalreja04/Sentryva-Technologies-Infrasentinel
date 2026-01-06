# 🛡️ InfraSentinel - AI-Powered Infrastructure Monitoring System

> **Production-Grade Infrastructure Defect Detection using YOLOv8 Deep Learning**

[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://streamlit.io/)
[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![YOLOv8](https://img.shields.io/badge/YOLOv8-00FFFF?style=for-the-badge&logo=YOLO&logoColor=black)](https://github.com/ultralytics/ultralytics)
[![Azure](https://img.shields.io/badge/Azure-0078D4?style=for-the-badge&logo=microsoft-azure&logoColor=white)](https://azure.microsoft.com/)

---

## 🎯 Overview

**SENTRYX** is an advanced AI-powered infrastructure monitoring system designed to detect and analyze structural defects in real-time. Built with cutting-edge YOLOv8 technology, SENTRYX provides comprehensive defect detection, analytics, and reporting capabilities for critical infrastructure monitoring.

### ✨ Key Features

- 🔍 **Real-time Defect Detection** - Instant identification of cracks, structural damage, and anomalies
- 📊 **Advanced Analytics** - Comprehensive confidence metrics and severity analysis
- 📈 **Trend Analysis** - Historical tracking and pattern recognition
- 🎨 **Premium UI/UX** - Modern, responsive interface with dark mode aesthetics
- ⚡ **High Performance** - Optimized for speed with model caching and efficient processing
- 📱 **Responsive Design** - Works seamlessly across all devices

---

## 🏗️ Project Structure

```
sentryx/
│
├── .streamlit/
│   └── config.toml              # Streamlit configuration
│
├── app.py                       # Main application entry point ✅
│
├── models/
│   ├── microsoft_infra.pt       # Custom infrastructure detection model ✅
│   └── yolov8s.pt              # YOLOv8 base model ✅
│
├── core/                        # Core business logic
│   ├── __init__.py
│   ├── model.py                # YOLO model loading & management
│   ├── detector.py             # Detection & prediction logic
│   └── analytics.py            # Statistics & confidence analysis
│
├── ui/                          # User interface components
│   ├── __init__.py
│   ├── styles.py               # CSS styling
│   ├── sidebar.py              # Sidebar UI & controls
│   └── components.py           # Reusable UI components
│
├── utils/                       # Utility functions
│   ├── __init__.py
│   └── file_utils.py           # File handling & temp management
│
├── assets/
│   └── images/                 # Static assets
│
├── packages.txt                # System dependencies (for Streamlit Cloud)
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
└── .gitignore                  # Git ignore rules
```

---

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip package manager
- Git (optional)

### Installation

1. **Clone or download the repository**
   ```bash
   git clone <repository-url>
   cd sentryx
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run app.py
   ```

4. **Access the application**
   - Open your browser and navigate to `http://localhost:8501`

---

## 📦 Dependencies

```txt
streamlit>=1.28.0
ultralytics>=8.0.0
opencv-python>=4.8.0
pillow>=10.0.0
plotly>=5.17.0
numpy>=1.24.0
```

---

## 💻 Usage

### Basic Workflow

1. **Upload Image**
   - Click on the upload section
   - Select an infrastructure image (JPG, JPEG, or PNG)

2. **Adjust Settings**
   - Use the sidebar to adjust detection confidence threshold
   - Higher values = more strict detection
   - Lower values = more sensitive detection

3. **View Results**
   - Original vs. Detection comparison
   - Detailed detection table
   - Interactive analytics charts
   - Confidence statistics

4. **Track History**
   - View recent detection history
   - Analyze detection trends over time
   - Monitor system statistics

### Advanced Features

- **Severity Analysis**: Automatic categorization (High/Medium/Low)
- **Type Distribution**: Breakdown by defect types
- **Trend Visualization**: Historical pattern analysis
- **Export Capabilities**: Save detection results (coming soon)

---

## 🏆 Architecture Highlights

### Why This Structure is Production-Grade

✅ **Modular Design**
- Clean separation of concerns
- Easy to maintain and extend
- Scalable architecture

✅ **Professional Organization**
- Industry-standard folder structure
- Clear naming conventions
- Comprehensive documentation

✅ **Competition-Ready**
- Azure/Imagine Cup compliant
- Easy to explain in presentations
- Demonstrates software engineering best practices

✅ **Performance Optimized**
- Model caching with `@st.cache_resource`
- Efficient file handling
- Optimized image processing

---

## 🎨 UI/UX Design

### Design Philosophy

- **Modern Aesthetics**: Gradient backgrounds, glassmorphism effects
- **Dark Mode**: Eye-friendly color scheme
- **Interactive Charts**: Plotly-powered visualizations
- **Responsive Layout**: Adapts to all screen sizes
- **Premium Feel**: Professional-grade interface

### Color Palette

- Primary: `#667eea` (Indigo)
- Secondary: `#764ba2` (Purple)
- Success: `#22c55e` (Green)
- Warning: `#f59e0b` (Amber)
- Danger: `#ef4444` (Red)
- Background: Dark gradient (`#0f0c29` → `#302b63` → `#24243e`)

---

## 🔧 Configuration

### Streamlit Configuration (`.streamlit/config.toml`)

```toml
[theme]
primaryColor = "#667eea"
backgroundColor = "#0f0c29"
secondaryBackgroundColor = "#1e1b4b"
textColor = "#ffffff"
font = "sans serif"

[server]
maxUploadSize = 10
enableCORS = false
```

---

## 📊 Model Information

### Microsoft Infrastructure Model (`microsoft_infra.pt`)

- **Type**: YOLOv8 Custom Trained
- **Purpose**: Infrastructure defect detection
- **Classes**: Cracks, structural damage, surface defects, anomalies
- **Input Size**: 1024x1024
- **Performance**: Optimized for real-time inference

### Base Model (`yolov8s.pt`)

- **Type**: YOLOv8 Small
- **Purpose**: General object detection (backup/testing)
- **Size**: ~22MB
- **Speed**: Fast inference

---

## 🌐 Deployment

### Streamlit Cloud

1. Push code to GitHub
2. Connect to Streamlit Cloud
3. Deploy with one click
4. Automatic HTTPS and scaling

### Azure Deployment

1. Create Azure Web App
2. Configure Python runtime
3. Deploy via GitHub Actions
4. Scale as needed

### Docker (Optional)

```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8501
CMD ["streamlit", "run", "app.py"]
```

---

## 🤝 Contributing

This project is designed for competition purposes. For collaboration:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

---

## 📄 License

This project is developed for educational and competition purposes.

---

## 👥 Team

**SENTRYX Development Team**
- AI/ML Engineering
- Full-Stack Development
- UI/UX Design
- Cloud Architecture

---

## 🎓 Competition Information

**Built for**: Microsoft Imagine Cup / Azure AI Challenge

**Category**: AI for Infrastructure & Smart Cities

**Technologies**:
- Azure Cloud Services
- YOLOv8 Deep Learning
- Streamlit Framework
- Computer Vision

---

## 📞 Support

For questions or issues:
- Open an issue on GitHub
- Contact the development team
- Check documentation

---

## 🚀 Future Enhancements

- [ ] Multi-model ensemble detection
- [ ] Real-time video stream processing
- [ ] Mobile application
- [ ] API endpoints for integration
- [ ] Automated reporting system
- [ ] Cloud storage integration
- [ ] Multi-language support
- [ ] Advanced export options

---

<div align="center">

**🛡️ Protecting Infrastructure with Advanced AI Detection**

Made with ❤️ by the SENTRYX Team

</div>
