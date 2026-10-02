from fastapi import FastAPI, Query
from models import PinCodeRequest, LocationResponse, BulkRequest, BulkResponse
from data import pincode_db
from exceptions import (
    PinCodeNotFoundError,
    InvalidPinCodeError,
    pincode_not_found_handler,
    invalid_pincode_handler,
)

app = FastAPI(
    title="Pincode Lookup",
    description="Auto fill city and state from India Pincode during checkout",
)

app.add_exception_handler(PinCodeNotFoundError, pincode_not_found_handler)
app.add_exception_handler(InvalidPinCodeError, invalid_pincode_handler)


@app.get("/")
def root():
    return {"message": "Pincode Lookup working"}


@app.get("/lookup/{pincode}", response_model=LocationResponse)
def lookup_pincode(pincode: str):
    if len(pincode) != 6 or not pincode.isdigit():
        raise InvalidPinCodeError(pincode, "Must be exactly 6 digits")
    data = pincode_db.get(pincode)
    if not data:
        raise PinCodeNotFoundError(pincode)
    return LocationResponse(pincode=pincode, **data)


@app.get("/lookup", response_model=LocationResponse)
def lookup_pincode_query(pincode: str = Query(..., min_length=6, max_length=6)):
    if not pincode.isdigit():
        raise InvalidPinCodeError(pincode, "Must be exactly 6 digits")
    data = pincode_db.get(pincode)
    if not data:
        raise PinCodeNotFoundError(pincode)
    return LocationResponse(pincode=pincode, **data)


@app.post("/bulk-lookup", response_model=BulkResponse)
def bulk_lookup(request: BulkRequest):
    results = []
    missing = []
    for code in request.pincodes:
        data = pincode_db.get(code)
        if data:
            results.append(LocationResponse(pincode=code, **data))
        else:
            missing.append(code)
    return BulkResponse(
        found=len(results),
        not_found=len(missing),
        result=results,
        missing=missing,
    )
