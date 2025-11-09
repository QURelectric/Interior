from fastapi import FastAPI
# Import the FastAPI class from the fastapi module
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
# Import necessary modules for HTML responses and templating

app = FastAPI()
# Create an instance of the FastAPI class

templates = Jinja2Templates(directory="app/templates")
# Set up Jinja2 templates, specifying the directory where HTML templates are stored

# Most Basic Example
@app.get("/", response_class=HTMLResponse)
# Define a GET endpoint at the root URL (Eg http://localhost:8000/) 
# and specify that it returns an HTML response
async def read_root(request: Request):
    # Define an asynchronous function to handle requests to this endpoint
    return templates.TemplateResponse("index.html", {"request": request, "message": "Hello World"})
    # Return a simple JSON response using the template "index.html" with a message



