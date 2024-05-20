# Copyright 2018-2024 contributors to the OpenLineage project
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing import Optional

from openlineage.client.generated.base import DatasetFacet
from pydantic import BaseModel, Field
from typing_extensions import Annotated


class Identifier(BaseModel):
    namespace: str
    """
    The dataset namespace
    """
    name: str
    """
    The dataset name
    """
    type: Annotated[str, Field(example="table")]
    """
    Identifier type
    """


class Model(BaseModel):
    symlinks: Optional[SymlinksDatasetFacet] = None


class SymlinksDatasetFacet(DatasetFacet):
    identifiers: Optional[list[Identifier]] = None
