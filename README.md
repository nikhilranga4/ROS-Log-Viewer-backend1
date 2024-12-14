# ROS Log Viewer Backend

This project is the backend part of the **ROS Log Viewer** full-stack application. It is built using **FastAPI** and is responsible for parsing and serving ROS log files via a REST API. The backend also supports handling CORS (Cross-Origin Resource Sharing) for communication with the frontend.

## Prerequisites

Before running the project, ensure that you have the following installed on your system:

1. **Python 3.8+**
   - You can download Python from [python.org](https://www.python.org/downloads/).
   
2. **Pip** (Python package installer)
   - Ensure you have pip installed by running `pip --version`.

3. **Docker** (Optional)
   - Docker can be used to containerize the backend. You can download Docker from [here](https://www.docker.com/products/docker-desktop).

## Installation

### 1. Clone the repository
First, clone this repository to your local machine:

```bash
git clone https://github.com/nikhilranga4/ROS-LOG-VIEWER-FULLSTACK.git
cd ROS-LOG-VIEWER-FULLSTACK/backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install flask-cor
pip install websockets
pip install fastapi uvicorn
pip install fastapi uvicorn python-multipart
pip3 install gunicorn
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
