from dataclasses import dataclass

@dataclass
class Point:
    lat: float
    long: float

def locate(latitude: float, longitude: float) -> Point:
    """Find an object in the map by its coordinates"""
    return None

print(locate.__annotations__)


def student_profile(name:str, age: int, grade: int):
    """"""