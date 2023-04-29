import json
from typing import List, Optional, Tuple

import numpy as np
import pandas as pd
from pydantic import BaseModel, ValidationError

from model.config.core import config


def validate_inputs(*, input_data: pd.DataFrame) -> Tuple[pd.DataFrame, Optional[dict]]:
    """Check model inputs for unprocessable values."""

    validated_data = input_data[config.model_config.features].copy()
    errors = None

    try:
        # replace numpy nans so that pydantic can validate
        MultipleDataInputs(
            inputs=validated_data.replace({np.nan: None}).to_dict(orient="records")
        )
    except ValidationError as error:
        errors = json.loads(error.json())

    return validated_data, errors


class DataInputSchema(BaseModel):

    num_passengers: Optional[int]
    sales_channel: Optional[str]
    purchase_lead: Optional[int]
    length_of_stay: Optional[int]
    flight_hour: Optional[int]
    flight_day: Optional[str]
    route: Optional[str]
    wants_extra_baggage: Optional[int]
    wants_preferred_seat: Optional[int]
    wants_in_flight_meals: Optional[int]
    flight_duration: Optional[float]


class MultipleDataInputs(BaseModel):
    inputs: List[DataInputSchema]
