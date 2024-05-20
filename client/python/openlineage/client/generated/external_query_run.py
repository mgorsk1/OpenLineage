# Copyright 2018-2024 contributors to the OpenLineage project
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing import Optional

from openlineage.client.generated.base import RunFacet
from pydantic import BaseModel, Field
from typing_extensions import Annotated


class ExternalQueryRunFacet(RunFacet):
    externalQueryId: Annotated[str, Field(example="my-project-1234:US.bquijob_123x456_123y123z123c")]
    """
    Identifier for the external system
    """
    source: Annotated[str, Field(example="bigquery")]
    """
    source of the external query
    """


class Model(BaseModel):
    externalQuery: Optional[ExternalQueryRunFacet] = None
