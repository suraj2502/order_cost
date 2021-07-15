import uvicorn
from configurations import API_HOST_IP, API_HOST_PORT


if __name__ == "__main__":
    uvicorn.run("app.api:app", host=API_HOST_IP, port=API_HOST_PORT, reload=True)