from typing import Any, List, Optional

from pydantic import BaseModel

from model.preprocessing.validation import DataInputSchema


class PredictionResults(BaseModel):
    errors: Optional[Any]
    version: str
    predictions: int


class MultipleDataInputs(BaseModel):
    inputs: List[DataInputSchema]

    class Config:
        schema_extra = {
            "example": {
                "inputs": [
                    {
                        "num_passengers": 2,
                        "sales_channel": "Internet",
                        "purchase_lead": 262,
                        "length_of_stay": 19,
                        "flight_hour": 7,
                        "flight_day": "Sat",
                        "route": "AKLDEL",
                        "wants_extra_baggage": 1,
                        "wants_preferred_seat": 0,
                        "wants_in_flight_meals": 0,
                        "flight_duration": 5.52,
                    }
                ]
            }
        }
