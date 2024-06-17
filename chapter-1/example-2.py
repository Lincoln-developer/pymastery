from dataclasses import dataclass

@dataclass
class ResponseType:
    response: dict
    latitude: float

def data_from_response(response: dict, latitude: float) -> ResponseType:
    """If the response is OK, return its payload

       -Response: A dict like::
       
       {
         "status": 200,
         "timestamp": "....",
         "payload: "...."
       }

       -Returns a dictionary like::
       {"data: {..}}

       -Raises:
       - ValueError if the HTTP status ! 200
    """
    if response['status'] != 200:
        raise ValueError
    return {'data':response['payload']}