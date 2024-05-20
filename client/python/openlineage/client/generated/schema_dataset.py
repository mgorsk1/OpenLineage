# Copyright 2018-2024 contributors to the OpenLineage project
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing import Optional

from openlineage.client.generated.base import DatasetFacet
from pydantic import BaseModel, Field
from typing_extensions import Annotated


class Model(BaseModel):
    schema_: Annotated[Optional[SchemaDatasetFacet], Field(alias="schema")] = None


class SchemaDatasetFacet(DatasetFacet):
    fields: Optional[list[SchemaDatasetFacetFields]] = None
    """
    The fields of the data source.
    """


class SchemaDatasetFacetFields(BaseModel):
    name: Annotated[str, Field(example="column1")]
    """
    The name of the field.
    """
    type: Annotated[Optional[str], Field(example="VARCHAR|INT|...")] = None
    """
    The type of the field.
    """
    description: Optional[str] = None
    """
    The description of the field.
    """
    fields: Optional[list[SchemaDatasetFacetFields]] = None
    """
    Nested struct fields.
    """
