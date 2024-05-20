# Copyright 2018-2024 contributors to the OpenLineage project
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing import Optional

from openlineage.client.generated.base import DatasetFacet
from pydantic import BaseModel, Extra


class ColumnLineageDatasetFacet(DatasetFacet):
    fields: dict[str, Fields]
    """
    Column level lineage that maps output fields into input fields used to evaluate them.
    """


class Fields(BaseModel):
    class Config:
        extra = Extra.allow

    inputFields: list[InputField]
    transformationDescription: Optional[str] = None
    """
    a string representation of the transformation applied
    """
    transformationType: Optional[str] = None
    """
    IDENTITY|MASKED reflects a clearly defined behavior. IDENTITY: exact same as input; MASKED: no original data available (like a hash of PII for example)
    """


class InputField(BaseModel):
    class Config:
        extra = Extra.allow

    namespace: str
    """
    The input dataset namespace
    """
    name: str
    """
    The input dataset name
    """
    field: str
    """
    The input field
    """


class Model(BaseModel):
    columnLineage: Optional[ColumnLineageDatasetFacet] = None
