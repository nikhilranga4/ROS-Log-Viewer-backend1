from main import app  # Replace 'main' with the name of your FastAPI app file

# You can run Uvicorn with Gunicorn worker here
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
