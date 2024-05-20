# Copyright 2018-2024 contributors to the OpenLineage project
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing import Optional

from openlineage.client.generated.base import JobFacet
from pydantic import BaseModel


class Model(BaseModel):
    sourceCode: Optional[SourceCodeJobFacet] = None


class SourceCodeJobFacet(JobFacet):
    language: str
    """
    Language in which source code of this job was written.
    """
    sourceCode: str
    """
    Source code of this job.
    """
