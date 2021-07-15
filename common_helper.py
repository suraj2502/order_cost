from fastapi.responses import JSONResponse


def ResponseModel(data, code, message):
    return JSONResponse(status_code=code, content={"data": data, "message": message})


def ErrorResponseModel(data, code, message):
    return JSONResponse(status_code=code, content={"data": data, "message": message})