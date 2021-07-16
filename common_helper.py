from fastapi.responses import JSONResponse


def ResponseModel(data, code, message):
    return JSONResponse(status_code=code, content={"data": data, "message": message})


def ErrorResponseModel(data, code, message):
    return JSONResponse(status_code=code, content={"data": data, "message": message})

def delivery_cost(distance):
            cost = 0
            if distance<=10000 :
                cost+= 5000
            elif distance<=20000:
                cost += 10000
            elif distance<= 50000:
                cost += 50000
            else:
                cost += 100000
            return cost
