# Copyright 2018-2024 contributors to the OpenLineage project
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing import Optional

from openlineage.client.generated.base import RunFacet
from pydantic import BaseModel, Field
from typing_extensions import Annotated


class Model(BaseModel):
    processing_engine: Optional[ProcessingEngineRunFacet] = None


class ProcessingEngineRunFacet(RunFacet):
    version: Annotated[str, Field(example="2.5.0")]
    """
    Processing engine version. Might be Airflow or Spark version.
    """
    name: Annotated[Optional[str], Field(example="Airflow")] = None
    """
    Processing engine name, e.g. Airflow or Spark
    """
    openlineageAdapterVersion: Annotated[Optional[str], Field(example="0.19.0")] = None
    """
    OpenLineage adapter package version. Might be e.g. OpenLineage Airflow integration package version
    """
