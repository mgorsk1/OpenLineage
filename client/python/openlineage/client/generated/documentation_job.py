# Copyright 2018-2024 contributors to the OpenLineage project
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing import Optional

from openlineage.client.generated.base import JobFacet
from pydantic import BaseModel


class DocumentationJobFacet(JobFacet):
    description: str
    """
    The description of the job.
    """


class Model(BaseModel):
    documentation: Optional[DocumentationJobFacet] = None
