# Copyright 2018-2024 contributors to the OpenLineage project
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing import Optional
from uuid import UUID

from openlineage.client.generated.base import RunFacet
from pydantic import BaseModel, Field
from typing_extensions import Annotated


class Job(BaseModel):
    namespace: Annotated[str, Field(example="my-scheduler-namespace")]
    """
    The namespace containing that job
    """
    name: Annotated[str, Field(example="myjob.mytask")]
    """
    The unique name for that job within that namespace
    """


class Model(BaseModel):
    parent: Optional[ParentRunFacet] = None


class ParentRunFacet(RunFacet):
    run: Run
    job: Job


class Run(BaseModel):
    runId: UUID
    """
    The globally unique ID of the run associated with the job.
    """
