from fastapi import FastAPI, Request

app = FastAPI(
    title="My New App",
    description="Ye meri pehli FastAPI application hai",
    version="1.0.0",
    docs_url="/docs",           # Swagger UI
    redoc_url="/redoc",         # ReDoc UI
    openapi_url="/openapi.json" # OpenAPI schema JSON
)


@app.get("/")
def read_root():
    "Root endpoint that returns a welcome message."
    # FastAPI automatically generates the OpenAPI schema and documentation based on the defined endpoints and their metadata. The root endpoint is defined here, which returns a simple JSON response with a welcome message.
    return {"message": "Welcome to new app"}

@app.get("/about")
def about():
    "About endpoint that provides information about the application."
    # This endpoint returns a JSON response with information about the application, including its name, description, and version.
    return {
        "app_name": app.title,
        "description": app.description,
        "version": app.version
    }

@app.get("/request/info")
def request_info(request: Request):
    "Request info endpoint that returns details about the incoming request."
    # This endpoint returns a JSON response with details about the incoming request, such as the client's IP address, user agent, and headers.
    return {
        "user_agent": request.headers.get("user-agent"),
        "headers": dict(request.headers),
        "client_host": request.client.host if request.client else None,

    }