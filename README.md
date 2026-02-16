# Yashwini Shetty - Professional CV Website

A modern, responsive personal CV website for Yashwini Shetty, Senior Automation Test Engineer.

| Python | Flask |
|--------|-------|
| 3.8+   | 3.0   |

---

## Table of Contents

- [How to Install Dependencies](#how-to-install-dependencies)
- [How to Run the Project](#how-to-run-the-project)
- [Project Structure](#project-structure)
- [Features](#features)
- [API](#api)
- [Customization](#customization)
- [Technology Stack](#technology-stack)
- [Contact](#contact)

---

## How to Install Dependencies

### Prerequisites

- **Python 3.8 or higher**

  Check your version:
```bash
  python --version
  ```

  or

  ```bash
  python3 --version
  ```
### Install Steps

1. **Open a terminal** in the project folder (yashwini_website).

2. **Optional but recommended: use a virtual environment**
```bash
   python -m venv venv
   ```

   - **Windows:**

   ```bash
     venv\Scripts\activate
     ```

   - **macOS/Linux:**

   ```bash
     source venv/bin/activate
     ```
3. **Install dependencies from requirements.txt**
```bash
   pip install -r requirements.txt
   ```

   This installs:
   - Flask==3.0.0
   - Werkzeug==3.0.1

---

## How to Run the Project

### Option 1: Command line (any OS)

From the project folder, with dependencies already installed:
```bash
python app.py
```

The app will start and print something like:
```text
* Running on http://0.0.0.0:5001
```

### Option 2: Windows batch file

1. Double-click **start.bat** in the project folder.
2. It will install dependencies (if needed) and then start the server.
3. When you see "Starting Flask server...", the app is running.

### Access the website

- **On your machine:** open a browser and go to **http://localhost:5001**
- **From another device on the same network:** use **http://YOUR_IP_ADDRESS:5001**

To stop the server, press **Ctrl+C** in the terminal (or close the terminal window).

---

## Project Structure
```text
yashwini_website/
|-- app.py              # Flask application and CV data
|-- requirements.txt    # Python dependencies
|-- start.bat           # Windows: install deps and run app
|-- static/             # Static assets (CSS, JS, images)
|-- templates/
|   |-- index.html      # Main HTML template
|-- README.md           # This file
```
---

## Features

- Modern, professional design
- Responsive layout (mobile, tablet, desktop)
- Fast and lightweight
- Comprehensive professional profile
- Social links and skills visualization
- Timeline-based experience
- JSON API for CV data

---

## API

| Property   | Value                        |
|-----------|------------------------------|
| **URL**   | http://localhost:5001/api/cv |
| **Method**| GET                          |
| **Response** | CV data in JSON format   |

---

## Customization

To change CV content, edit the cv_data dictionary in **app.py** (name, title, contact, experience, skills, education, etc.).

---

## Technology Stack

| Layer    | Technologies        |
|----------|---------------------|
| Backend  | Flask (Python)      |
| Frontend | HTML5, CSS3, JavaScript |
| Icons    | Font Awesome 6.4.0  |
| Layout   | CSS Grid & Flexbox  |

---

## Contact

|          | |
|----------|---|
| **Email**    | yashwini.j.shetty@gmail.com |
| **Phone**    | +966 548045247 |
| **LinkedIn** | [Yashwini J Shetty](https://www.linkedin.com/in/yashwini-j-shetty-83b3b7115) |
| **Location** | Al Qadisiayah, Riyadh, KSA |

---

(c) 2025 Yashwini Shetty. All Rights Reserved.