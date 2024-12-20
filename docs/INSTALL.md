# Installation Guide

This document provides step-by-step instructions for installing the VMAF Calculator project.

## Prerequisites

Before you begin, ensure you have met the following requirements:
- **Software**:
  - Python 3 or above
  - FFmpeg >= 5.0 installed (for video processing) build with **libvmaf**
  - PyQt5 for the front-end GUI

- **Python Packages**:
  - Required packages listed in the requirements.txt file

## Installation Steps

1. Clone the repository:
```
git clone https://github.com/TekMedia-Software/VMAF-Calculator.git
```

2. Navigate to the project directory:
```
cd VMAF-Calculator
```

3. Install Python: Download and install Python required version Python3 or above.
	
4. Install FFmpeg: Download and install FFmpeg >= 5.0 build it with libvmaf if it's not already installed. Ensure it is added to your system’s PATH.

5. Install dependencies: To install all necessary Python packages, run:
```
sudo apt-get install python3-pip
```
```
pip install -r requirements.txt
```

## Running the Project

To start the VMAF Calculator, run the following command:
```
python3 app.py
```

This will launch the PyQt5 GUI for analyzing video files and computing VMAF, PSNR, and SSIM metrics.

## Contact

If you encounter any issues or have questions regarding the installation, please contact:

- Awadh Bajpai - [awabaj@tekmediasoft.net](mailto:awabaj@tekmediasoft.net)
- Sushanthika Manikandan - [susman@tekmediasoft.net](mailto:susman@tekmediasoft.net)
    
