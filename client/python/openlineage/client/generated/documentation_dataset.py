# Copyright 2018-2024 contributors to the OpenLineage project
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing import Optional

from openlineage.client.generated.base import DatasetFacet
from pydantic import BaseModel, Field
from typing_extensions import Annotated


class DocumentationDatasetFacet(DatasetFacet):
    description: Annotated[str, Field(example="canonical representation of entity Foo")]
    """
    The description of the dataset.
    """


class Model(BaseModel):
    documentation: Optional[DocumentationDatasetFacet] = None
