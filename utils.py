def build_errors(resp: dict, errors: Exception) -> dict:
    resp["statusCode"] = 500
    resp["status"] = f"Internal Server Error: {errors}" 

    return resp


def build_data_dict(status: str, status_code: int, data: bool) -> dict:
    data_dict = { 
        "statusCode": status_code,
        "status": status,
    } 

    if data:
        data_dict["data"] = []

    return data_dict 

