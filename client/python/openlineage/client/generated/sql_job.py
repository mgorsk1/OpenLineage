# Copyright 2018-2024 contributors to the OpenLineage project
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing import Optional

from openlineage.client.generated.base import JobFacet
from pydantic import BaseModel, Field
from typing_extensions import Annotated


class Model(BaseModel):
    sql: Optional[SQLJobFacet] = None


class SQLJobFacet(JobFacet):
    query: Annotated[str, Field(example="SELECT * FROM foo")]
