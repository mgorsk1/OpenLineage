# Copyright 2018-2024 contributors to the OpenLineage project
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from datetime import datetime
from typing import Optional

from openlineage.client.generated.base import RunFacet
from pydantic import BaseModel, Field
from typing_extensions import Annotated


class Model(BaseModel):
    nominalTime: Optional[NominalTimeRunFacet] = None


class NominalTimeRunFacet(RunFacet):
    nominalStartTime: Annotated[datetime, Field(example="2020-12-17T03:00:00.000Z")]
    """
    An [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) timestamp representing the nominal start time (included) of the run. AKA the schedule time
    """
    nominalEndTime: Annotated[Optional[datetime], Field(example="2020-12-17T04:00:00.000Z")] = None
    """
    An [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) timestamp representing the nominal end time (excluded) of the run. (Should be the nominal start time of the next run)
    """
