from pydantic import BaseModel
from datetime import datetime

class Alert(BaseModel):
    boarder: str
    zone: str
    timestamp: str
    count_People: int
    count_weapons: int
    vehicle_type: str
    distance_from_fence_m: int
    quality_visibility: int

