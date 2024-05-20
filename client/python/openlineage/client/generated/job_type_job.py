# Copyright 2018-2024 contributors to the OpenLineage project
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing import Optional

from openlineage.client.generated.base import JobFacet
from pydantic import BaseModel, Field
from typing_extensions import Annotated


class JobTypeJobFacet(JobFacet):
    processingType: Annotated[str, Field(example="BATCH")]
    """
    Job processing type like: BATCH or STREAMING
    """
    integration: Annotated[str, Field(example="SPARK")]
    """
    OpenLineage integration type of this job: SPARK|DBT|AIRFLOW|FLINK
    """
    jobType: Annotated[Optional[str], Field(example="QUERY")] = None
    """
    Run type like: QUERY|COMMAND|DAG|TASK|JOB|MODEL
    """


class Model(BaseModel):
    jobType: Optional[JobTypeJobFacet] = None
