def data_from_response(response: dict) -> dict:
    if response['status'] != 200:
        raise ValueError
    return {'data':response['payload']}