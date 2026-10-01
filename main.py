from fastapi import FastAPI

app  = FastAPI(
    title="Restaurant Menu API",
    description="API for managing restaurant menu items",
    docs_url="/docs",

);


@app.get("/")
def root():
    return {"message":"Welcome to new app"}

