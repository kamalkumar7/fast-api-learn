from fastapi import FastAPI, Query, HTTPException

app = FastAPI(
    title="Pincode Lookpu",
    description  ="Auto fill city and state from India Pincode during checkout")

@app.get("/")
def root():
    return {"message":"Pincode Lookup working"}

