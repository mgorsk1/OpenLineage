# Copyright 2018-2024 contributors to the OpenLineage project
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing import Optional

from openlineage.client.generated.base import InputDatasetFacet
from pydantic import BaseModel, Field
from typing_extensions import Annotated


class Assertion(BaseModel):
    assertion: Annotated[str, Field(example="not_null")]
    """
    Type of expectation test that dataset is subjected to
    """
    success: bool
    column: Annotated[Optional[str], Field(example="id")] = None
    """
    Column that expectation is testing. It should match the name provided in SchemaDatasetFacet. If column field is empty, then expectation refers to whole dataset.
    """


class DataQualityAssertionsDatasetFacet(InputDatasetFacet):
    assertions: list[Assertion]


class Model(BaseModel):
    dataQualityAssertions: Optional[DataQualityAssertionsDatasetFacet] = None
