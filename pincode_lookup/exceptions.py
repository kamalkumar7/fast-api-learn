from fastapi.responses import JSONResponse
from fastapi import Request

class PinCodeNotFoundError(Exception):
    def __init__(self, pincode:str):
        self.pincode = pincode

class InvalidPinCodeError(Exception):
    def __init__(self, pincode:str,reason:str ="Invalid format"):
        self.pincode = pincode
        self.reason = reason



async def pincode_not_found_handler(request: Request, exc: PinCodeNotFoundError):
    return JSONResponse(
        status_code=404,
        content={
            "status": "error",
            "detail": f"Pincode '{exc.pincode}' not found",
        },
    )


async def invalid_pincode_handler(request: Request, exc: InvalidPinCodeError):
    return JSONResponse(
        status_code=400,
        content={
            "status": "error",
            "detail": f"Invalid pincode '{exc.pincode}': {exc.reason}",
        },
    )
