# Copyright 2018-2024 contributors to the OpenLineage project
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing import Optional

from openlineage.client.generated.base import DatasetFacet
from pydantic import BaseModel, Field
from typing_extensions import Annotated


class Model(BaseModel):
    ownership: Optional[OwnershipDatasetFacet] = None


class Owner(BaseModel):
    name: Annotated[str, Field(example="application:app_name")]
    """
    the identifier of the owner of the Dataset. It is recommended to define this as a URN. For example application:foo, user:jdoe, team:data
    """
    type: Annotated[Optional[str], Field(example="MAINTAINER")] = None
    """
    The type of ownership (optional)
    """


class OwnershipDatasetFacet(DatasetFacet):
    owners: Optional[list[Owner]] = None
    """
    The owners of the dataset.
    """
