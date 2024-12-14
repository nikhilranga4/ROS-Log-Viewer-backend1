from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import re
import os
import uvicorn

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://roslogviewer.netlify.app","http://localhost:3000"],  # Use your Netlify frontend URL
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

# Define the log structure
class LogEntry:
    def __init__(self, timestamp: str, severity: str, node: str, message: str):
        self.timestamp = timestamp
        self.severity = severity
        self.node = node
        self.message = message

# Function to parse ROS log file
def parse_log_file(file_content: str):
    logs = []
    # Regex to match the log format [timestamp] [severity] [node_name] message
    log_pattern = r"\[(?P<timestamp>[^\]]+)\] \[(?P<severity>[^\]]+)\] \[(?P<node>[^\]]+)\] (?P<message>.*)"
    
    for line in file_content.splitlines():
        if not line.strip():
            continue
        # Match the log line using regex
        match = re.match(log_pattern, line.strip())
        if match:
            timestamp = match.group('timestamp')
            severity = match.group('severity')
            node = match.group('node')
            message = match.group('message')
            
            # Create a LogEntry object and append to the logs list
            log_entry = LogEntry(timestamp, severity, node, message)
            logs.append(log_entry.__dict__)  # Convert to dictionary
            
    return logs

@app.get("/api/logs")
async def get_logs():
    try:
        # Ensure the log file exists or use a default log for now
        log_file_path = os.path.join(os.getcwd(), 'fake_ros_logs.log')
        
        # Check if the log file exists
        if not os.path.exists(log_file_path):
            return JSONResponse(status_code=404, content={"message": "Log file not found"})
        
        # Read the log file content
        with open(log_file_path, 'r') as f:
            file_content = f.read()
        
        # Parse the file content
        logs = parse_log_file(file_content)

        # Return the parsed logs as a JSON response
        return JSONResponse(content={"logs": logs})
    except Exception as e:
        # Handle any exceptions and return an error response
        return JSONResponse(status_code=500, content={"message": f"Error reading the log file: {str(e)}"})

# For running locally, not needed for Render deployment
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
